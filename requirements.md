## Software Requirements

It will be an external module that users can download from Python Packaging Index

It will handle dataframe objects created with the pandas module.

Scope
IN
MVP:
importable module that takes pandasDataframe or CSV file and provides the following functionality:
Checks cell data for correct formatting (ex. no leading char for int/float
not trailing char for int/float)
ease of column renaming
method that returns a copy of the original with scrubbed data
method that shows comparison of original to cleaned data for manual verification and tracing of any potential corruption in the cleaning process
convert common denomination notations such as 'k' 'm' etc

Stretch Goals:
Column Renamer

OUT
This module will never be converted into a standalone app.
This module will not run without pandas.

Functional Requirements
A user can install dataSoap module
A user can use a pandas dataframe to create a new dataframe with cleaned up number formatting for the specified columns
A user can see a comparison of the original and new dataframe

Data Flow:
Happy Path > Install dataSoap package, create pandas dataframe, manipulate data, output new data frame along with the original data frame

Processed data: CSV files (specifically data intended to be numbers)

Non-Functional Requirements
Usability - easy to use without errors or excessive complexity
Testability - ensure at least 80% coverage