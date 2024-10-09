########################################
# Name: Sophie Avery
# Collaborators:
# Estimated time spent (hrs): 1
########################################

from pgl import GWindow, GRect

WIDTH = 400             # The width of the graphics window
HEIGHT = 400            # The height of the graphics window
BRICK_WIDTH = 40        # The width of the bricks
BRICK_HEIGHT = 20       # The height of the bricks
BRICKS_IN_BASE = 6      # The number of bricks in the base of the pyramid

def draw_pyramid():
    """ 
    Draws a pyramid of bricks centered on the screen with a height of BRICKS_IN_BASE. 
    """

    gw = GWindow(WIDTH, HEIGHT) # Sets up the graphics window
    
    def make_brick(x:int, y:int): # Makes a brick at coordinates (x,y)
        rect = GRect(x, y, BRICK_WIDTH, BRICK_HEIGHT) # Makes a brick of BRICK_WIDTH x BRICK_HEIGHT at (x,y)
        rect.set_line_width(2)
        gw.add(rect)

    center_x = WIDTH // 2 # Calculates the center of the window (x and y coordinates)
    center_y = HEIGHT // 2
    
    corner_x = center_x - ((BRICKS_IN_BASE * BRICK_WIDTH) // 2) # Calculates the coordinates of the first brick (x and y)
    corner_y = center_y + (((BRICKS_IN_BASE * BRICK_HEIGHT) // 2) - BRICK_HEIGHT)
    
    row = 0 # Tracks the row being created
    
    for row_num in range(BRICKS_IN_BASE): # Creates the pyramid, looping through one row at a time
        
        for brick_num in range(BRICKS_IN_BASE - row): # Creates a row of bricks, length dependent on the current row
            make_brick(corner_x, corner_y)
            corner_x += BRICK_WIDTH
        
        corner_y -= BRICK_HEIGHT # Brings the y coordinate up by one brick
        row += 1
        corner_x = (center_x - ((BRICKS_IN_BASE * BRICK_WIDTH) // 2)) + ((BRICK_WIDTH // 2) * row) # Resets the x coordinate of the brick to the proper location


if __name__ == '__main__':
    draw_pyramid()
