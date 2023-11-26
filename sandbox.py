import os
import argparse
import logging
import logging.config

from dotenv import load_dotenv
from github import Github
import src.github_utils as gu
import src.ai_utils as au

logging.config.fileConfig("config/logs/local.conf")
logger = logging.getLogger(__name__)

if __name__ == "__main__":
    parser = argparse.ArgumentParser(
        description="Auto-readme"
    )
    parser.add_argument(
        "-r", "--repo", default="hyeniii/auto-readme", help="Specify github repository to create a readme on"
    )
    args = parser.parse_args()
    repo_name = args.repo
    logger.info("Repository name: %s", repo_name)

    # Load environment variables from .env file
    load_dotenv()

    GITHUB_API_TOKEN = os.getenv("GITHUB_API_TOKEN")
    OPEN_API_TOKEN = os.getenv("OPENAI_API_TOKEN")

    if GITHUB_API_TOKEN is None or OPEN_API_TOKEN is None:
        logger.error("API tokens not found in environment variables.")
        exit(1)  # Exit the program if tokens are not set

    try:
        # --- Extract Github Repo Content--- 
        g = Github(GITHUB_API_TOKEN)
        repo = g.get_repo(repo_name)
        logger.debug(repo.get_topics())
        logger.info("Retriving data from %s. This process might take time ...", repo.full_name)
        contents = repo.get_contents("")
        all_files = gu.get_all_files(repo)
        logger.debug(all_files)

        # --- Decode files ---
        # Flatten dictionary
        logger.info("Flattening dictionary...")
        flatten_files = gu.flatten(all_files)
        # Decode files (omit pdf, ipynb, csv, zip, pptx, images)
        logger.info("Dictionary flattened. Proceeding to decode files.")
        decoded_files, ignored_files = gu.decode_files(flatten_files)

        # Log decoded and omitted files.
        logger.info("Finished decoding files.")
        logger.info("   Files decoded:")
        for path in decoded_files.keys():
            logger.info("      - %s", path)
        logger.info("   Files ignored:")
        for file in ignored_files:
            logger.info("      - %s", file)

        # --- Create README file ---
        logger.info("Creating AI_README.md file...")
        with open("AI_README.md","w") as f:
            f.write(f"# {repo_name} \n\n")
        logger.info("AI_README.md file successfully created.")

        # --- Custom loader ---
        custom_loader = au.CustomCodeLoader(decoded_files)
        logger.info("Custom loader for files created.")
        documents = list(custom_loader.load())
        logger.info("Repo files loaded.")

        # --- Summary of files --- 
        logger.info("Extracting summary of files in repo. This process might take time...")
        file_summaries = au.get_file_summaries(documents, OPEN_API_TOKEN)
        logger.info("Summary of files in repo extracted.")

        # --- Get repo overview --- 
        logger.info("Extracting repo overview from summaries...")
        #answer = au.get_repo_overview(documents, OPEN_API_TOKEN)
        answer = au.get_repo_overview(file_summaries, OPEN_API_TOKEN)
        logger.info("Repo overview extracted.")

        with open("AI_README.md","a") as f:
            f.write("## Overview\n\n")
            f.write(f"{answer}\n\n")
        logger.info("Repo overview written to readme file.") 
        
        # --- Get repo structure from full list of paths --- 
        logger.info("Extracting repo structure ...")
        all_paths = [key for key in flatten_files.keys()]
        answer = au.get_repo_structure(all_paths, OPEN_API_TOKEN)
        logger.info("Repo structure extracted.")

        with open("AI_README.md","a") as f:
            f.write("## Repo Structure\n\n")
            f.write(f"{answer}\n\n")
        logger.info("Repo structure written to readme file.") 

        # --- Getting started instructions --- 
        logger.info("Extracting repo getting started instructions ...")
        try:
            answer = au.getting_started(repo_name, documents, OPEN_API_TOKEN)
            logger.info("Repo getting started instructions extracted.")
        except:
            answer = au.cloning_instructions(repo_name, 
                                             [doc["metadata"]["path"] for doc in documents], 
                                             OPEN_API_TOKEN)
            logger.info("Repo is too long to extract detailed instructions. Parsing not implemented yet. Returning cloning instructions only")
        
        with open("AI_README.md","a") as f:
            f.write("## Getting started\n\n")
            f.write(f"{answer}\n\n")
        logger.info("Getting stated instructions written to readme file.")

        # --- Write summary of files --- 
        #answer = au.get_file_summaries(documents, OPEN_API_TOKEN)
        #logger.info("Summary of files in repo extracted.")

        with open("AI_README.md","a") as f:
            f.write("## File descriptions \n\n")
            if ignored_files!=[]:
                f.write('**NOTE:** Code parsing is not implemented yet. Files with extentions *".DS_Store", ".pdf", ".ipynb", ".csv", ".zip", ".pptx", ".jpg", ".jpeg",".png"* will be ommited.\n\n')
            #for a in answer: 
            for a in file_summaries:
                f.write(f"{a}\n\n")
        logger.info("File descriptions writen to readme file.")
        logger.info("AI_README successfully created!!")

    except Exception as e:
        logging.error("Error occured in retrieving repo content", e)
