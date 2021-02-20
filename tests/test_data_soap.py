from data_soap import __version__
import pytest
import pandas as pd
from data_soap.data_soap import soap, pull_comma, pull_leading_character, pull_trailing_character, convert_unit


def test_version():
    assert __version__ == '0.1.0'


@pytest.fixture
def sample_dataframe():
    df = pd.read_csv('assets/googleplaystore.csv')
    df = pd.DataFrame(df.copy().drop(['Category', 'Rating', 'Type', 'Content Rating',
                                      'Genres', 'Last Updated', 'Current Ver', 'Android Ver'], axis=1)).iloc[200:240]
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
    actual = pull_leading_character('$4.99')
    expected = '4.99'
    assert actual == expected

# @pytest.mark.skip('pending code')
def test_pull_trailing_character_m():
    actual = pull_trailing_character('1m')
    expected = 1.0
    assert actual == expected

# @pytest.mark.skip('pending code')
def test_pull_trailing_character_k():
    actual = pull_trailing_character('1k')
    expected = .001
    assert actual == expected


# @pytest.mark.skip('pending code')
def test_soap_one_column_clean(sample_dataframe):
    rinsed = soap(sample_dataframe, ['Size'])
    actual = rinsed['Size'].iloc[9]
    expected = .023
    assert actual == expected


# @pytest.mark.skip('pending code')
def test_soap_more_columns(sample_dataframe):
    rinsed = soap(sample_dataframe, ['Reviews', 'Installs', 'Price', 'Size'])
    actual = rinsed.dtypes.all()
    expected = 'float64'
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
def test_convert_unit():
    actual = convert_unit('10k', 'M')
    expected = '0.01'
    assert actual == expected

