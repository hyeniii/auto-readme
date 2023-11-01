# Auto-Readme

Automatically generate `readme.md` files for your repositories by parsing the code and summarizing it using Openai API.

## Features

- Parse GitHub repositories without downloading them.
- Summarize code using Langchain.
- Generate human-readable summaries with OpenAI's GPT model.

## Prerequisites

- Python 3.8+
- GitHub API Token (https://github.com/settings/tokens)
- OpenAI API Key (https://beta.openai.com/signup)

## Installation

1. Clone Repository
2. Create a virtual environment `python -m venv .venv` and install packages in `requirements.txt`
2. Create .env file at the root of directory

```bash
GITHUB_API_TOKEN=<add-token-here>
OPENAI_API_TOKEN=<add-token-here>
```
