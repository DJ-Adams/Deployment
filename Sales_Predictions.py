## Import necessary packages
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO
import plotly as px
import Custom_Functions as fn


## TODO

## Global Variables
st.image('Images/Sales_Image.jpg')
## Data

## Image, title and Markdown subheader

st.title('Sales Price Analysis')
st.markdown("Data [Sales 2023](https://drive.google.com/file/d/1syH81TVrbBsdymLT_jl2JIf6IjPXtSQw/view)")
st.header("Product Sales Data")
## TODO


# @st.cache_data
def load_data():
    df = pd.read_csv('Data/2023_Sales_Preds_Clean.csv')
    return df
df = load_data()
## Display DataFrame
st.dataframe(df)
## TODO

## .info()
## Get string for .info()

## TODO

## Display .info()

## TODO

## Descriptive Statistics Subheader
## Descriptive Statistics
st.subheader('**Descriptive Statistics**')


## Button for Statistics
show_stats = st.button('Show Descriptive Statistics')
if show_stats:
    describe = df.describe()
    st.dataframe(describe)
## TODO
## Show Summary
## Get info as text
buffer = StringIO()
df.info(buf=buffer)
summary_info = buffer.getvalue()

st.subheader('**Summary Info**')

summary = st.button('Show Summary Info')
if summary:
    st.text(summary_info)


# display null values with button
st.markdown("#### Null Values")
nulls =df.isna().sum()
if st.button('Show Null Values'):
    st.dataframe(nulls)
    
    
## Eda Plots subheader

## TODO

## selectbox for columns

## TODO

## Conditional: if column was chosen

## TODO

    ## Check if column is object or numeric and use appropriate plot function

    ## TODO

    ## Show plot
    
    ## TODO
    
## Feature vs Target

## Create sidebar button

    ## Check if feature is numeric or object


    ## Display appropriate comparison