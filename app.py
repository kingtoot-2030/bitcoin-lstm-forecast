import streamlit as st
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import yfinance as yf

st.title("Bitcoin Price Forecast")

# تحميل البيانات من ياهو
btc_data = yf.download("BTC-USD", period="1d", interval="1h")

# رسم البيانات
st.line_chart(btc_data['Close'])
