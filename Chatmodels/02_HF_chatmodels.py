from langchain_huggingface import HuggingFaceEndpoint , ChatHuggingFace

from dotenv import load_dotenv

load_dotenv()

llm= HuggingFaceEndpoint(repo_id="TinyLlama/TinyLlama-1.1B-Chat-v1.0",
    task="text-generation")


Chat_model= ChatHuggingFace(llm=llm)

result= Chat_model.invoke("Who is President of India")
print(result.content)