from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate

from langchain_ollama import ChatOllama
# from langchain.output_parsers import StructuredOutputParser



if __name__ == "__main__":
    load_dotenv()

    print("Hello LangChain")
    information = """
       write poem on ch words
    """

    summary_template = """
    given the information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    llm = ChatOllama(model = "mistral" )

    chain = summary_prompt_template | llm   
    res = chain.invoke(input={"information": information})

    print(res)








