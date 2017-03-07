#       HANGMAN FOR NATALIE
#       22.02.2017
#       TOMASZ KLUCZKOWSKI
#       tomaszk1@hotmail.co.uk

import random, turtle, string


def generate_word(diff_lvl):
    """ Selects a random word from a list from Grade 1 to 5 depending on the value of diff_lvl.
        The list gets loaded from a file "Grade [diff_lvl] vocabulary_filtered.txt." """
    vocab_file_handle = open("Grade " + str(int(diff_lvl)) + " vocabulary_filtered.txt", "r")
    word_list = vocab_file_handle.readlines()
    vocab_file_handle.close()

    rng = random.Random()
    word = word_list[rng.randrange(1,len(word_list))]
    word = word.replace("\n", "")
    return word


def draw_word(guess, x_pos):
    """ Prints current guess on the trutle screen. The gap between letters used is 10p.  """
    tur_1.goto(x_pos,-200)
    for char in guess:
        tur_1.write(char, move=False, align="left", font=("Courier", 64, "normal"))
        tur_1.forward(74)


def draw_hint(letter, num_of_guesses):
    """ Prints used letter on the turtle screen. Num_of_guesses = 1 - print text message also """
    if num_of_guesses == 1:
        tur_3.goto(-600,-300)
        tur_3.write("You have used letter(s): " + letter + " ", True, align = "left", font = ("Courier", 12, "normal"))
    else:
        tur_3.write(letter + " ", True, align = "left", font = ("Courier", 12, "normal"))


def amend_guess(letter, word, guess):
    """ Finds all positions of guessed letter in word, displays them on the screen,
        amends current guess and returns it. """
    ix = 0
    while word.find(letter, ix) != -1:
        ix = word.find(letter, ix)
        guess = guess[:ix] + letter + guess[ix+1:]
        ix += 1
    draw_word(guess, x_pos)
    return guess


def draw_gallows():
    """ Draw gallows, only once, at the start of the program. """
    mr_gallows.hideturtle()
    mr_gallows.penup()
    mr_gallows.goto(150,-50)
    mr_gallows.pendown()
    mr_gallows.forward(300)
    mr_gallows.penup()
    mr_gallows.backward(150)
    mr_gallows.pendown()
    mr_gallows.left(90)
    mr_gallows.forward(300)
    mr_gallows.left(90)
    mr_gallows.forward(100)
    mr_gallows.left(90)
    mr_gallows.forward(50)


def draw_hangman(hangman_state):
    """ Draws the hangman in parts depending on current value of hangman_state. """
    hangman.speed(0)
    hangman.color("pink")
    hangman.hideturtle()
    # head
    if hangman_state == 1:
        hangman.pensize(3)
        hangman.penup()
        hangman.goto(200, 200)
        hangman.pendown()
        hangman.circle(-30)
    # eyes
    elif hangman_state == 2:
        hangman.pensize(1)
        hangman.penup()
        hangman.right(90)
        hangman.forward(30)
        hangman.left(90)
        hangman.backward(15)
        hangman.pendown()
        hangman.circle(5)
        hangman.penup()
        hangman.forward(30)
        hangman.pendown()
        hangman.circle(5)
    # nose
    elif hangman_state == 3:
        hangman.penup()
        hangman.goto(195,160)
        hangman.pendown()
        hangman.forward(10)
        hangman.left(120)
        hangman.forward(10)
        hangman.left(120)
        hangman.forward(10)
    # smile
    elif hangman_state == 4:
        hangman.setheading(-55)
        hangman.penup()
        hangman.goto(188,155)
        hangman.pendown()
        hangman.circle(15, 120)
    # neck
    elif hangman_state == 5:
        hangman.pensize(5)
        hangman.setheading(0)
        hangman.penup()
        hangman.goto(200, 140)
        hangman.pendown()
        hangman.right(90)
        hangman.forward(20)
    # arm 1
    elif hangman_state == 6:
        hangman.left(45)
        hangman.forward(70)
    # arm 2
    elif hangman_state == 7:
        hangman.penup()
        hangman.goto(200, 120)
        hangman.pendown()
        hangman.right(90)
        hangman.forward(70)
    # skirt
    elif hangman_state == 8:
        hangman.penup()
        hangman.goto(200, 120)
        hangman.pendown()
        hangman.goto(235, 25)
        hangman.setheading(180)
        hangman.forward(70)
        hangman.goto(200, 120)
    # leg 1
    elif hangman_state == 9:
        hangman.penup()
        hangman.goto(190, 25)
        hangman.pendown()
        hangman.setheading(270)
        hangman.forward(40)
        hangman.right(90)
        hangman.forward(20)
    # leg 2
    elif hangman_state == 10:
        hangman.penup()
        hangman.goto(210, 25)
        hangman.pendown()
        hangman.setheading(270)
        hangman.forward(40)
        hangman.left(90)
        hangman.forward(20)


