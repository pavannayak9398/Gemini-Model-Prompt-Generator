import os
import streamlit as st
import google.generativeai as genai


# Set up the API key
os.environ['GEMINI_API_KEY'] = 'AIzaSyDKUBG7p5o7fcHXYwQjm5ih9h2ue6WxDXQ'  # Replace with your actual API key
genai.configure(api_key=os.environ['GEMINI_API_KEY'])

# List of available Gemini models
AVAILABLE_MODELS = [
    "gemini-1.5-pro",
    "gemini-1.0-pro",
    "gemini-1.5-flash",
]

# Custom CSS for modern design
st.markdown(
    """
    <style>
    @import url('https://fonts.googleapis.com/css2?family=Poppins:wght@300;400;600&display=swap');

    html, body, [class*="st"] {
        font-family: 'Poppins', sans-serif;
    }

    body {
        background: linear-gradient(135deg, #667eea, #764ba2);
        color: #ffffff;
    }

    .stApp {
        background-color: rgba(0, 0, 0, 0.6);
        padding: 2rem;
        border-radius: 15px;
        margin: 2rem auto;
        max-width: 800px;
        box-shadow: 0px 0px 20px rgba(0, 0, 0, 0.3);
    }

    .stTextArea, .stSelectbox, .stButton {
        background-color: #ffffff;
        color: #333333;
        border-radius: 10px;
        padding: 0.8rem;
        box-shadow: 0px 5px 10px rgba(0, 0, 0, 0.1);
    }

    .stButton button {
        background-color: #ff7e5f;
        color: #ffffff;
        border: none;
        padding: 0.8rem 1.5rem;
        border-radius: 10px;
        font-size: 1rem;
        cursor: pointer;
        transition: background-color 0.3s ease;
    }

    .stButton button:hover {
        background-color: #ff6b4a;
    }

    .response-box {
        background-color: rgba(255, 255, 255, 0.9);
        color: #333333;
        padding: 1.5rem;
        border-radius: 10px;
        box-shadow: 0px 5px 15px rgba(0, 0, 0, 0.2);
        margin-top: 2rem;
    }

    h1 {
        text-align: center;
        font-weight: 600;
    }

    .footer {
        text-align: center;
        margin-top: 3rem;
        font-size: 0.9rem;
        color: #ddd;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Streamlit UI
st.title("🚀 Gemini Model Prompt Generator")
st.write("Generate responses using different Gemini models with a modern and stylish interface.")

# User input for the prompt
prompt = st.text_area("Enter your prompt:", "What is the meaning of dream & goal? How to reach the dream?")

# Dropdown to select the model
selected_model = st.selectbox("Select a Gemini model:", AVAILABLE_MODELS)

# Button to generate response
if st.button("Generate Response"):
    if prompt:
        try:
            # Initialize the selected Gemini model
            model = genai.GenerativeModel(selected_model)
            response = model.generate_content(prompt)

            # Display the response inside a styled container
            st.subheader("Generated Response:")
            st.markdown(f"<div class='response-box'>{response.text}</div>", unsafe_allow_html=True)
        except Exception as e:
            st.error(f"An error occurred: {e}")
    else:
        st.warning("Please enter a prompt before generating a response.")

# Footer
st.markdown("<div class='footer'>Built using Streamlit and Google Gemini Models</div>", unsafe_allow_html=True)
