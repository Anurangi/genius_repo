# Import required libraries
from src.config import read_conf
import streamlit as st
from streamlit_chat import message
from openai import OpenAI
import time

conf = read_conf()
client = OpenAI(api_key=conf["openai"]["api_key"])
assistant = client.beta.assistants.create(
        name="Hotel butler",
        instructions="You are a helpful personal butler working in a luxury hotel. you answer the questions of the "
                     "guest by referring to the document that's provided. When asked for a recommendation, "
                     "ask for supporting information that will help you make a more relevant suggestion.  when "
                     "providing a meal suggestion provide suggestions for a main course, dessert item and a beverage. "
                     "always make sure that these 3 items are distinct items and are never the same item. When making "
                     "the recommendations for the main course, the dessert and the beverages always ensure that all 3 "
                     "of these are from the same type of restaurant and the same style of cuisine. When asked about "
                     "the activities to do at the hotel. Follow the given structure when returning the output for the "
                     "prompt { 'intent' : Look at the prompt and classify whether the prompt asks for a "
                     "recommendation about food or an activity to do at the hotel. If the prompt is asking a "
                     "recommendation then return the string 'recommendation' else return 'other', 'response' : your "
                     "response}",
        tools=[{"type": "retrieval"}],
        model=conf["openai"]["model"], file_ids=conf["openai"]["file_ids"]
    )
# create a thread
thread = client.beta.threads.create()

# Set streamlit page configuration
st.set_page_config(page_title="Hotel Butler")
st.title("Your Personal Hotel Butler!")

# Initialize session state variables
if 'generated' not in st.session_state:
    st.session_state['generated'] = []  # Store AI generated responses

if 'past' not in st.session_state:
    st.session_state['past'] = []  # Store past user inputs

if 'entered_prompt' not in st.session_state:
    st.session_state['entered_prompt'] = ""  # Store the latest user input


def generate_response(prompt):
    """
    Generate AI response using the ChatOpenAI model.
    """
    # Add message to the thread
    _ = client.beta.threads.messages.create(
        thread_id=thread.id,
        role="user",
        content=prompt
    )

    # create a run
    run = client.beta.threads.runs.create(
        thread_id=thread.id,
        assistant_id=assistant.id,
        instructions="Please address the user as Anuja."
    )

    while run.status in ['queued', 'in_progress', 'cancelling']:
        time.sleep(1)  # Wait for 1 second
        run = client.beta.threads.runs.retrieve(
            thread_id=thread.id,
            run_id=run.id
        )
    # return the response back to the user
    if run.status == 'completed':
        messages = client.beta.threads.messages.list(
            thread_id=thread.id
        )
        return messages.data[0].content[0].text.value
    else:
        return run.status


# Define function to submit user input
def submit():
    # Set entered_prompt to the current value of prompt_input
    st.session_state.entered_prompt = st.session_state.prompt_input
    # Clear prompt_input
    st.session_state.prompt_input = ""


# Create a text input for user
st.text_input('YOU: ', key='prompt_input', on_change=submit)

if st.session_state.entered_prompt != "":
    # Get user query
    user_query = st.session_state.entered_prompt

    # Append user query to past queries
    st.session_state.past.append(user_query)

    # Generate response
    output = generate_response(user_query)

    # Append AI response to generated responses
    st.session_state.generated.append(output)

# Display the chat history
if st.session_state['generated']:
    for i in range(len(st.session_state['generated']) - 1, -1, -1):
        # Display AI response
        message(st.session_state["generated"][i], key=str(i))
        # Display user message
        message(st.session_state['past'][i],
                is_user=True, key=str(i) + '_user')

# Add credit
st.markdown("""
---
Made with 🤖 by GENius CODERS""")
