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

**Create environment and require packages**

* create virtual environment (Note remember virtual envirornment)
pipenv shell

* Install LangChain with OpenAI support / Google Generative AI support: ( for llm)
pipenv install langchain-openai 
or
pipenv install langchain_google_genai

* Install LangChain Community Edition (nclude additional tools, integrations, or community)
pipenv install langchain-community

* Install LangChainHub: (nclude additional resources, templates, or pre-built components)
pipenv install langchainhub

* Install Python Dotenv: (manage environment variables more easily by reading them from a .env file)
 pipenv install python-dotenv


