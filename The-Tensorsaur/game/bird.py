import pyglet, random
from pyglet import image
from ground import Ground
import gameboard
'''
Created on Dec 24, 2018

@author: wtmul
'''

class Bird(pyglet.sprite.Sprite):

    def __init__(self):
        super().__init__(img=image.load_animation('sprites/birdomation.gif', None, None))
        self.x = gameboard.window.width
        #70 for hits, 100 for no need to duck (will not have low jumps for birds)
        rand = random.randint(1, 3)
        if rand == 1:
            self.y = 100
        else:
            self.y = 65
        self.velocity_x = 0.0
        
    def update(self, dt):
        self.velocity_x = Ground.current_ground_speed
        self.x += self.velocity_x * dt
        if self.x + self.width <= 0:
            self.delete()
            gameboard.game_objects.remove(self)