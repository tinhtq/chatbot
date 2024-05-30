from langchain_community.llms import Ollama

llm = Ollama(model="llama3", base_url="http://localhost:11434")

resp = llm.invoke("Tell about the story")

print(resp)