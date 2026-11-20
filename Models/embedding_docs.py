from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",dimensions=32
)
documents=["Delhi is capital ofindia",
           "Mumbai is capital of maharashtra",
           "Bangalore is capital of karnataka",]


vector = embeddings.embed_documents(documents)

print(str(vector))
print(len(vector))