"""Imports
-Random
"""

class Hangman:
  def selector(self,mode): 
    easy = False
    medium = False
    hard = False
    if mode == 'e':
      self.easy()
      easy = True
    elif mode == 'm':
      self.medium()
      medium = True
    elif mode == 'h':
      self.hard()
      hard = True
  def word_generator(self): #Add functanality of changing the length of the word according to the input of selector
    pass
  def easy(self): #Add the word generated from word_generator
    print("This is easy mode")
  def medium(self): #Add the word generated from word_generator
    print("This is Medium mode")
  def hard(self): #Add the word generated from word_generator
    print("This is Hard mode")


hangman = Hangman()
m = input()
hangman.selector(m)

