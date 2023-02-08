import random
import tkinter as tk
from tk import *
from PIL import ImageTk, Image



screen = tk.Tk()
screen.geometry("%dx%d" % (screen.winfo_screenwidth(), screen.winfo_screenheight()))
screen.title("RADALOS")






#Below are file paths to images to add flare and formatting or whatever
portrait = Image.open('images/rathalos/portrait/r.jpg')
monPort = ImageTk.PhotoImage(portrait)
monPortLB = tk.Label()

fire = Image.open('images/rathalos/attacks/firerad.png')
monFire = ImageTk.PhotoImage(fire)

claw = Image.open('images/rathalos/attacks/clawrad.png')
monClaw = ImageTk.PhotoImage(claw)

tail = Image.open('images/rathalos/attacks/tailrad.png')
monTail = ImageTk.PhotoImage(tail)

tscreen = Image.open('images/screens/titlescreen.png')
title = ImageTk.PhotoImage(tscreen)

game_over = Image.open('images/screens/questf.png')
gover = ImageTk.PhotoImage(game_over)

quest_complete = Image.open('images/screens/questq.png')
qcomp = ImageTk.PhotoImage(quest_complete)

#Honestly have no Idea what this is here for but I used it to make something work so its cool
atk = ["Claw Slash", "Fireball", "Tail Smash"]

#clear screen function, just for formatting to make everything look nice
def clean():
    print("\033[H\033[J", end="")



#turn counter
turn = 0

#function for game over screen
def gameOver():
    print(game_over)

#Class to make objects with desired properties
class Entity:
    def __init__(self, h_val, s_val):
        self.health = h_val
        self.stamina = s_val


Hunter = Entity(150, 150)
Rathalos = Entity(300, 250)

#Player Turn Function, contains logic for the player's actions.
def playerTurn():
    global Hunter
    global Rathalos

    input_val = input(
        ("Attack with numbers 1 or 2 on your keyboard and press enter!\n" +
         "Overhead Slash [1] Strong Slash [2]\n"))
    if (input_val == "1"):
        print("The Rathalos currently has {} health.".format(Rathalos.health if Rathalos.health > 0 else 0))
        damage = random.randint(65, 70)
        Rathalos.health = Rathalos.health - damage
        print("You did {} damage.".format(damage))
        print("The monster now has {} health.".format(Rathalos.health if Rathalos.health > 0 else 0))
    elif (input_val == "2"):
        print("The Rathalos currently has {} health.".format(Rathalos.health if Rathalos.health > 0 else 0))
        damage = random.randint(85, 100)
        Rathalos.health = Rathalos.health - damage
        print("You did {} damage.".format(damage))
        print("The monster now has {} health.".format(Rathalos.health if Rathalos.health > 0 else 0))
    else:
        print("Invalid Attack Input.")

#Monster Turn Function, contains logic for the monster's (the computer) actions like attacks n' stuff.
def MonsterTurn():
    global Hunter
    global Rathalos

    atkChoice = random.choice(atk)
    print("You currently have {} health.".format(Hunter.health if Hunter.health > 0 else 0))
    print("")
    if atkChoice == atk[0]:
        attackDMG = random.randint(10, 25)
        Hunter.health -= attackDMG
        print(claw)
        print("The Rathalos uses it's Claws to attack you!\nThe Rathalos does {} damage.".format(attackDMG))

    if atkChoice == atk[1]:
        attackDMG2 = random.randint(15, 30)
        Hunter.health -= attackDMG2
        print(fire)
        print("The Rathalos Shoots a fireball at you!\nThe Rathalos does {} damage.".format(attackDMG2))
    if atkChoice == atk[2]:
        attackDMG3 = random.randint(10, 13)
        Hunter.health -= attackDMG3
        print(tail)
        print("The Rathalos slams it's tail on you!\nThe Rathalos does {} damage.".format(attackDMG3))
    print("")
    print("You now have {} health.".format(Hunter.health if Hunter.health > 0 else 0))

#Prints title screen and other game things you'd see on boot up
print(tscreen)

print("")
print("Press enter to continue")
print("")

input()

clean()

print(portrait)
print("Oh no, a wild Rathalos appeared!\n")
print("Save us, hunter!\n")

print("")
print("Press enter to continue")
print("")

input()
clean()


#This is where the game starts/Begins to function. Logic for the game is here. It's the first player will always go first and it's random who goes next afer. 
while (True):
  if Hunter.health <= 0:
    print("Quest Failed...")
    gameOver()
    print("You've fainted. \n THANK YOU FOR PLAYING!")
    break

  if Rathalos.health <= 0:
    print("Quest Complete!")
    print(quest_complete)
    print("You've completed the quest and defeatd Rathalos. \n THANK YOU FOR PLAYING!")
    break
    
  turn += 1

  
  if turn == 1:
    playerTurn()
    MonsterTurn()
    print("")
    print("Press enter to continue")
    print("")
    input()
    clean()
  elif turn > 1:
    makeChoice = random.randint(1, 2)
    if makeChoice == 1:
      playerTurn()
      MonsterTurn()
      print("")
      print("Press enter to continue")
      print("")
      input()
      clean()
    else:
      MonsterTurn()
      playerTurn()
      print("")
      print("Press enter to continue")
      print("")
      input()
      clean()

  
