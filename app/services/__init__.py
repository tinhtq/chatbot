from langchain_community.llms import Ollama
from app.core import configs
from .text_splitter import handle_pdf


class Initializer:
    def __init__(self):
        self.llm = Ollama(model="llama3", base_url=configs.BASEMODEL_URL)

    def ask(self, prompt):
        resp = self.llm.invoke(prompt)
        return resp
