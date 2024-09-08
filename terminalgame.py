### Terminal Game ###

import random
import time


print()
print()


def combat(fight):
    # We define the HP of the beasts according to the chosen character
    if fight == 'Magician':
        beast_hp = 1700
        print("You are facing an evil wizard beast!")
    elif fight == 'Warrior':
        beast_hp = 1650
        print("You are facing a fearsome warrior beast!")
    elif fight == 'Archer':
        beast_hp = 1950
        print("You are facing a skilled archer beast!")
    else:
        print("Invalid selection...")
        return
    
    player_hp = 1000  # Player HP
    
    while player_hp > 0 and beast_hp > 0:
        print(f'\nYour HP: {player_hp} | Beast HP: {beast_hp}')
        action = input("What will you do? (attack/defend/retreat): ").lower()
        
        if action == "attack":
            player_damage = random.randint(150, 500)
            beast_hp -= player_damage
            print(f'You dealt {player_damage} damage to the beast!')
            # We checked if it was a critical hit
            if player_damage > 380:
                print("¡Critical Hit!")
                
        elif action == "defend":
            print("You defend yourself, reducing damage from the next attack.")
            defense = True
        elif action == "retreat":
            retreat_chance = random.random()
            if retreat_chance > 0.5: # It will make escaping the fight harder or easier depending on the number you change to
                print("You successfully escaped!")
                return
            else:
                print("Retreat failed! The beast continues to attack.")
        else:
            print("Invalid action. The beast attacks!")
            defense = False
        
        # Beast Attack
        if beast_hp > 0:
            beast_damage = random.randint(1, 250)
            if 'defense' in locals() and defense:  # Reduces damage if the player defended
                beast_damage = beast_damage // 2
                defense = False
            player_hp -= beast_damage
            print(f'The beast returns {beast_damage} damage to you!')
        
        # Defeat Checker
        if beast_hp <= 0:
            print("¡¡¡YOU WIN!!!, you have Defeated the Beast!")
            print('Game Over')
            break
        if player_hp <= 0:
            print("You have been DEFEATED by the beast... Try Again!")
            print('Thanks for playing')
            print()
            print()
            break

def do_play():
    x = input("Will you play? yes or no (y/n):\n").lower()
    num = 3

    if x == "n":
        print("GAME OVER")
        exit()

    elif x == "y":
        print("STARTS IN:")
        while num >= 0:
            print(num)
            num -= 1
            time.sleep(1)
    else:
        print("Invalid selection")

def rol():
    characters = ['Magician', 'Warrior', 'Archer']
    
    ycha = input(f'Select your PJ {characters}: ').capitalize()
    
    if ycha == 'Magician':
        print('Excellent choice! Now you have a Magic Staff.')
        print(f'Now I\'m a powerful {ycha} with my new Magic Staff!')
    elif ycha == 'Warrior':
        print('Excellent choice! Now you wield a Saw Blade.')
        print(f'Now I\'m a great {ycha} with my new Saw Blade!')
    elif ycha == 'Archer':
        print('Excellent choice! You have infinite arrows at your disposal.')
        print(f'Now I\'m a super {ycha} with the magnificent Bow and Arrows.')
    else:
        print('Incorrect selection...')
        return None
    
    print(f'Your hero is ready for battle! {ycha}')
    return ycha


def welcome():
    print('Welcome to the battle game \nSelect your character and fight against the beast... \nWho will win ? \nShow your bravery')

# We call the functions
welcome()
do_play()
selected_character = rol() 
if selected_character:
    combat(selected_character)
