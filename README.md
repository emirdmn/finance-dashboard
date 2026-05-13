# 📈 Professional Financial Analysis & Trading Dashboard

This project is a real-time financial data visualization tool built with **Python** and **Streamlit**.

## 🎯 Key Features
* [cite_start]**Automated Data Retrieval:** Fetches **hourly (1h)** market data for the last **1 month** using Yahoo Finance API[cite: 571].
* [cite_start]**Data Persistence:** Automatically stores data in **`data.csv`** to comply with project requirements[cite: 571].
* [cite_start]**Technical Analysis:** Includes **SMA** and **RSI** indicators to explain market trends[cite: 573].
* [cite_start]**Interactive Visualizations:** Includes **Line, Bar, and Pie charts** along with detailed data **tables**[cite: 574].
* [cite_start]**Smart Alerts:** Provides real-time Buy/Sell signals based on RSI logic.

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
python -m streamlit run dashboard.py