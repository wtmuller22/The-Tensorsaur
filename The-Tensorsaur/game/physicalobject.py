'''
Created on Sep 7, 2018

@author: wtmul
'''
import pyglet
import gameboard

class PhysicalObject(pyglet.sprite.Sprite):
    
    dinoDist = 0.0
    current_ground_speed = -500.0
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.velocity_x, self.velocity_y = 0.0, 0.0
        self.acceleration_y = -4000
        self.isJumping = False
    
    #Updates object to move and check bounds
    def update(self, dt):
        if ((self == gameboard.movingGround or self == gameboard.movingGround2) and (self.velocity_x != self.current_ground_speed)):
            self.velocity_x = self.current_ground_speed
        self.x += self.velocity_x * dt
        #Dino jumping physics
        self.velocity_y += self.acceleration_y * dt
        if (self.y > 0):
            if (self.y + self.velocity_y * dt) < 0:
                self.velocity_y = 0
                self.y = 0
                self.image = gameboard.dinoRunning
            else:
                self.y += self.velocity_y * dt