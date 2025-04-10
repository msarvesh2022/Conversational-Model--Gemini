import streamlit as st
from langchain_google_genai import GoogleGenerativeAI
from dotenv import load_dotenv
import os

# Load environment variables
load_dotenv()

# Make sure we have the API key
api_key = os.getenv("GOOGLE_API_KEY")
if not api_key:
    st.error("GOOGLE_API_KEY not found. Please set it in your .env file or environment variables.")
    st.stop()

# Set page config
st.set_page_config(page_title="Gemini AI Assistant", page_icon="🤖")

# Initialize the LLM
@st.cache_resource
def get_llm():
    return GoogleGenerativeAI(model="gemini-2.5-pro-exp-03-25", temperature=0.2)

# App UI
st.title("🤖 Gemini AI Assistant")
st.write("Ask me anything, and I'll try to help!")

# Input area
query = st.text_input("Type your question here...", key="query")
submit_button = st.button("Ask Gemini")

# Display response
if submit_button and query:
    with st.spinner("Generating response..."):
        try:
            llm = get_llm()
            result = llm.invoke(query)
            
            st.markdown("### Answer:")
            st.write(result)
        except Exception as e:
            st.error(f"An error occurred: {str(e)}")
            
# Add some styling and instructions
st.markdown("""
---
### How to use:
1. Type your question in the text box
2. Click 'Ask Gemini' button
3. Wait for the AI to generate a response
""")

# Sidebar with information
with st.sidebar:
    st.header("About")
    st.write("This is a simple AI assistant powered by Google's Gemini API.")
    st.write("Built with Streamlit and LangChain.") 