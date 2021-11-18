from pandas import DataFrame
from pandas import read_excel
import numpy as np
import pandas as pd

#DF处理空值
df = read_excel(r'C:\Users\Woden\Desktop\python\rz.xlsx', sheet_name='Sheet2')
print(df)
print(df.isnull())
print(df.notnull())
print(df.dropna())
print(df.fillna(method='pad'))
print(df.fillna(df.mean()['高代':'解几']))

#DF切分数据
df = read_excel(r'C:\Users\Woden\Desktop\python\i_nuc.xls', sheet_name='Sheet4')
df['学号'] = df['学号'].astype(str)
print(df['学号'])
college = df['学号'].str.slice(0,2)
grade = df['学号'].str.slice(2,4)
myclass = df['学号'].str.slice(4,6)
sno = df['学号'].str.slice(6,10)
print(college)
print(grade)
print(myclass)
print(sno)

#DF分割列
df['IP'].str.strip()
newIP = df['IP'].str.split('.',4,True)
print(newIP)

# df = DataFrame({'age':[26,85,64,85,85],'name':['BEN','John','Jerry','John','John']})
# df = df.set_index('name')
# print(df)
# print(df.iloc[1])

#DF条件选择
print(df[df.电话>13400000000].head())
print(df[df.IP.str.contains('222.',na = False)])

#DF随机选取行
r = np.random.randint(0,10,3)
print(r)
print(df.iloc[r,:])
print(df.loc[1:4,'IP'])

#从字典初始化DF
d = {'a':[1,2,3],'b':[2,3,4]}
a1 = DataFrame.from_dict(d, orient='index')
print(a1)

#DF合并
df1 = read_excel(r'C:\Users\Woden\Desktop\python\i_nuc.xls', sheet_name='Sheet3')
df2 = read_excel(r'C:\Users\Woden\Desktop\python\i_nuc.xls', sheet_name='Sheet5')
df3 = pd.concat([df1,df2])
print(df3)
df3 = pd.concat([df1,df2], ignore_index=True)
print(df3)
he = df3['高代']+df3['解几']
print(he)
he = df3['高代'].astype(str)+df3['解几'].astype(str)
print(he)
