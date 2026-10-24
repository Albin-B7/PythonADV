import streamlit as st



def kalkulo(num1,num2,operations):
    if operations=="mbledhje":
        result = num1 + num2

    elif operations=="zbritje":
        result = num1 - num2

    elif operations=="shumzim":
        result = num1 * num2

    else:
        result = num1 / num2

    return result


def main():

    st.title("simple calculator")

    num1 = st.number_input("Sheno vleren e par")

    num2 = st.number_input("Sheno vleren e dyt")

    operations = st.radio("select an option", ["mbledhje", "zbritje","shumzim","pjestim"])

    result= kalkulo(num1,num2, operations)

    st.write(result)


if __name__=="__main__":
    main()