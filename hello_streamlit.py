# hello_streamlit.py
import streamlit as st

st.title('Hello, Streamlit!')

# Get user name
name = st.text_input("First Name", value = "Coding Dojo")
# Print message with user name
# If the button is pressed, print the message
if st.button("Say hello."):
    st.write(f"Hello, World! My name is {name}.")
# Get date information
# Updated date input with minimum and default values
import datetime as dt
date = st.date_input(label="Date of Birth", min_value=dt.date(1900,1,1), value=dt.date(2013,1,1))

# Create the select box with all options
season = st.selectbox("Favorite Season", ['Winter','Spring','Summer','Fall'])

# Add slider, text to be displayed, min value, max value, and default value
excitement = st.slider("How excited are you to learn Streamlit?? (1=Not at all; 10=Very!)",min_value=1, max_value=10,value=5)

# If the button is pressed, print message
if st.button("Introduce me!"):
    st.markdown(f"""
    > #### ***Hello, World!*** My name is {name}.
    - I was born on **{date}**.
    - My favorite season is **{season}**.
    - My excitement for learning streamlit is... **{excitement}/10.**""")
