def quit_prog():
    """ Quit turtle window after pressing Escape or if called by the program. """
    wn.bye()


def terminate_game():
    """ Ask user if they would like to quit the game, return quit_answer. """
    while True:
        quit_answer = wn.textinput("Do you want to quit playing?", "Please enter y / n:\t\t\t\t\t")
        if quit_answer == None or quit_answer not in ["y", "n"]:
            continue
        else:
            return quit_answer


def win_loss(condition):
    """ Display win/loss on the screen. In case of a loss display the unguessed word. """
    tur_2.penup()
    tur_2.goto(-600,0)
    if condition == 1:
        msg = "You Win !!!"
    else:
        msg = "You Lose !!!"
    tur_2.write(msg, move=False, align="left", font=("Times New Roman", 80, "normal"))
    draw_word(word, x_pos)

# control the turtle grahics screen size and position
turtle.setup(1.0, 1.0, 0, 0)
wn = turtle.Screen()
wn.title("Hangman for Natalie")

# this turtle will draw letters
tur_1 = turtle.Turtle()
tur_1.speed(0)
tur_1.hideturtle()
tur_1.penup()

# this turtle will draw win / loss screen
tur_2 = turtle.Turtle()
tur_2.speed(0)
tur_2.hideturtle()

# this turtle will draw hint letters
tur_3 = turtle.Turtle()
tur_3.hideturtle()
tur_3.penup()
tur_3.speed(0)

# this turtle will draw the gallows
mr_gallows = turtle.Turtle()
mr_gallows.speed(0)
mr_gallows.pensize(5)
mr_gallows.color("brown")
draw_gallows()

# this turtle will draw the hangman
hangman = turtle.Turtle()
hangman.hideturtle()

play_again = 0
wn.onkey(quit_prog, "Escape")
wn.listen()

# main game loop
while play_again != "n":

    # reset all variables before each game
    num_of_guesses = 0
    diff_lvl = 0
    hangman_state = 0
    user_quit = 0
    letter = ""
    word = ""
    guess = ""
    quit_answer = ""
    used_letters = ""

    # difficulty selection loop
    while diff_lvl not in range(1,6):
        diff_lvl = wn.numinput("Difficulty level selection", "Please enter difficulty level 1 - 5:\t\t", 1, minval = 1, maxval = 5)
        if diff_lvl == None:
            quit_answer = terminate_game()
        if quit_answer == "y":
            quit_prog()
            play_again = "n"
            break
        elif quit_answer == "n":
            quit_answer = ""
            continue

        word = generate_word(diff_lvl)
        word_lenght = len(word)

        # initially display the word as underscores only
        guess = "_" * word_lenght

        # initial absolute x position of tur_1 to keep the word in the middle of the screen
        # -((font size + gap) x num of letters in the word) / 2
        x_pos = -(len(guess) * 74) / 2
        draw_word(guess, x_pos)

    # loop for guessing all the letters
    while guess != word:
        letter = wn.textinput("Guess the word !", "Please enter a letter that is in the word:")

        if letter == None:
            quit_answer = terminate_game()
        if quit_answer == "y":
            quit_prog()
            play_again = "n"
            break
        elif quit_answer == "n":
            quit_answer = ""
            continue
        if len(letter) == 1 and letter in string.ascii_lowercase and letter not in used_letters:
            used_letters += letter

            if letter in word:
                guess = amend_guess(letter, word, guess)
                num_of_guesses += 1
                draw_hint(letter, num_of_guesses)
                if guess == word:
                    win = 1
            else:
                hangman_state += 1
                draw_hangman(hangman_state)
                num_of_guesses += 1
                draw_hint(letter, num_of_guesses)
                if hangman_state == 10:
                    win = 0
                    break
        else:
            continue                                # ask user to type a letter again
    if quit_answer != "y":
        win_loss(win)                               # call to display WIN / LOSS

        # continue game? loop
        while quit_answer != "y":
            play_again = wn.textinput("Do you want to play again?", "Please enter y / n:\t\t\t\t\t")
            if play_again == None:
                continue
            elif play_again == "y":
                hangman.reset()
                hangman.hideturtle()
                tur_1.clear()
                tur_2.clear()
                tur_3.clear()
                break
            elif play_again == "n":
                quit_answer = "y"
                quit_prog()
                break