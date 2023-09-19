#SOLUTION WITHOUT FUNCTIONS:

print("Welcome to the Number Guessing Game! \nI'm Thinking of a number between 1 and 100. ")
 
 
 
from random import randint
secret_number = randint(1,100)
 
 
 
difficulty = input("Choose a difficutly. Type 'easy' or 'hard': ")
if difficulty == "easy":
  chances = 10
  print(f"You have {chances} attempts remaining to guess the number.")
else:
  chances = 5
  print(f"You have {chances} attempts remaining to guess the number.")
 
 
should_continue=True
while chances >= 1 and should_continue==True:
  guess = int(input("Make a guess: "))
   
  if guess > secret_number:
    print("Too High.\nGuess again.")
    chances -= 1
    print(f"You have {chances} attempts remaining to guess the number")
  
  elif guess < secret_number:
    print("Too Low. \nGuess again")
    chances -= 1
    print(f"You have {chances} attempts remaining to guess the number")
 
  elif guess == secret_number:
    print(f"You got it! The answer was {secret_number}")
    should_continue=False
 
 
if chances == 0:
  print("You have run out of guesses, you lose.")
  


#SOLUTION WITH FUNCTIONS

from random import randint
from art import logo

EASY_LEVEL_TURNS = 10
HARD_LEVEL_TURNS = 5

#Function to check user's guess against actual answer.
def check_answer(guess, answer, turns):
  """checks answer against guess. Returns the number of turns remaining."""
  if guess > answer:
    print("Too high.")
    return turns - 1
  elif guess < answer:
    print("Too low.")
    return turns - 1
  else:
    print(f"You got it! The answer was {answer}.")

#Make function to set difficulty.
def set_difficulty():
  level = input("Choose a difficulty. Type 'easy' or 'hard': ")
  if level == "easy":
    return EASY_LEVEL_TURNS
  else:
    return HARD_LEVEL_TURNS

def game():
  print(logo)
  #Choosing a random number between 1 and 100.
  print("Welcome to the Number Guessing Game!")
  print("I'm thinking of a number between 1 and 100.")
  answer = randint(1, 100)
  print(f"Pssst, the correct answer is {answer}") 

  turns = set_difficulty()
  #Repeat the guessing functionality if they get it wrong.
  guess = 0
  while guess != answer:
    print(f"You have {turns} attempts remaining to guess the number.")

    #Let the user guess a number.
    guess = int(input("Make a guess: "))

    #Track the number of turns and reduce by 1 if they get it wrong.
    turns = check_answer(guess, answer, turns)
    if turns == 0:
      print("You've run out of guesses, you lose.")
      return
    elif guess != answer:
      print("Guess again.")


game() 
