import streamlit as st
import pandas as pd
import seaborn as sns
import matplotlib as plt
import plotly.express as px
import plotly.graph_objects as go

st.header("Adnan is learning machine learning")
st.text("Adnan is learning  python ka chilla")

phool = sns.load_dataset("iris")
st.write(phool.head())

fig = px.bar(phool, x="sepal_length", y="sepal_width", color="species")
st.plotly_chart(fig)

repellent = pd.read_csv('Average_data_repellent.csv')
st.write(repellent.head())


fig = px.bar(repellent, y="CPT", x="Test Group", color="Chamber", 
            title="Aedes aegypti deterence behaviour against three essential oils")
fig.update_xaxes(tickangle=50, tickfont=dict(family='Calibri', size=13, color='#04274a'))
fig.update_traces(width=0.7)
fig.update_layout(
    autosize=False,
    width=750,
    height=500)
st.plotly_chart(fig)



