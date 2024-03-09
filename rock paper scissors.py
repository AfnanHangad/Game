import random
while True:
     choices = ['rock', 'paper', 'scissors']
     computer = random.choice(choices)
     player = None
     while player not in choices:
          player = input("'rock', 'paper', 'scissors':").lower()
     if player == computer:
          print("computer chose", computer)
          print("player chose", player)
          print("Tie!")
     elif player == 'rock':
          if computer == 'paper':
               print("computer chose", computer)
               print("player chose", player)
               print("You loose!")
          if computer == 'scissors':
               print("computer chose", computer)
               print("player chose", player)
               print("You won!")
     elif player == 'scissors':
          if computer == 'paper':
               print("computer chose", computer)
               print("player chose", player)
               print("You win!")
          if computer == 'rock':
               print("computer chose", computer)
               print("player chose", player)
               print("You loose!")
     elif player == 'paper':
          if computer == 'scissors':
               print("computer chose", computer)
               print("player chose", player)
               print("You loose!")
          if computer == 'rock':
               print("computer chose", computer)
               print("player chose", player)
               print("You won!")

     play_again = input("Do you want to play again? (yes/no): ").lower()
     if play_again != "yes":
          break
print("bye")
