names = ["Adam","Alex","Mariah","Martine","Columbus"]

for name in names: 
  print name

  webster = {
  "Aardvark" : "A star of a popular children's cartoon show.",
  "Baa" : "The sound a goat makes.",
  "Carpet": "Goes on the floor.",
  "Dab": "A small amount."
}

# Add your code below!
for key in webster: 
  print webster[key]

#indentation for conditions in for loops
a = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10, 11, 12, 13]

for item in a: 
  if item % 2 == 0:
  	print item 

# Write your function below!
def fizz_count(x):
  count = 0
  for item in x: 
    if item == "fizz":
      count +=1
  return count

  #looping through strings
  for letter in "Codecademy":
  print letter
    
# Empty lines to make the output pretty
print
print

word = "Programming is fun!"

for letter in word:
  # Only print out the letter i
  if letter == "i":
    print letter

prices = {
"banana": 4,
"apple": 2,
"orange": 1.5,
"pear": 3
}

stock = {
"banana": 6,
"apple": 0,
"orange": 32,
"pear": 15
}

for key in prices: 
  print key
  print "price: %s" % prices[key]
  print "stock: %s" % stock[key]

for key in prices:
  print key
  print "price: %s" % prices[key]
  print "stock: %s" % stock[key]
  
total = 0

for price in prices: 
  print prices[price]*stock[price]
  total += prices[price]*stock[price]
print total

def compute_bill(food):
  total = 0
  for item in food:
    total += prices[item]
    
  return total

  """
Python
Rock Paper Scissors Game
"""
from random import randint

options = ["ROCK", "PAPER", "SCISSORS"]

message = {
  "tie": "Yawn it's a tie",
  "won": "Yay you won!", 
  "lost": "Aww you lost!"
}

def decide_winner(user_choice, computer_choice):
  print "You selected %" % user_choice
  print "Computer selected: %" % computer_choice
  if user_choice == computer_choice:
    print message["tie"]
  elif user_choice == options[0] and  computer_choice == options[2]:
    print message["won"]
  elif user_choice == options[1] and computer_choice == options[0]:
    print message["won"]
  elif user_choice == options[2] and computer_choice == options[1]:
    print message["won"]
  else:
    print message["lost"]
    
def play_RPS():
  user_choice = raw_input("Enter Rock, Paper, or Scissors: ")
  user_choice = user_choice.upper()
  computer_choice = options[randint(0, 2)]
  decide_winner(user_choice, computer_choice)
  
  
play_RPS()

#challenge

lloyd = {
  "name": "Lloyd",
  "homework": [90.0, 97.0, 75.0, 92.0],
  "quizzes": [88.0, 40.0, 94.0],
  "tests": [75.0, 90.0]
}
alice = {
  "name": "Alice",
  "homework": [100.0, 92.0, 98.0, 100.0],
  "quizzes": [82.0, 83.0, 91.0],
  "tests": [89.0, 97.0]
}
tyler = {
  "name": "Tyler",
  "homework": [0.0, 87.0, 75.0, 22.0],
  "quizzes": [0.0, 75.0, 78.0],
  "tests": [100.0, 100.0]
}

for student in students: 
  print student["name"]
  print student["homework"]
  print student["quizzes"]
  print student["tests"]

# Add your function below!
def average(numbers):
  total = sum(numbers)
  total = float(total)
  return total/len(numbers)

def get_average(student):
  homework = (average(student["homework"]))*0.1
  quizzes = (average(student["quizzes"]))*0.3
  tests = (average(student["tests"]))*0.6
  
  return homework + quizzes + tests

#Letter Grade
def get_letter_grade(score):
  if score >= 90:
    return "A"
  elif score >=80: 
    return "B"
  elif score >= 70:
    return "C"
  elif score >= 60:
    return "D"
  else:
    return "F"
  
print get_letter_grade(get_average(lloyd))

#get class average
def get_class_average(class_list):
  results = []
  for student in class_list:
    results.append(get_average(student))
    
  return average(results)

#Battleship game

from random import randint

board = []

for x in range(0, 5):
  board.append(["O"] * 5)

