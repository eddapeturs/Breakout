from OpenGL.GL import *
from OpenGL.GLU import *
from math import cos, sin, pi
from BaseObjects import *


class Ball:
    def __init__(self, position, direction):
        self.position = position            # point
        self.direction = direction          # vector
        self.speed = 30
        self.radius = 10
        self.DEG2RAD = 3.14159/180
        # self.angle = -90


    def update(self, delta_time):
        if(self.position.x <= 0 + self.radius):
            # self.position.x = 1
            self.direction.x = -self.direction.x
        if(self.position.x >= 800 - self.radius):
            # self.position.x = 799
            self.direction.x = -self.direction.x
        if(self.position.y >= 800 - self.radius):
            # self.position.y = 799
            self.direction.y = -self.direction.y
        self.position.x += self.direction.x * delta_time * self.speed
        self.position.y += self.direction.y * delta_time * self.speed

    def display(self):
        # print("self.position.x", self.position.x)
        # print("self.position.y", self.position.y)
        glPushMatrix()
        # glTranslate(self.position.x, self.position.y, 0)

        glBegin(GL_TRIANGLE_FAN)
        glColor3f(1.0, 1.0, 1.0) # set color
        for i in range(360):
            degInRad = float(i*self.DEG2RAD)
            glVertex2f(cos(degInRad)*self.radius + self.position.x,sin(degInRad)*self.radius + self.position.y)
        glEnd()

        glPopMatrix()

    def checkCollision(self, otherObject, delta_time):
        right_x = otherObject.x + otherObject.width
        upper_y = otherObject.y + otherObject.height

        # Add or subtract radius depending on the side of impact
        own_y = self.direction.y
        own_x = self.direction.x

        if self.direction.y < 0: # going down
            own_y = self.position.y - self.radius
        if self.direction.y > 0: # going up
            own_y = self.position.y + self.radius
        if self.direction.x < 0: # going left
            own_x = self.position.x - self.radius
        if self.direction.x > 0: # going right
            own_x = self.position.x + self.radius


        # Rather than doing this, I should find the point of collision from last delta time and calculate from there
        if (otherObject.x < own_x < right_x and otherObject.y < own_y < upper_y):
            x = self.position.x - ( self.direction.x / self.speed / delta_time ) # Last x bf collision
            y = self.position.y - ( self.direction.y / self.speed / delta_time ) # Last y bf collision

            print("------- Last point before collision -------")
            print("x: ", x)
            print("y: ", y)
            print("------- After collision -------")
            print("x: ", self.position.x)
            print("y: ", self.position.y)
            print("------- other.object -------")
            print("1x: ", otherObject.x)
            print("2x: ", right_x)
            print("1y: ", otherObject.y)
            print("2y: ", upper_y)



            self.direction.y = -self.direction.y

            # 𝑟=𝑑−2(𝑑⋅𝑛)𝑛
            # dot_d_n = (self.direction.x * normal[0] + self.direction.y * normal[1]) * 2
            # r_x = self.direction.x - dot_d_n * normal[0]
            # r_y = self.direction.y - dot_d_n * normal[1]
            # self.direction.x = r_x
            # self.direction.y = r_y

            # dot_d_n = (self.direction.x * normal[0] + self.direction.y * normal[1]) * 2
            # self.direction.x -= dot_d_n * normal[0]
            # self.direction.y -= dot_d_n * normal[1]

            print("Direction x: ", self.direction.x)
            print("Direction y: ", self.direction.y)
            
            
            # self.direction = Vector2.Reflect(self.direction, new Vector2(0, -1))


            if otherObject.type == "tile":
                # otherObject.hide = True
                return True
            print("self.position.x", round(float(self.position.x), 2))
            print("self.position.y", round(float(self.position.y), 2))
            # print("collision")
    