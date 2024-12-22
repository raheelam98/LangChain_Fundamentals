
PromptTemplate(
        input_variables=["information"], template=summary_template
    )
    
llm = ChatOllama(model = "llama3")

chain = summary_prompt_template | llm

response = chain.invoke(input={"information":information})

print(response)
