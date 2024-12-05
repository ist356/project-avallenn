import streamlit as st
import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

df = pd.read_csv('code/restaurantscleaned.csv')
st.title('Discover Syracuse Restaurants')
category_list = df['category'].str.split(',').explode().str.strip().unique()
category = st.selectbox('What type of Food sounds good?', category_list)

if category:
    st.write(f'Here are your options for {category}!')
    filtered_df = df[df['category'].str.contains(category)]
    st.dataframe(filtered_df)
    st.header('Average Rating by Price Category')

    col1, col2 = st.columns(2)
    with col1:
        fig1, ax1 = plt.subplots()
        sns.barplot(data=filtered_df, x='price', y="stars", estimator = 'mean' , hue = 'price', ax=ax1)
        ax1.set_ylim(3.9)
        st.pyplot(fig1)

    with col2:
        mean_stars = filtered_df.groupby('price')['stars'].mean()
        mean_stars = pd.DataFrame(mean_stars)
        max_stars = mean_stars['stars'].max()
        price_max = mean_stars[mean_stars['stars'] == max_stars].index.tolist()
        if len(price_max) > 1:
            st.write(f"There are multiple price categories with the highest average rating of {max_stars}. Therefore, you should not try to proritize price when choosing a {category} restaurant.")
        elif len(price_max) == 1:
            st.write(f"The suggested price category to dine at for {category} cuisine is {price_max}, as it has an average rating of {max_stars}")