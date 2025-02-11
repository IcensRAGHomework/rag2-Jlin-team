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
    full_text = "\n".join(doc.page_content for doc in docs)
    splitter = RecursiveCharacterTextSplitter(
        chunk_size=50,
        chunk_overlap=0,
         separators=[
           r'第 +[一二三四五六七八九十0-9/-]+ +[章條]'
        ],
         is_separator_regex=True
        )
    chunks = splitter.split_text(full_text)
    return len(chunks)

print(hw02_2(q2_pdf))