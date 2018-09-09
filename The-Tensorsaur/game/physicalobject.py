'''
Created on Sep 7, 2018

@author: wtmul
'''
import pyglet
import gameboard

class PhysicalObject(pyglet.sprite.Sprite):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.velocity_x, self.velocity_y = 0.0, 0.0
        self.isVisible = True
        self.acceleration_y = -4000
    
    #Updates object to move and check bounds
    def update(self, dt):
        self.x += self.velocity_x * dt
        self.velocity_y += self.acceleration_y * dt
        if (self.y + self.velocity_y * dt) < 0:
            self.velocity_y = 0
            self.y = 0
        else:
            self.y += self.velocity_y * dt
        self.check_bounds()
    
    #Checks if object is out of frame and resets it
    def check_bounds(self):
        min_x = -self.width
        min_y = -self.height / 2
        max_x = 1280
        max_y = 720 + self.height / 2
        if (self.x + self.width <= max_x):
            gameboard.cycleGround()
        if self.x < min_x:
            self.velocity_x = 0.0
            self.x = 1280
            self.isVisible = False
            