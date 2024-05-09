#Leo Howerdd #cbj7mn
#Runjiu Li #rl3kje

#WAHOODLE

import pygame
import gamebox
import random

# make camera
camera = gamebox.Camera(800, 600)

x_start = 200
y_start = 100  # was 100
x_grid = y_grid = 70
width = height = 60
bg_color = "black"

help_string1 = "Welcome to Wahoodle. In this wordle spinoff, you have to guess "
help_string2 = "4 words correctly. The first word is only 4 letters, but the "
help_string3 = "words will get longer by one letter after each correct guess. "
help_string4 = "You will have 6 tries to guess each word within the time limit. All of the words in "
help_string5 = "this game are related to UVA in some form. Many of the words "
help_string6 = "are important people on grounds, such as professors or "
help_string7 = "basketball players. Words could also be "
help_string8 = "buildings around grounds, places on the corner, or anything   "
help_string9 = "students like chatting about or significant to UVA culture."


#help mode grid

#ex1
ex1 = [gamebox.from_color(200, 300, "black", 60, 60),
   gamebox.from_color(270, 300, "black", 60, 60),
   gamebox.from_color(340, 300, "black", 60, 60),
   gamebox.from_color(410, 300, "black", 60, 60),
   gamebox.from_color(480, 300, "black", 60, 60)]

ex2 = [gamebox.from_color(200, 400, "black", 60, 60),
   gamebox.from_color(270, 400, "black", 60, 60),
   gamebox.from_color(340, 400, "black", 60, 60),
   gamebox.from_color(410, 400, "black", 60, 60),
   gamebox.from_color(480, 400, "black", 60, 60)]

ex3 = [gamebox.from_color(200, 500, "black", 60, 60),
   gamebox.from_color(270, 500, "black", 60, 60),
   gamebox.from_color(340, 500, "black", 60, 60),
   gamebox.from_color(410, 500, "black", 60, 60),
   gamebox.from_color(480, 500, "black", 60, 60)]

def grid(i, j):
   """
   this function draws the grid that holds the letters
   """
   return gamebox.from_color(x_start + i * x_grid, y_start + j * y_grid, bg_color, width, height)

# word banks
four_letter_words = ['RUNK', 'TRIN', 'LAWN', 'TONY',
                    'DISH', 'RICE', 'COMM', 'BOND', 'BICE', 'FRAT', 'SRAT',
                    'KENT', "RYAN", "SHEA", "ELMO", "HALL", "PAGE", "ECON"]

five_letter_words = ['OHILL', 'BODOS', 'ASADO', 'GOOCH',
                    'VASST', 'RUGBY', 'KIHEI', 'REECE', 'WAJEW', 'WAHOO',
                    'VIRGE', 'CURRY', 'SCOTT', 'BROWN', 'TUNDY', "FLOYD"
                     , "WOODY"]

six_letter_words = ['CROADS', 'BOYLAN', 'BATTEN', 'CROZET',
                   'CORNER', 'YIKYAK', 'CASTLE', 'WILSON', 'GIBSON', 'RIDLEY',
                   'MCLEOD', 'ROUSSE', 'CABELL', "ECHOLS", "COLLAB", "CHAPEL", "HILLEL",
                    "PRONTO", "DABNEY", "JELANI"]

seven_letter_words = ['CAFFARO', 'GARDNER', 'ROTUNDA',
                     'NEWCOMB', 'LAMBETH', 'GROUNDS', 'GIBBONS', "FRAILEY", "MADBOWL",
                      'PRECOMM', 'COPELY', "METCALF", "HANCOCK", "KELLOG", "CAUTHEN"
                      "ELZINGA", "DILLARD"]


letter_words = {
   4: four_letter_words,
   5: five_letter_words,
   6: six_letter_words,
   7: seven_letter_words,
}


MAX_LEVEL = 7
MIN_LEVEL = 4
level = MIN_LEVEL
MAX_TIMES = 6


def pick_word(word_list):
   """
   This function picks a random word from the passed list
   :param word_list: list of words that are all the same length
   :return: random word from passed list
   """
   num = random.randint(0, len(word_list) - 1)
   return word_list[num]


