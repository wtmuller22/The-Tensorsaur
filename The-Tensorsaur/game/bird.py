import pyglet, random
from pyglet import image
from ground import Ground
import gameboard
'''
Created on Dec 24, 2018

@author: wtmuller, cpendery
'''

class Bird(pyglet.sprite.Sprite):

    bird_flapped = image.load('sprites/birdFlapped.png')
    bird_flapping = image.load_animation('sprites/birdomation.gif', None, None)

    def __init__(self):
        super().__init__(img=Bird.bird_flapping)
        self.x = gameboard.window.width
        #70 for hits, 100 for no need to duck (will not have low jumps for birds)
        rand = random.randint(1, 6)
        if rand == 1 or rand == 2:
            self.y = 100
        elif rand == 3 or rand == 4:
            self.y = 65
        else:
            self.y = 0
        self.velocity_x = 0.0
        
    def update(self, dt):
        self.velocity_x = Ground.current_ground_speed
        self.x += self.velocity_x * dt
        if self.x + self.width <= 0:
            self.delete()
            gameboard.game_objects.remove(self)