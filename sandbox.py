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
        logger.info("Retriving data from %s ...", repo.full_name)
        contents = repo.get_contents("")
        all_files = gu.get_all_files(repo)
        logger.debug(all_files)

        # --- Decode files ---
        logger.info("Decoding files in repo...")
        decoded_files = gu.decode_files(all_files)
        logger.info("Files decoded. Proceeding to flatten dictionary.")
        decoded_files_flatten = gu.flatten(decoded_files)
        logger.info("Files flattened")

        # --- Create README file ---
        logger.info("Creating AI_README.md file...")
        with open("AI_README.md","w") as f:
            f.write(f"# {repo_name} \n\n")
        logger.info("AI_README.md file successfully created.")

        # --- Custom loader ---
        custom_loader = au.CustomCodeLoader(decoded_files_flatten)
        logger.info("Custom loader for files created.")
        documents = list(custom_loader.load())
        logger.info("Repo files loaded.")

        # --- Summary of files --- 
        logger.info("Extracting summary of files in repo...")
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
        
        # --- Get repo structure --- 
        logger.info("Extracting repo structure ...")
        answer = au.get_repo_structure(documents, OPEN_API_TOKEN)
        logger.info("Repo structure extracted.")

        with open("AI_README.md","a") as f:
            f.write("## Repo Structure\n\n")
            f.write(f"{answer}\n\n")
        logger.info("Repo structure written to readme file.") 

        # --- Getting started instructions --- 
        logger.info("Extracting repo getting started instructions ...")
        answer = au.getting_started(repo_name, documents, OPEN_API_TOKEN)
        logger.info("Repo getting started instructions extracted.")

        with open("AI_README.md","a") as f:
            f.write("## Getting started\n\n")
            f.write(f"{answer}\n\n")
        logger.info("Getting stated instructions written to readme file.")

        # --- Write summary of files --- 
        #answer = au.get_file_summaries(documents, OPEN_API_TOKEN)
        #logger.info("Summary of files in repo extracted.")

        with open("AI_README.md","a") as f:
            f.write("## File description \n\n")
            #for a in answer: 
            for a in file_summaries:
                f.write(f"{a}\n\n")
        logger.info("File descriptions writen to readme file.")
        logger.info("AI_README successfully created!!")

    except Exception as e:
        logging.error("Error occured in retrieving repo content", e)
