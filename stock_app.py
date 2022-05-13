import numpy as np
import pandas as pd
import matplotlib.pyplot as plt
import pandas_datareader as data
import streamlit as st
import datetime


current_time = datetime.datetime.now()
today = str(current_time.month) + "/" + \
    str(current_time.day) + "/" + str(current_time.year)
DATE_COLUMN = str(current_time.year) + "-" + \
    str(current_time.month) + "-" + str(current_time.day)
FIVE_YEARS = str(current_time.year - 5) + "-" + \
    str(current_time.month) + "-" + str(current_time.day)

st.title('Stocks')
st.header(today)

ticker = st.text_input("Enter Ticker", "GOOG")
favorites = ["COIN", "GOOG", "TSLA", "AAPL"]


def print_data(ticker):
    df = data.DataReader(ticker, 'yahoo', FIVE_YEARS, DATE_COLUMN)
    st.subheader(FIVE_YEARS + " to " + DATE_COLUMN)
    st.write(df.describe())


def make_graph(ticker):
    df = data.DataReader(ticker, 'yahoo', FIVE_YEARS, DATE_COLUMN)
    st.subheader("Closing Price for " + ticker)
    fig = plt.figure(figsize=(12, 6))
    plt.plot(df.Close)
    st.pyplot(fig)


print_data(ticker)
make_graph(ticker)
if st.checkbox('Show raw data'):
    st.subheader('Raw data')
    st.write(data.DataReader(ticker, 'yahoo', FIVE_YEARS, DATE_COLUMN))
# Makes a chart


st.write("Favorites:")
fav_text = ""
for tick in favorites:
    fav_text += tick + ", "
if len(fav_text) > 1:
    fav_text = fav_text[:-2]
st.write(fav_text)

for favorite in favorites:
    st.write(favorite)
    print_data(favorite)
    make_graph(favorite)

# def load_data(nrows):
#     data = pd.read_csv(df, nrows=nrows)
#     def lowercase(x): return str(x).lower()
#     data.rename(lowercase, axis='columns', inplace=True)
#     data[DATE_COLUMN] = pd.to_datetime(data[DATE_COLUMN])
#     return data


# data_load_state = st.text('Loading data...')
# data = load_data(10000)
# data_load_state.text("Done! (using st.cache)")


# st.subheader('Stock prince')
# hist_values = np.histogram(
#     data[DATE_COLUMN].dt.hour, bins=24, range=(0, 24))[0]
# st.bar_chart(hist_values)
