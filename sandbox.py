import os
import argparse
import logging
import logging.config

from dotenv import load_dotenv
from github import Github
import src.github_utils as gu

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

    # Load environment variables from .env file
    load_dotenv()

    GITHUB_API_TOKEN = os.getenv("GITHUB_API_TOKEN")
    OPEN_API_TOKEN = os.getenv("OPENAI_API_TOKEN")

    if GITHUB_API_TOKEN is None or OPEN_API_TOKEN is None:
        logger.error("API tokens not found in environment variables.")
        exit(1)  # Exit the program if tokens are not set

    try:
        g = Github(GITHUB_API_TOKEN)
        repo = g.get_repo("public-apis/public-apis")
        print(repo.get_topics())
        logging.info("Recetriving data from %s", repo.full_name)
        contents = repo.get_contents("")
        all_files = gu.get_all_files(repo)
        print(all_files)
    except Exception as e:
        logging.error("Error occured in retrieving repo content", e)
