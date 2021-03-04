from math import prod
n = int(input())
s = 0
for i in range(2,n+1):
    s+= sum(range(1,i+1))/prod(range(1,i+1))
print(s)