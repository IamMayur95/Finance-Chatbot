from langchain_astradb import AstraDBVectorStore
from langchain_openai import OpenAIEmbeddings
from dotenv import load_dotenv
from src.helper import load_file
import os

load_dotenv()

# Load environment variables
OPENAI_API_KEY = os.getenv("OPENAI_API_KEY")
ASTRA_DB_API_ENDPOINT = os.getenv("ASTRA_DB_API_ENDPOINT")
ASTRA_DB_APPLICATION_TOKEN = os.getenv("ASTRA_DB_APPLICATION_TOKEN")

os.environ["OPENAI_API_KEY"] = OPENAI_API_KEY
os.environ["ASTRA_DB_API_ENDPOINT"] = ASTRA_DB_API_ENDPOINT
os.environ["ASTRA_DB_APPLICATION_TOKEN"] = ASTRA_DB_APPLICATION_TOKEN

embedding = OpenAIEmbeddings(api_key=OPENAI_API_KEY)

def ingestdata(status , file_path):
    vstore = AstraDBVectorStore(
    embedding=embedding,
    collection_name="financebot",
    api_endpoint=ASTRA_DB_API_ENDPOINT,
    token=ASTRA_DB_APPLICATION_TOKEN,
    namespace="default_keyspace"
    )

    storage = status
    if storage == None:
        docs = load_file(file_path)
        inserted_ids = vstore.add_documents(docs)     
        return vstore,inserted_ids    
    else:
        return vstore,[]    

if __name__ == "__main__": 
    vstore, inserted_ids = ingestdata("Done", 
                                      "C:\\Users\\Mayur\\7_projects-live\\Finance-Chatbot\\data\\finance_data.pdf")
    print("Length of Inserted IDs:", len(inserted_ids))
    # To search documents, use the following:
    results = vstore.similarity_search("What is the current market trends for stocks?")
    for result in results:
        print(f"*{result.page_content}[{result.metadata}]")
    
