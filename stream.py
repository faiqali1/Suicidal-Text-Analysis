import joblib
import streamlit as st

file_name = "finalized_model.sav"
loaded_model = joblib.load(file_name)

st.title("Suicide Analysis")
# st.header("Suicide Analysis")

st.markdown("Enter text below to see whether the text you have entered is suicidal or not.")

# removing the streamlit banner at the bottom
hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

st.text_input("Text", key="user_text")

# You can access the value at any point with:
text = st.session_state.user_text
print(text)

result = loaded_model.predict([text])

st.write(result[0])

# Run `python -m streamlit run stream.py`
# to run the file
