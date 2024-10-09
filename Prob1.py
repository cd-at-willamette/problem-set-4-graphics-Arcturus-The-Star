############################################################
# Name:
# Name(s) of anyone worked with:
# Est time spent (hr):
############################################################

from pgl import GWindow, GRect, GOval, GLine, GLabel

# Setting up initial window dimensions. 
# You can change these if you want. They are in number of pixels.
WIDTH = 600
HEIGHT = 600

def draw_image():
    """ Creates a window and draws a student's creation"""

    # Creating the window
    gw = GWindow(WIDTH, HEIGHT)
    
    # And now it is your turn! Add your code below! Make sure you meet all the requirements!
    def make_rect(x,y,w,h,color):
        rect = GRect(x,y,w,h)
        rect.set_color(color)
        rect.set_filled(True)
        gw.add(rect)
    def make_oval(x,y,w,h,color):
        oval = GOval(x,y,w,h)
        oval.set_color(color)
        oval.set_filled(True)
        gw.add(oval)
    def make_line(x0,y0,x1,y1,thickness,color):
        line = GLine(x0,y0,x1,y1)
        line.set_line_width(thickness)
        line.set_color(color)
        gw.add(line)
    def make_label(text,x,y,color):
        label = GLabel(text,x,y)
        label.set_color(color)
        gw.add(label)
    make_rect(0,0,600,600, "Orange")
    make_rect(100, 100, 300,300,"Red")
    make_oval(100,100,300,300,"Blue")
    make_line(100,100,250,250,5,"Green")
    make_label("gleep glorp", 240, 240, "Red")
    make_label("gleep glorp", 250, 255, "Red")
    make_label("gleep glorp", 240, 270, "Red")
    make_line(100,400,100,100,5,"Green")
    make_line(100,400,250,250,5,"Green")
    make_oval(120,225,50,50,"Yellow")
    make_oval(500,500,50,50,"Purple")
    make_rect(508,508,35,35,"Orange")
    make_line(399,399,508,508,6,"Brown")

if __name__ == '__main__':
    draw_image()
