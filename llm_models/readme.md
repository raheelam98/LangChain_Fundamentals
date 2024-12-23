
.env

GEMINI_API_KEY= your gemini key if require

LANGCHAIN_API_KEY= your langchain key if require

LANGSMITH_API_KEY= your langsmith key if require

OPENAI_API_KEY= your openai key if require

ollama= your ollama key if require

LANGCHAIN_TRACING_V2=true

LANGCHAIN_PROJECT=project name


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









