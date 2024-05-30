from langchain_community.llms import Ollama
from app.core import configs


class Initializer():
    def __init__(self):
        self.llm = Ollama(model="llama3", base_url=configs.BASEMODEL_URL)

    def invoke(self, prompt: str):
        resp = self.llm.Invoke(prompt)
        print(resp)
