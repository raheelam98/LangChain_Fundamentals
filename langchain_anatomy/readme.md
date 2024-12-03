## LangChain Anatomy

### 1- Components

* LLM Wrappers
* Prompt Templates
* Indexes for relevant information 

### 2- Chain

* Assemble components to slove a specific task 

### 3 - Agents

* Agents allows LLMs to interact with it's environments.

**Details**  

### 1- Components

### 1a - Modules (LLM  Wrapper)

**Load environment variables**
```bash
from dotenv import load_dotenv
load_dotenv()
```
    
### 1b - Chat Modules

**import schema for chat messages and ChatOpenAI in order to query**

```bash
from langchain.schema import (
    AIMessage,
    HumanMessage,
    SystemMessage
)

from langchain_openai import ChatOpenAI
llm = ChatOpenAI(model="gpt-4o",temperature=0)

messages = [
    SystemMessage(content="..."),
    HumanMessage(content="... ")
]
response=chat(messages)

print(response.content,end='\n')
```

### 2 - Prompts Templates 

Prompts are what we send to our language model. Prompt templates are often dynamic and used in applications to translate user inputs into structured instructions, 
using dictionary variables to generate coherent language model responses.

**Import prompt and define PromptTemplate**

```bash

from langchain.prompts.prompt import PromptTemplate

    information = """
        Karachi is the capital city of the Pakistani province of Sindh. 
        It is the largest city in Pakistan and 12th largest in the world, with a population of over 20 million
    """

    summary_template = """
    given the information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )
```
### 3 - Chain 
A chain takes a language model and a prompt template, combining them into an interface that takes input from the user and outputs answers from the language model.

**Run LLM with PromptTemplate**

```bash
llm = ChatOpenAI(model="gpt-4o",temperature=0)
```

**Import LLMChain and define chain with language model and prompt.**

```bash
    chain = summary_prompt_template | llm
    res = chain.invoke(input={"information": information})

    print(res)
```

### 4 - Embedding and Vector Stores

Divide long paragraphs into chunks so we can store them in a vector store in Pinecone.

### 5 - Agents 

