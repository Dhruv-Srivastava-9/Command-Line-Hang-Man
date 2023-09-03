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
      self.easy()
      
      
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

  def game_logic(self,word,guesses,correct):
    guessed = 0
    lil = list(self.word)
    print(f"\nYou got {guesses} Guesses")
    print(f"\nYou have to guess {correct} letters")
    hid = self.word_hider2(self.word)
    print(self.word) #Test
    print(f"\nThe word is: {hid}")
    while correct > 0:
      guess = input()
      if guess.isdigit():
        print("Nice Try Bud, but no numbers are allowed")
        print(hid)
      elif len(guess) >1:
        print("Hey, Only 1 character at a time")
        print(hid)
      elif len(guess) == 0:
        print("Atleast give an input...")
        print(hid)
      else:
        if guess in lil:
          index = lil.index(guess)
          guesses = guesses - 1
          correct = correct-1
          hid[index] = guess
          print(f"Correct Gyess, {hid}")
          
          if guessed == correct:
            print("\n",hid)
            print("\nGg you did it!")
            print("\nBack to the selection screen")
            break

        elif not guess in lil:
          print("Wrong Guess")
          errors = errors+1
          guesses = guesses - 1
          if guesses == 0:
            print("\nGame over")
            again = input("Wanna Play again?")
            if again.lower():
              print("Sure Thing, Loading back to home screen")
              print("Please run again")
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
mode = input()
if mode.isdigit == True:
  print("No Numbers Please")
else:
  hangman.selector(mode)