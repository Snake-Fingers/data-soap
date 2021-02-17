from data_soap import __version__
import pytest 
import pandas as pd
from data_soap.data_soap import soap, pull_comma, pull_leading_character, pull_trailing_character, convert_all
def test_version():
    assert __version__ == '0.1.0'


@pytest.fixture
def sample_dataframe():
    df = pd.read_csv('assets/googleplaystore.csv')
    # df = pd.DataFrame(df.copy().drop(['Category', 'Reviews', 'Rating', 'Type', 'Content Rating', 'Genres', 'Last Updated', 'Current Ver', 'Android Ver'], axis = 1)).iloc[200: 240]
    df = pd.DataFrame(df.copy().drop(['Category', 'Reviews', 'Rating', 'Type', 'Content Rating', 'Genres', 'Last Updated', 'Current Ver', 'Android Ver'], axis = 1))
    # print(df.info())
    return df
    

# def test_sample_test(sample_dataframe):
#     df = sample_dataframe()
#     print(df.info)
# @pytest.mark.skip('pending code')
def test_pull_comma():
    actual = pull_comma('1,000,000')
    expected = '1000000'
    assert actual == expected

# @pytest.mark.skip('pending code')
def test_pull_leading_character(sample_dataframe):
    df = sample_dataframe
    actual = pull_leading_character(df['Price'].iloc[235])
    expected = '4.99'
    assert actual == expected

# @pytest.mark.skip('pending code')
def test_pull_trailing_character(sample_dataframe):
    df = sample_dataframe
    df_installs = df['Installs'].iloc[232] 
    actual = pull_trailing_character(df_installs)
    expected = '10,000,000'
    assert actual == expected

@pytest.mark.skip('pending code')
def test_convert_all(sample_dataframe):
    df = sample_dataframe
    df_size = df['Size'].iloc[211]
    actual = convert_all(df_size)
    expected = '.023'
    assert actual == expected


# @pytest.mark.skip('pending code')
# @pytest.mark.skip('pending code')
# @pytest.mark.skip('pending code')
# @pytest.mark.skip('pending code')
# @pytest.mark.skip('pending code')
    
    
    
  
    


