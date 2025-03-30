from langchain_community.document_loaders import PyPDFLoader
from langchain.text_splitter import RecursiveCharacterTextSplitter


def load_file(file_path):
    loader = PyPDFLoader(file_path)
    pages = loader.load()
    pages = pages[10:20]
    raw_text = ""
    for i , page in enumerate(pages):
        raw_text += page.page_content
    
    text_splitter = RecursiveCharacterTextSplitter(chunk_size=500,chunk_overlap=100)

    texts = text_splitter.split_text(raw_text)

    return texts