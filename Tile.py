from OpenGL.GL import *
from OpenGL.GLU import *

class Tile:
    def __init__(self, x, y, width, height, color=[1.0, 1.0, 1.0]):
        self.x = x
        self.y = y
        self.width = width
        self.height = height
        self.visible = True
        self.color = color
        self.type = 'tile'
        self.hide = False

    def draw_tile(self):
        # print("Drawing tile: (", self.
        # x,",", self.y, ")")
        if not self.hide:
            color1 = self.color[0]
            color2 = self.color[1]
            color3 = self.color[2]
            glBegin(GL_QUADS)                                                   # start drawing a rectangle
            glColor3f(color1, color2, color3)                                            # set color
            glVertex2f(self.x, self.y)                                      # bottom left point
            glVertex2f(self.x + self.width, self.y)                       # bottom right point
            glVertex2f(self.x + self.width, self.y + self.height)       # top right point
            glVertex2f(self.x, self.y + self.height)                      # top left point
            glEnd()
        if self.hide:
            self.x = -1000
            self.y = -1000
