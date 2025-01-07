import streamlit as st
from pymongo import MongoClient
import pandas as pd
import matplotlib.pyplot as plt

# MongoDB connection
mongo_client = MongoClient("mongodb://localhost:27017/")
mongo_db = mongo_client["user_activity_db"]
mongo_collection = mongo_db["user_activity"]

# Fetch data from MongoDB
data = list(mongo_collection.find())
df = pd.DataFrame(data)

# Convert timestamp to datetime
df['timestamp'] = pd.to_datetime(df['timestamp'])

# Set up Streamlit app
st.title("User Activity Dashboard")

# Visualization 1: Activity distribution
st.subheader("1. Activity Distribution")
activity_counts = df['activity'].value_counts()

fig1, ax1 = plt.subplots()
activity_counts.plot(kind='bar', ax=ax1)
ax1.set_title("Activity Distribution")
ax1.set_xlabel("Activity")
ax1.set_ylabel("Count")
st.pyplot(fig1)

# Visualization 2: User-specific activity count
st.subheader("2. User-specific Activity Count")
user_activity_counts = df['user_id'].value_counts()

fig2, ax2 = plt.subplots()
user_activity_counts.head(10).plot(kind='bar', ax=ax2)  # Top 10 users
ax2.set_title("Top 10 Active Users")
ax2.set_xlabel("User ID")
ax2.set_ylabel("Count")
st.pyplot(fig2)

# Visualization 3: Purchases over time
st.subheader("3. Purchases Over Time")
purchase_data = df[df['activity'] == 'purchase']
purchase_trend = purchase_data.groupby(purchase_data['timestamp'].dt.minute).size()

fig3, ax3 = plt.subplots()
purchase_trend.plot(kind='line', ax=ax3)
ax3.set_title("Purchases Over Time (by Minute)")
ax3.set_xlabel("Minute")
ax3.set_ylabel("Purchase Count")
st.pyplot(fig3)