import pytest 
from src.functions import extract_ranking, extract_stars, extract_category, extract_price
import pandas as pd

def test_should_pass():
    print("\nAlways True!")
    assert True

TEST_DATA = pd.DataFrame({
    'restaurant': [
        '1. Apizza Regionale',
        '2. Dinosaur Bar-B-Que',
        '3. Eva\'s European Sweets$'
    ],
    'information': [
        '5.0 of 5 bubbles268 reviewsClosed NowItalian, Pizza$$ - $$$Menu',
        '4.5 of 5 bubbles2,768 reviewsClosed NowAmerican, Bar$$ - $$$Menu',
        '4.5 of 5 bubbles232 reviewsClosed NowPolish, European$$ - $$$Menu'
    ]
})
print(TEST_DATA)

def test_extract_ranking():
    result_df = extract_ranking(TEST_DATA)
    expect = '1'
    actual = result_df['ranking'][0]
    print(f"Actual: {actual}, Expect: {expect}")
    assert expect == actual

def test_extract_stars():
    result_df = extract_stars(TEST_DATA)
    expect = '4.5'
    actual = result_df['stars'][1]
    print(f"Actual: {actual}, Expect: {expect}")
    assert expect == actual

def test_extract_category():
    result_df = extract_category(TEST_DATA)
    expect = ' American, Bar'
    actual = result_df['category'][1]
    print(f"Actual: {actual}, Expect: {expect}")
    assert expect == actual

def test_extract_price():
    result_df = extract_price(TEST_DATA)
    expect = 'Moderate'
    actual = result_df['price'][1]
    print(f"Actual: {actual}, Expect: {expect}")
    assert expect == actual

if __name__ == "__main__":
    test_should_pass()
    test_extract_ranking()
    test_extract_stars()
    test_extract_category()
    test_extract_price()