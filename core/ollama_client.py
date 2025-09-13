from langchain_ollama import OllamaLLM
from langchain.memory import ConversationBufferMemory
from langchain.chains import ConversationChain

llm=OllamaLLM(Model="llama3")
memory=ConversationBufferMemory()

conv=ConversationChain(
  llm=llm,
  memory=memory,
  verbose=False
)

def ask_ollama(prompt):
  try:
    return conv.run(prompt)
  except Exception as e:
    return f"Ollama error : {e}"