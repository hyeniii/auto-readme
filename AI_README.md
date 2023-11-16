# AlejandraLLI/auto-readme-toytest 

## Overview

This project is a script that generates a README file for a specified GitHub repository. It uses modules such as `aiohttp`, `PyGithub`, and `requests` to interact with the GitHub API. The script sets up logging using a configuration file and retrieves content from the repository. It then decodes the repository files, creates a README file, extracts an overview of the repository, extracts the repository structure, provides getting started instructions, and includes summaries of the files in the repository. The project also includes utility files such as `ai_outputparsers.py`, which contains classes to parse and format the output of a language model, and `github_utils.py`, which contains functions to work with GitHub repositories.

## Repo Structure

```
.
├── .gitignore
├── LICENSE
├── config
│   └── logs
│       └── local.conf
├── requirements.txt
├── sandbox.py
└── src
    ├── __init__.py
    ├── ai_outputparsers.py
    ├── ai_utils.py
    └── github_utils.py
```

## Getting started

To get started with the **AlejandraLLI/auto-readme-toytest** repository, follow these steps:

**Cloning the Repository:**
1. Open your terminal or command prompt.
2. Navigate to the directory where you want to clone the repository.
3. Run the following command to clone the repository:
   ```
   git clone https://github.com/AlejandraLLI/auto-readme-toytest.git
   ```
4. The repository will be cloned to your local machine.

**Installing Dependencies:**
1. Make sure you have Python installed on your machine.
2. Open your terminal or command prompt.
3. Navigate to the cloned repository's directory.
4. Run the following command to install the dependencies:
   ```
   pip install -r requirements.txt
   ```
5. The required dependencies will be installed.

**Special Credentials:**
1. You need to set up the following environment variables:
   - GITHUB_API_TOKEN: This token is required to access the GitHub API. Please obtain a personal access token from GitHub and assign it to this environment variable.
   - OPENAI_API_TOKEN: This token is required to access the OpenAI API. Please obtain an API key from OpenAI and assign it to this environment variable.

Note: Ensure that the `.env` file is present in the repository directory and contains the required environment variables with their respective values.

Now you are ready to use the repository. You can explore the code files and run the `sandbox.py` file to execute the functionality provided by the repository.

## File description 

**.gitignore** 

This file specifies the content that should be ignored by Git when tracking changes in a repository. The content in this .gitignore file includes: 
- .env files
- .venv/ directory
- .vscode/ directory
- .log files
- .pyc files
- tokens/ directory

**LICENSE** 

The file LICENSE contains the MIT License, which grants permission to any person obtaining a copy of the software to use, copy, modify, merge, publish, distribute, sublicense, and/or sell copies of the software. The license also includes a warranty disclaimer and limitations of liability.

**config/logs/local.conf** 

This configuration file defines the logging settings for the application. It specifies the loggers, handlers, and formatters to be used. The loggers section specifies two loggers: root and src. The handlers section defines two handlers: consoleHandler and fileHandler. The formatters section defines one formatter: sampleFormatter. The logger_root and logger_src sections specify the level, handlers, and propagate settings for the respective loggers. The handler_consoleHandler section specifies the class, level, formatter, and arguments for the consoleHandler. The handler_fileHandler section specifies the class, level, formatter, and arguments for the fileHandler. The formatter_sampleFormatter section defines the format and date format for the sampleFormatter.

**requirements.txt** 

This file contains a list of Python package requirements for a project. The packages include aiohttp, aiosignal, async-timeout, attrs, certifi, cffi, charset-normalizer, cryptography, Deprecated, frozenlist, idna, multidict, openai, pycparser, PyGithub, PyJWT, PyNaCl, python-dateutil, python-dotenv, requests, six, tqdm, typing_extensions, urllib3, and wrapt.

**sandbox.py** 

This file is a script that generates a README file for a specified GitHub repository. It imports necessary modules, sets up logging, and retrieves content from the repository. It then decodes the repository files, creates a README file, extracts an overview of the repository, extracts the repository structure, provides getting started instructions, and includes summaries of the files in the repository.

**src/__init__.py** 

This file is the initialization file for the src module. It is commonly used to define any necessary setup or configuration for the module.

**src/ai_outputparsers.py** 

The file contains three classes: FormattedOutputConvertToText, MarkdownTreeStructureOutputParser, and FormattedOutputParserSummary. 

The FormattedOutputConvertToText class parses and formats the output of a language model as a simple string. 

The MarkdownTreeStructureOutputParser class parses and formats the output of a language model to represent a repository structure in Markdown. It splits the text into lines, each representing a file path, and organizes the paths into a tree structure. Finally, it formats the tree structure for Markdown output. 

The FormattedOutputParserSummary class parses and formats the output of a language model to highlight file paths and their summaries. It assumes the text format is "File Path: {file_path} Summary: {summary}". It extracts the file path and summary from the text and formats them as a bold file path and a paragraph summary.

**src/ai_utils.py** 

This file contains a class called CustomCodeLoader which is a subclass of BaseLoader. It also includes several functions such as get_language_from_extension, load, get_repo_overview, get_repo_structure, getting_started, and get_file_summaries.

**src/github_utils.py** 

This file contains functions to work with GitHub repositories. It includes functions to get all files from a repository, decode base64-encoded file contents, and flatten nested dictionaries.

