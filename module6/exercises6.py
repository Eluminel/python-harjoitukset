import random
# Ex1
# Write a program that asks the user how many dice to roll. 
# The program rolls all the dice once and prints out the sum of the numbers. Use a for loop.

number = int(input("How many dice to roll?: "))
sum = 0

for n in range(number):
    if n <= number:
        dice = random.randint(1, 6)
        sum += dice
    print(sum)


#Ex2
#Write a program that asks the user to enter numbers until they input an empty string to quit. 
#At the end, the program prints out the five greatest numbers sorted in descending order. 
#Hint: You can reverse the order of sorted list items by using the sort method with the reverse=True argument.
  

number_list = []
num = input("Enter a number: ")

while num != "":
    number_list.append(int(num))
    num = input("Enter a number: ")

number_list.sort(reverse=True)

new_list = []

for num in number_list[:5]:
    new_list.append(str(num))

print(new_list)

#Ex3
#Write a program that asks the user for an integer and tells if the number is a prime number. 
# Prime numbers are number that are only divisible by one or the number itself.
# For example, 13 is a prime number as it can only be divided by 1 or 13 so that the result is an integer.
# On the other hand, 21 is not a prime number as it is divisible by 3 and 7.

num = int(input("Enter a number: "))

is_prime = True

for n in range(2, num):
    if num % n == 0:
        is_prime = False
if is_prime == False:
    print(f"{num} is composite number")
else:
    print(f"{num} is prime number")

#Ex4
# Write a program that asks the user to enter the names of five cities one by on 
# (use a for loop for reading the names) and stores them into a list structure. 
# Finally, the program prints out the names of the cities one by one, 
# one city per line, in the same order they were read as input. 
# Use a for loop for asking the names and a for/in loop to iterate through the list.


cities = []

for city in range(5):
    cities.append(input("Enter a city: "))

print(cities)

for city in cities:
    print(city)