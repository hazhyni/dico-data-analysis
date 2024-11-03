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
This App will help you to know business improvement according to the data provided.
"""
)

# Dashboard sidebar
st.title('Dashboard')
add_selectbox = st.sidebar.selectbox(
    'Which Question In Your Mind?',
    ('Sales Trend', 'Top Sales', 'Most Used Payment',
     'Delivery Services', 'Negative Feedback Checker')
)

# Show section to view and edit existing tickets in a table.
st.header("Sales Trend Over Time")
st.write(f"Data Required: `orders.csv`, `order_items.csv`, `order_payments.csv`, `order_reviews.csv`, `products.csv`, `sellers.csv`, `customers.csv`, `geolocation")
st.info(
    "As a analyst, We need to know more about sales trends and their total revenue to make the right decisions.",
    "Here's our clean and structured data to analyze.")

def load_data(url):
    df = pd.read_csv(url)  # 👈 Download the data
    return df

df = load_data(
    "data/visual1.csv")
st.dataframe(df)
# Generate data

# Set the title of the app
st.title('Matplotlib with Streamlit Example')

# Generate data
x = np.linspace(0, 10, 100)
y = np.sin(x)

# Create a Matplotlib figure
fig, ax = plt.subplots()
ax.plot(x, y)
ax.set_title('Sine Wave')
ax.set_xlabel('X-axis')
ax.set_ylabel('Y-axis')

# Display the plot in Streamlit
st.pyplot(fig)
