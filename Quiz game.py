def new_game():
    guesses = []
    correct_guesses = 0
    question_num = 1

    for key in questions:
        print("---------------")
        print(key)

        for i in options[question_num-1]:
            print(i)
        guess = input("Answer(A,B,C,D)")
        guess = guess.upper()
        guesses.append(guess)
        correct_guesses += check_answer(questions.get(key),guess)
        question_num += 1
    display_score(correct_guesses,guesses)

def check_answer(answer,guess):
    if answer == guess:
        print("Correct!")
        return 1
    else:
        print("Incorrect!")
        return 0

def display_score(correct_guesses,guesses):
    print("------------")
    print("results")
    print("------------")
    print("Answers: ", end=" ")
    for i in questions:
        print(questions.get(i))
    print
    print("Guesses: ", end=" ")
    for i in guesses:
        print(i, end=" ")
    print()
    score = (correct_guesses/len(questions)*100)
    print("Your score is: "+str(score)+"%")
def play_again():
    response = input("Would you like to play again? (yes or no):")
    if response == "yes":
        return True
    else:
        return False

questions = {
 "Who was oppenhiemer?: ":"B",
 "How many parts does transformers have?: ":"C",
 "Who directed the movie Gangs Of Wasseypur?: ":"A",
 "Which is Indias most elite commando force?: ":"D",
 "What was the stand of switzerland in WW2?: ":"C",
}

options = [["A.Musician", "B.Atomic Scientist", "C.Adventurer", "D.Sportsman"],
           ["A.Four", "B.Five", "C.Seven", "D.Three"],
           ["A.A.Kashyap", "B.K.Johar", "C.B.kapoor", "D.Achint"],
           ["A.NSG", "B.Para sf", "C.Garud", "D.Marcos"],
           ["A.Allied", "B.Axes", "C.Neutral", "D.Both"]]

new_game()
while play_again():
    new_game()

print("Thank you for playing!")
