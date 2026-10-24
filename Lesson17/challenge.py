
import streamlit as st

if "people" not in st.session_state:
    st.session_state.people = []

st.title("Person Information")

user_input = st.text_input("Enter name")

age = st.number_input("Enter age", min_value=0, max_value=100, step=1)

weight = st.number_input(
    "Enter Weight in Kilograms [kg]",
    min_value=0.0,
    max_value=300.0,
    step=0.5
)

height = st.number_input(
    "Enter height in centimeters [cm]",
    min_value=0.0,
    max_value=250.0,
    step=0.5
)

if st.button("Add Person"):
    if user_input.strip():
        person = {
            "Name": user_input,
            "Age": age,
            "Weight (kg)": weight,
            "Height (cm)": height
        }

        st.session_state.people.append(person)
        st.success("Person added successfully!")
    else:
        st.warning("Please enter a name.")

# Display all added people
st.subheader("All People")

if st.session_state.people:
    st.dataframe(
        st.session_state.people,
        use_container_width=True,
        hide_index=True
    )
else:
    st.info("No people added yet.")