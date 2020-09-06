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


class Breakout():
    def __init__(self):
        # Screen attributes
        self.screen_width = 800
        self.screen_height = 800
        self.level = 0
        self.max_level = 3
        self.clock = pygame.time.Clock()
        self.hearts = Hearts(Point(650, 780))
        self.game_won = False
        self.game_lost = False

        pygame.display.init()
        pygame.display.set_caption('Breakout')
        pygame.display.set_mode((self.screen_width, self.screen_height), DOUBLEBUF|OPENGL)

        glClearColor(0.0, 0.0, 0.0, 0.0)

        pygame.mixer.init(44100, -16, 2, 64)
        self.tile_sound = pygame.mixer.Sound('assets/cymbal.wav')

        self.restart()

    
    def restart(self):
        paddle_width = 170 - (self.level * 20)
        self.paddle = Paddle(self.screen_width, self.screen_height, paddle_width, 20)
        self.ball = Ball(Point(200, 100), Vector(2, 6))
        # self.hearts = Hearts(Point(650, 780))
        self.tiles = []

        self.colors = [
            [1.0, 0.0, 0.0], # Red
            [1.0, 0.5, 0.0], # Orange
            [1.0, 1.0, 0.0], # Yellow
            [0.0, 1.0, 0.0], # Green
            [0.0, 0.0, 1.0], # Blue
            [1.0, 0.0, 1.0]  # Cyan
        ]

        self.init_tiles()
        self.level += 1

    def init_tiles(self):
        # columns = 5 + (self.level * 5)
        # rows = 4 + (self.level * 2)
        columns = 2
        rows = 1
        no_of_paddings = columns - 1
        padding_left = 20
        padding_right = 20
        padding_between = 5

        tile_width = (self.screen_width - (no_of_paddings * padding_between) - padding_left - padding_right) / columns
        tile_height = 30

        tile_x_pos = padding_left
        tile_y_pos = self.screen_height - 80
        for i in range (0, rows):
            tile_color = self.colors[i % len(self.colors)]
            for j in range (0, columns):
                tile = Tile(tile_x_pos, tile_y_pos, tile_width, tile_height, tile_color)
                self.tiles.append(tile) 
                tile_x_pos += tile.width + padding_between
            tile_y_pos -= tile_height + padding_between
            tile_x_pos = padding_right
        

    def update(self):
        self.delta_time = self.clock.tick()/1000.0
        self.paddle.move_paddle()
        self.ball.update(self.delta_time)

        if self.ball.position.y < 100:
            self.ball.check_collision(self.paddle, self.delta_time)
            if(self.ball.check_loss()):
                # remove a life & make a new ball
                self.hearts.remove_life()
                if self.hearts.lives == 0:
                    self.game_lost = True
                self.ball = Ball(Point(200, 100), Vector(2, 6))


        for tile in self.tiles:
            if(self.ball.check_collision(tile, self.delta_time)):
                self.tile_sound.play()
                self.tiles.remove(tile)

        if self.tiles == []:
            if self.level == self.max_level:
                self.game_won = True
            else:
                self.restart()
        

    def display(self):
        vp_width = int(self.screen_width/2)
        vp_height = int(self.screen_height/2)

        glClear(GL_COLOR_BUFFER_BIT)
        glMatrixMode(GL_PROJECTION)
        glLoadIdentity()
        glMatrixMode(GL_MODELVIEW)
        glLoadIdentity()
        glViewport(0,0,self.screen_width,self.screen_height)
        gluOrtho2D(0, 800, 0, 800)
        
        self.paddle.draw_paddle()
        self.ball.display()
        self.hearts.display()

        for tile in self.tiles:
            tile.draw_tile()

        pygame.display.flip()

    def game_loop(self):
        # global paddle
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            elif event.type == pygame.KEYDOWN:
                if event.key == K_ESCAPE:
                    pygame.quit()
                    quit()
                elif event.key == K_LEFT:
                    self.paddle.going_left = True
                elif event.key == K_RIGHT:
                    self.paddle.going_right = True            
            elif event.type == pygame.KEYUP:
                if event.key == K_LEFT:
                    self.paddle.going_left = False
                elif event.key == K_RIGHT:
                    self.paddle.going_right = False

        if self.game_won or self.game_lost:        
            self.win_or_lose()
        else:
            self.update()
            self.display()

    def win_or_lose(self):
        if self.game_won:
            
        if self.game_lost:
            print("L")

if __name__ == "__main__":
    # init_game()
    game = Breakout()
    while True:
        game.game_loop()
