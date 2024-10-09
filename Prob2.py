########################################
# Name:
# Collaborators:
# Estimated time spent (hrs):
########################################

from pgl import GWindow, GRect

WIDTH = 400 #window width
HEIGHT = 400 #window height
BRICK_WIDTH = 40
BRICK_HEIGHT = 20
BRICKS_IN_BASE = 5

def draw_pyramid():
    """ 
    Draws a pyramid of bricks centered on the screen with a height of BRICKS_IN_BASE. 
    """

    gw = GWindow(WIDTH, HEIGHT) #sets up the graphics window
    def make_brick(x:int, y:int): #the function to make a brick at coordinates (x,y)
        rect = GRect(x, y, BRICK_WIDTH, BRICK_HEIGHT) # make a brick of BRICK_WIDTH x BRICK_HEIGHT at (x,y)
        rect.set_line_width(2) #makes the line width 2
        gw.add(rect) #actually adds the rectangle

    center_x = WIDTH // 2 #calculates the center of the window (x and y coordinates)
    center_y = HEIGHT // 2
    corner_x = center_x - ((BRICKS_IN_BASE * BRICK_WIDTH) // 2) #calculates the coordinates of the first brick (x and y)
    corner_y = center_y + (((BRICKS_IN_BASE * BRICK_HEIGHT) // 2) - BRICK_HEIGHT)
    row = 0
    for row_num in range(BRICKS_IN_BASE):
        for brick_num in range(BRICKS_IN_BASE - row):
            make_brick(corner_x, corner_y)
            corner_x += BRICK_WIDTH
        corner_y -= BRICK_HEIGHT #brings the y coordinate up by one brick
        row += 1
        corner_x = (center_x - ((BRICKS_IN_BASE * BRICK_WIDTH) // 2)) + ((BRICK_WIDTH // 2) * row) #resets the x coordinate of the brick to the proper location


if __name__ == '__main__':
    draw_pyramid()
