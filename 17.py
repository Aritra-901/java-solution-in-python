#** ** ** ** **
#** ** ** ** **
#** ** ** ** **
#** ** ** ** **


print("first pattern")
for i in range(4):
    for j in range(10):
        print("*",end='')
    print()


#*
#**
#***
#****
#*****



print("second pattern")
for i in range(1,6):
    for j in range(1,i+1):
        print("*",end='')
    print()



#    *
#   **
#  ***
# ****
#*****



print("third pattern")
for i in range(1,6):
    for j in range(5,i,-1):
        print(" ",end='')
    for k in range(1,i+1):
        print("*",end='')
    print()



#    *
#   ***
#  *****
# *******
#*********



print("fourth pattern")
for i in range(1,6):
    for j in range(5,i,-1):
        print(" ",end='')
    for k in range(1,2*i):
        print("*",end='')
    print()



#    1
#   222
#  33333
# 4444444
#555555555



print("fifth pattern")
for i in range(1,6):
    for j in range(5,i,-1):
        print(" ",end='')
    for k in range(1,2*i):
        print(i,end='')
    print()



#    1
#   212
#  32123
# 4321234
#543212345



print("sixth pattern")
for i in range(1,6):
    for j in range(5,i,-1):
        print(" ",end='')
    for k in range(i,0,-1):
        print(k,end='')
    for l in range(2,i+1):
        print(l,end='')
    print()