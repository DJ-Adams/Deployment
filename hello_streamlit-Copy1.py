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








# Let's also add a widget for favorite seasons. Rather than open-ended text, we will provide a list of options from a drop-down menu.


# In addition to a text box, we can obtain information for dates, from select boxes, or sliders.  with st.date_input


# The final piece of our app will be a slider that accepts a value from 1 to 10. This will be the user's excitement for learning streamlit!

# Wrap all input within our button. To finalize our app, we will add print statements for each of our inputs, and wrap them in a single conditional button.





st.header("Display text and examples are below")


# Explore title, headers, and subheaders
st.title("This is a Title")
st.header("This is a Header")
st.subheader("This is a Subheader")


# Text and Markdown are created with the below commands


# Basic text
st.write("This is standard text")
# Markdown-example shows bold and italics
st.markdown("This is markdown showing **bold** and *italics*")



# Dataframes: Streamlit can display Pandas dataframes.


# Create a simple dataframe
import pandas as pd
df = pd.DataFrame({'A':[1,2,3],"B":[5,6,7]})
# Display dataframe
st.dataframe(df)



# Interactive Features: Our goal will be to allow users to input their names, and our app will then provide a personalized introduction code is above






















