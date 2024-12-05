## Project Requirments 

File Permissions with chmod -- only for mac user
grants all users full read, write, and execute permissions on the specified folder and its contents
```bash
sudo chmod -R 777 /path/to/folder

sudo chmod -R 777  /Users/user-name/Documents/folder-name
```

**current working directory**
```bash
pwd
```

**clone repository**

```shell
git clone URL
```

**Clone Branch** 

```shell
git clone -b branch_name https://github.com/github_account_name/repository_name.git
```

**install all the dependencies**

create a virtual environment and install all the dependencies specified in your pyproject.toml file, but it won’t install the project itself as a package.

```bash
poetry install --no-root
```

### Create environment and require package

* create virtual environment (Note remember virtual envirornment)

```shell
pipenv shell
```

* Install LangChain with OpenAI support / Google Generative AI support: ( for llm)

```shell
pipenv install langchain-openai 
```

```shell
pipenv install langchain_google_genai 
```

* Install LangChain Community Edition (nclude additional tools, integrations, or community)

```shell
pipenv install langchain-community
```

* Install LangChainHub: (nclude additional resources, templates, or pre-built components)

```shell
pipenv install langchainhub
```

* Install Python Dotenv: (manage environment variables more easily by reading them from a .env file)

```shell
 pipenv install python-dotenv
```
### Enviorment Setting 

**VS Code Command Palette**  mac:  cmd+ shif + P

**VS Code Command Palette**  windows: ctrl+ shif + P

Step1 :-  Select Python interpreter 

Step2 :-  Select virtual environment (we just created)

Step3 :- run code to check it is working

### Create Json file (to load environment variables from .env)

* From right corner of vs-code select the Run and Debug (bug-icon)
* Click on :-  create a launch.json file
* From pallet  select Python
* Then select :-  Python File Debug the current active Python file
* Add new entry :- envFile 
* Change the name :- Ice Breaker Runner


### API Keys

In LangGraph, we can use out-of-the-box features, such as LLMs (API Keys).

**(llm / toocalling) :**  GEMINI_API_KEY(llm)

**GEMINI_API_KEY=**

HumanMessage can pass a prompt to the model using the GEMINI_API_KEY (LLM)

[Gemini API](https://aistudio.google.com/app/apikey)


**LANGCHAIN_API_KEY=**

LangSmith is a standalone platform for building, monitoring, and evaluating production-grade LLM applications, ensuring quick and confident deployments.

[Get started with LangSmith](https://docs.smith.langchain.com/)

* login 
* create API Key
* setting (click on 3 dots at bottom) 
* create API Key







