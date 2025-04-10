from langchain_google_genai import GoogleGenerativeAI

from dotenv import load_dotenv
load_dotenv()

LLM= GoogleGenerativeAI(model="gemini-2.5-pro-exp-03-25", temperature= 0.2)

result= LLM.invoke("Name top 5 pakistan state name")
print(result)