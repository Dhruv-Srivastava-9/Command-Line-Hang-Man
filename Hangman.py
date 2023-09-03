"""Imports
-Random
-String
"""
import random
import string

class Hangman:
  def selector(self,mode):

    
    
    #Selecting mode based on user's input
    if mode == 'e':
      self.easy()
      
      
    elif mode == 'm':
      self.medium()
      
      
    elif mode == 'h':
      self.hard()
      
      #else invalid
    else:
      print("Invalid Input")
      

    self.mode = mode


  def word_generator(self,mode):
    #Generate the word based on user's mode choice: 
    letters = string.ascii_lowercase
    if mode == 'e':
        self.word = ''.join(random.choice(letters) for i in range(3))

    elif mode == 'm':
        self.word = ''.join(random.choice(letters) for i in range(5))

    elif mode == 'h':
        self.word = ''.join(random.choice(letters) for i in range(7))

  def word_hider2(self,word):
      #Convert the word into list and store in hidden
      hiddden = list(word)
      #Loop it to iterate over each element
      for i in range(len(word)):
        hiddden[i]='_' #Replace each element with _ to hide it
      return hiddden #reuturn the value

  def game_logic(self,word,guesses,correct):
    guessed = 0
    #Convert the word into list
    lil = list(self.word)

    print(f"\nYou got {guesses} Guesses")
    print(f"\nYou have to guess {correct} letters")
    #Hide the word using the word_hider2 function and store in hid
    hid = self.word_hider2(self.word) 

    print(f"\nThe word is: {hid}")
    while correct > 0:
      guess = input()
      if guess.isdigit(): #check if the guess is digit or not
        print("Nice Try Bud, but no numbers are allowed")
        print(hid)
      elif len(guess) >1: #Check if the guess is more than 1 character
        print("Hey, Only 1 character at a time")
        print(hid)
      elif len(guess) == 0: #Check if the guess is nothing
        print("Atleast give an input...")
        print(hid)
      else:
        if guess in lil:
          index = lil.index(guess) #Get the index of the guess in the list lil
          guesses = guesses - 1
          correct = correct-1
          hid[index] = guess #Replace _ of hid on the index of guess in lil and replace with guess
          print(f"Correct Gyess, {hid}")
          
          if guessed == correct: #To stop the game💀
            print("\n",hid)
            print("\nGg you did it!")
            print("\nBack to the selection screen")
            break

        elif not guess in lil: #if guess is incorrect
          print("Wrong Guess")
          guesses = guesses - 1
          print(f"Number of Guesses left: {guesses}")
          if guesses == 0: #if the amount of guesses the user has = 0:
            print("\nGame over")
            print(f"\nThe word was: {self.word}")
            print("\nBetter luck next time")
            break
            
    
  def easy(self):
    self.game_logic(self.word_generator("e"),5,3)


  def medium(self): 
    self.game_logic(self.word_generator("m"), 3, 5)

  def hard(self):
    self.game_logic(self.word_generator("h"), 3, 7)

#Creating Instance
hangman = Hangman()
modes_list = ["e for Easy","m for Medium","h f  or Hard"]
print(modes_list)
mode = input("Enter a mode from the above list: ")


if mode.isdigit == True: 
  print("No Numbers Please")
else:
  hangman.selector(mode)