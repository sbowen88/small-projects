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
from random import randit

options = ["ROCK", "PAPER", "SCISSORS"]

message = {
  "tie": "Yawn it's a tie",
  "won": "Yay you won!", 
  "lost": "Aww you lost!"
}