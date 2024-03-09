import pandas as pd 
import yfinance as yf
import matplotlib.pyplot as plt

tickers = ['XOM', 'CVX', 'BP', 'SHEL']
df = yf.download(tickers, '2023-03-01', '2024-03-03')['Adj Close']

df.columns = ['Adj Close', 'Adj Close', 'Adj Close', 'Adj Close']

print(df.head())
print(df.columns)


first_adj_close = df.iloc[0] 
#df['Normalized_Return'] = df['Adj Close'] / first_adj_close

#print(df.head())

#df.to_csv('energy_stocks.csv')   # print to csv


