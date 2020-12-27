print("Welcome to my first game!")
name = input("What is your name? ")
age = int(input("What is your age? "))
health = 10

print("Hello", name, "you are", age, "years old.")

if age >= 11:
    print("You are old enough to play!")
else:
    print("You are not old enough to play...")

wants_to_play = input("Do you want to play? (yes/no) ")
if wants_to_play == "yes":
    print("You are starting with", health, "health.")
    print("Let's play!")
if wants_to_play == "no":
    print("Okay, you can close the game!")


left_or_right = input("First choice... Left or Right? (left/right) ")
if left_or_right == "left":
    ans = input("Nice, you follow the path and reach a lake...  Do you swim across or go around? (across/around) ")
if left_or_right == "right":
    print("You fell down and lost...") #because it gives an error and i don't want to see it :/
    print("You fell down and lost...") #because it gives an error and i don't want to see it :/
    print("You fell down and lost...") #because it gives an error and i don't want to see it :/
    print("You fell down and lost...") #because it gives an error and i don't want to see it :/
    print("You fell down and lost...") #because it gives an error and i don't want to see it :/
    print("You fell down and lost...") #because it gives an error and i don't want to see it :/
    print("You fell down and lost...") #because it gives an error and i don't want to see it :/
    print("You fell down and lost...") #because it gives an error and i don't want to see it :/
    print("You fell down and lost...") #because it gives an error and i don't want to see it :/



if ans == "around":
    ans = input("You made it around the lake and found a Cabin do you want to go in or continue your journey? (cabin/continue) ")
if ans == "across":
    print("You were killed by a shark...")
    print("You lose...")

if ans == "cabin":
    print("You decided to go inside the Cabin, in there you found a Scary Lady that killed you...")
    print("You lose...")

if ans == "continue":
    print("You find yourself in your cozy bed, your cat is laying next to you, you find out it was all a dream. A WILD Dream.")
    print("You win!")