# -*- coding: utf-8 -*-
'''
杨辉三角定义如下：

          1
        1   1
      1   2   1
    1   3   3   1
  1   4   6   4   1
1   5   10  10  5   1
'''

def triangles():
    l = [1]
    yield l
    while True:
        l = [1] + [l[i] + l[i + 1] for i in range(len(l) - 1)] + [1]
        yield l
        
# 期待输出:
# [1]
# [1, 1]
# [1, 2, 1]
# [1, 3, 3, 1]
# [1, 4, 6, 4, 1]
# [1, 5, 10, 10, 5, 1]
# [1, 6, 15, 20, 15, 6, 1]
# [1, 7, 21, 35, 35, 21, 7, 1]
# [1, 8, 28, 56, 70, 56, 28, 8, 1]
# [1, 9, 36, 84, 126, 126, 84, 36, 9, 1]
n = 0
for t in triangles():
    print(t)
    n = n + 1
    if n == 10:
        break


'''
 L= [1]
  while True:
     yield L
     T = []
     for i in range(len(L)-1):
         T.append(L[i]+L[i+1])
     L = [1] + T + [1]
'''


'''
def triangles(max):
    L=[1]
    n=0
    while n<max:
        yield L
        L=[1]+[L[i]+L[i+1] for i in range(len(L)-1)]+[1]
        n=n+1

for t in triangles(10):
    print(t)
'''

'''
def triangles(max):
    L=[1]
    n=0
    while(n<max):
        yield L
        L.insert(0,1)
        for i in range(1,len(L)-1):
            L[i]+=L[i+1]
        n+=1

for i in triangles(10):
    print(i)
'''
