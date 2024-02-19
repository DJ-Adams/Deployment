## Import necessary packages
import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
from io import StringIO
import plotly as px
import Custom_Functions as fn
import plotly.express as px
import plotly.io as pio
pio.templates.default='seaborn'

## TODO

## Global Variables
st.image('Images/Sales_Image.jpg')
## Data

## Image, title and Markdown subheader

st.title('Outlet Sales Analysis')
st.markdown("Data [Sales 2023](https://drive.google.com/file/d/1syH81TVrbBsdymLT_jl2JIf6IjPXtSQw/view)")
st.header("Outlet Sales Data")
## TODO


# @st.cache_data
def load_data():
    df = pd.read_csv('Data/2023_Sales_Preds_Clean.csv')
    return df
df = load_data()

## Columns for EDA
columns = df.columns
features = [col for col in columns if col != 'Item_Outlet_Sales']
target = 'Item_Outlet_Sales'

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
    

# Copy list of columns

# Remove target from list of features



## Eda Plots subheader
## Eda Plots
st.subheader('Explore a Column')

## selectbox for columns
eda_column = st.selectbox('Column to Explore', columns, index=None)


## Conditional: if column was chosen
if eda_column:
    ## Check if column is object or numeric and use appropriate plot function
    if df[eda_column].dtype == 'object':
        fig = fn.explore_categorical(df, eda_column)
    else:
        fig = fn.explore_numeric(df, eda_column)

    ## Show plot
    st.subheader(f'Display Descriptive Plots for {eda_column}')
    st.pyplot(fig)

## Feature vs Target

feature_vs_target = st.sidebar.selectbox('Compare Feature to Target', features, index=None)

if feature_vs_target:
    ## Check if feature is numeric or object
    if df[feature_vs_target].dtype == 'object':
        comparison = df.groupby('Item_Outlet_Sales').count()
        title = f'Count of {feature_vs_target} by {target}'
    else:
        comparison = df.groupby('Item_Outlet_Sales').mean()
        title = f'Mean {feature_vs_target} by {target}'

    ## Display appropriate comparison
    pfig = px.bar(comparison, y=feature_vs_target, title=title)
    st.plotly_chart(pfig)
