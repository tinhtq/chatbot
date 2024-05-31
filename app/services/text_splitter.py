import io

from fastapi import HTTPException
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain_community.document_loaders.pdf import PDFPlumberLoader

embedding = FastEmbedEmbeddings()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20, length_function=len,
                                               is_separator_regex=False)


def handle_pdf(file):
    loader = PDFPlumberLoader(file)
    docs = loader.load_and_split()
    chunks = text_splitter.split_documents(docs)
    return len(chunks)
