from langchain_community.llms import Ollama
from dotenv import load_dotenv
import os

load_dotenv()

llm = Ollama(model="llama3", base_url=os.getenv("BASEMODEL_URL"))

resp = llm.invoke("Tell about the story")

print(resp)