import numpy as np
import pandas as pd

s = pd.Series(np.random.randn(5), index=['a', 'b', 'c', 'd', 'e'])
print(s)
print(s[1])
print(s['a':'c'])
print(s[['a','c','b']])
#s.append(6)
n = pd.Series([6])
s = s.append(n)
print(6 in s.values)
#print(s.drop(0))
print(s.index[2])
print(s[6!=s.values])
s[s.index[s.values!=6]]=6
print(s.index[s.values == 6])
print(s[1:] + s[:-1])
s = s.reindex(['a', 'b', 'c', 'd', 'e', 'f'], fill_value=0)
print(s)