def print_board(board):
  for row in board:
    print " ".join(row)

def random_row(board):
  return randint(0, len(board) - 1)

def random_col(board):
  return randint(0, len(board[0]) - 1)

ship_row = random_row(board)
ship_col = random_col(board)

#debugging 
print ship_row
print ship_col

# don't forget to properly indent!
for turn in range(4):
  print "Turn", turn + 1
  guess_row = int(raw_input("Guess Row: "))
  guess_col = int(raw_input("Guess Col: "))

  if guess_row == ship_row and guess_col == ship_col:
    print "Congratulations! You sank my battleship!"   
    break
  else:
    if guess_row not in range(5) or \
      guess_col not in range(5):
      print "Oops, that's not even in the ocean."
    elif board[guess_row][guess_col] == "X":
      print( "You guessed that one already." )
    else:
      print "You missed my battleship!"
      board[guess_row][guess_col] = "X"
    print_board(board)
  if turn == 3:
    print "Game Over"
#While loop
num = 1

while num < 11:  # Fill in the condition
 print (num ** 2)
 num += 1   

choice = raw_input('Enjoying the course? (y/n)')

while choice != 'y' and choice != 'n':  # Fill in the condition (before the colon)
  choice = raw_input("Sorry, I didn't catch that. Enter again: ")
# simple errors corrected
count = 0

while count < 10: # Add a colon
  print count
  count += 1
  # Increment count
#break implemented
count = 0

while True:
  print count
  count += 1
  if count >= 10:
    break
#while/else
import random

print "Lucky Numbers! 3 numbers will be generated."
print "If one of them is a '5', you lose!"

count = 0
while count < 3:
  num = random.randint(1, 6)
  print num
  if num == 5:
    print "Sorry, you lose!"
    break
  count += 1
else:
  print "You win!"

#second example
from random import randint

# Generates a number from 1 through 10 inclusive
random_number = randint(1, 10)

guesses_left = 3
# Start your game!
guess = int(raw_input("Your guess: "))
while guesses_left > 0:
  if guess == random_number:
    print "You win!"
    break
  guesses_left -= 1
else:
  print "You lose."
#Pressure formula

def solution(molar_mass1, molar_mass2, given_mass1, given_mass2, volume, temp) :
    # your code goes here
    #PV = nRT
    pressure_1 = ((given_mass1/molar_mass1)*0.082*(temp+273.15))/volume
    pressure_2 = ((given_mass2/molar_mass2)*0.082*(temp+273.15))/volume

    pressure = pressure_1 + pressure_2

    return pressure

#bit counter function

def range_bit_count(a, b):
    #coding and coding..
    list = []
    for i in range(a,b+1):
        i = format(i, "b")
        list.append(i)
    count = "".join(list)
    total = count.count("1")
    print (total)

range_bit_count(28, 36)
# print (format(5, "b"))

#returns whole number
def is_int(x):
  absolute = abs(x)
  rounded = round(absolute)
  return absolute - rounded == 0

#factorial function
def factorial(x):
  c = x-1
  while c > 0:
    x = c * x
    c -=1
  return x

#reverse text without using reverse or [::-1]
def reverse(text):
    word = ""
    l = len(text) - 1
    while l >= 0:
        word = word + text[l]
        l -= 1
    return word

#scrabble
def scrabble_score(word):
  word = word.lower()
  total = 0
  for letter in word:
    for leter in score:
      if letter == leter:
        total = total + score[leter]
  return total

#censor function
def censor(text, word):
    words = text.split()
    result = ''
    stars = '*' * len(word)
    count = 0
    for i in words:
        if i == word:
            words[count] = stars
        count += 1
    result =' '.join(words)

    return result
#count function
def count(sequence, item):
    count = 0
    for i in sequence:
        if i == item:
            count += 1
    return count    

#purify function
def purify(stuff):
  new_list = []
  for i in stuff:
    if i  % 2 == 0:
      new_list.append(i)
  return new_list
  
#product

def product(stuff):
  product = 1
  for i in stuff:
    product *= i
  return product