def get_letter(keys):
   """
   This function returns the keys that are pressed
   by the user
   :return: either a letter or delete; return will be added later
   """

   letter = ""

   if pygame.K_a in keys:
       letter = "A"
   if pygame.K_b in keys:
       letter = "B"
   if pygame.K_c in keys:
       letter = "C"
   if pygame.K_d in keys:
       letter = "D"
   if pygame.K_e in keys:
       letter = "E"
   if pygame.K_f in keys:
       letter = "F"
   if pygame.K_g in keys:
       letter = "G"
   if pygame.K_h in keys:
       letter = "H"
   if pygame.K_i in keys:
       letter = "I"
   if pygame.K_j in keys:
       letter = "J"
   if pygame.K_k in keys:
       letter = "K"
   if pygame.K_l in keys:
       letter = "L"
   if pygame.K_m in keys:
       letter = "M"
   if pygame.K_n in keys:
       letter = "N"
   if pygame.K_o in keys:
       letter = "O"
   if pygame.K_p in keys:
       letter = "P"
   if pygame.K_q in keys:
       letter = "Q"
   if pygame.K_r in keys:
       letter = "R"
   if pygame.K_s in keys:
       letter = "S"
   if pygame.K_t in keys:
       letter = "T"
   if pygame.K_u in keys:
       letter = "U"
   if pygame.K_v in keys:
       letter = "V"
   if pygame.K_w in keys:
       letter = "W"
   if pygame.K_x in keys:
       letter = "X"
   if pygame.K_y in keys:
       letter = "Y"
   if pygame.K_z in keys:
       letter = "Z"
   if pygame.K_BACKSPACE in keys:
       letter = "1"

   return letter

#win status
win = None
#holds user input
user_word = ""
#which of the grid is being used
row = 0
#list of the users guesses
guesses = [''] * MAX_TIMES
#pick the first word
word = pick_word(letter_words[level])
#list of all the words picked for each letter
words = ['', '', '', '']
#just stores number that makes it easier to draw text
levels_y = 150
#start game not in help mode
help_mode = False
#amount of time for starting level
seconds = 180


def init():
   """
   This function init the situation
   :return: None
   """
   global user_word, row, guesses, word, seconds
   user_word = ""
   row = 0
   guesses = [''] * MAX_TIMES
   word = pick_word(letter_words[level])
   if level == 5:
       seconds = 210
   if level == 6:
       seconds = 240
   if level == 7:
       seconds = 270

