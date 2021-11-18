# -*- coding: utf-8 -*-
# MyString = "Hello world!"
# print(MyString+"\n")
import tensorflow as tf
print(tf.test.gpu_device_name())


# Value = 1 / 3.0
# print(Value)

# print('%e' % Value)

# print('%4.2f' % Value)

# print('{0:4.2f}'.format(Value))

# print(1 < 2)

# print(2.0 >= 1)

# print(2.0 == 2.0)

# print(2.0 != 2.0)

# print(1 < 2 and 2 < 3)

# print(1 < 2 or 2 > 3)

# print(0o1, 0o20, 0o377)

# print(0x01, 0x10, 0xff)

# print(0b1, 0b10000, 0b11111111)

# print(64, 0o100, 0x40, 0b1000000)

# print(int('64'), int('100', 8), int('40', 16), int('1000000', 2))

# print(int('0x40', 16), int('0b1000000', 2))

# import math

# print(math.pi, math.e)

# print(math.sqrt(144), math.sqrt(2))

# print(pow(2, 4), 2 ** 4, 2.0 ** 4.0)

# print(abs(-2.0), sum((1, 2, 3)))

# print(min(3, 1, 2), max( 3, 1, 2))

# x = set('abcde')

# y = set('bdxyz')

# print(x)

# print(y)

# print(x-y)

# print(x|y)

# print(x&y)

# print(x^y)

# print('e' in x, 'e' in 'Camel', 'e' in ['a', 'e', 'o'])

# S = "HILab"

# print(S[0], S[-2])

# print(S[1:3], S[1:], S[:-1])

# print(S[0:5:2])

# print(ord('s'))

# print(chr(115))

# #错误的更改字符串内容的方法
# # #S[0] = 'A’

# SS='A' + S[1:]

# print(SS)

# x = 1234

# res = 'integers:   [%d]   [%-6d]   [%06d]' % (x, x, x)

# print(res)

# print(len([1, "a", 2, "b", 3, "c"]))

# print([1, 2, 3] + ["a", "b", "c"])

# print(["Hello", "World"] * 3)

# print(str([1, 2]) + "34")

# print([1, 2] + list("34"))

# tList = ["Hello", "world", "!"]

# print(tList)

# print(tList[2], tList[-2], tList[1:])

# tMatrix = [[1, 2, 3], [4, 5, 6], [7, 8, 9]]

# print(tMatrix[1])

# print(tMatrix[2][1])

# L = ['abc', 'ABD', 'aBe']

# L.sort()

# print(L)

# L = ['abc', 'ABD', 'aBe']

# L.sort(key=str.lower, reverse=True)

# print(L)

# D = {'spam': 2, 'ham': 1, 'eggs': 3}

# print(D['spam'])

# ##Case sensitive error
# # print(D['SPAM'])

# print(len(D))

# print("ham" in D)

# print(list(D.keys()))

# D = {'spam': 2, 'ham': 1, 'eggs': 3}

# D['ham'] = ['grill', 'bake', 'fry']

# print(D)

# del D['eggs']

# print(D)

# D['brunch'] ='Bacon'

# print(D)

# del D['ham']

# print(D)

# D = {'spam': 2, 'ham': 1, 'eggs': 3}

# D2 = {'toast':4, 'muffin':5}

# D.update(D2)

# print(D)

# branch = {'eggs': 0.99, 'ham': 1.99, 'spam': 1.25}
# print(branch)

# print(branch.get('spam', 'Bad choice'))

# print(branch.get('spam1', 'Bad choice'))
# import sys
# myfile = open(r"D:\OLD\GRC\Classes of Python\McTwo-datasets.csv")
# try:
#     for line in myfile:
#         print(line)
# finally:
#     myfile.close()
#     print(myfile)

# X, Y, Z = 43, 44, 45
# S = 'Spam'
# D = {'a': 1, 'b': 2}
# L = [1, 2, 3]

# F = open('datafile.txt', 'w')
# F.write(S + '\n')
# F.write('%s,%s,%s\n' % (X, Y, Z))
# F.write(str(L) + '$' + str(D) + '\n')
# F.close()
# chars = open('datafile.txt').read()
# print(chars)

