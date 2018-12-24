import pyglet
import gameboard
'''
Created on Dec 24, 2018

@author: wtmul
'''

class Lose(pyglet.sprite.Sprite):

    def __init__(self):
        super().__init__(img=pyglet.image.load('sprites/gameOver.png'))
        self.x = (gameboard.window.width/5 - 100)
        self.y = (gameboard.window.height/5)
        self.opacity = 0