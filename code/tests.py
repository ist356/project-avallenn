import pytest 
from functions import extract_ranking, extract_stars, extract_category, extract_price
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
    text = TEST_DATA['restaurant'][0]
    expect = '1'
    actual = extract_ranking(text)
    print(f"Actual: {actual}, Expect: {expect}")
    assert expect == actual

def test_extract_stars():
    text = TEST_DATA['information'][2]
    expect = '4.5'
    actual = extract_stars(text)
    print(f"Actual: {actual}, Expect: {expect}")
    assert expect == actual

def test_extract_category():
    text = TEST_DATA['information'][1]
    expect = 'American, Bar$$ - $$$Menu'
    actual = extract_category(text)
    print(f"Actual: {actual}, Expect: {expect}")
    assert expect == actual

def test_extract_price():
    text = TEST_DATA['category'][0]
    expect = 'Moderate'
    actual = extract_price(text)

if __name__ == "__main__":
    test_should_pass()
    test_extract_ranking()
    test_extract_stars()
    test_extract_category()
    test_extract_price()