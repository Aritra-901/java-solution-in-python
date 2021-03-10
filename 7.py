#Write a program that prompts the user to input a positive integer. It should then print the multiplication table of that number.



num = int(input(" multiplication table of"))
# using for loop to iterate multiplication 10 times
for i in range(1,11):
   print(num,'x',i,'=',num*i)