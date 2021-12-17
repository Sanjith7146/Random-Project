from turtle import *
from random import randint 
from random import choice



def singapore_flag():
  '''
  Red part
  '''
  color("red")
  begin_fill()
  fd(1000/2)
  lt(90)
  fd((1000/3*2)/2)
  lt(90)
  fd(1000/2)
  lt(90)
  fd((1000/3*2)/2)
  end_fill()
  '''
  White part
  '''
  penup()
  goto(0,0)
  pendown()
  color("white")
  begin_fill()
  lt(90)
  fd(1000/2)
  lt(90)
  fd((1000/3*2)/4)
  lt(90)
  fd(1000/2)
  lt(90)
  fd((1000/3*2)/4)
  end_fill()
  '''
  border
  '''
  penup()
  goto(0,0)
  pendown()
  color("black")
  lt(90)
  fd(1000/2)
  lt(90)
  fd((1000/3*2)/2)
  lt(90)
  fd(1000/2)
  lt(90)
  fd((1000/3*2)/2)
  '''
  stars
  '''
  penup()
  goto(160,290)
  pendown()
  color("white")
  begin_fill()
  for i in range(5):
    rt(140)
    fd(((1000/3*2)/2)/12)
  end_fill()
  penup()
  goto(200,250)
  pendown()
  color("white")
  begin_fill()
  for i in range(5):
    rt(144)
    fd(((1000/3*2)/2)/12)
  end_fill()
  penup()
  goto(175,200)
  pendown()
  color("white")
  begin_fill()
  for i in range(5):
    rt(144)
    fd(((1000/3*2)/2)/12)
  end_fill()
  penup()
  goto(120,200)
  pendown()
  color("white")
  begin_fill()
  for i in range(5):
    rt(144)
    fd(((1000/3*2)/2)/12)
  end_fill()
  penup()
  goto(110,260)
  pendown()
  color("white")
  begin_fill()
  for i in range(5):
    rt(144)
    fd(((1000/3*2)/2)/12)
  end_fill()
  '''
  cresent
  '''
  x=108
  y=20
  color("white")
  penup()
  goto(110,320)
  rt(x)
  pendown()
  circle(70,180)
  fd(y)
  penup()
  goto(111,320)
  rt(x+72)
  pendown()
  circle(70,180)
  fd(y)
  penup()
  goto(112,320)
  rt(x+72)
  pendown()
  circle(70,180)
  fd(y)
  penup()
  goto(113,320)
  rt(x+72)
  pendown()
  circle(70,180)
  fd(y)
  penup()
  goto(114,320)
  rt(x+72)
  pendown()
  circle(70,180)
  fd(y)
  penup()
  goto(115,320)
  rt(x+72)
  pendown()
  circle(70,180)
  fd(y)
  penup()
  goto(116,320)
  rt(x+72)
  pendown()
  circle(70,180)
  fd(y)
  penup()
  goto(117,320)
  rt(x+72)
  pendown()
  circle(70,180)
  fd(y)
  penup()
  goto(118,320)
  rt(x+72)
  pendown()
  circle(70,180)
  fd(y)
  penup()
  goto(119,320)
  rt(x+72)
  pendown()
  circle(70,180)
  fd(y)
  penup()
  goto(120,320)
  rt(x+72)
  pendown()
  circle(70,180)
  fd(y)
  penup()
  goto(121,320)
  rt(x+72)
  pendown()
  circle(70,180)
  fd(y)
  penup()
  goto(122,320)
  rt(x+72)
  pendown()
  circle(70,180)
  fd(y)
  penup()
  goto(123,320)
  rt(x+72)
  pendown()
  circle(70,180)
  fd(y)
  penup()
  goto(124,320)
  rt(x+72)
  pendown()
  circle(70,180)
  fd(y)
  penup()
  goto(125,320)
  rt(x+72)
  pendown()
  circle(70,180)
  fd(y)
  penup()
  goto(126,320)
  rt(x+72)
  pendown()
  circle(70,180)
  fd(y)
  penup()
  goto(127,320)
  rt(x+72)
  pendown()
  circle(70,180)
  fd(y)
  penup()
  goto(128,320)
  rt(x+72)
  pendown()
  circle(70,180)
  fd(y)
  penup()
  goto(129,320)
  rt(x+72)
  pendown()
  circle(70,180)
  fd(y)
  penup()
  goto(500,500)
  speed(0)

  
  

