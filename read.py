#Develop a python program to read n digit interger, and separate the integer number and display each digit.

n = input("Enter the number: ")
length = len(n)
n = int(n)
divisor = 10 ** (length - 1)

print("The digits are:")

while divisor > 0:
    digit = n // divisor
    print(digit)
    n = n % divisor
    divisor = divisor // 10
