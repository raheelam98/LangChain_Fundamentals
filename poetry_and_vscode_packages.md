
### Project Setup: Lang Graph with Poetry

Create a new directory for the project
```bash
mkdir reflection-agent
```

Change into the project directory
```bash
cd reflection-agent
```

Initialize a new poetry project
```bash
poetry init
```

List the files in the project directory
```bash
ls
```

Display the contents of the pyproject.toml file
```bash
cat pyproject.toml
```

Add the specified dependencies to the project using poetry
```bash
poetry add python-dotenv black isort langchain langchain-openai langgraph langchain_google_genai
```

Install grandalf package using pip
```bash
pip install grandalf
```

Add the grandalf package to the project using poetry
```bash
poetry add grandalf
```

Run graph

https://mermaid.live/ 

Creating virtualenv relection-agent-TJA1TPkj-py3.12 in /Users/raheelam/Library/Caches/pypoetry/virtualenvs

Current virtual environment for Poetry project in VSCode,
```bash
poetry env info --path
```

**Set the Python interpreter in VSCode:**

* Press Cmd + Shift + P (or Ctrl + Shift + P on Windows/Linux) to open the command palette.

* Type "Python: Set Interpreter" and select it.

* Select the path you obtained from the previous step and press Enter. 

Install a Python package in editable mode (dot . refers to the current directory)

```bash
python -m pip install -e .

python -m pip install -e <path_to_package>
```

### Deployment

[Deployment](https://github.com/langchain-ai/langchain-academy/blob/main/module-1/deployment.ipynb)

**Run LangGraph Server Locally**

Ensure you have LANGSMITH_API_KEY environment variable in .env file.

Installs **`langgraph-cli`** globally or in the currently active virtual environment.

upgrade and install the langgraph-cli package with the [inmem] option.
```bash
pip install -U "langgraph-cli[inmem]"
```

```bash
pip install langgraph-cli
```

poetry
```bash
poetry add langgraph-cli
```

```bash
langgraph up
```


[How to Set Up a LangGraph Application for Deployment](https://langchain-ai.github.io/langgraph/cloud/deployment/setup_pyproject/)


If you are using pyproject.toml or setuptools:
python3 -m pip install -e .

If you are using requirements.txt:
python3 -m pip install -r requirements.txt

Command to Refresh and Set Up LangGraph Development Environment

uvx --refresh --from "langgraph-cli[inmem]" --with-editable . --python 3.12 langgraph dev



#### Initialize the language model as an instance of ChatOpenAI.

**`llm = ChatGoogleGenerativeAI(model="gemini-1.5-flash")`**

**`llm = ChatOllama(model=Configuration.local_llm, temperature=0)`**


poetry add fastapi uvicorn\[standard\] 













