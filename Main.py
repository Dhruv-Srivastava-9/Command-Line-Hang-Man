"""Imports
-Random
"""

class Hangman:
  def check(self, running):
    #If True then run the word_generator, if false break
    while running == True:
      word = self.word_generator()
  def selector(self,mode):
    easy = False
    medium = False
    hard = False
    print(f"Mode is {mode}")
    self.running = True
    while True:
      self.check(self.running)
      break

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
    mode = self.mode
    if mode == 'e':
      print("3 letter string")#Write code to generate for easy one
    elif mode == 'm':
      print("5 letter string") #Wrie code to generate for medium one
    elif mode == 'h':
      print("7 letter string") #Write code to generate for hard one

  def easy(self,): #Add the word generated from word_generator
    print("This is easy mode")
  def medium(self): #Add the word generated from word_generator
    print("This is Medium mode")
  def hard(self): #Add the word generated from word_generator
    print("This is Hard mode")


hangman = Hangman()
m = input()
hangman.selector(m)

