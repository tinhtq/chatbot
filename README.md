# Building Backend AI Chatbot

## Pre-setup

Execute the below command to create docker ollama
```
docker run -d -v ollama:/root/.ollama -p 11434:11434 --name ollama ollama/ollama
```
Pull model llama3
```
docker exec ollama ollama pull llama3  
```
