"""Imports
-Random
-String
"""
import random
import string

class Hangman:
  def selector(self,mode):


    
    self.running = True
    if mode == 'e':
      self.easy(self.word_generator(mode))
      
      
    elif mode == 'm':
      self.medium()
      
      
    elif mode == 'h':
      self.hard()
      
      
    else:
      print("Invalid Input")
      y = "Invalid"

    self.mode = mode


  def word_generator(self,mode):
    
    letters = string.ascii_lowercase
    if mode == 'e':
        self.word = ''.join(random.choice(letters) for i in range(3))

    elif mode == 'm':
        self.word = ''.join(random.choice(letters) for i in range(5))

    elif mode == 'h':
        self.word = ''.join(random.choice(letters) for i in range(7))

  def word_hider2(self,word):
      print(type(word))
      hiddden = list(word)
      for i in range(len(word)):
        hiddden[i]='_'
      return hiddden
    
    
  def easy(self,word):
    guesses = 5
    errors = 0
    correct = 3
    lil = list(self.word)
    print("\nEasy Mode Prompt")
    print(f"\nYou got {guesses} Guesses")
    print(f"\nYou have to guess {correct} letters")
    hid = self.word_hider2(word)
    print(f"\nThe word is: {hid}")
    print(self.word) #Test
    guess = input()
    if not guess.isalnum:
      print("Nice Try Bud, but no numbers are there")
    elif len(guess) >1:
      print("Hey 1 character at a Time")
    else:
      if guess in lil:
        index = lil.index(guess)
        hid.replace(index, guess)
        print(f"Correct Guess, {hid}")
        
    

  def medium(self): 
    print("This is Medium mode")
  def hard(self):
    print("This is Hard mode")

#Creating Instance
hangman = Hangman()
modes_list = ["e for Easy","m for Medium","h for Hard"]
print(modes_list)
mode = input()
if mode.isdigit == True:
  print("No Numbers Please")
else:
  hangman.selector(mode)