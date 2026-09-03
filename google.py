from langchain_google_genai import ChatGoogleGenerativeAI
from dotenv import load_dotenv
load_dotenv()

model = ChatGoogleGenerativeAI(
    model="gemini-3.5-flash-lite"
)

response = model.invoke(
    "Tell me a brief introduction of the Netflix series Stranger Things."
)

print(response.content)