def tick(keys):

   global win, user_word, row, guesses, word, level, words, levels_y, MIN_LEVEL, help_mode, help_string1, help_string2\
       , help_string3, help_string4, help_string5, help_string6, help_string7, help_string8, help_string9, seconds, ex1\
       , ex2, ex3

   camera.clear("white")

   #list of word for each level

   if not help_mode:
      for i in range(MAX_TIMES):
         for j in range(level):
            camera.draw(grid(j, i))

   #get user input
   user_letter = get_letter(keys)

   # update string of the letters gussed by the user while guesses remain
   if win is None and not help_mode:
       if len(user_word) < level:
           user_word += user_letter
       # let user backspace at 5 letters
       elif len(user_word) == level:
           if user_letter == "1":
               user_word += user_letter

   # check that there is a letter to backspace
   if win is None and len(user_word) > 0:
       # delete most recent letter
       if user_word[len(user_word) - 1] == "1":
           temp_word = user_word[0:len(user_word) - 2]
           user_word = temp_word

   #draw words that that user is typing
   for i in range(len(user_word)):
       (camera.draw(gamebox.from_text(
           grid(i, row).x, grid(i, row).y, user_word[i], 60, 'white')))

   # check if user confirms their guess and redraw the letters in propor color
   if win is None and len(user_word) == level and pygame.K_RETURN in keys:
       guesses[row] = user_word
       if guesses[row] == word:
           words[level - 4] = word
           if level == MAX_LEVEL:
               # win
               win = True
           else:
               # level up and reset
               level += 1
               init()
               return
       row += 1
       if row == MAX_TIMES and win is None:
           win = False
       user_word = ""

   #draw the guessed words in their proper colors
   if not help_mode:
      for i in range(row):
          guess = [[guesses[i][j], False] for j in range(level)]
          w = list(word)

          # right location
          for j in range(level):
              g = guess[j]
              if g[0] == word[j]:
                  camera.draw(gamebox.from_text(
                  grid(j, i).x, grid(j, i).y, guesses[i][j], 60, 'green'))
                  g[1] = True
                  w.remove(g[0])

          # wrong location but in word
          for j in range(level):
              g = guess[j]
              if not g[1] and g[0] in w:
                  camera.draw(gamebox.from_text(
                  grid(j, i).x, grid(j, i).y, guesses[i][j], 60, 'yellow'))
                  g[1] = True
                  w.remove(g[0])

          # gray
          for j in range(level):
              g = guess[j]
              if not g[1]:
                  camera.draw(gamebox.from_text(
                  grid(j, i).x, grid(j, i).y, guesses[i][j], 60, 'gray'))

   
   if win:
       camera.draw(gamebox.from_text(340, 520, 'Win', 60, 'red'))
   elif win is not None:

       if level > 4:
          camera.draw(gamebox.from_text(390, 520, 'You lost, press R to start over at level 1 or press S to try '
                'this level again', 30, 'red'))
       else:
           camera.draw(gamebox.from_text(390, 520, "You lost, press R to try again with a new word", 30, 'red'))

       camera.draw(gamebox.from_text(360, 550, "The word was " + word, 30, "blue"))

       #ask user if they want to restart and reset
       if pygame.K_r in keys:
           user_word = ''
           level = MIN_LEVEL
           init()
           win = None
       #restart at current level
       if pygame.K_s in keys:
           user_word = ''
           init()
           win = None


   #display the correct word for each level after they have been guessed
   if not help_mode:
      if words[0] != '':
         camera.draw(gamebox.from_text(80, levels_y, "Level 1: " + words[0], 25, 'blue'))
      if words[1] != '':
         camera.draw(gamebox.from_text(80, levels_y + 40, ("Level 2: " + words[1]), 25, 'blue'))
      if words[2] != '':
         camera.draw(gamebox.from_text(80, levels_y + 80, ("Level 3: " + words[2]), 25, 'blue'))
      if words[3] != '':
         camera.draw(gamebox.from_text(80, levels_y + 120, ("Level 4: " + words[3]), 25, 'blue'))

   #draw current level
   if not help_mode:
    camera.draw(gamebox.from_text(600, 40, "Current Level: " + str(level - 3), 30, 'blue'))

   if not help_mode:
      camera.draw(gamebox.from_text(630, 560, "Press 5 for game details", 30, 'blue'))
   #see if user enters help mode
   if pygame.K_5 in keys:
       help_mode = True

   #draw help text
   if help_mode:

      #write basic description
      camera.draw(gamebox.from_text(345, 100, help_string1, 15, 'blue'))
      camera.draw(gamebox.from_text(333, 120, help_string2, 15, 'blue'))
      camera.draw(gamebox.from_text(340, 140, help_string3, 15, 'blue'))
      camera.draw(gamebox.from_text(390, 160, help_string4, 15, 'blue'))
      camera.draw(gamebox.from_text(345, 180, help_string5, 15, 'blue'))
      camera.draw(gamebox.from_text(335, 200, help_string6, 15, 'blue'))
      camera.draw(gamebox.from_text(300, 220, help_string7, 15, 'blue'))
      camera.draw(gamebox.from_text(345, 240, help_string8, 15, 'blue'))
      camera.draw(gamebox.from_text(335, 260, help_string9, 15, 'blue'))

      camera.draw(gamebox.from_text(345, 80, "How To Play", 40, 'blue'))

      #draw the example grids
      for box1 in ex1:
          camera.draw(box1)
      for box2 in ex2:
           camera.draw(box2)
      for box3 in ex3:
           camera.draw(box3)

      temp_word = "WAHOO"

      #draw example 1 word
      for i in range(len(temp_word)):
          if temp_word[i] == "A":
              camera.draw(gamebox.from_text(ex1[i].x, ex1[i].y, temp_word[i], 60, 'green'))
          else:
              camera.draw(gamebox.from_text(ex1[i].x, ex1[i].y, temp_word[i], 60, 'white'))
      camera.draw(gamebox.from_text(340, 350, "The letter A is in the word and in the correct spot", 30, "orange"))

      #draw example 2 word
      for i in range(len(temp_word)):
          if temp_word[i] == "W":
              camera.draw(gamebox.from_text(ex2[i].x, ex2[i].y, temp_word[i], 60, 'yellow'))
          else:
              camera.draw(gamebox.from_text(ex2[i].x, ex2[i].y, temp_word[i], 60, 'white'))
      camera.draw(gamebox.from_text(340, 450, "The letter W is in the word but in the wrong spot", 30, "orange"))

      #draw example 3 word
      for i in range(len(temp_word)):
           if temp_word[i] == "H":
               camera.draw(gamebox.from_text(ex3[i].x, ex3[i].y, temp_word[i], 60, 'gray'))
           else:
               camera.draw(gamebox.from_text(ex3[i].x, ex3[i].y, temp_word[i], 60, 'white'))

      camera.draw(gamebox.from_text(340, 550, "The letter h is not in the word in any spot", 30, "orange"))

      camera.draw(gamebox.from_text(340, 580, "Press 6 to exit help mode", 30, "orange"))

   #check if user exits help mode
      if pygame.K_6 in keys:
         help_mode = False

   #draw title
   camera.draw(gamebox.from_text(340, 40, "WAHOODLE", 50, "orange"))

   #draw time remaining
   if not help_mode:
    camera.draw(gamebox.from_text(120, 40, "Time Remaining: " + str(round(seconds, 0)//1), 20, "red"))

   #decrease time remaining
   if win is None and not help_mode:
      seconds -= .1
   #check if time has run out
   if seconds <= 0:
       win = False

   #display everything
   camera.display()


fps = 10
gamebox.timer_loop(fps, tick)