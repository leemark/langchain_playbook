# NOTE: since this script uses streamlit, it must be run with "streamlit run <filename>"

# Import required modules
from dotenv import load_dotenv  # To load environment variables
from langchain_core.messages import HumanMessage, AIMessage  # Import message classes
from langchain_core.prompts import ChatPromptTemplate  # Import prompt template class
from langchain_core.output_parsers import StrOutputParser  # Import output parser
from langchain_openai import ChatOpenAI  # Import ChatOpenAI for OpenAI interactions
import streamlit as st  # Import Streamlit for web app functionality

# Load environment variables from .env file
load_dotenv()

# Initialize session state for chat history if it doesn't exist
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Set Streamlit page configuration
st.set_page_config(page_title="LangChain Streaming", page_icon=":robot:")

# Display the title of the web page
st.title("LangChain Streaming w/Streamlit")

# Function to generate AI response based on user prompt and chat history
def generate_response(user_prompt, chat_history):
    # Define the prompt template for generating responses
    template = """
        You are an AI assistant who is helpful, creative, clever, and very friendly. 
        Answer the user's question while taking into account the previous conversation below.

        Previous conversation:{chat_history}

        User's question: {user_prompt}
    """
    # Create a chat prompt template from the template string
    prompt = ChatPromptTemplate.from_template(template)
    
    # Initialize the language model with a specific model
    llm = ChatOpenAI(model="gpt-3.5-turbo")
    
    # Initialize the output parser to parse string outputs
    output_parser = StrOutputParser()
    
    # Create a processing chain combining the prompt, language model, and output parser
    chain = prompt | llm | output_parser
    
    # Execute the chain using stream (rather than invoke) with the provided user prompt and chat history, and return the response
    return chain.stream({"user_prompt": user_prompt, "chat_history": chat_history})

# Display previous messages from chat history
for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.markdown(message.content)
    else:
        with st.chat_message("AI"):
            st.markdown(message.content)

# Input field for user to ask a question
user_prompt = st.chat_input("Ask a question:")

# Check if user prompt is not empty
if user_prompt is not None and user_prompt != "":
    # Append user's message to chat history
    st.session_state.chat_history.append(HumanMessage(content=user_prompt))
    
    # Display user's message
    with st.chat_message("Human"):
        st.markdown(user_prompt)
    
    # Generate and display AI response
    with st.chat_message("AI"):
        # for streaming, need use write_stream and run the generator inside of it 
        ai_response = st.write_stream(generate_response(user_prompt, st.session_state.chat_history))
        st.session_state.chat_history.append(AIMessage(content=ai_response))
