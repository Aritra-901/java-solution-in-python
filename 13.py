#Write a program to calculate HCF of Two given number.
def compute_hcf(x, y):
   while(y):
       x, y = y, x % y
   return x

hcf = compute_hcf(200, 600)
print("The HCF is", hcf)