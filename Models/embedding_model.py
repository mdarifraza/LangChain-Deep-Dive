from langchain_google_genai import GoogleGenerativeAIEmbeddings
from dotenv import load_dotenv

load_dotenv()

embeddings = GoogleGenerativeAIEmbeddings(
    model="models/gemini-embedding-001",dimensions=32
)

vector = embeddings.embed_query(
    "What is LangChain?"
)

print(vector)
print(len(vector))