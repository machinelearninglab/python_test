from pandas import DataFrame
df1 = DataFrame({'age':[21,22,23],'name':['KEN','John','JIMI']})
df2 = DataFrame({'age':[21,22,23],'name':['KEN','John','JIMI']}, index = ['first','second','third'])
#访问行
print(df1[1:100])
print(df1[2:2])
print(df1[4:1])
print(df2['third':'third'])
print(df2['first':'third'])
#访问列
print(df1['age'])
print(df1[df1.columns[0:1]])
#访问块
print(df1.iloc[0:1,0:1])
#访问位置
print(df1.at[1,'name'])
print(df2.at['second','name'])
#print(df2.at[1,'name'])

df1.columns = ['age2','name2'] #修改列名
df1.index = range(1,4) #修改行索引
df1.drop(1, axis=0) #删除行，axis可以省略
df1.drop('age2', axis=1) #删除列，axis不以省略
del df1['age2'] #删除列
df1['age2'] = [0,2,4] #增加列
df2.loc[len(df2)] = [6, 'Keno'] #增加行，效率低

#合并DF
df = DataFrame([[1,2],[3,4]], columns=list('AB'))
df2 = DataFrame([[5,6],[7,8]], columns=list('AB'))
print(df.append(df2))
print(df.append(df2, ignore_index = True))

#DF去重
df = DataFrame({'age':[26,85,64,85,85],'name':['BEN','John','Jerry','John','John']})
print(df)
print(df.duplicated())
print(df.duplicated('name', keep=False))
print(df.duplicated('age', keep='last'))
print(df.drop_duplicates('age'))