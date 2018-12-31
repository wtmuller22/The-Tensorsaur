import pyglet, gameboard, random
from pyglet import image
from ground import Ground
'''
Created on Dec 24, 2018

@author: wtmuller, cpendery
'''

class Cactus(pyglet.sprite.Sprite):

    big_cactus = image.load('sprites/bigCactus.png')
    small_cactus = image.load('sprites/smallCactus.png')
    small_cactus_doub = image.load('sprites/smallCactusDoub.png')
    small_cactus_trip = image.load('sprites/smallCactusTrip.png')

    def __init__(self):
        super().__init__(img=image.load('sprites/bigCactus.png'))
        self.rand_image()
        self.x = gameboard.window.width 
        self.velocity_x = Ground.current_ground_speed
        
    def update(self, dt):
        self.velocity_x = Ground.current_ground_speed
        self.x += self.velocity_x * dt
        if self.x + self.width <= 0:
            self.delete()
            gameboard.game_objects.remove(self)
            
    def rand_image(self):
        num = random.randint(1, 5)
        if num == 1:
            self.image = Cactus.big_cactus
        elif num == 2:
            self.image = Cactus.small_cactus
        elif num == 3:
            self.image = Cactus.small_cactus_doub
        else:
            self.image = Cactus.small_cactus_trip