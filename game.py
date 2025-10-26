import random
import time

hp = 0
stealth = 0
bosshp = 200
bossdmg = 50
name = ""
attack = 0
turns = 0

print("Hello Adventurer, its time for you to enroll on an adventure to defeat a dragon!")
time.sleep(0.5)
print("but first, choose your class(1-3): ")
print("1) berserker 2) mage 3) ninja")
c = int(input("class: "))
if c == 1:
    name = "berserker"
    hp = 150
    attack = random.randint(30, 50)
    stealth = 0
elif c == 2:
    name = "mage"
    hp = 75
    attack = random.randint(70, 90)
    stealth = 0
elif c ==3:
    name = "ninja"
    hp = 100
    stealth = 1
    attack = 60
else:
    print("print your class to properly continue!")

print(f"Nice, you picked {name}! Let’s start the adventure.")
time.sleep(1)
print("you arrive at the cave what you do:")
print("1) you enter cave(berserker, mage, ninja)")
print("2) you lure the dragon from the cave(berserker, mage, ninja)")
if name == "ninja":
    print("3) you deploy smoke bomb and attack dragon from behind!(ninja)")
if name == "mage":
    print("3) you duplicate yourself to misguide the dragon!(mage)")
if name == "berserker":
    print("3) you rage and roar at the dragon!(berserker) ")
a= int(input("choice: "))

if a == 1:
    print("you face the dragon!(no changes in stats)")
if a ==2:
    print("dragon wakes up and goes out of the cave (-20% damage taken because he is tired)")
    bossdmg = bossdmg * 0.8
if a ==3 and name == "ninja":
    print("The dragon senses you and puts you straight to the ground(-40%hp)")
    hp = hp*0.6
elif a == 3 and name == "berserker":
    print("SUPER EFFECTIVE! You actually applied critical damage to dragon, who because of roar got scared and you were able to deal 2x damage(2xattack)")
    bosshp = bosshp - 2 * int(attack)
elif a ==3 and name == "mage":
    print("not very effective, dragon - using his tail killed your clone, and knocked you back out, luckily you were able to damage him a little...")
    bosshp = bosshp - 0.5 * int(attack)
else:
    print("choose correct option!")

time.sleep(1)
print("what is your next move?")
print("1) attack")
print("2) defend")
if name == "mage":
    print("3) gain health")
if name == "ninja":
    print("3) stealth attack")
if name == "berserker":
    print("3) reckless rage")

while hp > 0 and bosshp > 0:
    turns = turns + 1
    if turns >=6:
        print("you broke your turn limit. you lost!")
    else:

        move = int(input(f"turn {turns}, choose your move: "))

        if move == 1:
            bosshp = bosshp - attack
            print(f"You attack the dragon and deal {attack} damage! Dragon HP: {bosshp}")
        elif move == 2:
            print("You brace yourself against the dragon attack, reducing its damage dealt.")
            bossdmg = bossdmg * 0.5
        elif move == 3 and name == "mage":
            heal = 60
            hp = hp + heal
            print(f"You cast a healing spell and restore {heal} HP, your Current HP: {hp}")
        elif move == 3 and name == "ninja":
            bosshp = bosshp - attack * 1.5
            print(f"You strike from the shadows, dealing {attack * 1.5} damage! Dragon HP: {bosshp}")
        elif move == 3 and name == "berserker":
            bosshp = bosshp - attack * 2
            hp = hp - 30
            print(f"In a reckless fury, you deal {attack * 2} damage but take 30 damage yourself! HP: {hp}")
        else:
            print("Invalid move.")
        


        if bosshp <= 0:
            print("CONGRATS, YOU WON!")
            break

        time.sleep(1)
        print("The dragon attacks you!")
        hp = hp - bossdmg
        print(f"The dragon deals {bossdmg} damage! Your HP: {hp}")
        bossdmg = 50

        if hp <= 0:
            print("Unfortunately the dragon killed you.")
            break

