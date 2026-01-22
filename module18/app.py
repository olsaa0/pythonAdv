import pandas as pd
import streamlit as st
import plotly.express as px

st.header("displaying dataframe")

df = pd.DataFrame({
    'Name': ['Olsa','Kiki','Olsi'],
    'Age': [24,27,22],
    'City':["Prishtina",'Fushkosove','Harilaqi']
})

st.write(df)

st.title("Bestselling books analysis")
st.write("This app analyses the amazon top selling books from 2009 to 2022")

books_df = pd.read_csv('module18/bestsellers_with_categories_2022_03_27.csv')

st.subheader("summary statistics")
total_books = books_df.shape[0]
unique_titles = books_df['Name'].nunique()
average_rating = books_df['User Rating'].mean()
average_price = books_df['Price'].mean()


col1, col2, col3, col4 = st.columns(4)
col1.metric("Total Books", total_books)
col2.metric("Unique Titles", unique_titles)
col3.metric("Average Rating",  f"{average_rating:.2f}")
col4.metric("average Price", f"${average_price:.2f}")

st.subheader("Dataset Preview")
st.write(books_df.head())

col1, col2 = st.columns(2)

with col1:
    st.subheader("Top 10 Book titles")
    top_titles = books_df['Name'].value_counts().head(10)
    st.bar_chart(top_titles)


with col2:
    st.subheader("Top 10 Authors")
    top_authors = books_df['Author'].value_counts().header(10)
    st.bar_chart(top_authors)


st.subheader("Number of fiction vs non-fiction books over the years")
size = books_df.groupby(['Year', 'Genre']).size().reset_index(name='Counts')
fig = px.bar(size, x='Year', y='counts', color='Genre',title="Number of fiction vs non-fiction books from 2009-20222",
             color_discrete_sequence=px.sequential.Plasmma, barmode='group')

st.plotly_chart(fig)
