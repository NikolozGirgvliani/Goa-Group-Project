# Text-Based Adventure Game

def intro():
    print("Welcome to the Adventure Game!")
    print("you wake up in a forest")
    print("Your goal is to find a place to stay")
    print("")

def first_choice():
    print("You see two paths before you: Left and Right.")
    choice = input("Which way do you go? (left/right): ").strip().lower()
    if choice == "left":
        haunted_house()
    elif choice == "right":
        treasure_room()
    else:
        print("Invalid choice. Please type 'left' or 'right'.")
        first_choice()

def haunted_house():
    print("\nYou saw a haunted house")
    print("Something is chasing you. Think Fast!")
    print("Will you enter the house or Run?")
    choice = input("Choose an action (Run/Enter): ").strip().lower()
    if choice == "run":
        print("\nYou got lucky and ran away Congrats!")
    elif choice == "Enter":
        print("\nYou enter Haunted house and ghosts killed you! you lose!")
    else:
        print("Invalid choice. Please type 'run' or 'enter'.")
        haunted_house()

def treasure_room():
    print("\nYou enter a room filled with gold and jewels!")
    print("Congratulations, you found the treasure!")
    print("Do you take some treasure or leave it behind?")
    choice = input("Choose an action (take/leave): ").strip().lower()
    if choice == "take":
        print("\nYou take some treasure and leave the cave. You're rich!")
    elif choice == "leave":
        print("\nYou decide to leave the treasure behind and exit the cave peacefully. A wise choice!")
    else:
        print("Invalid choice. Please type 'take' or 'leave'.")
        treasure_room()

# Game Start
def start_game():
    intro()
    first_choice()

if __name__ == "__main__":
    start_game()
