import pygame
from pygame.locals import *

from OpenGL.GL import *
from OpenGL.GLUT import *
from OpenGL.GLU import *
# from freetype import *

# from OpenGL.GL import *
# from OpenGL.GLU import *

# from math import cos, sin

import random

from Ball import *
from Paddle import *
from BaseObjects import *
from Tile import *
from Hearts import *
# from random import *

# Screen attributes
screen_width = 800
screen_height = 800

clock = None
# delta_time = None

paddle = Paddle(screen_width, screen_height, 150, 20)
ball = Ball(Point(200, 100), Vector(2, 6))
hearts = Hearts(Point(650, 780))
tiles = []
# tile = Tile(10, 10)
title = "Hello"

colors = [
    [1.0, 0.0, 0.0], # Red
    [1.0, 0.5, 0.0], # Orange
    [1.0, 1.0, 0.0], # Yellow
    [0.0, 1.0, 0.0], # Green
    [0.0, 0.0, 1.0], # Blue
    [1.0, 0.0, 1.0]  # Cyan
]

def init_game():
    global screen_height, screen_width, clock, tiles
    clock = pygame.time.Clock()
    pygame.display.init()
    pygame.display.set_mode((screen_width, screen_height), DOUBLEBUF|OPENGL)
    glClearColor(0.0, 0.0, 0.0, 0.0)
    clock.tick()

    columns = 10
    rows = 8
    no_of_paddings = columns - 1
    padding_left = 20
    padding_right = 20
    padding_between = 5

    # tile_color = 

    tile_width = (screen_width - (no_of_paddings * padding_between) - padding_left - padding_right) / columns
    tile_height = 30

    tile_x_pos = padding_left
    tile_y_pos = screen_height - 80
    for i in range (0, rows):
        tile_color = colors[i % len(colors)]
        for j in range (0, columns):
            tile = Tile(tile_x_pos, tile_y_pos, tile_width, tile_height, tile_color)
            tiles.append(tile) 
            tile_x_pos += tile.width + padding_between
        tile_y_pos -= tile_height + padding_between
        tile_x_pos = padding_right


def update():
    delta_time = clock.tick()/1000.0
    paddle.move_paddle()
    ball.update(delta_time)

    if ball.position.y < 100:
        ball.checkCollision(paddle, delta_time)

    for tile in tiles:
        # print("drawing tile")
        if(ball.checkCollision(tile, delta_time)):
            tiles.remove(tile)
    

def display():
    global paddle, ball, tile, delta_time


    # glClear( GL_COLOR_BUFFER_BIT | GL_DEPTH_BUFFER_BIT )
    # glMatrixMode(GL_PROJECTION)
    # glLoadIdentity()
    # gluOrtho2D(0.0, 1.0, 0.0, 1.0)
    # glMatrixMode(GL_MODELVIEW)
    # glColor3f(1,1,1)
    # glRasterPos2f(100,100)

    # # glut_print( 10 , 10 , GLUT_BITMAP_9_BY_15 , "Hallo World" , 1.0 , 1.0 , 1.0 , 1.0 )
    # text = "Hello hallo hallo hallo "
    # for ch in text :
    #     glutBitmapCharacter( GLUT_BITMAP_8_BY_13 , ctypes.c_int( ord(ch) ) )
    # glutSwapBuffers()



    # delta_time = clock.tick()/1000.0
    vp_width = int(screen_width/2)
    vp_height = int(screen_height/2)

    glClear(GL_COLOR_BUFFER_BIT)
    glMatrixMode(GL_PROJECTION)
    glLoadIdentity()
    glMatrixMode(GL_MODELVIEW)
    glLoadIdentity()
    glViewport(0,0,screen_width,screen_height)
    # glViewport(0,0,vp_width,vp_height)
    gluOrtho2D(0, 800, 0, 800)
    
    paddle.draw_paddle()
    # ball.update(delta_time)
    ball.display()
    hearts.display()

    for tile in tiles:
        # print("drawing tile")
        # if(ball.checkCollision(tile)):
            # tiles.remove(tile, delta_time)
        tile.draw_tile()

    pygame.display.flip()

    # for i in title:
    #     glutBitmapCharacter(GLUT_BITMAP_TIMES_ROMAN_24,i)

def game_loop():
    global paddle
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            quit()
        elif event.type == pygame.KEYDOWN:
            if event.key == K_ESCAPE:
                pygame.quit()
                quit()
            elif event.key == K_LEFT:
                paddle.going_left = True
            elif event.key == K_RIGHT:
                paddle.going_right = True            
        elif event.type == pygame.KEYUP:
            if event.key == K_LEFT:
                paddle.going_left = False
            elif event.key == K_RIGHT:
                paddle.going_right = False

    update()
    display()

if __name__ == "__main__":
    init_game()
    while True:
        game_loop()
