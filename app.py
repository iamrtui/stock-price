from nbformat import write
import streamlit as st
import pandas as pd
import yfinance as yf

listTickers = pd.Series(['AAPL', 'NFLX', 'GOOG', 'AMZN', 'META', 'CSCO', 'ORCL', 'SAP', 'CRM'])

if __name__ == "__main__":
    # Sidebar
    st.sidebar.header("Filters")
    tickerSymbol = st.sidebar.selectbox('Ticker', listTickers)

    # Description
    st.title("Stock Price")
    st.write(f"Currently displayed: {tickerSymbol}")

    # Fetch data
    tickerData = yf.Ticker(tickerSymbol)
    tickerDf = tickerData.history(period='max')

    st.write("Closing Price")
    st.line_chart(tickerDf.Close)
    
    st.write("Volume")
    st.line_chart(tickerDf.Volume)
