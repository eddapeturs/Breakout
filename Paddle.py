from OpenGL.GL import *
from OpenGL.GLU import *

class Paddle:
    def __init__(self, screen_width, screen_height, width, height):
        self.width = width
        self.height = height
        self.screen_width = screen_width
        self.x = (screen_width / 2) - (width / 2)
        self.y = screen_height / 20

        self.color = (0.2, 0.0, 0.0)
        self.mov_speed = 5
        self.going_left = False
        self.going_right = False

        self.top_right_x = self.x + self.width
        self.top_right_y = self.y + self.height
        self.top_left_y = self.y + height
        self.type = 'paddle'


    def move_paddle(self):
        if(self.x == (self.screen_width - self.width)):
            self.going_right = False
        if(self.x == 0):
            self.going_left = False    
        if self.going_left:
            self.x -= self.mov_speed
        if self.going_right:
            self.x += self.mov_speed

    def draw_paddle(self):
        self.right_x = self.x + self.width
        self.top_y = self.y + self.height

        glBegin(GL_QUADS)                                           # start drawing a rectangle
        glColor3f(0.5, 0.5, 1.0)                                    # set color
        glVertex2f(self.x, self.y)                                  # bottom left point
        glVertex2f(self.right_x, self.y)                            # bottom right point
        glVertex2f(self.right_x, self.top_y)                        # top right point
        glVertex2f(self.x, self.top_y)                              # top left point
        glEnd() 
