import streamlit as st
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

st.set_page_config(page_title="ZomatoX Dashboard", layout="wide")
st.title("🍽️ ZomatoX — Restaurant Data Analysis")
st.markdown("Exploratory Data Analysis on Zomato Restaurant Dataset")

# Load Data
@st.cache_data
def load_data():
    df = pd.read_csv("Zomato data .csv")
    df['rate'] = df['rate'].astype(str).str.replace('/5', '').str.strip()
    df['rate'] = pd.to_numeric(df['rate'], errors='coerce')
    return df

df = load_data()

# Sidebar Filters
st.sidebar.header("Filters")
restaurant_type = st.sidebar.multiselect(
    "Select Restaurant Type",
    options=df['listed_in(type)'].unique(),
    default=df['listed_in(type)'].unique()
)
online_order = st.sidebar.radio("Online Order", ["All", "Yes", "No"])

# Apply Filters
filtered_df = df[df['listed_in(type)'].isin(restaurant_type)]
if online_order != "All":
    filtered_df = filtered_df[filtered_df['online_order'] == online_order]

# KPI Metrics
st.markdown("### 📊 Key Metrics")
col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Restaurants", len(filtered_df))
col2.metric("Avg Rating", round(filtered_df['rate'].mean(), 2))
col3.metric("Avg Cost for Two", f"₹{round(filtered_df['approx_cost(for two people)'].mean(), 0)}")
col4.metric("Total Votes", filtered_df['votes'].sum())

st.markdown("---")

# Q1 - Restaurant Type Distribution
st.markdown("### Q1: Most Popular Restaurant Types")
fig1, ax1 = plt.subplots(figsize=(10, 4))
sns.countplot(data=filtered_df, x='listed_in(type)', palette='Set2', ax=ax1)
ax1.set_xlabel("Restaurant Type")
ax1.set_ylabel("Count")
plt.xticks(rotation=45)
st.pyplot(fig1)

# Q2 - Votes by Restaurant Type
st.markdown("### Q2: Votes by Restaurant Type")
votes_df = filtered_df.groupby('listed_in(type)')['votes'].sum().reset_index()
fig2, ax2 = plt.subplots(figsize=(10, 4))
sns.barplot(data=votes_df, x='listed_in(type)', y='votes', palette='Set1', ax=ax2)
ax2.set_xlabel("Restaurant Type")
ax2.set_ylabel("Total Votes")
plt.xticks(rotation=45)
st.pyplot(fig2)

# Q3 - Rating Distribution
st.markdown("### Q3: Rating Distribution")
fig3, ax3 = plt.subplots(figsize=(10, 4))
ax3.hist(filtered_df['rate'].dropna(), bins=20, color='steelblue', edgecolor='black')
ax3.set_xlabel("Rating")
ax3.set_ylabel("Count")
st.pyplot(fig3)

# Q4 - Spending Pattern
st.markdown("### Q4: Couple Spending Pattern")
fig4, ax4 = plt.subplots(figsize=(10, 4))
ax4.hist(filtered_df['approx_cost(for two people)'].dropna(), 
         bins=20, color='coral', edgecolor='black')
ax4.set_xlabel("Approx Cost for Two (₹)")
ax4.set_ylabel("Count")
st.pyplot(fig4)

# Q5 - Online vs Offline Ratings
st.markdown("### Q5: Online vs Offline Order Ratings")
fig5, ax5 = plt.subplots(figsize=(8, 5))
sns.boxplot(data=filtered_df, x='online_order', y='rate', palette='pastel', ax=ax5)
ax5.set_xlabel("Online Order")
ax5.set_ylabel("Rating")
st.pyplot(fig5)

# Q6 - Heatmap
st.markdown("### Q6: Restaurant Type vs Online Order Heatmap")
pivot = filtered_df.pivot_table(
    index='listed_in(type)', 
    columns='online_order', 
    aggfunc='count', 
    values='name'
)
fig6, ax6 = plt.subplots(figsize=(8, 5))
sns.heatmap(pivot, annot=True, fmt='.0f', cmap='YlOrRd', ax=ax6)
st.pyplot(fig6)

st.markdown("---")
st.caption("Built by Aishwarya Deshwal | ZomatoX Data Analysis Project")
 