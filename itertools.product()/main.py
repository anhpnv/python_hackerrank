from itertools import product

A = [int(i) for i in input().split()]
B = [int(i) for i in input().split()]

C = [A, B]
D = list(product(*C))
print(*D,sep=" ")