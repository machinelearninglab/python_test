from pandas import read_excel
import matplotlib.pyplot as plt
import numpy as np
import pandas as pd
from scipy import stats
from statsmodels.formula.api import ols
from statsmodels.stats.anova import anova_lm
from sklearn.decomposition import PCA
from sklearn.datasets import load_iris

df = read_excel(r'G:\课程\Python\i_nuc.xls', sheet_name='Sheet7')
print(df.head())
#基本分析
print(df.数分.describe())
print(df.数分.size)
print(df.数分.max())
print(df.数分.min())
print(df.数分.sum())
print(df.数分.mean())
print(df.数分.var())
print(df.数分.std())
print(df.数分.mode()) #众数
print(df.数分.median())

#plt.rcParams['font.family'] = ['Kaiti']
plt.rcParams['font.sans-serif'] = ['SimSun']
df.boxplot(column = ['军训','英语','体育','数分'],
           sym = 'o', # 异常值形式
           vert = True, #垂直显示
           whis = 1.5, #IQR
           patch_artist = True, #箱子是否填充
           meanline = False, #均值线是否显示
           showmeans = True,
           showbox = True,#是否显示箱子
           showfliers = True, #是否显示异常值
           notch = True, #中位数是否有缺口
           return_type='dict'
)
plt.show()

#分组分析
print(df.groupby('班级')['军训','英语','体育','性别'].mean())
print(df.groupby(['班级','性别'])['军训','英语'].agg({
    '人数':np.size,
    '平均数':np.mean,
    '标准差':np.std
}))

#分组分布
df['总分'] = df.英语+df.体育+df.军训+df.数分+df.高代+df.解几
print(df['总分'].describe())
bins = [min(df['总分'])-1, 400, 450,max(df['总分'])+1]
labels = ['400及以下','400-450','450及以上']
df['总分分层'] = pd.cut(df.总分,bins,labels=labels)
print(df.tail())
print(df.groupby('总分分层')['英语'].agg(人数=np.size))
#交叉分析
print(df.pivot_table(values=['总分'],
               index=['总分分层'],
               columns=['性别'],
               aggfunc=[np.size, np.mean]))
#结构分析
df_pt = df.pivot_table(values=['总分'],
               index=['班级'],
               columns=['性别'],
               aggfunc=[np.sum])
print(df_pt.div(df_pt.sum(axis = 1), axis=0))#按列占比
print(df_pt.div(df_pt.sum(axis = 0), axis=1))#按行占比
#相关分析
print(df['高代'].corr(df['数分'], method = 'kendall'))
print(df['高代'].corr(df['数分'], method = 'spearman'))
print(df['高代'].corr(df['数分'], method = 'pearson'))
print(df.loc[:,['英语','体育','军训','数分','高代','解几']].corr())
#t-test
print(stats.ttest_ind(df['高代'],df['数分'], equal_var = False))
#anova
df.boxplot(column = ['数分','体育'],
           by = ['总分分层'],
           sym = 'o', # 异常值形式
           vert = True, #垂直显示
           whis = 1.5, #IQR
           patch_artist = True, #箱子是否填充
           meanline = False, #均值线是否显示
           showmeans = True,
           showbox = True,#是否显示箱子
           showfliers = True, #是否显示异常值
           notch = True, #中位数是否有缺口
           return_type='dict'
)
plt.show()
model = ols('数分 ~ 总分分层',df).fit()
anovat = anova_lm(model)
print(anovat)
print(anova_lm( ols('体育 ~ 总分分层',df).fit()))
#PCA
y=df.总分分层
x=df.loc[:,['英语','体育','军训','数分','高代','解几']]
pca=PCA(n_components=2)     #加载PCA算法，设置降维后主成分数目为2
reduced_x=pca.fit_transform(x)#对样本进行降维
red_x,red_y=[],[]
blue_x,blue_y=[],[]
green_x,green_y=[],[]
for i in range(len(reduced_x)):
    if y[i] =='400及以下':
        red_x.append(reduced_x[i][0])
        red_y.append(reduced_x[i][1])
    elif y[i]=='400-450':
        blue_x.append(reduced_x[i][0])
        blue_y.append(reduced_x[i][1])
    else:
        green_x.append(reduced_x[i][0])
        green_y.append(reduced_x[i][1])
#可视化
plt.scatter(red_x,red_y,c='r',marker='x')
plt.scatter(blue_x,blue_y,c='b',marker='D')
plt.scatter(green_x,green_y,c='g',marker='.')
plt.show()

#鸢尾花分类为例
data=load_iris()
y=data.target
x=data.data
pca=PCA(n_components=2)     #加载PCA算法，设置降维后主成分数目为2
reduced_x=pca.fit_transform(x)#对样本进行降维
red_x,red_y=[],[]
blue_x,blue_y=[],[]
green_x,green_y=[],[]
for i in range(len(reduced_x)):
    if y[i] ==0:
        red_x.append(reduced_x[i][0])
        red_y.append(reduced_x[i][1])
    elif y[i]==1:
        blue_x.append(reduced_x[i][0])
        blue_y.append(reduced_x[i][1])
    else:
        green_x.append(reduced_x[i][0])
        green_y.append(reduced_x[i][1])
#可视化
plt.scatter(red_x,red_y,c='r',marker='x')
plt.scatter(blue_x,blue_y,c='b',marker='D')
plt.scatter(green_x,green_y,c='g',marker='.')
plt.show()