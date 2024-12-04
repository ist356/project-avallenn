import pandas as pd
import streamlit as st

#convert restaurants.csv to a dataframe
restaurants = pd.read_csv('code/restaurants.csv')

def extract_ranking(df : pd.DataFrame):
    #extract ranking from the restaurant column '1. Chick-fil-A'
    df['ranking'] = df['restaurant'].apply(lambda row: row.split('.')[0])
    df['restaurant'] = df['restaurant'].apply(lambda row: row.split('.')[1])
    return df


if __name__ == '__main__':
    restaurants = extract_ranking(restaurants)
    st.dataframe(restaurants)