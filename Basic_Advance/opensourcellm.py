from langgraph.graph import StateGraph, END, START
from typing import TypedDict
from langchain_huggingface import HuggingFaceEndpoint, ChatHuggingFace
from dotenv import load_dotenv

load_dotenv()

llm = HuggingFaceEndpoint(
    repo_id="mistralai/Mistral-7B-Instruct-v0.2",
    task="text-generation",
    max_new_tokens=1000,
    temperature=0.1
)

model = ChatHuggingFace(llm=llm)

response = model.invoke(
    "Write a detailed blog post on the impact of artificial intelligence on modern healthcare."
)

print(response.content)

