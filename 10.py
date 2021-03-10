#Write a program that prompts the user to input an integer and then outputs the number with the digits reversed. For example, if the input is 12345, the output should be 54321.

n = 1234;
rev = 0

while (n > 0):
    a = n % 10
    rev = rev * 10 + a
    n = n // 10

print(rev)