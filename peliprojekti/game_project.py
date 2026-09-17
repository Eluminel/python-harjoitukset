#Create a program in the folder that asks for the player’s name and age, 
# stores them in variables, and prints them to the console.

username = input("Enter your name: ")
age = int(input("Enter your age: "))

print("Name: " + username)
print("Age: " + str(age))

# Modify the game project program so that if the user enters an age under 12, 
# the program informs them that they are a minor and shuts down. 
# Otherwise, the program greets the user, displays the main menu, and asks for commands until the user enters "lopeta".
# Add a few fictional commands that each produce a different output in the console. 
# After a command, always display the menu again.

if age < 12:
    print("The game is rated 12+. Access denied.")
    exit()
else:
    print("Welcome!")

inventory = []

def start(): 
    print("Game is starting now!") 

def add_item(): 
    item = input("Enter an item: ") 
    inventory.append(item) 
    print("Item added to inventory.") 

def show_inventory(): 
    print("In your inventory:") 
    for item in inventory: 
        print(item)

print("1. start \n2. character_class \n3. stats \n4. inventory \n5.add_item \6. lopeta")

command = input("Enter any command: ")

while command != "lopeta": 
    if command == "start": 
        start() 
    elif command == "add_item": 
        add_item() 
    elif command == "inventory": 
        show_inventory() 
    elif command == "character_class":
            print("Your character class is ...")
    elif command == "stats":
            print(" health is... \n strength is... \n agility is... \n intelligence is ... \n damage is... \n mana is...")
    else: print("Command not found.")
        
    print("1. start \n2. character_class \n3. stats \n4. inventory \n5.add_item \6. lopeta")
    command = input("Enter any command: ")

# Main Menu Functions and “Inventory”
# Continue developing the game project: Create a separate function for each main menu function (at least three), 
# which is executed when the user selects that function.
# One function must ask the user for information (e.g. an item) that is added to a list variable.
# Another function must print the contents of the list to the user.
# The other functions can be designed and implemented freely.
