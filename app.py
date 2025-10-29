import pandas as pd
import streamlit as st
import plotly.express as px
import nltk
from nltk.sentiment.vader import SentimentIntensityAnalyzer

# Download VADER sentiment lexicon
nltk.download('vader_lexicon')

# Page configuration
st.set_page_config(page_title="Customer Sentiment Dashboard", layout="wide", page_icon="💬")

# Title and intro
st.title("💬 Customer Sentiment Analysis Dashboard")
st.markdown("Analyze customer reviews and visualize sentiment trends across products.")

# Upload CSV file (or load default)
uploaded_file = st.file_uploader("📂 Upload a CSV file", type=["csv"])

if uploaded_file:
    df = pd.read_csv(uploaded_file)
else:
    df = pd.read_csv("customer_reviews_500.csv")

# Display dataset preview
st.subheader("📄 Dataset Preview")
st.dataframe(df.head())

# Sentiment Analysis using VADER
sid = SentimentIntensityAnalyzer()
df["compound"] = df["Review_Text"].apply(lambda x: sid.polarity_scores(str(x))["compound"])
df["Sentiment"] = df["compound"].apply(lambda x: "Positive" if x > 0.05 else ("Negative" if x < -0.05 else "Neutral"))

# --- KPIs ---
total = len(df)
pos = len(df[df["Sentiment"] == "Positive"])
neg = len(df[df["Sentiment"] == "Negative"])
neu = len(df[df["Sentiment"] == "Neutral"])

col1, col2, col3 = st.columns(3)
col1.metric("Total Reviews", total)
col2.metric("Positive", pos)
col3.metric("Negative", neg)

# --- Pie Chart ---
fig_pie = px.pie(
    df,
    names="Sentiment",
    title="Sentiment Distribution",
    hole=0.4,
    color_discrete_map={"Positive": "green", "Negative": "red", "Neutral": "gray"}
)
st.plotly_chart(fig_pie, use_container_width=True)

# --- Line Chart (if Date column exists) ---
if "Date" in df.columns:
    df["Date"] = pd.to_datetime(df["Date"])
    trend = df.groupby(["Date", "Sentiment"]).size().reset_index(name="Count")
    fig_trend = px.line(trend, x="Date", y="Count", color="Sentiment", title="📈 Sentiment Trend Over Time")
    st.plotly_chart(fig_trend, use_container_width=True)

# --- Product-wise Sentiment Breakdown ---
product_summary = df.groupby(["Product_Name", "Sentiment"]).size().reset_index(name="Count")
fig_bar = px.bar(product_summary, x="Product_Name", y="Count", color="Sentiment",
                 title="🛍️ Sentiment Breakdown by Product", barmode="stack")
st.plotly_chart(fig_bar, use_container_width=True)

# --- Data Table ---
st.subheader("📋 Review Sentiment Table")
st.dataframe(df[["Customer_Name", "Product_Name", "Review_Text", "Sentiment"]].head(20))


