*****
datasoap  
*****

*****
What is it? 
*****

**datasoap** is a Python package that provides the ability to reformat values of a **pandas** dataframe column in such a way as to be operable with standard mathematics and plotting. It is designed to work with **pandas** data in a way that maximizes efficiency and decreases frustrations caused by mismatched numerical data types. By using **datasoap**, users can remove non-digit characters from numeric strings, convert specific unit measurements, and see a comparison of the original data and the cleaned up version of the data.

**datasoap** works well with any **pandas** dataframe objects, which include the 2 primary data structures: Series (1-dimensional) and Dataframe (2-dimensional). As a dependency of **datasoap**, **pandas** is also integrated with **NumPy**. 

Things **datasoap** can do:   
*   Reformat values in a *pandas* dataframe instance to allow correct conversion to the correct datatype.  
| Show a comparison of the original and re-formatted dataframes.
| Pull commas out of numeric strings (1,000 -> 1000).
| Pull non-alphanumeric trailing characters (1000+ -> 1000). 
| Pull leading non-numeric characters ($4.99 -> 4.99).
| Convert all unit values to a specified common unit. E.g. ‘10k’ becomes ‘.01’ where ‘M’ is the common unit.   

These methods were the focus of the package, as data analysis gets frustratingly complicated when numerical values cannot be manipulated due to mismatched datatypes or formatting. Working with data usually involves a lot of cleaning up before getting to use it, and *datasoap* aims to alleviate some of the biggest pain points of data analysis.

For more information on **pandas**, please visit: https://pandas.pydata.org/pandas-docs/version/0.25.3/ 

*****
Main Features
*****

*   Strips unnecessary characters from numerical data fields in pandas dataframes to ensure consistent data formatting.
*   Provides before and after representations of dataframes to allow for comparison.

*****
Repository
*****

Source code is hosted on: `<github.com/snake-fingers/data-soap/>`_

*****
Dependencies
*****

pandas - Python package that provides fast, flexible, and expressive data structures designed to make working with “relational” or “labeled” data both easy and intuitive.

*****
Attributes & Methods
*****

| `clean_copy`: re-formatted version of the pandas dataframe.  
| `show_diff()`: calls pd.DataFrame.info method on both the original and the re-formatted dataframes for easy comparison of the data type transformation.  

For pandas methods and attributes, please visit: https://pandas.pydata.org/pandas-docs/stable/reference/api/pandas.DataFrame.html

*****
Installation
*****

`poetry add datasoap`  

*****
Basic Functionality
*****

.. code-block:: python

    from datasoap.data_soap import Soap
    import pandas as pd

    df = pd.read_csv(‘filename.csv’)

    variable_name = Soap(df, [‘Column Name’])

*****
Example Usage:
*****

.. code-block:: python

    In [1]: from datasoap.data_soap import Soap  
    In [2]: import pandas as pd  

    In [3]: df = pd.read_csv('numbers.csv')  

    In [4]: percent = Soap(df, ['Percentage'])  

    In [5]: percent.clean_copy.head())  
    Out [5]:  
    Number  Percentage    Price Trailing Alpha Trailing Char  
    0      24       130.5   $26.54            11k            5+  
    1      44       121.9  $105.00             5m           10+  
    2      21        81.0   $21.00            10K          234+  
    3      25        79.7   $46.00             6m        12341+  
    4      49        77.1   $50.00            42m         2315+  

    In [6]: percent.show_diff())  
    Out [6]:  
    Original DataFrame.info:  

    <class 'pandas.core.frame.DataFrame'>  
    RangeIndex: 5 entries, 0 to 4  
    Data columns (total 5 columns):  
    #   Column          Non-Null Count  Dtype  
    ---  ------          --------------  -----  
    0   Number          5 non-null      int64  
    1   Percentage      5 non-null      object  
    2   Price           5 non-null      object  
    3   Trailing Alpha  5 non-null      object  
    4   Trailing Char   5 non-null      object  
    dtypes: int64(1), object(4)  
    memory usage: 328.0+ bytes  

    Re-Formatted DataFrame.info:  

    <class 'pandas.core.frame.DataFrame'>  
    RangeIndex: 5 entries, 0 to 4  
    Data columns (total 5 columns):  
    #   Column          Non-Null Count  Dtype  
    ---  ------          --------------  -----  
    0   Number          5 non-null      int64  
    1   Percentage      5 non-null      float64  
    2   Price           5 non-null      object  
    3   Trailing Alpha  5 non-null      object  
    4   Trailing Char   5 non-null      object  
    dtypes: float64(1), int64(1), object(3)  
    memory usage: 328.0+ bytes  


*****
Background
*****

**datasoap** originated from a Code Fellows 401 Python midterm project. The project team includes Alex Angelico, Grace Choi, Mason Fryberger, and Jae Choi. After working with a few painful datasets using, we wanted to create a library that allows users to more efficiently manipulate clean datasets extracted from CSVs that may have inconsistent formatting.