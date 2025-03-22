import random

def generate_stats():
    return {
        "Strength": random.randint(1, 100),
        "Dexterity": random.randint(1, 100),
        "Intelligence": random.randint(1, 100),
        "HP": random.randint(1, 50) + 50
    }

def skill_check():
    return random.randint(1, 100)

def rock_paper_scissors():
    choices = {"rock": 1, "paper": 2, "scissors": 3}
    pInp = input("Rock, Paper, or Scissors? > ").lower()
    if pInp not in choices:
        print("Invalid choice! Try again.")
        return rock_paper_scissors()
    
    random_result = random.randint(1, 3)
    enemy_choice = list(choices.keys())[random_result - 1]
    print(f"Enemy chose {enemy_choice.capitalize()}")
    
    outcome = (choices[pInp] - random_result) % 3
    if outcome == 0:
        print("It's a draw!")
    elif outcome == 1:
        print("Enemy wins!")
    else:
        print("You win!")

def enter_dungeon():
    print("You enter the dungeon...")
    while True:
        room = random.choice([room1, room2])
        room()
        if not continue_game():
            break

def continue_game():
    choice = input("Do you continue? (Yes/No) > ").lower()
    return choice == "yes"

def room1():
    print("The room is dank and smells bad.")
    actions()

def room2():
    print("This room is darker and eerily quiet.")
    actions()

def actions():
    options = {
        "trap": check_trap,
        "item": check_item,
        "look": look_around
    }
    actionChoice = input("What do you do? (trap/item/look) > ").lower()
    if actionChoice in options:
        options[actionChoice]()
    else:
        print("Invalid choice.")
        actions()

def check_trap():
    if skill_check() >= player["Intelligence"]:
        print("You successfully detect a trap!")
    else:
        print("You find nothing... but that doesn't mean it's safe.")

def check_item():
    print("You check your inventory: Bedrolls, Food, Water")

def look_around():
    print("You take a careful look around the room...")
    print("It seems safe... or does it?")

def main():
    global player
    print("Welcome to Way of the Rock, a Rock Paper Scissors RPG!")
    player_name = input("Enter your character's name: > ")
    player = generate_stats()
    
    print(f"Welcome, {player_name}! Here are your stats:")
    for stat, value in player.items():
        print(f"{stat}: {value}")
    
    enter_dungeon()
    print("Game Over.")

if __name__ == "__main__":
    main()  
