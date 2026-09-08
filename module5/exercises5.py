import random
#Ex1
#Write a program that uses a while loop to print out all numbers divisible by three in the range of 1-1000.

number = 1
while number <= 1000:
    if number % 3 == 0:
        print(number)
    number += 1


#Ex2
#Write a program that converts inches to centimeters until the user inputs a negative value. 
# Then the program ends.

number = float(input("Enter a number: "))
while number >= 0:
    number_centimeters = number * 2.54 
    print(number_centimeters)
    number = float(input("Enter a number: "))

#Ex3
# Write a program that asks the user to enter numbers until they enter an empty string to quit. 
# Finally, the program prints out the smallest and largest number from the numbers it received.

number = input("Enter a number: ")

number_list = []
while number != "":
    number_list.append(float(number))
    number = input("Enter a number: ")
number_list.sort(reverse=True)

print(number_list[0], number_list[-1])

#Ex4
# Write a game where the computer draws a random integer between 1 and 10. 
# The user tries to guess the number until they guess the right number.
# After each guess the program prints out a text: Too high, Too low or Correct. 
# Notice that the computer must not change the number between guesses.

random_number = random.randint(1, 10)
guess_number = int(input("Enter the number you want to guess: ")) 
while random_number != guess_number:
    if guess_number > random_number:
        print("Too high")
    else:
        print("Too low")
    guess_number = int(input("Try to guess again: "))
print(f"Correct number {guess_number}")

#Ex5
# Write a program that asks the user for a username and password. 
# If either or both are incorrect, the program ask the user to enter the username and password again. 
# This continues until the login information is correct or wrong credentials have been entered five times. 
# If the information is correct, the program prints out Welcome. 
# After five failed attempts the program prints out Access denied. 
# The correct username is python and password rules.

username = input("Enter your username: ").lower()
password = input("Enter yout password: ").lower()
correct_username = "python"
correct_password = "rules"

attempts = 1

while attempts < 5:
    if username == correct_username and password == correct_password:
        print("Welcome")
        break
    elif username == correct_username and password != correct_password:
        print("Incorrect password")
        password = input("Try again. Enter yout password: ").lower()
    elif username != correct_username and password == correct_password:
        print("Incorrect username")
        username = input("Try again. Enter your username: ").lower()
    elif username != correct_username and password != correct_password:
        print("Incorrect username and password")
        password = input("Try again. Enter yout password: ").lower()
        username = input("Try again. Enter your username: ").lower()
    attempts += 1

else:
    print("Access denied")

#Ex6
# Implement an algorithm for calculating an approximation for the value of pi (π). 
# Let’s assume that A is a unit circle. 
# A unit circle has the radius of one and it is centered at the origin (0,0). 
# Smallest possible square B is drawn around the unit circle so that circle A is completely inside the square. 
# The corners of the square are now (-1,-1), (1, -1), (1, 1), and (-1, 1). 
# If a large number of random points are scattered inside the square, 
# the fraction of points that fall inside the circle A correlates with the fraction of the area of circle A 
# compared to the area of square B: πr^2/4 = π*1^2/4 = π/4. This can be used as a simple method 
# for calculating an approximation of the value of pi: Let’s generate a large number of random points, 
# such as one million, inside square B. Let N be the total number of random points. 
# Each point inside the square is tested for whether it resides inside circle A. 
# Let n be the total number of points that fall inside circle A. 
# Now we have n/N≈π/4, and from that we get π≈4n/N. 
# Write a program that asks the user how many random points to generate, 
# and then calculates the approximate value of pi using the method explained above. 
# At the end, the program prints out the approximation of pi to the user. 
# (Notice that it is easy to test if a point falls inside circle A by testing if it fulfills 
# the inequation x^2+y^2<1.).

points = int(input("How many points need to be created? "))

counter = 0
inside_the_circle = 0

while counter < points:
    x = random.uniform(-1, 1)
    y = random.uniform(-1, 1)
    if x**2 + y**2 < 1:
        inside_the_circle += 1
    counter += 1

Pi = 4 * inside_the_circle / points

print(Pi)