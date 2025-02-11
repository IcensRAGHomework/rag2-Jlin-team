from langchain_community.document_loaders import PyPDFLoader
from langchain_text_splitters import (CharacterTextSplitter,
                                      RecursiveCharacterTextSplitter)

q1_pdf = "OpenSourceLicenses.pdf"
q2_pdf = "勞動基準法.pdf"

def hw02_1(q1_pdf):
    loader = PyPDFLoader(q1_pdf)
    docs = loader.load()
    splitter = CharacterTextSplitter(chunk_overlap=0)
    chunks  = splitter.split_documents(docs)
    return chunks[len(chunks)-1]

def hw02_2(q2_pdf):
    loader = PyPDFLoader(q2_pdf)
    docs = loader.load()
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=170,chunk_overlap=0)
    chunks = splitter.split_documents(docs)
    return len(chunks)