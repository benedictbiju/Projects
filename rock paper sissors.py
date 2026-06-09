# ask user if he wants to play
# if yes then start the game it should be out 3
# generate a random action for computer and ask user whats his action
# add score to whoever scores 
# when someone scores 2 points game ends

import random

print("hi welcome to rock paper sissor game by benedict")
print("the game is played out of 3")

actions = ["rock", "paper", "sissor"]

computer_score = 0
user_score = 0
draw = 0


while True:
    
    # play 1
    
    computer_action1 = random.choice(actions)
    user_action1 = str(input("rock paper or sissor\n  >>"))
    user_action1 = user_action1.strip().lower()
    
    if computer_action1 == "rock" and user_action1 == "paper":
        user_score += 1
        print(f"computer selected {computer_action1}")
    elif computer_action1 == "paper" and user_action1 == "rock":
        computer_score += 1
        print(f"computer selected {computer_action1}")
    elif computer_action1 == "paper" and user_action1 == "sissor":
        user_score += 1
        print(f"computer selected {computer_action1}")
    elif computer_action1 == "sissor" and user_action1 == "paper":
        computer_score += 1
        print(f"computer selected { computer_action1}")
    elif computer_action1 == "rock" and user_action1 == "sissor":
        computer_score += 1
        print(f"computer selected {computer_action1}")
    elif computer_action1 == "sissor" and user_action1 == "rock":
        user_score += 1
        print(f"computer selected {computer_action1}")
    elif computer_action1 == user_action1:
        print("its a draw")
        draw += 1
    
    if computer_score == 1:
            print(f"computer scored {computer_score}")
    elif user_score == 1:
        print(f"you scored {user_score}")

    
    
    # play 2
    
    computer_action2 = random.choice(actions)
    user_action2 = str(input("rock paper or sissor\n  >>"))
    user_action2 = user_action2.strip().lower()
    
    if computer_action2 == "rock" and user_action2 == "paper":
        user_score += 1
        print(f"computer selected {computer_action2}")
    elif computer_action2 == "paper" and user_action2 == "rock":
        computer_score += 1
        print(f"computer selected {computer_action2}")
    elif computer_action2 == "paper" and user_action2 == "sissor":
        user_score += 1
        print(f"computer selected {computer_action2}")
    elif computer_action2 == "sissor" and user_action2== "paper":
        computer_score += 1
        print(f"computer selected {computer_action2}")
    elif computer_action2 == "rock" and user_action2 == "sissor":
        computer_score += 1
        print(f"computer selected {computer_action2}")
    elif computer_action2 == user_action2:
        print("its a draw")
        draw += 1
    else:
        user_score += 1
        print(f"computer selected {computer_action2}")
    
    if computer_score == 2:
        print(f"computer scored {computer_score}")
    else:
        print(f"you scored {user_score}")
    

    
    # play 3
    
    computer_action3 = random.choice(actions)
    user_action3 = str(input("rock paper or sissor\n  >>"))
    user_action3 = user_action3.strip().lower()
    
    if computer_action3 == "rock" and user_action3 == "paper":
        user_score += 1
        print(f"computer selected {computer_action3}")
    elif computer_action3 == "paper" and user_action3 == "rock":
        computer_score += 1
        print(f"computer selected {computer_action3}")
    elif computer_action3 == "paper" and user_action3 == "sissor":
        user_score += 1
        print(f"computer selected {computer_action3}")
    elif computer_action3 == "sissor" and user_action3 == "paper":
        computer_score += 1
        print(f"computer selected {computer_action3}")
    elif computer_action3 == "rock" and user_action3 == "sissor":
        computer_score += 1
        print(f"computer selected {computer_action3}")
    elif computer_action3 == user_action3:
        print("its a draw")
        draw += 1
    else:
        user_score += 1
        print(f"computer selected {computer_action3}")

    
    if computer_score > user_score:
        winner = "computer"
        print(f"computer scored {computer_score}")
    elif computer_score == user_score:
        print("it is a draw")
    else:
        winner = "you"
        print(f"you scored {user_score}")
    print(f"{winner} won")
    break




    
    
    



