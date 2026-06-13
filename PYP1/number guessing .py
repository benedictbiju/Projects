import random

print("are you ready to play a random guessing game?")
print("enter the amount of numbers from which you want to guess")
n1 = 0
n2 = int(input("> "))
print(f"you have selected {n2} numbers, you will have unlimited guesses")

random_num = random.randint(n1, n2)
guess_count = 0

while True:
    guess_count += 1
    guess = int(input(f"guess{guess_count}> "))
    if guess == random_num:
        print(f"congradulations you have guessed the randome in {guess_count} attempts")
    else:
        print("your guess was wrong")
        print("do you want to try again?")
    yesORno = str(input(">"))
    if yesORno.strip().lower() == "yes":
        print("good luck")
    else:
        break
