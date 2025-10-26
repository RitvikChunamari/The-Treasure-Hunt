# Import Libraries 

# We need 'time' to make the game pause for a second
import time

# Variable Definitions

# We can keep track of items in a list
inventory = []
game_over = False # Use a boolean to know if the game is over

# Main Game Tasks 

# Start the game and get the player's name
print("--- Welcome to the Treasure Hunt! ---")
name = input("What is your name, adventurer? \n> ")

print(f"\nWelcome, {name}! You are on a beach with a jungle in front of you.")
time.sleep(1) # wait for one second

# Decision Layer 1 
print("To your left, you see an opening to the 'jungle'.")
print("To your right, you see a dark 'cave'.")
print("Where do you want to go?")
choice1 = input("> ").lower() # make the input lowercase

# Check the first choice
if choice1 == "jungle":
    print("\nYou walk into the jungle. It's hot and loud.")
    time.sleep(1)
    
    # Decision Layer 2 (Jungle Path)
    print("You find an old temple covered in vines.")
    print("Do you want to 'climb' the temple or 'look' around the base?")
    choice2 = input("> ").lower()

    if choice2 == "climb":
        # End Point (Win)
        print("\nYou climb to the top and find an old treasure map!")
        print("🎉 You Win! 🎉")
        
    elif choice2 == "look":
        # End Point (Lose)
        print("\nYou step on a loose stone... it's a trap! You fall into a pit.")
        print("GAME OVER ☠️")
        game_over = True # set the game over flag
        
    else:
        print("That's not an option! A monkey stole your bag while you waited.")
        game_over = True

elif choice1 == "cave":
    print("\nYou walk into the dark cave. You hear a loud snoring sound.")
    time.sleep(1)
    
    # Decision Layer 2 (Cave Path)
    print("You see a giant bear sleeping in the corner!")
    print("Do you try to 'sneak' past it or 'run' away?")
    choice3 = input("> ").lower()

    if choice3 == "sneak":
        print("\nYou hold your breath and tiptoe past the bear...")
        time.sleep(1)
        
        # Decision Layer 3 (Cave Path)
        print("You are in a back room! You see a 'gold' chest and a 'wood' chest.")
        print("Which one do you open?")
        choice4 = input("> ").lower()

        if choice4 == "gold":
            # Add item to our list
            inventory.append("Gold Coins") 
            # End Point (Win)
            print("\You open the chest and it's full of gold coins!")
            print("🎉 You Win! 🎉")
            
        elif choice4 == "wood":
            # End Point (Lose)
            print("\nYou open the wooden chest. It's full of old, moldy clothes.")
            print("GAME OVER ☠️")
            game_over = True
            
        else:
            print("That's not an option! The bear is starting to wake up.")
            game_over = True
            
    elif choice3 == "run":
        # End Point (Lose)
        print("\nYou turn to run, but you trip. The bear wakes up!")
        print("GAME OVER ☠️")
        game_over = True
        
    else:
        print("That's not an option! The bear woke up from the noise.")
        game_over = True

else:
    # This catches any bad input from the first question
    print("You have to choose! While you waited, a high tide came in and swept you away.")
    game_over = True


# Final Report

# This 'if' statement checks the boolean we set earlier
if game_over == True:
    print("\n...Better luck next time, {name}.")
else:
    # This 'for' loop will print all the items in our list
    print(f"\nGood job, {name}! Here is what you found:")
    for item in inventory:
        print(f"- {item}")

print("Thanks for playing!")