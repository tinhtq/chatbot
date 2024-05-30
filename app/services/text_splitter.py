from langchain.text_splitter import RecursiveCharacterTextSplitter
from langchain_community.embeddings.fastembed import FastEmbedEmbeddings
from langchain.document_loaders import PDFPlumberLoader

embedding = FastEmbedEmbeddings()

text_splitter = RecursiveCharacterTextSplitter(chunk_size=100, chunk_overlap=20, length_function=len, is_separator_regex=False)


def handle_pdf(file):
    loader = PDFPlumberLoader(file)
    docs = loader.load_and_split()
    return len(docs)