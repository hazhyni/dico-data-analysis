import datetime
import random

import altair as alt
import numpy as np
import pandas as pd
import streamlit as st

# Show app title and description.
st.set_page_config(page_title="E-commerce Data Analysis",
                   page_icon=":shopping_bags:")
st.write(
    """
# :shopping_bags: Brazilian E-Commerce Public Dataset by Olist

**Welcome to Hazhiyah Yumni's Data Analysis X Dicoding Indonesia!**
This App will help you to know the business improvement over their history and data
"""
)

# Show section to view and edit existing tickets in a table.
st.header("Sales Trend Over Time")
st.write(f"Nama Tabel: `orders.csv`")
st.info("Let's check this out!")


def load_data(url):
    df = pd.read_csv(url)  # 👈 Download the data
    return df

df = load_data(
    "data/visual1.csv")
st.dataframe(df)

arr = np.random.normal(1, 1, size=100)
fig, ax = plt.subplots()
ax.hist(arr, bins=20)

st.pyplot(fig)
