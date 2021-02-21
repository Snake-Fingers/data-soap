import pandas as pd 
import numpy as np 
import re   
from unit_data.conversion import units


class Soap:
    def __init__(self, data, dirty):
        self.data = data
        self.dirty = dirty
        self.clean_copy = self.soap(self.data, self.dirty)
    
    def __str__(self):
        return f'Instance of Soap class. attr `clean_copy` is a pandas dataframe object with values converted into operable datatypes.'

    def __repr__(self):
        return f'Instance of {type(self.clean_copy)}'


    def soap(self, data, dirty:list):
        """[Method used by the Soap class to reformat values in a pandas.dataframe instance to allow correct conversion to correct datatype.]

        Args:
            data ([pandas.DataFrame]): [pandas dataframe instance]
            dirty (list): [list of column names as strings that need reformatting for conversion to operable data types]

        Raises:
            TypeError: [data argument must be a pandas.DataFrame Object]

        Returns:
            [pandas.DataFrame]: [returns copy of the origial dataframe with the specified values converted to the correct dtype]
        """
        if not isinstance(data, pd.DataFrame):
            raise TypeError(f'TypeError: expected pd.DataFrame object, pd.Series object, or list-like: got {type(data)}')
        # create copy of the dataframe to be cleaned
        clean_data = data.copy()
        for col in dirty:
            clean_data[f'{col}'].replace(clean_data[f'{col}'].values, [pd.to_numeric(self.pull_trailing_character(self.pull_leading_character(self.pull_comma(val))), errors='coerce') for val in clean_data[f'{col}']], inplace=True)
        
        return clean_data
     

    @staticmethod
    def show_diff(self):
        """Shows both the original and cleaned dataframes.
        """

        # in order to accomplish this we may need to wrap all the logic in a class with a property for before and after 
        # otherwise we may have some issues with being able to retrieve a specific comparison assuming a user needs to clean
        # more than one dataset. 

        # show the `.info()` for the original and the cleaned copy
        # show the `.describe` for the original and the cleaned copy
        # accomplised by returning an iterable of print statements for each.
        # e.g. return [(print(f'{origin_info}'), print(f'{cleaned_info}')), (print(f'{origin_describe}'), print(f'{cleaned_describe}'))]
        # pass 

    # define methods for pulling commas out of a String
    @staticmethod
    def pull_comma(line: str)-> str:
        """[static method used by Soap class instances to pull commas out of numeric strings]

        Args:
            line (str): [string to be re-formatted e.g. '2,000']

        Returns:
            str: [numeric string e.g. (see Args) --> '2000']
        """
        if ',' in line:
            line = line.split(',')
            line = ''.join(line)
            return line
        else:
            return line
                

    # define methods for pulling leading characters
    @staticmethod
    def pull_trailing_character(line:str)-> str:
        """[Static method used by Soap class instance to Identify trailing characters and convert values in thousands to values as fractions of a million. also pulls non-alphanumeric trailing characters]

        Args:
            line ([str]): [String to be re-formatted, e.g. '10k' or '1000+' etc]

        Returns:
            [str]: [numeric string converted to correct unit. e.g. (see Args)--> '.01' or '1000']
        """
        # print(line[0:len(line)-1])
        if line[-1].lower() == 'k':
            return (int(float(line[0:len(line)-1])*1000) / 1000000)
        elif line[-1].lower() == 'm':
            return (int(float(line[0:len(line)-1])*1000000) / 1000000)
        elif line[-1].isalpha() == False:
            return line if line[-1].isdigit() else (line[0:len(line)-1]) 
        else:
            return line


    # define methods for pulling trailing characters
    @staticmethod
    def pull_leading_character(line:str)-> str:
        """[Static method used by Soap class instance to remove leading non-numeric characters from numeric strings]

        Args:
            line ([str]): [numeric string with leading character, e.g. '$4.99. method assumes no whitespace between char and digit]

        Returns:
            [str]: [re-formatted numeric string with no leading characters]
        """
        return line[0:] if line[0].isdigit() else line[1:len(line)]
        # current solution assumes trailing char only == 'm || M' or 'k || K' and converts 'k || K' to a decimal of 1Million. 
        # mvp: keep assumption and note it in Docs. stretch: account for all unit conversion types.
        # current solution takes form ` if str[-1] == 'k': convert to str[:-1]//100^10 else return str[:-1]`
        


    # identify highest denomination and convert all figures to fraction of that denomination
    @staticmethod
    def convert_unit(line:str, unit_target:str)-> str:
        """[Static method used by Soap class instances to identify units of measure and convert to fractions of specified whole unit. e.g. '10k' to '.01'million]

        Args:
            line ([str]): [numeric string with a trailing unit of measure character]
            unit_target ([str]): [The preferred unit of measure for numeric strings to be converted to e.g. 'M' or 'k']

        Returns:
            [str]: [reformated numeric string as fraction of specified unit_target or numeric string with no trailing non-numeric characters]
        """
        # step 1: identify the suffix line -1
        for i in units.keys():
            print(f'i in convert_unit{i} \n units.keys{units.keys()}')
            if i in str(line):
                line = int(float(line[0: line.index(i)]))*units[i] /units[unit_target]
            else:
                pass
        return str(line)
        # no current logic written for this, previously was handled as part of  pull_trailing logic. 
     




