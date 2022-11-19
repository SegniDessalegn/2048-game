import random
import turtle

# this is the original array and it is this that gets updated
the_array = [[0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0], [0, 0, 0, 0]]

# these are the numbers that are to be randomised
occurrence = [2, 2, 2, 2, 2, 2, 2, 2, 2, 4]

score = 0
game_is_over = True
the_same_counter = 0
zero_counter = 0

# declaring the turtles that are used
number_writer = turtle.Turtle()
score_writer = turtle.Turtle()
game_over = turtle.Turtle()
game_over.hideturtle()
screen = turtle.Screen()
screen.colormode(255)
screen.setup(width=1.0, height=1.0, startx=None, starty=None)
turtle.tracer(0, 0)


# this draws the gaming board
def board_drawer():
    drawer = turtle.Turtle()
    drawer.hideturtle()
    drawer.speed(1000)
    drawer.penup()
    drawer.setposition(-250, 250)
    drawer.pendown()
    for i in range(4):
        for j in range(4):
            drawer.forward(100)
            drawer.right(90)
            drawer.forward(100)
            drawer.right(90)
            drawer.forward(100)
            drawer.right(90)
            drawer.forward(100)
            drawer.right(90)
            drawer.penup()
            drawer.forward(130)
            drawer.pendown()
        drawer.penup()
        drawer.right(180)
        drawer.forward(520)
        drawer.left(90)
        drawer.forward(130)
        drawer.left(90)
        drawer.pendown()


# randomizes between 2 and 4 and puts the number at a random place in the 2d list
def random_number():
    global zero_counter
    zero_counter = 0
    for i in range(4):
        zero_counter = zero_counter + the_array[i].count(0)
    if zero_counter != 0:
        while True:
            r = random.randrange(4)
            t = random.randrange(4)
            if the_array[r][t] == 0:
                the_array[r].remove(0)
                the_array[r].insert(t, random.choice(occurrence))
                break


# removes the zeros so that the numbers are swapped in the same direction
# if index==3, then that means the movement has to be towards left
# if index==0, then that means the movement has to be towards right
def remove_zeros(array, index):
    if index == 3:
        for i in range(0, 4):
            for j in array[i]:
                if j == 0:
                    array[i].remove(0)
                    array[i].insert(index, 0)
    if index == 0:
        for i in range(0, 4):
            for j in range(len(the_array[i])):
                if array[i][-j - 1] == 0:
                    array[i].reverse()
                    array[i].remove(0)
                    array[i].insert(3, 0)
                    array[i].reverse()


# finds equal numbers and add them together
# the index indicates the position where zero is added, since on the addition one element of the list is reduced
# it also counts the score, depending on the numbers added
def add_equal_numbers(array, index, scores):
    global score
    global game_is_over, the_same_counter
    check_equality(array)

    if not game_is_over:
        if index == 3:
            for i in range(4):
                for j in range(len(the_array) - 1):
                    if array[i][j] == array[i][j + 1] and array[i][j] != 0:
                        score = scores + array[i][j] + array[i][j + 1]
                        array[i][j] = array[i][j] + array[i][j + 1]
                        array[i].pop(j + 1)
                        array[i].insert(3, 0)
        else:
            for i in range(4):
                for j in range(len(the_array) - 1):
                    if array[i][-j - 1] == array[i][-j - 2] and array[i][-j - 1] != 0:
                        score = scores + array[i][-j - 1] + array[i][-j - 2]
                        array[i][-j - 1] = array[i][-j - 1] + array[i][-j - 2]
                        array[i].pop(-j - 2)
                        array[i].insert(0, 0)


# transposes the required lists
# used when dealing with the up and down movements
def transpose():
    double_count_prevent = 0
    for i in range(4):
        for j in range(double_count_prevent, 4):
            the_array[i][j], the_array[j][i] = the_array[j][i], the_array[i][j]
        double_count_prevent += 1


