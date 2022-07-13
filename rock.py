# DONT TOUCH THE CODE IN THIS SECTION 👇
import random

rps = ['''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
''',
'''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
''',
'''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
''']
# END OF SECTION 👆

# WRITE YOUR CODE BELOW THIS LINE 👇
while True:
  possible_input = ['rock','paper','scissors']
  user_input= input(f"\nChoose one of the options (rock,paper,scissors):   ")
  computer_input= random.choice(possible_input)

  if user_input == 'quit':
    break
# print(computer_input)


  print((computer_input))
  
  print(f"\nYou inputed {user_input}, while computer chose   {computer_input}.\n")


####ASCII image
  if user_input == "rock":
    print(rps[0])
  elif user_input == 'paper':
    print(rps[1])
  elif user_input == 'scissors':
    print(rps[2])

  if computer_input == "rock":
    print(rps[0])
  elif computer_input == 'paper':
    print(rps[1])
  elif computer_input == 'scissors':
    print(rps[2])


####checking out the win and loose options
  if user_input == (computer_input):
      print(f"Both players selected {user_input}. It's a tie!")
  elif user_input == "rock":
    if (computer_input) == "scissors":
      print("Rock smashes scissors! You win!")
    else:
      print("You lose.")

  elif user_input == "scissors":
    if (computer_input) == "paper":
          print("Scissors cuts rock! You win!")
    else:
          print("You lose.")

  elif user_input == "paper":
    if (computer_input) == "rock":
          print("Paper covers rock! You win!")
    else:
          print("You lose.")

# continue = input("continue playing? y/n: ")
#   if continue.lower() != 'y':
#     break


 
