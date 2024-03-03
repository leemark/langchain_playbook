#get environment variables
from dotenv import load_dotenv
load_dotenv()

from langchain_core.messages import HumanMessage, AIMessage
import streamlit as st

if "chat_history" not in st.session_state:
    st.session_state.chat_history = []


st.set_page_config(page_title="LangChain Streaming", page_icon=":robot:")

st.title("LangChain Streaming")

for message in st.session_state.chat_history:
    if isinstance(message, HumanMessage):
        with st.chat_message("Human"):
            st.markdown(message.content)
    else:
        with st.chat_message("AI"):
            st.markdown(message.content)
                    


user_prompt = st.chat_input("Ask a question:")
if user_prompt is not None and user_prompt != "":
    st.session_state.chat_history.append(HumanMessage(content=user_prompt))

    with st.chat_message("Human"):
        st.markdown(user_prompt)

    with st.chat_message("AI"):
        ai_response = "lol  lol"
        st.markdown(ai_response)
    st.session_state.chat_history.append(AIMessage(content=ai_response))
