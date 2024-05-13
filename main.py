def start_game():
  print("Welcome to The Possible Game!")
  print("You suddenly find yourself in a dark tropical maze with three paths ahead   of you.")
  print("Which path will you choose?")
  user_choice = input("Enter 1, 2, or 3:")
  
  if user_choice == '1':
    path_1()
  elif user_choice == '2':
    path_2()
  elif user_choice == '3':
    path_3()
  else:
    print("Invalid Input, Please try again.")
    start_game()

#First Path
def path_1():
  print("You chose path 1.")
  print("You encountered a wise hippo")
  print("What do you want to ask the hippo?")
  user_input = input("Enter your question:")

  if len(user_input) > 0:
    print("You asked:",user_input)
  else:
    print("Invalid input, Please try again.")
    path_1()
  
  print("The wise hippo responds with a fun little riddle.")
  print("What disappears as soon as you say its name?")
  user_answer = input("Enter your answer:")
  
  if user_answer.lower() == "silence":
    print("Correct answer! You may continue.")
    path_2()
  else:
    print("Incorrect answer. The tree dissapeared and you are now lost.")
    game_over()

#Second Path
 
def path_2():
  print("You have chosen path 2.")
  print("You come across a bridge. Under it is a river.")
  print("Do you swim across the river or take the bridge?(Enter 'swim' or 'bridge')")
  user_choice = input ("Enter your choice:")

  if user_choice.lower() == "swim":
    print("You attempt to swim across the river.")
    print("A strong current pulls you under the water and you slowly drown.")
    game_over()
  elif user_choice.lower() == "bridge":
    print("You choose to take the bridge")
    print("As you're crossing the bridge you notice a huge pile of gold")
    print("Do you dig in it? (Enter 'yes' or 'no')")
    user_choice = input("Enter your choice:")
  
    if user_choice.lower() == "yes":
      print("You go to the pile of gold and start digging, you then find valuable treasure.")
      print("Congratulations, you won!")
      quit_game()
    elif user_choice.lower() == "no":
      print("You decide not to dig into the pile of gold and continue your journey.")
      path_3()
    else:
      print("Invalid input. Please try again.")
      path_2()

#Third Path

def path_3():
  print("You chose path 3.")
  print("You came across a cave.")
  print("Do you want to enter the cave? (Enter 'yes' or 'no')")
  user_choice = input("Enter your choice.")
  if user_choice.lower() == "no":
    print("There's no turning back now")
    path_3()
  elif user_choice.lower() == "yes":
    print("You enter the cave and find a sea serpent!")
    print("Do you fight the sea serpent or run away? (Enter 'fight' or 'run')")
    user_choice = input("Enter your choice.")
    if user_choice.lower() == "fight":
      print("You bravely fight the sea serpent but are no match for its jet of boiling water.")
    elif user_choice.lower() == "run":
      print("You quickly run out of the cave, closely escaping the dragon. Looks like you didn't win!")
      quit_game()
  else:
    print("Invalid Input. Please try again")
    path_3()
  
def game_over():
  print("Game over. Would you like to play again? (Enter 'yes' or 'no')")
  user_choice = input("Enter your choice.")                    
  if user_choice.lower() == "yes":
    start_game()
  elif user_choice.lower() == "no":
    quit_game()
  else:
    print("Invalid Input. Please try again")
    game_over()

# Quit Game
def quit_game():
  print("Thanks for playing!")

start_game()

if False:
  pass
if 0:
  pass
if None:
  pass
if "":
  pass

user_input1 = int(input("Enter a number:"))
user_input2 = int(input("Enter another number:"))





  
  