def india_flag():
  '''
  Orange
  '''
  penup()
  goto(-100,100)
  color("Black")
  pendown()
  begin_fill()
  fillcolor("orange")
  left(90)
  forward(90)
  right(90)
  forward(600)
  right(90)
  forward(90)
  right(90)
  forward(600)
  end_fill()
  '''
  white &
  ashoka chakra
  '''
  left(90)
  forward(90)
  left(90)
  forward(300)
  color("Blue")
  circle(45)
  for spoke in range(0,24):
    goto(200,55)
    right(15)
    pendown()
    forward(45)
    penup()
  color("black")
  penup()
  goto(200,10)
  pendown()
  forward(300)
  left(90)
  forward(90)
  '''
  Green
  '''
  penup()
  goto(-100,10)
  right(180)
  begin_fill()
  fillcolor("green")
  pendown()
  forward(90)
  left(90)
  forward(600)
  left(90)
  forward(90)
  end_fill()
  penup()
  goto(200,55)
  color("blue")
  penup()
  goto(500,500)

def awesome_stars():
  speed(0)
  hideturtle()

  def star(length):
    for i in range(5):
      fd(length)
      rt(144)

  def square(length):
    for i in range(4):
      fd(length)
      rt(90)


  length = 5
  def draw_sky():
    color("black")
    begin_fill()
    square(500)
    end_fill()
  goto(-250,250)
  draw_sky()


  penup()
  goto(0, 40)
  write(randint(1, 10))
  goto(0, 20)
  write(randint(1, 10))
  goto(0, 0)
  write(randint(1, 10))


  color("white")

  for j in range(30):
  
    penup()
    random_x=randint(-250,250)
    random_y=randint(-250,250)
    goto(random_x,random_y)
    pendown()
    begin_fill()
    star(15)
    end_fill()

def Triangle_spiral():
  hideturtle()
  speed(0)

  def square(length):
    for i in range(4):
      fd(length)
      rt(90)

  length = 1000
  def draw_sky():
    penup()
    goto(-length/2,length/2)
    pendown()
    color("black")
    begin_fill()
    square(length)
    end_fill()
  draw_sky()
  colors = ['#ff3300', '#ff00ff', '#1a8cff', '#00ff00', '#00ffcc','#ff3333','#ffbb33',"#ffa31a"]
  penup()
  goto(0,0)
  pendown() 

  for i in range(380):
      colors = ['#ff3300', '#ff00ff', '#1a8cff', '#00ff00', '#00ffcc','#ff3333','#ffbb33',"#ffa31a"]  
      pencolor(colors[i / 50])
      forward(i * 2) 
      right(121)

  
 
def fruit_hangman():
  list_of_fruit=['apple', 'apricot', 'avocado', 'banana','blackberry','blackcurrant', 'blueberry', 'currant', 'cherry', 'coconut','cranberry', 'cucumber', 'custard apple', 'date','dragonfruit', 'durian', 'elderberry', 'fig', 'gooseberry','grape', 'raisin', 'grapefruit', 'guava', 'honeyberry','huckleberry', 'jackfruit', 'jambul', 'jujube', 'kiwifruit','kumquat', 'lemon', 'lime', 'longan', 'lychee', 'mango','melon', 'cantaloupe', 'honeydew', 'watermelon','miracle fruit', 'mulberry', 'olive', 'orange','blood orange', 'mandarine', 'tangerine', 'papaya','passionfruit', 'peach', 'pear', 'persimmon', 'plum','prune', 'pineapple', 'pomegranate', 'pomelo', 'mangosteen','raspberry', 'salmonberry', 'rambutan', 'redcurrant','soursop', 'star fruit', 'strawberry', 'yuzu']
  
  
  
  answer = choice(list_of_fruit)
  life = 10
  chosen_letters = []
  game_over = False

  def display_blanks():
    """
    To displsy wrong ans with _ and right ans with the letter
    """

    display_txt=''

  
    for letter in answer:
      if letter in chosen_letters:
        display_txt=display_txt+letter+' '
      else:
        display_txt=display_txt+'_'+' '
    return display_txt + "\n"
    

  print("_ " * len(answer))

  while life > 0 and game_over == False:
    print("Life: "+str(life))
    input_letter =input('Please enter a letter:')
    if input_letter in chosen_letters:
      print("You have entered these letter before: " + str(chosen_letters) + "\n")
      print(output_text)
    elif input_letter in answer:
      chosen_letters.append(input_letter)
      

      output_text = display_blanks()

      

      if "_" in output_text:
        print(output_text)
      else:
        game_over = True
    else:
      
      life=life-1

      print(display_blanks())

  print("Game over!")
  print("Answer:"+str(answer))

