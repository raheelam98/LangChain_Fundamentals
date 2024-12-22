from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
#from langchain_openai import ChatOpenAI
from langchain_ollama import ChatOllama

from third_parties.linkedin import scrape_linkedin_profile

information = """
Alexander III of Macedon, also known as Alexander the Great, a king of the ancient Greek kingdom of Macedonia in 336 BC 
at the age of 20, succeeding his father, Philip II. He is renowned for his extensive military campaigns across 
Western Asia, Central Asia, parts of South Asia, and Egypt1. By the age of 30, Alexander had established one of history's 
largest empires, stretching from Greece to northwestern India
"""

if __name__ == "__main__":
    load_dotenv()

    print("Hello LangChain")

    summary_template = """
    given the information {information} about a person I want you to create:
    1. A short summary
    2. two interesting facts about them
    """

    summary_prompt_template = PromptTemplate(
        input_variables=["information"], template=summary_template
    )

    #llm = ChatOpenAI(model="gpt-4o",temperature=0)

    llm = ChatOllama(model = "llama3")

    chain = summary_prompt_template | llm

    response = chain.invoke(input={"information":information})

    print(response)

