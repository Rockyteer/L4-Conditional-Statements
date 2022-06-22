'''
isHungry = input("Y/N: Are you hungry?")
isBored = input("Y/N: Are you bored?")
if(isHungry == "Y" or isHungry == "y"):
  print("go eat")
else:
  print("Don't eat")
if(isBored == "Y" or isHungry == "y"):
  print("Go exercise")
else:
  print("Do nothing")

userNumber = int(input("Give me a number: "))
if(userNumber >= 0):
  print("Your number is positive")
else:
  print("Your number is negative")
  #Ask the user for their age. IF the user is 17 or older, let them know they can watch all movies

#if they're younger than 17 but older than 13, let them know that they can watch G-rated and PG-13
#if they're younger than 13 they"re only allowed to watch just G-rated movies

userNumber=int(input("What is your age: "))
if(userNumber >= 17):
  print("You are old enough to watch all movies.")
elif(13 <= userNumber <= 17):
  print("You are old enough to watch G-rated and PG-13 movies but not R-rated")
else:
  print("You can only watch G-rated movies")
'''
#ask the user for an x and a y value
#Based on the x and y value, output which quadrant they're in.

X = int(input("Give me a x-value: "))
Y = int(input("Give me a y-value: "))

if(X > 0 and Y > 0):
  print("You are in Quadrant I")
elif(X < 0 and Y > 0):
  print("You are in quadrant II")
elif(X < 0 and Y < 0):
  print("You are in quadrant III")
elif(X > 0 and Y < 0):
  print("You are in quadrant IV")
elif(X == 0 and Y != 0):
  print("y-axis")
elif(X != 0 and Y == 0):
 print("x-axis")
else:
  print("Origin")

  
  
