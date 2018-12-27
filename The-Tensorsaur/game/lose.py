import pyglet
import gameboard
'''
Created on Dec 24, 2018

@author: wtmuller, cpendery
'''

class Lose(pyglet.sprite.Sprite):

    def __init__(self):
        super().__init__(img=pyglet.image.load('sprites/gameOver.png'))
        self.x = (gameboard.window.width/2 - 200)
        self.y = (gameboard.window.height - 100)
        self.opacity = 0