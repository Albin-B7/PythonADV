import streamlit as st

st.sidebar.header("Sidebar")

st.sidebar.write("this is sidebar")

st.sidebar.selectbox("chose options", ["Option 1", "Option 2", "Option 3"])
st.sidebar.radio("Go to", ["Home", "settings"])