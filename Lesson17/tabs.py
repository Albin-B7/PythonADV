import streamlit as st

tab1,tab2,tab3 = st.tabs(["tab1","tab2","tab3"])

with tab1:
    st.header("content of tab 1")
    st.button("Click")

with tab2:
    st.header("content of tab 2")
    st.write("Welcome")

with tab3:
    st.header("content of tab 3")
    st.write("hello")