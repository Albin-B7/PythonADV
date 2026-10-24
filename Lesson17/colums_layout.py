import streamlit as st

col1,col2,col3,col4,col5 = st.columns(5, gap="small", vertical_alignment="center")

with col1:
    st.header("Kolona e par")

    st.write("Kjo eshte kolona e par")

with col2:
    st.header("Kolona e dyt")

    st.write("Kjo eshte kolona e dyt")

with col3:
    st.header("Kolona e tret")

    st.write("Kjo eshte kolona e tret")

with col4:
    st.header("Kolona e katert")

    st.write("Kjo eshte kolona e katert")

with col5:
    st.header("Kolona e pest")

    st.write("Kjo eshte kolona e pest")