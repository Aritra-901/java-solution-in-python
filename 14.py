#Write a program to print out all Armstrong numbers between 1 and 500. If sum of cubes of each digit of the number is equal to the number itself, then the number is called an Armstrong number.
#For example, 153 = ( 1 * 1 * 1 ) + ( 5 * 5 * 5 ) + ( 3 * 3 * 3 )

def armstrong_number(x):
    st=str(x)
    n=len(st)
    sum=0
    for i in range(n):
        sum+=pow(int(st[i]),n)
    if x==sum:
        return "armstrong number"
    else:
        return "not armstrong number"
print(armstrong_number(153))