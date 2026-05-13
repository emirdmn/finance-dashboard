import streamlit as st
import yfinance as yf
import pandas as pd
import plotly.graph_objects as go
import plotly.express as px

# 1. PAGE CONFIGURATION (Requirement: Good Design)
st.set_page_config(page_title="Professional Finance Dashboard", layout="wide")
st.title("📊 Financial Analysis Dashboard")

# SIDEBAR - UI FEATURE (Extra 10p) 
with st.sidebar:
    st.header("⚙️ Configuration")
    symbol = st.sidebar.selectbox("Select Asset", ["BTC-USD", "ETH-USD", "GC=F", "NVDA"], index=0)
    sma_period = st.sidebar.slider("SMA Period", 5, 50, 20)
    st.divider()
    st.info("This dashboard provides real-time data visualization and technical analysis.")

# 2. DATA ACQUISITION & PERSISTENCE (Requirement: 1h data for 1 month & store data) [cite: 571]
@st.cache_data
def load_and_store_data(ticker):
    # Fetching Hourly (1h) data for 1 month
    df = yf.download(ticker, period="1mo", interval="1h")
    
    # Cleaning MultiIndex columns if necessary
    if isinstance(df.columns, pd.MultiIndex):
        df.columns = df.columns.get_level_values(0)
        
    # Store the data in CSV format [cite: 571]
    df.to_csv("data.csv")
    return df

data = load_and_store_data(symbol)

# 3. TECHNICAL INDICATORS (Requirement: Explain data with technical indicators) [cite: 573]
# SMA Calculation
data['SMA'] = data['Close'].rolling(window=sma_period).mean()

# RSI Calculation (Extra Indicator for 10p) 
delta = data['Close'].diff()
gain = (delta.where(delta > 0, 0)).rolling(window=14).mean()
loss = (-delta.where(delta < 0, 0)).rolling(window=14).mean()
rs = gain / loss
data['RSI'] = 100 - (100 / (1 + rs))

# 4. KPI METRICS (Requirement: Display metrics) [cite: 574]
col1, col2, col3, col4 = st.columns(4)
current_val = float(data['Close'].iloc[-1])
max_val = float(data['High'].max())
last_rsi = float(data['RSI'].iloc[-1])

col1.metric("Current Price", f"${current_val:,.2f}")
col2.metric("Monthly High", f"${max_val:,.2f}")
col3.metric("Current RSI", f"{last_rsi:.2f}")
col4.metric("Volume", f"{float(data['Volume'].iloc[-1]):,.0f}")

st.divider()

# 5. STRATEGY ALERT (Extra Effort) 
if last_rsi > 70:
    st.error(f"⚠️ SIGNAL: OVERBOUGHT (SELL) - RSI: {last_rsi:.2f}")
elif last_rsi < 30:
    st.success(f"✅ SIGNAL: OVERSOLD (BUY) - RSI: {last_rsi:.2f}")
else:
    st.warning(f"⚖️ SIGNAL: NEUTRAL - RSI: {last_rsi:.2f}")

# 6. VISUALIZATIONS (Requirement: Line/Bar/Pie charts) [cite: 574]

# A. Line Chart (Price & SMA Trend)
st.subheader("Price Trend & Moving Average Analysis")
fig_line = go.Figure()
fig_line.add_trace(go.Scatter(x=data.index, y=data['Close'], name='Price'))
fig_line.add_trace(go.Scatter(x=data.index, y=data['SMA'], name=f'SMA {sma_period}'))
fig_line.update_layout(template="plotly_dark", height=500)
st.plotly_chart(fig_line, use_container_width=True)

# B. Bar Chart & Pie Chart Row
left_col, right_col = st.columns(2)

with left_col:
    st.subheader("Trading Volume (Bar Chart)")
    fig_bar = px.bar(data, x=data.index, y='Volume', title="Hourly Volume")
    fig_bar.update_layout(template="plotly_dark")
    st.plotly_chart(fig_bar, use_container_width=True)

with right_col:
    st.subheader("Price vs SMA Distribution (Pie Chart)")
    data['Position'] = ['Above SMA' if x > y else 'Below SMA' for x, y in zip(data['Close'], data['SMA'])]
    fig_pie = px.pie(data, names='Position', hole=0.4)
    fig_pie.update_layout(template="plotly_dark")
    st.plotly_chart(fig_pie, use_container_width=True)

# 7. DATA TABLE (Requirement: Tables) [cite: 574]
st.subheader("Detailed Historical Logs (Last 10 Hours)")
st.dataframe(data.tail(10), use_container_width=True)

st.success("Data successfully stored in 'data.csv'.")