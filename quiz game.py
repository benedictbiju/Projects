# ask the user which topic they want to play
# ask mcq about the selected topic
# and after the quiz give the user a final score.

topic_1 = "football"
topic_2 = "movies"
topic_3 = "games"

print("hi welcome to the quiz game \nwhich topic do you want to play? \n1.football 2.movies 3.games")
quiz_topic_input = str(input(">"))
quiz_topic = quiz_topic_input.lower()
quiz_topic = quiz_topic_input.strip()

if quiz_topic == topic_1:
    print(f"you have selected {topic_1} as your topic")
elif quiz_topic == topic_2:
    print(f"you have selected {topic_2} as your topic")
elif quiz_topic == topic_3:
    print(f"you have selected {topic_3} as your topic")
else:
    print("invalid topic")

count = 0


# topic 1
while quiz_topic == topic_1:
    # q1
    print("1. How many players are on the field for a single football team during a standard match?")
    print("A)10 \nB)11 \nC)12 \nD)15")
    ans_q1_topic_1_input = str(input("Answer: "))
    ans_q1_topic_1 = ans_q1_topic_1_input.strip()
    if ans_q1_topic_1 == "11":
        count += 1
        print("correct")

    # q2
    print("2. Which country has won the most FIFA World Cup titles in history?")
    print("A)germany \nB)italy \nC)argentina \nD)brazil")
    ans_q2_topic_1_input = str(input("Answer: "))
    ans_q2_topic_1 = ans_q2_topic_1_input.strip()
    if ans_q2_topic_1 == "brazil":
        count += 1
        print("correct")

    # q3
    print("3. What is the standard duration of a regular football match (excluding extra time)?")
    print("A)80minutes \nB)90minutes \nC)100minutes \nD)120minutes")
    ans_q3_topic_1_input = str(input("Answer: "))
    ans_q3_topic_1 = ans_q3_topic_1_input.strip()
    if ans_q3_topic_1 == "90minutes":
        count += 1
        print("correct")

    # score
    final_score_topic_1 = count
    print(f"your final score is {final_score_topic_1} out of 3")
    break
