import io
from tempfile import NamedTemporaryFile

from fastapi import HTTPException
from langchain_text_splitters import RecursiveCharacterTextSplitter
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain_community.document_loaders.pdf import PDFPlumberLoader

embedding = FastEmbedEmbeddings()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20, length_function=len,
                                               is_separator_regex=False)


def handle_pdf(file):
    loader = PDFPlumberLoader(file)
    # print("hello")
    # docs = loader.load_and_split()
    return "hello"


def convert_pdf(upload_file):
    contents = upload_file.file.read()
    temp_file = io.BytesIO()
    temp_file.write(contents)
    return temp_file
