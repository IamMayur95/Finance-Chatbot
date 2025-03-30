from langchain_core.prompts import ChatPromptTemplate
from langchain_openai import ChatOpenAI
from src.data_ingestion import ingestdata
from langchain_core.runnables import RunnablePassthrough
from langchain_core.output_parsers import StrOutputParser

def generation(vstore):
    retriever = vstore.retriever = vstore.as_retriever(search_kwargs={"k":3}) # k is the number of documents to return
    
    FINANCE_BOT_TEMPLATE = """" 
    Your finance bot is an expert in finance related advice.
    Ensure your answers are relevant to the query context and refrain from straying off-topic.
    Your responses should be concise and informative.

    CONTEXT:
    {context}

    QUESTION: {question}

    YOUR ANSWER:
    """
    prompt = ChatPromptTemplate.from_template(FINANCE_BOT_TEMPLATE)

    llm = ChatOpenAI()

    chain = (
        {"context":retriever , "question":RunnablePassthrough()}
        | prompt
        | llm
        | StrOutputParser()
    )

    return chain

if __name__ == "__main__":
    vstore, inserted_ids = ingestdata("Done",
                         "C:\\Users\\Mayur\\7_projects-live\\Finance-Chatbot\\data\\finance_data.pdf")
    chain = generation(vstore)
    print(chain.invoke("What is the current market trend in finance?"))



