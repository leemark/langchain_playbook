# Import the dotenv module to load environment variables from a .env file
from dotenv import load_dotenv
# Load environment variables
load_dotenv()

# Import the ChatOpenAI class from the langchain_openai module
from langchain_openai import ChatOpenAI

# Initialize the ChatOpenAI object with the model 'gpt-3.5-turbo'
llm = ChatOpenAI(model="gpt-3.5-turbo")

# Define the query to be sent to the model
query = "Tell me a joke about Sam Altman."

# Use the 'invoke' method of the ChatOpenAI object to send the query and receive a response
response = llm.invoke(query)

# Print the content of the response to the console
print(response.content)
