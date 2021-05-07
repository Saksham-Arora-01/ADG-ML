import pandas as pd
 
empl = pd.DataFrame({
    'Code': ['1', '0'],
    'Name': ['Saksham', 'Rohit'],
    'Occupation': ['WC', 'President'],
    'Date Of Join': ['2021-05-20', '2020-01-01'],
    'Age': [19, 21]})
 
print("\n------------ BEFORE ----------------\n")
print(empl)
 
line = pd.DataFrame({'Code': ['3'],
    'Name': ['Rahul'],
    'Occupation': ['ML'],
    'Date Of Join': ['2020-01-01'],
    'Age': [21]}, index=[0])
 
empl = pd.concat([line,empl.iloc[:]]).reset_index(drop=True)
print("\n------------ AFTER ----------------\n")
print(empl)
######################################33
Output ::

------------ BEFORE ----------------

Code     Name Occupation Date Of Join  Age
0    1  Saksham         WC   2021-05-20   19
1    0    Rohit  President   2020-01-01   21
------------ AFTER ----------------

Code     Name Occupation Date Of Join  Age
0    3    Rahul         ML   2020-01-01   21
1    1  Saksham         WC   2021-05-20   19
2    0    Rohit  President   2020-01-01   21
> 

