import pandas as pd
import streamlit as st

#convert restaurants.csv to a dataframe
restaurants = pd.read_csv('code/restaurants.csv')

def extract_ranking(df : pd.DataFrame):
    #extract ranking from the restaurant column '1. Chick-fil-A'
    df['ranking'] = df['restaurant'].apply(lambda row: row.split('.')[0])
    df['restaurant'] = df['restaurant'].apply(lambda row: row.split('.')[1])
    return df

def extract_stars(df : pd.DataFrame):
    df = extract_ranking(df)
    df['stars'] = df['information'].apply(lambda row: row.split(' ')[0])
    # delete " from information column
    df['stars'] = df['stars'].replace('"', '')
    return df

def extract_category(df : pd.DataFrame):
    df = extract_stars(df)
    df['information'] = df['information'].str.replace('Closed Now', ' ')
    df['information'] = df['information'].str.replace('Closed Today', ' ')
    df['information'] = df['information'].str.replace('Open Now', ' ')
    df['category'] = df['information'].apply(lambda row: row.split('reviews')[1])
    df['category'] = df['category'].apply(lambda row: row.split('$')[0])
    return df

def extract_price(df: pd.DataFrame):
    df = extract_category(df)  
    df['price'] = df['information'].str.extract('(\$+)', expand=False)
    df['price'] = df['price'].str.len().apply(lambda row: 'Inexpensive' if row == 1 
                                                else ('Moderate' if row == 2 
                                                      else ('Expensive' if row == 4 else '')))
    df.drop('information', axis=1, inplace=True)
    return df

if __name__ == '__main__':
    restaurants = extract_price(restaurants)
    st.dataframe(restaurants)
    restaurants.to_csv('code/restaurantscleaned.csv', index=False)