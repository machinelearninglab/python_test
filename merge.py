from pandas import read_excel
from pandas import DataFrame
from pandas import merge
import pandas as pd
from datetime import datetime
#from sklearn import perprocessing

#更改DF内容
df1 = read_excel(r'C:\Users\Woden\Desktop\python\i_nuc.xls', sheet_name='Sheet3')
print(df1.head())

print(df1.replace('作弊',0))  #单值替换，用0替换作弊
print(df1.replace({'体育':'作弊','军训':'缺考'},0)) #指定列单值替换
print(df1.replace(['成龙','周怡'],['陈龙','周毅'])) #多值替换
print(df1.replace({'成龙':'陈龙','周怡':'周毅'}))
print(df1.replace({'成龙','周怡'},{'陈龙','周毅'}))

#DF排序
d = {'Ohio':[3,0,3],'Texas':[7,4,1],'California':[2,8,5]}
df = DataFrame(d,index = ['a','d','c'])
print(df.sort_index())
print(df.sort_values(by = 'Ohio'))
print(df.sort_values(by = ['Ohio', 'Texas']))
print(df.sort_index(axis = 1, ascending=False))

#DF按列合并
df2 = read_excel(r'C:\Users\Woden\Desktop\python\i_nuc.xls', sheet_name='Sheet4')
df3 = merge(df1,df2,left_on='学号',right_on='学号', how='left')
print(df3)

#DF标准化（商差标准化）
scale = (df1['数分']-df1['数分'].min())/(df1['数分'].max()-df1['数分'].min())
print(scale)

#DF分组
bins = [min(df1.解几)-1,60,70,80,max(df1.解几)+1]
labs = ['不及格','及格','良好','优秀']
demo = pd.cut(df1.解几,bins,right=False,labels=labs)
#print(demo)
df1['demo'] = demo
print(df1.head())

#DF处理时间格式
df4 = pd.read_csv(r'C:\Users\Woden\Desktop\python\rz3.csv')
print(df4.head())
df_dt = pd.to_datetime(df4.date, format='%Y/%m/%d')
print(df_dt.head())
df_dt_str = df_dt.apply(lambda x: datetime.strftime(x,'%Y/%m/%d'))
print(df_dt_str.head())