from __future__ import print_function
import os
if os.name == "nt":
    import msvcrt
    import colorama
    colorama.init()
else:
    import sys
    import select
    import tty
    import termios
import threading
import time
import random
import maps

osName = os.name
clearCommand = 'cls' if osName == 'nt' else 'clear'


# Clear the screen (works on both windows and linux)
def clear():
    os.system(clearCommand)


# The INITIAL map - this is converted into a gameMapList list at the start
# Do NOT edit this during the game execution, edit gameMapList instead
gameMap = """
############################################################
#                                                          #
#                                                          #
#                                                          #
#                                                          #
#                                                          #
#                                                          #
#                                                          #
#                                                          #
#                                                          #
#                                                          #
#                                                          #
#                                                          #
#                                                          #
#                                                          #
#                                                          #
#                                                          #
#                                                          #
#                                                          #
############################################################
"""

# Scan the maps.py file
def fetch_maps():
    running = True
    count = 1
    output = ["0) Default"]
    while running:
        try:
            exec("output.append(str(count) + \") \" + maps.map" + str(count) + "[0])")
            count += 1
        except AttributeError:
            running = False
    return output

# Get the user's input to choose a map
print(*fetch_maps(), sep="\n")
maps_prompt_input = input("> ")

# Select the map according to the user's input
if maps_prompt_input != 0 and maps_prompt_input.strip() != "":
    exec("gameMap = maps.map" + maps_prompt_input + "[1]")

mapX = gameMap.split("\n")[1].__len__()  # Get the lenght of the map
mapY = gameMap.split("\n").__len__() - 2  # Get the height of the map

# Convert gameMap to a list so we can manipulate it
gameMapList = list(gameMap)


# Clear the screen and print the stuff contained in gameMapList
def update_map():
    global gameMap
    global gameMapList

    gameMap = ''.join(gameMapList)
    clear()
    print(gameMap)


# Change an element in the list gameMapList at (x, y) -> index
# Note that this doesn't call the update_map() function
def change_char_at(char, x, y):
    global gameMapList
    global mapX

    gameMapList[(mapX * (y - 1) + x) + y - 1] = char


# This is executed in a thread to get the user's input
# without stopping the program
def unix_input_key_pressed():
    return select.select([sys.stdin], [], [], 0) == ([sys.stdin], [], [])


def unix_input_read_key():
    return sys.stdin.read(1)


def unix_input_restore_settings():
    termios.tcsetattr(sys.stdin, termios.TCSADRAIN, old_settings)


if osName != "nt":
    old_settings = termios.tcgetattr(sys.stdin)

    tty.setcbreak(sys.stdin.fileno())


def input_listener():
    global currentInput
    while True:
        if osName == 'nt':
            currentInput = msvcrt.getch().decode("utf-8").lower()
        elif unix_input_key_pressed():
            currentInput = unix_input_read_key().lower()


# The snake/player class
class Snake:
    def __init__(self, x, y, head, body):
        global mapX
        global mapY
        global apple

        self.going = "d"
        self.x = x
        self.y = y
        self.positions = []

        self.eatenApples = 1
        self.dead = False

        self.head = head
        self.body = body

        self.loopCount = 0

    def die(self):
        self.dead = True
        print("\u001b[31mYOU DIED\u001b[0m")
        if osName != "nt":
            unix_input_restore_settings()
        input()
        exit()

    # Main method
    def update(self):
        def change_dir():
            global currentInput
            if currentInput == "d":
                if self.going != "a":
                    self.going = "d"
                    self.x += 1
                else:
                    currentInput = self.going
                    self.x -= 1

            elif currentInput == "a":
                if self.going != "d":
                    self.going = "a"
                    self.x -= 1
                else:
                    currentInput = self.going
                    self.x += 1

            elif currentInput == "w":
                if self.going != "s":
                    self.going = "w"
                    self.y -= 1
                else:
                    currentInput = self.going
                    self.y += 1

            elif currentInput == "s":
                if self.going != "w":
                    self.going = "s"
                    self.y += 1
                else:
                    currentInput = self.going
                    self.y -= 1
            else:
                currentInput = self.going
                change_dir()

        if self.x == 1 or self.x == mapX or self.y == 1 or self.y == mapY or (self.x, self.y) in self.positions:
            self.die()

        self.positions.append((self.x, self.y))
        if self.positions.__len__() > self.eatenApples:
            self.positions.pop(0)

        if self.x == apple.x and self.y == apple.y:
            self.eatenApples += 1
            apple.eaten = True

        if not self.dead:
            change_dir()
        self.render()
    ##################################################

    # Update gameMapList so, later, it can be displayed
    def render(self):
        for n, i in enumerate(gameMapList):
            if i == self.body:
                gameMapList[n] = " "

        for i in self.positions:
            change_char_at(self.body, i[0], i[1])

        change_char_at(self.head, self.x, self.y)


# The apple class
class Apple:
    def __init__(self, char):
        global mapX
        global mapY
        global snake
        self.char = char
        self.x = 1
        self.y = 1
        self.eaten = True

    def spawn(self):
        if self.eaten:
            self.x = random.randint(2, mapX - 1)
            self.y = random.randint(2, mapY - 1)

            if (self.x, self.y) not in snake.positions:
                change_char_at(self.char, self.x, self.y)
                self.eaten = False
            else:
                # print("ahah found")
                self.spawn()  # I know, I know, I shouldn't be doing this lol


# Get the user's input without stopping the program
currentInput = "d"
inputListener = threading.Thread(target=input_listener)
inputListener.daemon = True
inputListener.start()

# Game objects
GapBetweenFrames = 0.15
snake = Snake(4, 10, "\u001b[32m@\u001b[0m", "\u001b[32mo\u001b[0m")
apple = Apple("\u001b[31mX\u001b[0m")

# Start the game
clear()
print("Move with \u001b[36mWASD\u001b[0m")
print(4)
time.sleep(1)
print(3)
time.sleep(1)
print(2)
time.sleep(1)
print(1)
time.sleep(1)

previous_time = time.time()
dt = 0
# Game loop
while not snake.dead:
    time.sleep(GapBetweenFrames)
    snake.update()
    apple.spawn()
    update_map()

    print("Score: " + str(snake.eatenApples - 1))

    dt = time.time() - previous_time
    previous_time = time.time()

    # Debug
    print("Delta time: " + str(dt))
