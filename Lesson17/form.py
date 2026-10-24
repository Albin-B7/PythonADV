import streamlit as st

with st.form ("my form", clear_on_submit=True):
    name = st.text_input("Name")

    age = st.slider("Age", min_value=0, max_value=100)

    email = st.text_input("Email")

    biography = st.text_area("Short bio")

    terms = st.checkbox("I agree to the terms and conditions")

    submit_button = st.form_submit_button(label="Submit")

if submit_button:
    st.write("Name of person is", name)
    st.write("Age of person is", age)
    st.write("Email of person is", email)
    st.write("Bio of person is", biography)

    if terms:
        st.write("You agreed to terms and conditions")
    else:
        st.write("You did not agreed to terms and conditions")