from datasoap import __version__
import pytest
import pandas as pd
# from data_soap.data_soap import soap, pull_comma, pull_leading_character, pull_trailing_character, convert_unit
from datasoap.data_soap import Soap


def test_version():
    assert __version__ == '0.1.0'

# ================= Fixtures =================


@pytest.fixture
def sample_dataframe():
    """[creates a smaller dataframe from a dataset downloaded @: [Kaggle.com](https://www.kaggle.com/ltx1171135686/googleplaystore-acsv)]

    Returns:
        [<class pd.DataFrame]: [a smaller copy of dataframe created with pandas.read_csv]
    """
    df = pd.read_csv('assets/googleplaystore.csv')
    df = pd.DataFrame(df.copy().drop(['Category', 'Rating', 'Type', 'Content Rating',
                                      'Genres', 'Last Updated', 'Current Ver', 'Android Ver'], axis=1)).iloc[200:240]
    # print(df.info())
    return df


@pytest.fixture
def soap_sample(sample_dataframe):
    """[creates a sample instance of the Soap class using the sample_dataframe fixture]

    Args:
        sample_dataframe ([pd.DataFrame]): [sample dataframe to be cleaned]

    Returns:
        [<class Soap]: [returns an instance of Soap class where the clean data is stored in attr `clean_copy`]
    """

    return Soap(sample_dataframe, ['Reviews', 'Installs', 'Price', 'Size'], 'M')


# ================== End Fixtures ================

# ======== Testing of Private and Static Methods =====

# @pytest.mark.skip('pending code')
def test_pull_comma_when_trail_char():
    actual = Soap.pull_comma('1,000,000+')
    expected = '1000000+'
    assert actual == expected


# @pytest.mark.skip('pending code')
def test_pull_comma_when_lead_char():
    actual = Soap.pull_comma('$1,000,000')
    expected = '$1000000'
    assert actual == expected


# @pytest.mark.skip('pending code')
def test_pull_comma_when_no_comma():
    actual = Soap.pull_comma('$1000000')
    expected = '$1000000'
    assert actual == expected


# @pytest.mark.skip('pending code')
def test_pull_comma_when_NaN():
    actual = Soap.pull_comma('this, is NaN')
    expected = 'this is NaN'
    assert actual == expected


# @pytest.mark.skip('pending code')
def test_pull_leading_character():
    actual = Soap.pull_leading_character('$4.99')
    expected = '4.99'
    assert actual == expected


# @pytest.mark.skip('pending code')
def test_pull_trailing_character_m():
    actual = Soap.pull_trailing_character('1m')
    expected = 1.0
    assert actual == expected


# @pytest.mark.skip('pending code')
def test_pull_trailing_character_k():
    actual = Soap.pull_trailing_character('1k')
    expected = .001
    assert actual == expected


# @pytest.mark.skip('pending code')
def test_soap_one_column_clean(sample_dataframe):
    rinsed = Soap(sample_dataframe, ['Size'], 'M').clean_copy
    actual = rinsed['Size'].iloc[9]
    expected = .023
    assert actual == expected


# @pytest.mark.skip('pending code')
def test_soap_more_columns(sample_dataframe):
    rinsed = Soap(sample_dataframe, ['Reviews', 'Installs', 'Price', 'Size'], 'M')
    actual = rinsed.clean_copy.dtypes.all()
    expected = 'float64'
    assert actual == expected

# below test are for convert_unit method

# @pytest.mark.skip('pending code')
def test_convert_unit():
    actual = Soap.convert_unit('10k', 'M')
    expected = '0.01'
    assert actual == expected

# @pytest.mark.skip('pending code')
def test_one_unit_above_base():
    actual = Soap.convert_unit('10k', 'M')
    expected = '0.01'
    assert actual == expected

# @pytest.mark.skip('pending code')
def test_multi_unit_above_base():
    actual = Soap.convert_unit('10da', 'M')
    expected = '0.0001'
    assert actual == expected

# @pytest.mark.skip('pending code')
def test_one_unit_below_base():
    actual = Soap.convert_unit('10c', 'd')
    expected = '1.0'
    assert actual == expected


# @pytest.mark.skip('pending code')
def test_multi_unit_below_base():
    actual = Soap.convert_unit('10m', 'd')
    expected = '0.09999999999999999'
    assert actual == expected

