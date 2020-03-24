# dic1 = {4:"b", 2:"d", 3:"a", 1:"c"}
# list1 = ((4, "b"), (2, "d"), (3, "a"), (1, "c"))
# #dic1.sort(key=lambda i: i[1])
# #for k in sorted(dic1.values()):
# #    print (k, ':', dic1[k])
# print(sorted(list1, key=lambda student: list1[0]))
# #print(list1)

import numpy as np

# a = np.array([[1, 2, 3], [4, 5, 6]])
# x = []
# y = 0
# print (len(a)+1)
# for i in range(len(a)+1):
#     x.append([(a[0,i]), (a[1,i])])
# print(x)

x=[[1,2],[2,3]]
y=[[2,3],[3,4]]
# if min(y) in x:
#     print("yes")
#     print(min(y))
#     y.pop(y.index(min(y)))
z = [x[0][0]+y[0][0], x[0][1]+y[0][1]]
print(z)