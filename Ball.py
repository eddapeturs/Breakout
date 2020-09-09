from OpenGL.GL import *
from OpenGL.GLU import *
from math import cos, sin, pi, sqrt
from BaseObjects import *


class Ball:
    def __init__(self, position, direction):
        self.position = position            # point
        self.direction = direction          # vector
        self.radius = 10
        self.DEG2RAD = 3.14159/180

    def update(self, delta_time):
        if(self.position.x <= 0 + self.radius):
            self.position.x = self.radius + 2               # Done to make sure ball doesn't get "trapped"
            self.direction.x = -self.direction.x
        if(self.position.x >= 800 - self.radius):
            self.position.x = 800 - (self.radius + 2)
            self.direction.x = -self.direction.x
        if(self.position.y >= 800 - self.radius):
            self.position.y = 800 - (self.radius + 2)
            self.direction.y = -self.direction.y
        self.position.x += self.direction.x * delta_time
        self.position.y += self.direction.y * delta_time

    def display(self):
        glPushMatrix()

        glBegin(GL_TRIANGLE_FAN)
        glColor3f(1.0, 1.0, 1.0) # set color
        for i in range(360):
            degInRad = float(i*self.DEG2RAD)
            glVertex2f(cos(degInRad)*self.radius + self.position.x,sin(degInRad)*self.radius + self.position.y)
        glEnd()

        glPopMatrix()

    def check_collision(self, otherObject, delta_time):
        right_x = otherObject.x + otherObject.width
        upper_y = otherObject.y + otherObject.height

        x = self.position.x
        y = self.position.y
                             
        if self.direction.y < 0: # going down
            y = self.position.y - self.radius
        if self.direction.y > 0: # going up
            y = self.position.y + self.radius
        if self.direction.x < 0: # going left
            x = self.position.x - self.radius
        if self.direction.x > 0: # going right
            x = self.position.x + self.radius

        if (otherObject.x < x < right_x and otherObject.y < y < upper_y):
            last_x = x - ( self.direction.x * delta_time ) # Last x bf collision
            last_y = y - ( self.direction.y * delta_time ) # Last y bf collision

            if self.direction.x < 0: # Right
                vec = (1, 0)
                p_hit = self.vector_helper(vec, last_x, last_y, otherObject.right_x, otherObject.top_y, delta_time)
                if p_hit and (vec[0]*(p_hit[0]-otherObject.right_x))+(vec[1]*(p_hit[1]-otherObject.top_y)) == 0:
                    self.reflect(vec)

            if self.direction.x > 0: # Left
                vec = (-1, 0)
                p_hit = self.vector_helper(vec, last_x, last_y, otherObject.x, otherObject.top_y, delta_time)
                if p_hit and (vec[0]*(p_hit[0]-otherObject.x))+(vec[1]*(p_hit[1]-otherObject.top_y)) == 0:
                    self.reflect(vec)
                    print("Left")
            if self.direction.y < 0: # Top
                vec = (0, 1)
                p_hit = self.vector_helper(vec, last_x, last_y, otherObject.right_x, otherObject.top_y, delta_time)
                if p_hit and (vec[0]*(p_hit[0]-otherObject.right_x))+(vec[1]*(p_hit[1]-otherObject.top_y)) == 0:
                    if otherObject.type == 'paddle':
                        x_hit = p_hit[0] - otherObject.center_x
                        normalized_x_hit = x_hit/(otherObject.width/2)
                        bounce_angle = pi/6 * normalized_x_hit
                        ballVx = sin(bounce_angle)
                        ballVy = cos(bounce_angle)
                        vec_len = sqrt(self.direction.x**2 + self.direction.y**2)
                        self.direction.x = ballVx * vec_len
                        self.direction.y = ballVy * vec_len
                    else:
                        self.reflect(vec)

            if self.direction.y > 0: # Bottom
                vec = (0, -1)
                p_hit = self.vector_helper(vec, last_x, last_y, otherObject.right_x, otherObject.y, delta_time)
                if p_hit and (vec[0]*(p_hit[0]-otherObject.right_x))+(vec[1]*(p_hit[1]-otherObject.y)) == 0:
                    self.reflect(vec)
                    print("Bottom")

            if otherObject.type == "tile":
                return True

    def vector_helper(self, vec, last_x, last_y, other_x, other_y, delta_time):
        B_A = (other_x - last_x, other_y - last_y)
        n_dot_BA = (vec[0] * B_A[0]) + (vec[1] * B_A[1])
        n_dot_c = (vec[0]*self.direction.x) + (vec[1]*self.direction.y)
        t_hit = n_dot_BA / n_dot_c
        if 0 < t_hit < delta_time:
            p_hit = (last_x + t_hit*self.direction.x, last_y + t_hit*self.direction.y)
            return p_hit
            # if (vec[0]*(p_hit[0]-other_x))+(vec[1]*(p_hit[1]-other_y)) == 0:
            #     return True

    def reflect(self, vec):
        a_dot_n = self.direction.x * vec[0] + self.direction.y * vec[1]
        r_x = self.direction.x - (2*a_dot_n*vec[0])
        r_y = self.direction.y - (2*a_dot_n*vec[1])
        self.direction.x = r_x
        self.direction.y = r_y

    
    def check_loss(self):
        if self.position.y < -200:
            return True
        