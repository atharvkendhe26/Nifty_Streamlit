import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sb
import streamlit as st

# App title
st.title("📈 Stock Closing Price Viewer")

# Load data
@st.cache_data
def load_data():
    df = pd.read_csv('Stocl.L.csv')
    df['Date'] = pd.to_datetime(df['Date'])
    return df

df = load_data()

# Stock selector
stocks = df['Stock'].unique()
st.sidebar.header("Controls")
selected_stock = st.sidebar.selectbox(
    "Select Stock",
    stocks
)

# Filter data
r = df[df['Stock'] == selected_stock].sort_values('Date')

# Plot
st.subheader(f"{selected_stock} Closing Price Over Time")

fig, ax = plt.subplots(figsize=(10, 5))
sb.lineplot(data=r, x='Date', y='Close', ax=ax)
ax.set_xlabel("Date")
ax.set_ylabel("Close Price")
ax.grid(True)

st.pyplot(fig)

# Optional: show raw data
with st.expander("📄 Show raw data"):
    st.dataframe(r)
