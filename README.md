# 📈 Professional Financial Analysis & Trading Dashboard

This project is a real-time financial data visualization tool built with **Python** and **Streamlit**.

```markdown
## 🎯 Key Features
* **Automated Data Retrieval:** Fetches hourly (1h) market data for the last 1 month using Yahoo Finance API.
* **Data Persistence:** Automatically stores data in data.csv to comply with project requirements.
* **Technical Analysis:** Includes SMA and RSI indicators to explain market trends.
* **Interactive Visualizations:** Includes Line, Bar, and Pie charts along with detailed data tables.
* **Smart Alerts:** Provides real-time Buy/Sell signals based on RSI logic.

## 🛠️ Tech Stack
* **Language:** Python
* **UI Framework:** Streamlit
* **Libraries:** Pandas, YFinance, Plotly

## 🚀 How to Run
1. Navigate to the project folder in your terminal.
2. Install requirements:
   ```bash
   pip install -r requirements.txt
3. Launch the dashboard:
   ```bash
   python -m streamlit run dashboard.py
