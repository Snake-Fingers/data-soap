from data_soap import __version__
import pytest 
import pandas as pd
from data_soap.data_soap import soap, pull_comma, pull_leading_character, pull_trailing_character, convert_all
def test_version():
    assert __version__ == '0.1.0'


@pytest.fixture
def sample_dataframe():
    df = pd.read_csv('assets/googleplaystore.csv')
    df = pd.DataFrame(df.copy().drop(['Category', 'Reviews', 'Rating', 'Type', 'Content Rating', 'Genres', 'Last Updated', 'Current Ver', 'Android Ver'], axis = 1)).iloc[200: 240]
    # print(df.info())
    return df
    

# def test_sample_test(sample_dataframe):
#     df = sample_dataframe()
#     print(df.info)
# @pytest.mark.skip('pending code')
def test_pull_comma_when_trail_char():
    actual = pull_comma('1,000,000+')
    expected = '1000000+'
    assert actual == expected

# @pytest.mark.skip('pending code')
def test_pull_comma_when_lead_char():
    actual = pull_comma('$1,000,000')
    expected = '$1000000'
    assert actual == expected

# @pytest.mark.skip('pending code')
def test_pull_comma_when_no_comma():
    actual = pull_comma('$1000000')
    expected = '$1000000'
    assert actual == expected


# @pytest.mark.skip('pending code')
def test_pull_comma_when_NaN():
    actual = pull_comma('this, is NaN')
    expected = 'this is NaN'
    assert actual == expected


# @pytest.mark.skip('pending code')
def test_pull_leading_character():
    df = sample_dataframe
    actual = pull_leading_character('$4.99')
    expected = '4.99'
    assert actual == expected

# @pytest.mark.skip('pending code')
def test_pull_trailing_character_m():
    actual = pull_trailing_character('1000000m')
    expected = 1
    assert actual == expected

# @pytest.mark.skip('pending code')
def test_pull_trailing_character_k():
    df = sample_dataframe
    actual = pull_trailing_character('1,000k')
    expected = .001
    assert actual == expected

# @pytest.mark.skip('pending code')
# re-design needed convert takes any unit of measure and converts to common denomination of that measure e.g: x'k' to .x 'm' or x 'ml' to .x'lt' etc.
def test_convert_all(sample_dataframe):
    df = sample_dataframe
    actual = test_convert_all(df['Size'].iloc[211])
    expected = '.023'
    assert actual == expected


# @pytest.mark.skip('pending code')
def test_soap_one_column_clean_commas(sample_dataframe):
    rinsed = soap(sample_dataframe, ['Installs'])
    actual = rinsed.iloc[211]['Installs']
    expected = .023
    assert actual == expected


@pytest.mark.skip('pending code')
def test_soap_one_column_clean_trailing(sample_dataframe):
    rinsed = soap(sample_dataframe, ['Reviews'])
    actual = rinsed.iloc[200]['Reviews']
    expected = 10000000
    assert actual == expected


@pytest.mark.skip('pending code')
def test_soap_more_columns(sample_dataframe):
    rinsed = soap(sample_dataframe, ['Reviews', 'Installs', 'Price'])
    data_types = ['object', 'float64'*3]
    actual = rinsed.dtypes.values
    expected = data_types
    assert actual == expected


@pytest.mark.skip('pending code')
def test_soap_wrong_input_type():
    bad_input = 'not a dataframe or series'
    with pytest.raises(Exception) as excinfo:
        soap(bad_input, ['NaN'])
    actual = excinfo.value
    expected = 'TypeError: expected pd.DataFrame object, pd.Series object, or list-like: got str'
    assert actual == expected


# @pytest.mark.skip('pending code')
    
    
    
  
    


