# 💬 Customer Sentiment Analysis Dashboard

### 🌐 Live App: [https://pravs2025-sentiment-dashboard.streamlit.app](https://pravs2025-sentiment-dashboard.streamlit.app)

---

## 🧠 **Project Overview**

The **Customer Sentiment Analysis Dashboard** helps businesses analyze customer feedback and understand the overall sentiment toward their products.  
It uses **Natural Language Processing (NLP)** with **VADER Sentiment Analysis** to classify customer reviews as **Positive**, **Negative**, or **Neutral** — and visualizes these insights interactively.

---

## 🎯 **Objectives**

- Identify customer sentiment trends across multiple products  
- Help businesses improve product quality and customer satisfaction  
- Visualize insights in an easy-to-use Streamlit dashboard  

---

## ⚙️ **Tech Stack**

| Tool | Purpose |
|------|----------|
| **Python** | Core programming language |
| **Streamlit** | Web framework for dashboard |
| **Pandas** | Data manipulation and cleaning |
| **NLTK (VADER)** | Sentiment analysis |
| **Plotly** | Interactive data visualization |
| **Faker** | Generate realistic sample customer data |

---

## 🧩 **Features**

✅ Upload your own CSV dataset of customer reviews  
✅ Automatic text sentiment classification (Positive / Neutral / Negative)  
✅ Interactive charts for insights:
   - Pie chart for sentiment distribution  
   - Line chart for sentiment trend over time  
   - Bar chart for product-wise sentiment breakdown  
✅ KPIs for Total Reviews, Positive, and Negative counts  
✅ Data table preview of reviews with sentiment labels  

---

## 📊 **Dashboard Preview**

| Section | Description |
|----------|--------------|
| **Dataset Preview** | Displays the first few rows of uploaded customer reviews |
| **Sentiment KPIs** | Shows total, positive, and negative reviews |
| **Pie Chart** | Visual representation of sentiment share |
| **Line Chart** | Sentiment trend over time (if `Date` column exists) |
| **Bar Chart** | Product-level sentiment distribution |
| **Data Table** | Displays customer names, product, review text, and sentiment |

---

## 🧠 **Model Used**

**VADER (Valence Aware Dictionary and Sentiment Reasoner)**  
A rule-based sentiment analysis model that works exceptionally well on text like product reviews and social media data.

Sentiment classification logic:
```python
if compound > 0.05 → Positive  
if compound < -0.05 → Negative  
otherwise → Neutral
