import random


# # Part 1
# # Create a program in the folder that asks for the player’s name and age,
# # stores them in variables, and prints them to the console.
#
# # Part 2
# # Modify the game project program so that if the user enters an age under 12,
# # the program informs them that they are a minor and shuts down.
# # Otherwise, the program greets the user, displays the main menu, and asks for commands until the user enters "lopeta".
# # Add a few fictional commands that each produce a different output in the console.
# # After a command, always display the menu again.
#
# # Part 3
# # Main Menu Functions and “Inventory”
# # Continue developing the game project: Create a separate function for each main menu function (at least three),
# # which is executed when the user selects that function.
# # One function must ask the user for information (e.g. an item) that is added to a list variable.
# # Another function must print the contents of the list to the user.
# # The other functions can be designed and implemented freely.
#
# # Main Menu Functions and “Inventory”
# # Continue developing the game project: Create a separate function for each main menu function (at least three),
# # which is executed when the user selects that function.
# # One function must ask the user for information (e.g. an item) that is added to a list variable.
# # Another function must print the contents of the list to the user.
# # The other functions can be designed and implemented freely.
#
# # Part 4

class Game:
    def __init__(self, username, age):
        if age < 12:
            print("The game is rated 12+. Access denied.")
            exit()
        else:
            print("Welcome!")
            self.starting_item = Item("Wooden Sword", 730)
            self.starting_room = Room("Starting Room", self.starting_item)
            self.player = Player(username, self.starting_room)
            self.amount_of_rooms = random.randint(3, 10)
            self.items = self.generate_items(self.amount_of_rooms)
            self.rooms = self.generate_rooms_and_their_items(self.amount_of_rooms)


    def menu(self):
        print("------- MENU -------")
        print("1. Collect item \n2. Inventory \n3. Move \n4. Character class \n5. Current location \n6. Lopeta")
        print("------- --- -------")

        command = input("Enter command number: ")

        while command != "6":

            if command == "1":
                self.player_collect_item()
            elif command == "2":
                self.show_player_inventory()
            elif command == "3":
                self.player_move()
                break
            elif command == "4":
                print(f"~~~ Your character class is {self.player.name}! ~~~")
            elif command == "5":
                self.player_current_location()
            else:
                print("Command not found.")

            print("------- MENU -------")
            print("1. Collect item \n2. Inventory \n3. Move \n4. Character class \n5. Current location \n6. Lopeta")
            print("------- --- -------")

            command = input("Enter command number: ")


    def generate_rooms_and_their_items(self, amount_of_rooms):
        rooms = []
        for room in range(amount_of_rooms):
            item = self.items[room - 1]
            generated_room = Room(f"Room {room}", item)
            rooms.append(generated_room)

        return rooms

    def generate_items(self, amount_of_rooms):
        items = []
        quality_of_item = {"Wooden", "Magic", "Gold", "Silver", "Platinum", "Radioactive", "Fruity"}
        varaity_of_item = {"Sword", "Axe", "Gun", "Branch", "Ball", "Stick", "Rat", "Skull"}
        for _item in range(amount_of_rooms):
            item_name = random.choice(list(quality_of_item)) + " " + random.choice(list(varaity_of_item))
            item = Item(item_name, random.randint(500, 1500))
            items.append(item)
        return items

    def show_player_inventory(self):
        self.player.show_inventory()

    def player_collect_item(self):
        self.player.collect_item()

    def player_move(self):
        print("Where you would like to move?")
        for i, room in enumerate(self.rooms):
            if room.visited != True:
                print(f"{i}. The room with {room.item.name}")

        room_number = input("\nEnter room number:")
        self.player.move(self.rooms[int(room_number)])

        self.menu()

    def player_current_location(self):
        self.player.current_location()

class Item:
    def __init__(self, name, weight):
        self.name = name
        self.weight = weight
        self.owned = False


class Room:
    def __init__(self, name, item):
        self.name = name
        self.item = item
        self.visited = False


class Player:
    def __init__(self, name, location):
        self.name = name
        self.items = []
        self.location = location

    def move(self, destination):
        self.location = destination
        self.location.visited = True
        print(f"\n\n~~~ You now in room with {self.location.item.name}! ~~~\n\n")

    def collect_item(self):
        item = self.location.item
        if item.owned != True:
            self.items.append(item)
            item.owned = True
            print(f"\n\n~~~ You collected {item.name}! ~~~\n\n")
        else:
            print("\n\n~~~You already collect item from this room ~~~\n\n")

    def show_inventory(self):
        print("\nInventory: ")
        for item in self.items:
            print(f"- {item.name}.")
        print("\n")

    def current_location(self):
        print(f"\nYour current location is Room with {self.location.item.name}.\n")



name = input("Enter your name: ")
age = int(input("Enter your age: "))

game = Game(name, age)
game.menu()