# print({'job': ['dev', 'mgr'], 'name': {'last': 'Smith', 'first': 'Bob'}, 'age': 40.5})
# name = dict(first='Bob', last='Smith')
# rec = dict(name=name, job=['dev', 'mgr'], age=40.5)
# import json
# json.dump(rec, fp=open('testjson.txt', 'w'), indent=4)
# P = json.load(open('testjson.txt'))
# print(P == rec)

# import csv
# rdr = csv.reader(open("McTwo-datasets.csv"))
# for row in rdr: print(row)

# x='SPAM'
# if 'rubbery' in 'shrubbery':
#     print(x*8)
#     x += 'NI'
#     if x.endswith('NI'):
#         x *=2
#         print(x)


# x='SPAM'
# if 'rubbery' in 'shrubbery':
#     print(x*8)
#     x += 'NI'
#     if x.endswith('NI'):
#         x *=2
#         print(x)

# a=b=c=d=e=f=g=2
# if a==b and c==d and \
#     d==e and f==g:
#     print('olde')

# if (a==b and c==d and
#     d==e and f==g):
#     print('new')

# x=1; y=2; print(x)

# if 1:print('hello')

# T = [(1, 2), (3, 4), (5, 6),(7,8),(10,11)]
# for (a, b) in T:
#     print(a, b)

# range(1, 10, 3)
# print (list(range(1, 10, 3)))

# range(0,5)
# print(list(range(0,5)))

# def intersect(seq1, seq2):
#     res = [] # Start empty
#     for x in seq1: # Scan seq1
#         if x in seq2: # Common item?
#             res.append(x) # Add to end
#     return res

# s1 = "SPAM"
# s2 = "SCAM"
# print(intersect(s1, s2))


# ['S', 'A', 'M']

# def mysum(L):
#     print(L) # Trace recursive levels
#     if not L: # L shorter at each level
#         return 0
#     else:
#         return L[0] + mysum(L[1:])

# mysum([1, 2, 3, 4, 5])

# import numpy as np
# import array
# import pandas as pd
# import operator
# import csv
# import scipy

# def efReadCSV( tFileName ):
#     tLines = csv.reader(open(tFileName))
#     tDataset = list(tLines)
#     tLength = len(tDataset[0])
#     tFeature = tDataset[0][2:(tLength-1)]
#     tSample = list(range(len(tDataset)-1))
#     tClass = list(range(len(tDataset)-1))
#     tMatrix = list(range(len(tDataset)-1))
#     for i in range(1, len(tDataset)):
#         tSample[i-1] = tDataset[i][0]
#         tClass[i-1] = tDataset[i][1]
#         tMatrix[i-1] = [float(x) for x in tDataset[i][2:(tLength-1)]]
#     return (tFeature), (tSample), (tClass), (tMatrix)

# eg=efReadCSV("McTwo-datasets.csv")
# egFeature=eg[2]
# data=np.array(eg[3])
# x=data[:,0]
# y=data[:,1]

# from scipy import stats
# # np.random.seed(888)
# (elTvalue, elPvalue) = stats.ttest_ind(x, y)
# idxRank = np.asarray(range(len(egFeature)))
# elDict = {}
# for tI in range(len(idxRank)): elDict[idxRank[tI]] = elPvalue[tI]
# tempRS = np.asarray(sorted(elDict.items(), key=lambda d: d[1]))[:,0]
# idxRankSort = range(len(tempRS))
# # for tI in range(len(tempRS)): idxRankSort[tI] = int(tempRS[tI])

# import matplotlib.pyplot as plt
# egFigure = plt.figure(figsize=[12, 7], dpi=120)
# egFigure.add_subplot(111).scatter(data[:,idxRankSort[0]], data[:,idxRankSort[1]])

# a = [1, 3, 5, 7, 9]
# print(a[2:4])
# [5, 7]
# b = [[1, 3, 5, 7, 9], [2, 4, 6, 8, 10]]
# print(b[0])
# [1, 3, 5, 7, 9]
# print(b[1][2:4])
# a = [1, 3, 5, 7, 9]
# b = [3, 5, 6, 7, 9]
# c = a + b
# print(c)

# as vectors from lists
import numpy as np
# a = numpy.array([1, 3, 5, 7, 9])
# b = numpy.array([3, 5, 6, 7, 9])
# c = a + b
# print (c)

# type(c)
# print(c.shape)

# l = [[1, 2, 3], [3, 6, 9], [2, 4, 6]]  # create a list
# a = np.array(l)  # convert a list to an array
# print(a)
# print(a.shape)
# print(a.dtype)  # get type of an array

