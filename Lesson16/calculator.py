import streamlit as st
from jinja2.lexer import operators


def kalkulo(num1,num2,operations):
    if operations=="mbledhje":
        result = num1 + num2

    else:
        result = num1 - num2

    return result


def main():

    st.title("simple calculator")

    num1 = st.number_input("Sheno vleren e par")

    num2 = st.number_input("Sheno vleren e dyt")

    operations = st.radio("select an option", ["mbledhje", "zbritje"])

    result= kalkulo(num1,num2, operations)

    st.write(result)


if __name__=="__main__":
    main()