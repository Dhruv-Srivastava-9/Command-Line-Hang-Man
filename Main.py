"""Imports
-Random
-String
"""
import random
import string

class Hangman:
  def selector(self,mode):

    modes_list = ["e for Easy","m for Medium","h for Hard"]
    print(modes_list)
    
    self.running = True
    if mode == 'e':
      self.easy(self.word)
      
      y = "Easy"
    elif mode == 'm':
      self.medium()
      
      y = "Medium"
    elif mode == 'h':
      self.hard()
      
      y = "Hard"
    else:
      print("Invalid Input")
      y = "Invalid"
    print(f"Mode is{y}")
    self.mode = mode


  def word_generator(self):
    letters = string.ascii_lowercase
    if self.mode == 'e':
        self.word = ''.join(random.choice(letters) for i in range(3))
    elif self.mode == 'm':
        self.word = ''.join(random.choice(letters) for i in range(5))
    elif self.mode == 'h':
        self.word = ''.join(random.choice(letters) for i in range(7))

  def word_hider(word):
    hiddden = word
    for i in range(len(word)):
      hiddden[i]='_'
    return hiddden
    
  def word_checker(self):
    pass

  
  def easy(self,word):
    guesses = 5
    errors = 0
    correct = 3
    print("\nEasy Mode Prompt")
    print(f"\nYou got {guesses} Guesses")
    print(f"\nYou have to guess {correct} letters")

    print(word) #Test
    guess = input()
    if not guess.isalnum:
      print("Nice Try Bud, but no numbers are there")
    elif len(guess) >1:
      print("Hey 1 character at a Time")

  def medium(self): 
    print("This is Medium mode")
  def hard(self):
    print("This is Hard mode")

#Creating Instance
hangman = Hangman()
m = input()
if not m.isalpha:
  print("Bro, only strings")
else:
  hangman.word_hider("Haha")