# prints the numbers on the board
# depending on the value of the numbers, it also gives it color
def prints():
    m = 0
    score_writer.reset()
    score_writer.hideturtle()
    score_writer.penup()
    score_writer.setposition(-150, 250)
    score_writer.write("Score: ", font=("normal", 50, "normal"))
    score_writer.forward(200)
    score_writer.write(score, font=("normal", 50, "normal"))
    number_writer.reset()
    number_writer.hideturtle()
    number_writer.clear()
    number_writer.speed(0)
    number_writer.penup()
    number_writer.setposition(-250, 250)
    number_writer.pendown()
    for ij in range(4):
        n = 0
        for  ji in range(4):
            number_writer.begin_fill()
            number_writer.forward(100)
            number_writer.right(90)
            number_writer.forward(100)
            number_writer.right(90)
            number_writer.forward(100)
            number_writer.right(90)
            number_writer.forward(30)
            number_writer.right(90)
            number_writer.penup()
            number_writer.forward(10)
            if the_array[m][n] == 0:
                number_writer.pencolor("white")
            number_writer.write(the_array[m][n], font=("normal", 30, "normal"))
            if the_array[m][n] == 0:
                number_writer.pencolor("black")
                number_writer.fillcolor("white")
            elif the_array[m][n] < 16:
                number_writer.fillcolor(255, 255 - 8 * the_array[m][n], 155 - 5 * the_array[m][n])
            elif the_array[m][n] <= 64:
                number_writer.fillcolor(255, 150 - the_array[m][n], 150 - the_array[m][n])
            elif the_array[m][n] <= 512:
                if the_array[m][n] == 128:
                    number_writer.fillcolor(255, 255, 0)
                if the_array[m][n] == 256:
                    number_writer.fillcolor(255, 128, 0)
                if the_array[m][n] == 512:
                    number_writer.fillcolor(255, 0, 0)
            else:
                number_writer.fillcolor(0, 0, 255)
            number_writer.backward(10)
            number_writer.pendown()
            number_writer.left(90)
            number_writer.forward(70)
            number_writer.end_fill()
            number_writer.right(90)
            number_writer.penup()
            number_writer.forward(130)
            number_writer.pendown()
            n += 1
        number_writer.penup()
        number_writer.right(180)
        number_writer.forward(520)
        number_writer.left(90)
        number_writer.forward(130)
        number_writer.left(90)
        number_writer.pendown()
        m += 1

        '''if there are no zeros in the board and the consecutive numbers 
            are not equal, both horizontally and vertically, then that means it is a game over'''
        if zero_counter == 0 and game_is_over:
            game_over.reset()
            game_over.penup()
            game_over.setposition(-300, 0)
            game_over.pencolor("red")
            game_over.write("game over", font=("normal", 100, "normal"))


# checks the equality of the consecutive numbers both horizontally and vertically
def check_equality(array):
    global game_is_over
    game_is_over = True
    for g in range(4):
        for h in range(3):
            if array[g][h] == array[g][h + 1] and array[g][h] != 0:
                game_is_over = False
    transpose()
    for p in range(4):
        for q in range(3):
            if array[p][q] == array[p][q + 1] and array[p][q] != 0:
                game_is_over = False
    transpose()


# called when the player hits the Right key
def right():
    remove_zeros(the_array, 0)
    add_equal_numbers(the_array, 0, score)
    random_number()
    prints()


# called when the player hits the Left key
def left():
    remove_zeros(the_array, 3)
    add_equal_numbers(the_array, 3, score)
    random_number()
    prints()


# called when the player hits the Up key
def up():
    transpose()
    remove_zeros(the_array, 3)
    add_equal_numbers(the_array, 3, score)
    transpose()
    random_number()
    prints()


# called when the player hits the Down key
def down():
    transpose()
    remove_zeros(the_array, 0)
    add_equal_numbers(the_array, 0, score)
    transpose()
    random_number()
    prints()


# setting up the initial condition
board_drawer()
random_number()
prints()

# takes the Key values and calls the corresponding function
screen.onkey(right, 'Right')
screen.onkey(left, "Left")
screen.onkey(up, "Up")
screen.onkey(down, "Down")
screen.listen()

turtle.update()
turtle.done()