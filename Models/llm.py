### chat models
from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv

load_dotenv()
llm=ChatGoogleGenerativeAI(model="gemini-2.5-flash",
                           temperature=0.1,max_output_tokens=5)
response=llm.invoke("what is the capital of india?")
print(response)

print("="*50)
print(response.content)

##openai
# from langchain_openai import ChatOpenAI
# from dotenv import load_dotenv

# load_dotenv()

# llm = ChatOpenAI(
#     model="gpt-4o-mini",
#     temperature=0
# )

# response = llm.invoke(
#     "What is LangChain? Explain in simple words."
# )

# print(response.content)