import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('code/restaurantscleaned.csv')
st.title('Discover Syracuse Restaurants')
category_list = df['category'].str.split(',').explode().str.strip().unique()
category = st.selectbox('What type of Food sounds good?', category_list)
st.write(f'Here are your options for {category}!')
filtered_df = df[df['category'].str.contains(category)]
st.dataframe(filtered_df)

fig1, ax1 = plt.subplots()
sns.barplot(data=filtered_df, x='price', y="stars", estimator = 'mean' , hue = 'price', ax=ax1)
ax1.set_ylim(3.9)
st.pyplot(fig1)