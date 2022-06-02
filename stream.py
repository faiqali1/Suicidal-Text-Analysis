import joblib

file_name = "finalized_model.sav"
loaded_model = joblib.load(file_name)
result = loaded_model.predict(["I like KFC", "I wanna die"])
print(result)

import streamlit as st
st.text_input("Text", key="user_text")

# You can access the value at any point with:
text = st.session_state.user_text
print(text)

result = loaded_model.predict([text])

st.write(result[0])

# remove Streamlit banner at the bottom.
hide_streamlit_style = """
            <style>
            footer {visibility: hidden;}
            </style>
            """
st.markdown(hide_streamlit_style, unsafe_allow_html=True)

