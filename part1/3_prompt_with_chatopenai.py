from dotenv import load_dotenv
from langchain.prompts.prompt import PromptTemplate
from langchain_openai import ChatOpenAI

if __name__ == "__main__":
    load_dotenv()

    print("Hello LangChain")
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

    llm = ChatOpenAI(model="gpt-4o",temperature=0)

    chain = summary_prompt_template | llm
    res = chain.invoke(input={"information": information})

    print(res)
