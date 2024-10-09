########################################
# Name: Sophie Avery
# Collaborators:
# Estimate time spent (hrs): 1.5
########################################

from pgl import GWindow, GRect, GLabel
from random import randint

debugging = False                           # Toggles debugging print statements

GW_WIDTH = 600                              # Width of window
GW_HEIGHT = 600                             # Height of window
SQUARE_SIZE = 50                            # Width and height of square
SCORE_DX = 10                               # Distance from left of window to origin
SCORE_DY = 10                               # Distance up from bottom of window to baseline
SCORE_FONT = "bold 40pt 'serif'"            # Font for score

box_x = GW_WIDTH // 2 - SQUARE_SIZE // 2    # The starting location of the box (x and y coordinates)
box_y = GW_HEIGHT // 2 - SQUARE_SIZE // 2

def clicky_box(): # The main function that contains everything

    def on_mouse_down(event): # What happens when the mouse is clicked
        global box_x, box_y # Makes box_x and box_y editable inside this function

        mouse_x = event.get_x() # Retrieves the x and y coordinates of the mouse
        mouse_y = event.get_y()

        debugging and print("mouse x is", mouse_x, "mouse y is", mouse_y)

        coords_x = [] # Stores the coordinates that the box contains
        coords_y = []

        for i in range(SQUARE_SIZE): # Adds every coordinate inside the box to the storing lists
            coords_x.append(i + box_x)
            coords_y.append(i + box_y)

        debugging and print("coords_x =", coords_x)
        debugging and print("coords_y =", coords_y)
        debugging and print("box x is", box_x, "box y is", box_y)

        if mouse_x in coords_x and mouse_y in coords_y:
            gw.score.set_label(str(int(gw.score.get_label()) + 1)) # Retrieves the score, turns it into an integer, adds one, and turns it back into a string
            box_x = randint(0, GW_WIDTH - SQUARE_SIZE) # Sets the boxes next location to a random integer inside the graphics window
            box_y = randint(0, GW_HEIGHT - SQUARE_SIZE)
            gw.box.set_location(box_x,box_y)
        else:
            gw.score.set_label("0") #If the click wasn't inside the box, resets the score

    gw = GWindow(GW_WIDTH, GW_HEIGHT) # Defines the graphics window
    gw.add_event_listener("click", on_mouse_down) # Runs on_mouse_down when the mouse is clicked

    def make_square(x:int,y:int): # Makes a square at location (x, y)
        square = GRect(x,y,SQUARE_SIZE,SQUARE_SIZE)
        square.set_color("darkred")
        square.set_filled(True)
        gw.add(square)
        return square # Returns the square for later use

    def make_label(text:str, x:int, y:int): # Creates a label that displays "text" at coordinates (x, y)
        label = GLabel(text, x, y)
        label.set_font(SCORE_FONT)
        gw.add(label)
        return label # Returns the label for later use

    gw.box = make_square(GW_WIDTH // 2 - SQUARE_SIZE // 2, GW_HEIGHT // 2 - SQUARE_SIZE // 2) # Creates the initial square and stores it for later modification
    gw.score = make_label("0",SCORE_DX, GW_HEIGHT - SCORE_DY) #Creates the scoreboard, sets it to zero, and stores it for later use

if __name__ == '__main__':
    clicky_box()
