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
      self.medium(self.word_generator(mode))
      
      
    elif mode == 'h':
      self.hard(self.word_generator(mode))
      
      
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
    guessed = 0
    lil = list(self.word)
    print("\nEasy Mode Prompt")
    print(f"\nYou got {guesses} Guesses")
    print(f"\nYou have to guess {correct} letters")
    hid = self.word_hider2(self.word)
    print(f"\nThe word is: {hid}")
    print(self.word)
    while correct > 0:
      guess = input()
      if not guess.isalnum:
        print("Nice Try Bud, but no numbers are there")
      elif len(guess) >1:
        print("Hey 1 character at a Time")
      elif len(guess) == 0:
        print('Atleast give an input...')
        print(hid)
      else:
        if guess in lil:
          index = lil.index(guess)
          hid[index] = guess
          print(f"Correct Guess, {hid}")
          guesses = guesses-1
          correct = correct-1
          guessed = guessed + 1
          
        if guessed == 3:
          print("\nGG, You did")
          print(f"\nYou guessed {guessed} letters!")
          print("\nBack to the selection screen...")
          break

        elif not guess in lil:
          print("Wrong Guess")
          errors = errors + 1
          guesses = guesses-1
          print(f"\nGuesses left are: {guesses}")
          print(hid)
          if errors == 3:
            print("\nGame Over")
            print(f"You guessed {guessed} letters")
            print(f"The word was {self.word}")
            break


  def medium(self,word): 
    guesses = 3
    errors = 0
    correct = 5
    guessed = 0
    lil = list(self.word)
    print("\Medium Mode Prompt")
    print(f"\nYou got {guesses} Guesses")
    print(f"\nYou have to guess {correct} letters")
    hid = self.word_hider2(self.word)
    print(f"\nThe word is: {hid}")
    print(self.word)
    while correct > 0:
      guess = input()
      if not guess.isalnum:
        print("Nice Try Bud, but no numbers are there")
      elif len(guess) >1:
        print("Hey 1 character at a Time")
      elif len(guess) == 0:
        print('Atleast give an input...')
        print(hid)
      else:
        if guess in lil:
          index = lil.index(guess)
          hid[index] = guess
          print(f"Correct Guess, {hid}")
          guesses = guesses-1
          correct = correct-1
          guessed = guessed + 1
          
        if guessed == 5:
          print("\nGG, You did")
          print(f"\nYou guessed {guessed} letters!")
          print("\nBack to the selection screen...")
          break

        elif not guess in lil:
          print("Wrong Guess")
          errors = errors + 1
          guesses = guesses-1
          print(f"\nGuesses left are: {guesses}")
          print(hid)
          if errors == 3:
            print("\nGame Over")
            print(f"You guessed {guessed} letters")
            print(f"The word was {self.word}")
            break

  def hard(self):
    guesses = 3
    errors = 0
    correct = 7
    guessed = 0
    lil = list(self.word)
    print("\Medium Mode Prompt")
    print(f"\nYou got {guesses} Guesses")
    print(f"\nYou have to guess {correct} letters")
    hid = self.word_hider2(self.word)
    print(f"\nThe word is: {hid}")
    print(self.word)
    while correct > 0:
      guess = input()
      if not guess.isalnum:
        print("Nice Try Bud, but no numbers are there")
      elif len(guess) >1:
        print("Hey 1 character at a Time")
      elif len(guess) == 0:
        print('Atleast give an input...')
        print(hid)
      else:
        if guess in lil:
          index = lil.index(guess)
          hid[index] = guess
          print(f"Correct Guess, {hid}")
          guesses = guesses-1
          correct = correct-1
          guessed = guessed + 1
          
        if guessed == 7:
          print("\nGG, You did")
          print(f"\nYou guessed {guessed} letters!")
          print("\nBack to the selection screen...")
          break

        elif not guess in lil:
          print("Wrong Guess")
          errors = errors + 1
          guesses = guesses-1
          print(f"\nGuesses left are: {guesses}")
          print(hid)
          if errors == 3:
            print("\nGame Over")
            print(f"You guessed {guessed} letters")
            print(f"The word was {self.word}")
            break

#Creating Instance
hangman = Hangman()
modes_list = ["e for Easy","m for Medium","h for Hard"]
print(modes_list)
mode = input()
if mode.isdigit == True:
  print("No Numbers Please")
else:
  hangman.selector(mode)