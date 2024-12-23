## Tutorials

[Lang Chain - Components](https://python.langchain.com/v0.1/docs/modules/)

* Model I/O :- Prompts, Chat models, LLMs
* Retrieval :- Document loaders, Text splitters, Embedding models, Vectorstores, Retrievers
* Composition :- Tools, Agents, Chains
* Memory, Callbacks

[Lang Chain - Prompt Templates](https://python.langchain.com/docs/concepts/prompt_templates/)

Prompt templates help to translate user input and parameters into instructions for a language model. 

[Lang Chain - Chain](https://python.langchain.com/v0.1/docs/modules/chains/)

Chains refer to sequences of calls - whether to an LLM, a tool, or a data preprocessing step.

[Lang Chain - Output parsers](https://www.udemy.com/course/langchain/learn/lecture/44709555#overview)

Output parsers are responsible for taking the output of a model and transforming it to a more suitable format for downstream tasks

[Lang Chain - Agents](https://python.langchain.com/v0.1/docs/use_cases/tool_use/agents/)

Agents (llm) allow the model to autonomously determine the sequence and frequency of tool usage based on the input.

[Lang Chain - Build an Agent](https://python.langchain.com/docs/tutorials/agents/)

[Lang Graph - How to interact with the deployment using RemoteGraph](https://langchain-ai.github.io/langgraph/how-tos/use-remote-graph/)

### Lang Chain Videos

[Lang Chain - Self-reflective RAG with LangGraph: Self-RAG and CRAG - 7 Feb 2024](https://www.youtube.com/watch?v=pbAd8O1Lvm4)

[IBM Technology - LangChain vs LangGraph: A Tale of Two Frameworks - 4 Nov 2024 ](https://www.youtube.com/watch?v=qAF1NjEVHhY)


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








