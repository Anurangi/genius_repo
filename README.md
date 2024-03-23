
# Introduction
In this POC we have used a simple Q&A chain and agent over a pandas dataframe. This project will allow to ask questions regarding the dataframe provided (ie: uploaded csv filefrom the frontend) and provide the natural language answer.


# Getting Started
Below are the repo details for this project

- Azure DevOps Repo link - https://dev.azure.com/JKGroupAA/OCTAVE_MODELMANAGEMET_GOV/_git/octave_gpt?path=%2FREADME.md&version=GBchatgpt_chatbot&_a=contents
- Repo Branch - octave_gpt_pandas_querying


# Data Sources
- User to upload a csv file from the chat interface.

# Folders & Modules
- conf folder - contains the confoguration details in a yaml file.
- src - contains all the modules related to ingesting and querying data.
    - src/config.py - function to read the config.yaml file
    - query_data.py - congtains the functions to query the dataframe using the given natural language question using azure openai gpt-35-turbo
    - utils.py - congtains the functions to authenticate azure openai models.
    - app.py - streamlit module to run the chatbot.
- README.md - contains the details about the project.
- requirements.txt - contains the libraries required to create the python environment. (If you are using the same code base in here please use only the mentioned library versions in this file)


# Architectural Diagram
![alt text](<img/Architectural diagram.PNG>)


# Environment
Create a venv environment with python 3.9 or 3.10. Install the libraries mentioned in the requirements.txt

# References
- Langchain - https://python.langchain.com/docs/use_cases/csv
- Azure OpenAI Pricing and Products - https://community.openai.com/t/what-is-the-prompt-and-completion-price-in-gpt-4-api/225130​ , https://azure.- microsoft.com/en-us/pricing/details/cognitive-services/openai-service/​ , https://help.openai.com/en/articles/4936856-what-are-tokens-and-how-to-count-them#h_63fd902129​ , https://platform.openai.com/tokenizer 