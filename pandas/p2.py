import pandas as pd
 
n = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9]
 
i = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
 
series = pd.Series(n, index=i)

print("\n [:4:2] \n")
print(series[:4:2])
 
print("\n [4::2] \n")
print(series[4::2])
 
print("\n [::-1] \n")
print(series[::-1])

##################################

Output ::

[:4:2]
 
A      0
C      2
dtype: int64
 
 [4::2]
 
E    4
G    6
I    8
dtype: int64
 
 [::-1]
 
J    9
I    8
H    7
G    6
F    5
E    4
D    3
C    2
B    1
A    0
dtype: int64