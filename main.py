from art import logo, vs 
from game_data import data
from replit import clear
import random
# import logo
print(logo) 

def game():
  #generate a random number for A and B
  A,B=random.sample(data, 2)
  loss=False
  score = 0
  #loop through the list till loss = True
  while(loss!=True):
    #print the value to compare A vs B
    print(f"Compare A: {A['name']}, {A['description']}, {A['country']}\n {vs}\n Against B: {B['name']}, {B['description']}, {B['country']}\n ")
    #function to know the greatest of A and B 
    greatest = greater(A, B)
    #take user guess
    guess = input("Who has more followers? Type 'A' or 'B' ")
    #function to retrieve correct guess
    guess= know_guess(guess, A, B)
    #if guess is right
    if guess == greatest:
       update_play(guess, A, B, data)
      #update global score
       update_score(score)
      #clear
       clear()
       print(f"You're right! current score = {score}")
    else:
      loss= True
      print(score)
   

def greater(A, B):
  if (A['follower_count']>B['follower_count']):
    return A
  else:
    return B

def know_guess(guess, A, B):
  if (guess=="A"):
      guess = A
  else:
      guess = B
  return guess

def update_play(guess, A, B, data):
     A = guess
     B = random.choice(data)
     if(B == A):
          B = random.choice(data)

def update_score(count):
  count+=1

game()

 




#print (vs)