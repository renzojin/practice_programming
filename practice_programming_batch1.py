from colorama import Fore, Style, init
init(autoreset=True)

# #Prog01: Create a program that ask user to input 2 numbers. Print the bigger number.
num1 = (int(input(Fore.CYAN + "Enter First Number:")))
num2 = (int(input(Fore.CYAN + "Enter Second Number:")))

if num1 > num2:
    print (num1)
elif num1 < num2:
    print (num2)
print(" ")

# #Prog02: Create a program that ask user to input 2 numbers. Print "Equal" when the numbers are the same.
num1 = (int(input(Fore.YELLOW + "Enter First Number:")))
num2 = (int(input(Fore.YELLOW + "Enter Second Number:")))

if num1 == num2:
    print ("The numbers are equal.")
else:
    print ("The numbers are not equal.")
print(" ")

# #Prog03: Create a program that ask user to input 2 numbers. Print the sum of the two numbers.
num1 = (int(input(Fore.CYAN + "Enter First Number:")))
num2 = (int(input(Fore.CYAN + "Enter Second Number:")))

sum = num1 + num2
print(sum)
print(" ")

# #Prog04: Create a program that ask user to input 2 numbers. Print the product of the two numbers.
num1 = (int(input(Fore.YELLOW + "Enter First Number:")))
num2 = (int(input(Fore.YELLOW + "Enter Second Number:")))

product = num1 * num2
print(product)
print(" ")

#Prog05: Create a program that ask user to input 2 numbers. Print the quotient of the two numbers with the decimal point
num1 = (int(input(Fore.CYAN + "Enter First Number:")))
num2 = (int(input(Fore.CYAN + "Enter Second Number:")))

quotient = num1 / num2
print(quotient)
print(" ")

#Prog06: Create a program that ask user to input 2 numbers. Print the result when the first number is raised to the second number.
num1 = (int(input(Fore.YELLOW + "Enter First Number:")))
num2 = (int(input(Fore.YELLOW + "Enter Second Number:")))

result = num1 ** num2
print(result)
print(" ")

# Prog07: Create a program that ask user to input 10 numbers. Print the sum of all the numbers.
sum = 0

for i in range(10):
    num = int(input(Fore.CYAN + "Enter number: "))
    sum += num

print(sum)
print(" ")

#Prog08: Create a program that ask user to input 10 numbers. Print how many are odd numbers.
odd_count = 0

for i in range(10):
    num = int(input(Fore.YELLOW + "Enter number: "))

    if num % 2 != 0:
        odd_count += 1

print(odd_count)
print(" ")

#Prog09: Create a program that print all the even numbers starting from 0 to 100. (Use for loop)
for i in range(0, 101):
    if i % 2 == 0:
        print(i)
print(" ")

#Prog10: Create a program that print all the numbers starting from 0 to 100 except numbers ending in zero.
for i in range(0, 101):
    if i % 10 != 0:
        print(i)
