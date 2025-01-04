import streamlit as st
import pandas as pd
import plotly.express as px

#tira a margem
st.set_page_config(layout="wide")

df_reviews = pd.read_csv("./datasets/customer reviews.csv")
df_top100_books = pd.read_csv("./datasets/Top-100 Trending Books.csv")


#.max() vai procurar pelo maior valor da coluna book price
#que esta na tabela top_100_books

price_max = df_top100_books["book price"].max() 
price_min = df_top100_books["book price"].min() 

max_price = st.sidebar.slider("Price Renge", price_min, price_max, price_max)
df_books = df_top100_books[df_top100_books["book price"] <= max_price]
df_books

fig = px.bar(df_books["year of publication"].value_counts())
fig2 = px.histogram(df_books["book price"])

col1, col2 = st.columns(2)
col1.plotly_chart(fig)
col2.plotly_chart(fig2)



#print(df_reviews.index) # conteudo da planinha Excel
#print(df_reviews.columns)# mostra quais são os nomes das colunas 
#print(df_reviews['book name']) # mostra o conteudo de uma coluna
#print(df_top100_books[df_top100_books["book price"]< 10])
