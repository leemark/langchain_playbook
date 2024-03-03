# NOTE: since this script uses streamlit, it must be run with "streamlit run <filename>"

# Import required modules
from dotenv import load_dotenv  # To load environment variables
from langchain_core.messages import HumanMessage, AIMessage  # Import message classes for handling chat messages
import streamlit as st  # Import Streamlit for web app functionality

# Load environment variables from .env file
load_dotenv()

# Initialize session state for chat history if it doesn't exist
# This is used to store the conversation history between the user and AI
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# Set Streamlit page configuration with a title and a page icon
st.set_page_config(page_title="LangChain Streaming", page_icon=":robot:")

# Display the title of the web page
st.title("LangChain Streaming")

# Display previous messages from chat history
# This loop goes through each message in the chat history and displays it
# according to whether it's a message from the human user or the AI
for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.markdown(message.content)
    else:
        with st.chat_message("AI"):
            st.markdown(message.content)

# Input field for the user to ask a question
user_prompt = st.chat_input("Ask a question:")

# Check if the user prompt is not empty to process it
if user_prompt is not None and user_prompt != "":
    # Append the user's message to the chat history
    st.session_state.chat_history.append(HumanMessage(content=user_prompt))

    # Display the user's message in the chat interface
    with st.chat_message("Human"):
        st.markdown(user_prompt)

    # Since this script doesn't actually generate an AI response,
    # we simulate an AI response with a static message for demonstration purposes
    with st.chat_message("AI"):
        ai_response = "lol lol"  # Static AI response
        st.markdown(ai_response)  # Display the AI response
    
    # Append the AI's response to the chat history for future reference
    st.session_state.chat_history.append(AIMessage(content=ai_response))
