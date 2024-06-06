import io

from fastapi import HTTPException
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain_community.document_loaders.pdf import PDFPlumberLoader
from langchain_community.vectorstores import Chroma

folder_path = "db"

embedding = FastEmbedEmbeddings()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20, length_function=len,
                                               is_separator_regex=False)


def handle_pdf(file):
    loader = PDFPlumberLoader(file)
    docs = loader.load_and_split()
    chunks = text_splitter.split_documents(docs)
    vector_store = Chroma.from_documents(
        documents=chunks, embedding=embedding, persist_directory=folder_path
    )
    vector_store.persist()
    return len(docs)
