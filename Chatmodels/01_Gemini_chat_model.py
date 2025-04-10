from langchain_google_genai import ChatGoogleGenerativeAI

from dotenv import load_dotenv
load_dotenv()

LLM= ChatGoogleGenerativeAI(model="models/gemini-2.0-flash")

result= LLM.invoke("Who won cricket world cup 2011")
print(result)