# # or directly as matrix
# M = numpy.array([[1, 2], [3, 4]])
# print(M.shape)
# print(M.dtype)

# only one type
# M[0,0]= "hello"
# print(M)

# M = numpy.array([[1, 2], [3, 4]], dtype=complex)
# print(M)
# print(M.dtype)

# print(a)
# print(a[0])  # this is just like a list of lists

# print(a[1, 2])  # arrays can be given comma separated indices

# print(a[1, 1:3])  # and slices

# print(a[:, 1])

# a[1, 2] = 7
# print(a)

# a[:, 0] = [0, 9, 8]
# print(a)

# x = np.arange(0, 10, 1) # arguments: start, stop, step
# print(x)
# lin=np.linspace(0, 10, 25)
# print(lin)
# log=np.logspace(0, 10, 10, base=np.e)
# print(log)

# dia = np.diag([1, 2, 3])
# print(dia)
# b = np.zeros(5)
# print(b)
# print(b.dtype)

# n = 1000
# my_int_array = np.zeros(n, dtype=np.int)
# print(my_int_array.dtype)

# c = np.ones((3, 3))
# print(c)

# d = np.arange(5)  # just like range()
# print(d)

# d[1] = 9.7
# print(d)  # arrays keep their type even if elements changed


# print(d*0.4)  # operations create a new array, with new type


# d = np.arange(5, dtype=np.float)
# print(d)


# print(np.arange(3, 7, 0.5))  # arbitrary start, stop and step

# egMatrix = np.array([[0, 1, 2], [3, 4, 5]])
# print(egMatrix.ndim)
# print(egMatrix.shape)
# print(egMatrix.size)
# print(egMatrix.dtype)
# print(egMatrix.itemsize)
# print(egMatrix)

# x = np.array([1, 2, 3, 4])
# y = x
# print(x is y)
# print(id(x), id(y))

# x[0] = 9
# print(y)
# print(x)

# x[0] = 1
# z = x[:]
# print(z)
# print(x)
# print(x is z)

# print(id(x), id(z))

# x[0] = 8
# print(z)
# print(x)

# x = np.array([1, 2, 3, 4])
# y = x.copy()
# print(x is y)
# print(id(x), id(y))
# x[0] = 9
# print(x)
# print(y)

# a = np.arange(4.0)
# print(a)
# b = a * 23.4
# print(b)
# c = b/(a+1)
# print(c)
# c += 10
# print(c)


# arr = np.arange(100, 200)
# select = [5, 25, 50, 75, -5]
# print(arr[select])  # can use integer lists as indices

# arr = np.arange(10, 20)
# div_by_3 = arr % 3 == 0  # comparison produces boolean array
# print(div_by_3)

# print(arr[div_by_3])  # can use boolean lists as indices

# arr = np.arange(10, 20).reshape((2, 5))
# print(arr)

# arr = np.array([4.5, 2.3, 6.7, 1.2, 1.8, 5.5])
# arr.sort()  # acts on array itself
# print(arr)

# x = np.array([4.5, 2.3, 6.7, 1.2, 1.8, 5.5])
# np.sort(x)
# print(np.sort(x))

# print(x)

# s = x.argsort()
# print(s)
# print(x[s])
# y=np.arange(6.0)
# print(y)
# print(y[s])

# print(arr.sum())
# print(np.sum(arr))

# a = np.array([[1.0, 2.0], [4.0, 3.0]])
# print(a)

# transA = a.transpose()
# print(transA)

# invA =np.linalg.inv(a)
# print(invA)

# u = np.eye(2)  # unit 2x2 matrix; "eye" represents "I"

# print(u)

# j = np.array([[0.0, -1.0], [1.0, 0.0]])

# print(np.dot(j, j))  # matrix product

# a = np.array([1, 4, 3, 8, 9, 2, 3], float)
# print(np.median(a))
# print(np.mean(a))

# a = np.array([[1,2],[3,4]]) 
# m = np.mat(a) 
# n=a.copy()
# a[0,1]=100
# print(a)
# print(m)


# a = np.array([[1,2],[3,4]]) 

# m = np.asmatrix(a)
# print(m)
# a[0,0]=100
# print(m)
# print(a)
import tensorflow as tf
print(tf.test.gpu_device_name())