def scissors_paper_stone():
  options = ['scissors','paper','stone']
  computer = choice(options)
  player =input('Please enter your choice?(scissors, paper,stone): ') 
  if player == computer:
    print('You are tied with the computer who also chose ' + computer)

  elif player == 'scissors':
    if computer == 'stone': 
      print("You lose! " + computer + " breaks " + player)
    elif computer == 'paper':
      print("You win! " + player + " cuts " + computer)
     
  elif player == 'paper':
    if computer == 'scissors' : 
      print("You lose! " + computer + " breaks " + player)
    elif computer == 'stone' :
      print("You win! " + player + " wraps " + computer)
  
  elif player == 'stone':
    if computer == 'scissors':
      print("You win! " + player + " cuts " + computer)
    elif computer == 'paper':  
      print("You lose! " + computer + " breaks " + player)
    
  else:
    print('Please spell correctly and run the program again.')
    print('Please type either "scissors", "paper", or "stone"')


def Guess_the_number():
  num_of_guesses = 0
  guess_wrongly = True
  "number of guesses left:"
  secret_num = randint(1, 20)

  print("I am thinking of a number between 1 and 20.")
  print("You have 5 guesses")
  

  while guess_wrongly and num_of_guesses < 5:
    print("Number of guesses left: "+str(5 - num_of_guesses))
    curr_guess = input("Guess the number:")
    curr_guess = int(curr_guess)
    num_of_guesses += 1
    
    if curr_guess > secret_num:
      print("Your guess is too high.")
    elif curr_guess < secret_num:
      print("Your guess is too low.")
    else:
      print("Good job.")
      guess_wrongly=False

  print("The secret number is "+str(secret_num))

def random_number_generator():
  from random import randint
  maximum = int(input('Please enter the largest number:'))
  rand_num = randint(1, maximum)
  print('Number: '+str(rand_num))

def wish_to_play():
  wishing_to_play=True
  while wishing_to_play:

    user_wish1=input('Which type of codes would like to see? Press 1 for Turtle drawings! Press 2 for console games!')

    if user_wish1 == '1':
      clear()
      print('You chose 1!')
      user_wish2=input('Which type of drawing would you like to see? Press 1 for the Singapore Flag! Press 2 for the India Flag! Press 3 for awesome stars! Finally press 4 for a colorful spiral')
      if user_wish2=='1':
        singapore_flag()
        speed(0)
      elif user_wish2=='2':
        india_flag()
        speed(0)
      elif user_wish2=='3':
        awesome_stars()
      elif user_wish2=='4':
        Triangle_spiral()

      else:
        print('ERROR! Please enter 1,2,3,4 or 5.Try Again')
    elif user_wish1=='2':
      print('You chose 2!')
      user_wish3=input('Which type of game would you like to play? Press 1 for a fruity hangman ! Press 2 for a game of Scissors,Paper,stone game.! Press 3 for Guess the number game! Finally press 4 for a random number generator')
      if user_wish3 == '1':
        fruit_hangman()
      elif user_wish3 == '2':
        scissors_paper_stone()
      elif user_wish3 == '3':
        Guess_the_number()
      elif user_wish3 == '4':
        random_number_generator()
      else:
        print('ERROR! Please enter 1,2,3 or 4.Try Again')

    else:
      print('ERROR! Please enter 1 or 2.Try Again')
    
    user_wish4=input('Do you wish to try again?')
    
    if user_wish4 in ['no','No','NO','n','N']:
      wishing_to_play=False
    elif user_wish4 in ['yes','Yes','YES','y','Y']:
      print(' ')
    else:
      print('ERROR! Please enter Yes or No.')
      break

wish_to_play()
speed(0)
