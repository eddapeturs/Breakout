from OpenGL.GL import *
from OpenGL.GLU import *
from math import cos, sin, pi
from BaseObjects import *


class Hearts:
    def __init__(self, position):
        self.position = position            # First circle x, y
        self.radius = 8
        self.DEG2RAD = 3.14159/180
        self.lives = 3
        # self.angle = -90


    def display(self):
        glPushMatrix()
        # glTranslate(self.position.x, self.position.y, 0)
        x = self.position.x
        y = self.position.y
        for i in range(0, self.lives):
            glBegin(GL_TRIANGLE_FAN)
            glColor3f(1.0, 1.0, 1.0) # set color
            for i in range(360):
                degInRad = float(i*self.DEG2RAD)
                glVertex2f(cos(degInRad)*self.radius + x,sin(degInRad)*self.radius + y)
            for i in range(360):
                degInRad = float(i*self.DEG2RAD)
                glVertex2f(cos(degInRad)*self.radius + x + self.radius * 2,sin(degInRad)*self.radius + y)
            glEnd()


            glBegin(GL_QUADS)
            glColor3f(1.0, 1.0, 1.0)
            glVertex2f(x-self.radius, y - 4)                                      
            glVertex2f(x + self.radius, y - self.radius*2 - 4) 
            glVertex2f(x + self.radius * 3, y - 4) 
            glVertex2f(x + self.radius, y+4)
            glEnd()

            x = x + self.radius * 5
        # x = x * self.radius * 5

        glPopMatrix()

    def remove_life(self):
        self.lives -= 1
        if self.lives == 0:
            return "game over"