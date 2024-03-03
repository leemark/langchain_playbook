#get environment variables
from dotenv import load_dotenv
load_dotenv()

from langchain_openai import ChatOpenAI

llm = ChatOpenAI(model="gpt-3.5-turbo")

query = "Tell me a joke about Sam Altman."
response =llm.invoke(query)

print(response.content)