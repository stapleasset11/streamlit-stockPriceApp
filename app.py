import pandas as pd
import yfinance as yf
import streamlit as st

st.write('''
    # Simple stock app
    
    Shown are the stock **closing price** and ***volume*** of Google,Apple,Microsoft and Amazon.

'''
    
)


tickerSymbol = ['AAPL','GOOGL','MSFT','AMZN','TSLA']

for t in tickerSymbol:

    tickerData = yf.Ticker(t)

    tickerDf = tickerData.history(period='1d',start='2020-5-31', end = '2024-5-31')

    st.subheader(f'More information about the stock: {t}')

    specific_info= {
        'Company Name':tickerData.info.get("longName"),
        'CEO':tickerData.info.get("companyOfficers")[0]["name"],
        'Market Cap': tickerData.info.get('marketCap'),
        'PE Ratio': tickerData.info.get('forwardPE'),
        'Dividend Yield': tickerData.info.get('dividendYield'),
        '52 Week High': tickerData.info.get('fiftyTwoWeekHigh'),
        '52 Week Low': tickerData.info.get('fiftyTwoWeekLow')
    }
    for key, value in specific_info.items(): 
        st.write(f"{key}: {value}")

    st.subheader(f'{t} Closing Price')
    st.line_chart(tickerDf.Close)


    st.subheader(f'{t} Volume')
    st.line_chart(tickerDf.Volume)