# @pytest.mark.skip('pending code')
def test_non_alpha_trailing_character():
    actual = Soap.convert_unit('100+', 'M')
    expected = '100'
    assert actual == expected


# @pytest.mark.skip('pending code')
def test_non_numeric_input_nan():
    actual = Soap.convert_unit('varies with device', 'T')
    expected = 'varies with device'
    assert actual == expected


# @pytest.mark.skip('pending code')
def test_non_numeric_input_type():
    actual = type(Soap.convert_unit('varies with device', 'T'))
    expected = str
    assert actual == expected

# @pytest.mark.skip('pending code')
def test_convert_unit_all_digit():
    actual = Soap.convert_unit('1000', 'da')
    expected = '1000'
    assert actual == expected

# === End Testing of Private and Static methods ===

# ============== Testing of Class =================

# @pytest.mark.skip('pending code')
def test_class_instance_clean_copy_type(soap_sample):
    actual = isinstance(soap_sample.clean_copy, pd.DataFrame)
    expected = True
    assert actual == expected


# @pytest.mark.skip('pending code')
def test_class_instance_str(soap_sample):
    actual = soap_sample.__str__()
    expected = 'Instance of Soap class. attr `clean_copy` is a pandas dataframe object with values converted into operable datatypes.'
    assert actual == expected


# @pytest.mark.skip('pending code')
def test_class_instance_repr(soap_sample):
    actual = soap_sample.__repr__()
    expected = 'Instance of <class \'pandas.core.frame.DataFrame\'> with values in columns: [\'Reviews\', \'Installs\', \'Price\', \'Size\'], re-formated into operable datatype; \'float64\' or \'int64\''
    assert actual == expected


# @pytest.mark.skip('pending code')
def test_class_instance_show_diff(soap_sample, capsys):
    soap_sample.show_diff()
    cap = capsys.readouterr()
    actual = cap.out
    expected = (
        'Original DataFrame.info: \n'
        '\n'
        "<class 'pandas.core.frame.DataFrame'>\n"
        'RangeIndex: 40 entries, 200 to 239\n'
        'Data columns (total 5 columns):\n'
        ' #   Column    Non-Null Count  Dtype \n'
        '---  ------    --------------  ----- \n'
        ' 0   App       40 non-null     object\n'
        ' 1   Reviews   40 non-null     object\n'
        ' 2   Size      40 non-null     object\n'
        ' 3   Installs  40 non-null     object\n'
        ' 4   Price     40 non-null     object\n'
        'dtypes: object(5)\n'
        'memory usage: 1.7+ KB\n'
        '\n'
        'Re-Formatted DataFrame.info: \n'

        "<class 'pandas.core.frame.DataFrame'>\n" 
        'RangeIndex: 40 entries, 200 to 239\n' 
        'Data columns (total 5 columns):\n' 
        ' #   Column    Non-Null Count  Dtype  \n' 
        '---  ------    --------------  -----  \n' 
        ' 0   App       40 non-null     object \n' 
        ' 1   Reviews   40 non-null     int64  \n' 
        ' 2   Size      24 non-null     float64\n' 
        ' 3   Installs  40 non-null     int64  \n' 
        ' 4   Price     38 non-null     float64\n' 
        'dtypes: float64(2), int64(2), object(1)\n' 
        'memory usage: 1.7+ KB\n')
    assert actual == expected


# ============= End Class Testing ====================

# ========== Testing Inputs of Public Methods ========

# @pytest.mark.skip('pending code')
def test_soap_wrong_input_data():
    bad_input = 'not a dataframe or series'
    with pytest.raises(Exception) as excinfo:
        Soap(bad_input, ['NaN'], 'M').clean_copy
    actual = str(excinfo.value)
    expected = str(TypeError(
        'TypeError: expected pd.DataFrame object, pd.Series object, or list-like: got <class \'str\'>'))
    assert actual == expected

# @pytest.mark.skip('pending code')
def test_soap_wrong_input_dirty(sample_dataframe):
    bad_input = 'not a list'
    with pytest.raises(Exception) as excinfo:
        Soap(sample_dataframe, bad_input, 'base').dirty 
    actual = str(excinfo.value)
    expected = str(TypeError('TypeError: expected <class \'list\'>, got <class \'str\'>'))
    assert actual == expected