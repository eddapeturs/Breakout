from OpenGL.GL import *
from OpenGL.GLU import *
from math import *

class Paddle:
    def __init__(self, screen_width, screen_height, width, height):
        self.width = width
        self.height = height
        self.screen_width = screen_width
        self.x = (screen_width / 2) - (width / 2)
        self.y = screen_height / 20

        self.color = (0.2, 0.0, 0.0)
        self.mov_speed = 10
        self.going_left = False
        self.going_right = False

        self.right_x = self.x + self.width
        self.center_x = self.x + self.width/2
        self.top_y = self.y + self.height
        self.type = 'paddle'

        normal_x = self.x - self.right_x
        normal_y = self.y - self.top_y
        normal_len = sqrt(normal_x**2 + normal_y**2)
        self.normal = [(normal_x/normal_len), (normal_y/normal_len)]
        self.DEG2RAD = 3.14159/180


    def move_paddle(self):
        if(self.x >= (self.screen_width - self.width)):
            self.x = self.screen_width - self.width
            self.going_right = False
        if(self.x <= 0):
            self.x = 0
            self.going_left = False    
        if self.going_left:
            self.x -= self.mov_speed
        if self.going_right:
            self.x += self.mov_speed

        normal_x = self.x - self.right_x
        normal_y = self.y - self.top_y
        normal_len = sqrt(normal_x**2 + normal_y**2)
        self.normal = [-(normal_y/normal_len), (normal_x/normal_len)]

    def draw_paddle(self):
        self.right_x = self.x + self.width
        self.top_y = self.y + self.height
        self.center_x = self.x + self.width/2

        glBegin(GL_QUADS)                                           # start drawing a rectangle
        glColor3f(0.5, 0.5, 1.0)                                    # set color
        glVertex2f(self.x, self.y)                                  # bottom left point
        glVertex2f(self.right_x, self.y)                            # bottom right point
        glVertex2f(self.right_x, self.top_y)                        # top right point
        glVertex2f(self.x, self.top_y)                              # top left point
        glEnd()

        # glBegin(GL_TRIANGLE_FAN)
        # glColor3f(1.0, 1.0, 1.0) # set color
        # x = self.x + self.width/2
        # for i in range(180):
        #     degInRad = float(i*self.DEG2RAD)
        #     glVertex2f(cos(degInRad)*self.width/2 + x,sin(degInRad)*self.height*2 + self.y)
        # glEnd()