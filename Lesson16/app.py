import streamlit as st
from pyexpat.errors import messages


if st.button("Click me"):
    st.write("Button has been clicked")

if st.checkbox("check me to show text"):
    st.write("you are seeing this because you checked the checkbox")


user_input = st.text_input("Enter some text")

st.write("You entered: ", user_input)

age = st.number_input("Enter age", min_value=0, max_value=100)

st.write(f"your age is {age}")

message3 = st.text_area("Enter a message")

st.write("you have entered ", message3)

choice = st.radio("pick one", ["ai", "python adv", "code 1"])

if st.button("Success"):
    st.success("Operation was succesful")



try:
    1/0

except Exception as e:
    st.exception(e)
