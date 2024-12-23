### Environment
.env

GEMINI_API_KEY= your gemini key if require

LANGCHAIN_API_KEY= your langchain key if require

LANGSMITH_API_KEY= your langsmith key if require

OPENAI_API_KEY= your openai key if require

ollama= your ollama key if require

LANGCHAIN_TRACING_V2=true

LANGCHAIN_PROJECT=project name


### LLM
main.py

```bash
from langchain_google_genai import ChatGoogleGenerativeAI
llm = ChatGoogleGenerativeAI(model="gemini-1.5-pro")
```

```bash
from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-4o",temperature=0)
```

```bash
from langchain_ollama import ChatOllama
llm = ChatOllama(model = "llama3")
```

### Install Packages 

**Poetry Environment**
```bash
poetry add fastapi sqlmodel uvicorn\[standard\] psycopg 
```

**Langgraph**
```bash
poetry add python-dotenv langchain langchain-openai langgraph langchain_google_genai 
```

**Install a Python package with optional extras using** 
```bash
poetry add "langgraph-cli[inmem]"
```

ollama
```bash
pip install -U langchain-ollama
```

**Chatbot with Tools :** Integrate a web search tool into the bot.

First, install the requirements to use the [Tavily Search Engine](https://python.langchain.com/docs/integrations/tools/tavily_search/), and set your [TAVILY_API_KEY](https://tavily.com/).

```bash
poetry add tavily-python langchain_community
```

```bash
poetry add black isort
```

**Current virtual environment for your Poetry project**

```bash
poetry env info --path
```

List all virtual environments associated with the current project

```bash
poetry env list
```

**`AsyncIteratorCallbackHandler`**  in LangChain is used to process asynchronous, streamed responses in real-time

**Tutorials**

[DataStreaming with LangChain & FastAPI - 8 Aug 2023](https://www.youtube.com/watch?v=Gn54EbU9mRg&list=PLNVqeXDm5tIp1KyNfHsVPxcuoBurCtaRp&index=7)








