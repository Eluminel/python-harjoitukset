import random
import math

#Ex1
# Write a function that returns a random dice roll between 1 and 6.
# The function should not have any parameters. Write a main program that rolls the dice until the result is 6. 
# The main program should print out the result of each roll.

def dice_function():
    dice = random.randint(1, 6)
    while dice != 6:
        print(f"The number on the dice is {dice}")
        dice = random.randint(1, 6)
    print(f"The number on the dice is {dice}")
    return

dice_function()

#Ex2
# Modify the function above so that it gets the number of sides on the dice as a parameter.
# With the modified function you can for example roll a 21-sided role-playing dice. 
# The difference to the last exercise is that the dice rolling in the main program continues 
# until the program gets the maximum number on the dice, which is asked from the user at the beginning.

def dice_function(number_of_sides):
    dice = random.randint(1, number_of_sides)
    while dice != number_of_sides:
        print(f"The number on the dice is {dice}")
        dice = random.randint(1, number_of_sides)
        
    print(f"The number on the dice is {dice}")
    return

dice_function(20)
dice_function(50)
dice_function(100)

#Ex3 
#Write a function that gets the quantity of gasoline in American gallons
#and returns the number converted to litres. 
#Write a main program that asks for a volume in gallons from the user and converts the value to liters. 
#The conversion must be done by using the function. Conversions continue until the user inputs a negative value.

def converts_function():
    liquid_gallon = float(input("Enter the quantity of gasoline in American gallons: "))
    while liquid_gallon > 0:
        litres = liquid_gallon * 3.78541
        print(f"The volume in liters is equal to {litres}")
        liquid_gallon = float(input("Enter the quantity of gasoline in American gallons: "))
    return

converts_function()

#Ex4 
# Write a function that gets a list of integers as a parameter. 
# The function returns the sum of all the numbers in the list. 
# For testing, write a main program where you create a list, call the function, 
# and print out the value it returned.

def summa(integers):
    sum = 0
    for integer in integers:
        sum += integer
    return sum

numbers = [1, 2, 3, 4, 5]
result = summa(numbers)
print(f"Sum of numbers: {result}")

#Ex5
# Write a function that gets a list of integers as a parameter. 
# The function returns a second list that is otherwise the same as the original list except that all 
# uneven numbers have been removed. For testing, write a main program where you create a list, 
# call the function, and then print out both the original as well as the cut-down list.


def even_number_list(integers):
    even_list = []
    for integer in integers:
        if integer % 2 == 0:
            even_list.append(integer)
    return even_list

numbers = input("Enter a list of integers as a parameter: ").split()
int_list = [int(x) for x in numbers]
even_list = even_number_list(int_list)
print(f"Original list {int_list}")
print(f"cut-down list {even_list}")

#Ex6
# Write a function that receives two parameters: 
# the diameter of a round pizza in centimeters and the price of the pizza in euros. 
# The function calculates and returns the unit price of the pizza per square meter. 
# The main program asks the user to enter the diameter and price of two pizzas and 
# tells the user which pizza provides better value for money (which of them has a lower unit price). 
# You must use the function you wrote for calculating the unit prices.


def pizza_selection(diameter, price):
    price_per_square_meter = price/(math.pi*((diameter/2)**2)/10000)
    return price_per_square_meter


pizza_1_diameter = float(input("Enter the diameter of the first pizza: "))
pizza_1_price = float(input("Enter the price of the first pizza: "))
pizza_2_diameter = float(input("Enter the diameter of the second pizza: "))
pizza_2_price = float(input("Enter the price of the second pizza: "))

price_1_per_square_meter = pizza_selection(pizza_1_diameter, pizza_1_price)
price_2_per_square_meter = pizza_selection(pizza_2_diameter, pizza_2_price)

if price_1_per_square_meter > price_2_per_square_meter:
    print("Buy pizza number 2!")
elif price_1_per_square_meter == price_2_per_square_meter:
    print("Buy either one, they cost the same per square meter!")
else:
    print("Buy pizza number 1!")
