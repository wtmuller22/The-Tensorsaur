'''
Created on Sep 7, 2018

@author: wtmul, cpendery
'''
import pyglet
import gameboard

class PhysicalObject(pyglet.sprite.Sprite):
    
    dino_dist = 0.0
    current_ground_speed = -500.0
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.velocity_x, self.velocity_y = 0.0, 0.0
        self.acceleration_y = -4000
        self.isJumping = False
        self.bird = False
    
    def setBird(self, val):
        self.bird = val
    #Updates object to move and check bounds
    def update(self, dt):        
        if ((self == gameboard.moving_ground or self == gameboard.moving_ground_2) and (self.velocity_x != self.current_ground_speed)):
            self.velocity_x = self.current_ground_speed
        if (self != gameboard.dino):
            self.velocity_x = self.current_ground_speed
        self.x += self.velocity_x * dt
        #Dino jumping physics
        self.velocity_y += self.acceleration_y * dt
        if (self.y > 0 and self.bird == False):
            if (self.y + self.velocity_y * dt) < 0:
                self.velocity_y = 0
                self.y = 0
                self.image = gameboard.dino_running
            else:
                self.y += self.velocity_y * dt
                
    #[num1, num2] lower value in the left, higher value in the right
    def overlap(self, range1:list, range2:list):
        return range1[0] <= range2[1] and range2[0] <= range1[1]
                
    #checks if the self, the dino, is in a state of collision with the
    #other physical object
    def collision(self, other) -> bool:
        #little adjustments for the dinosaur as it will always be self
        x_range_self = [self.x - 20, self.x + self.width - 15]
        y_range_self = [self.y - 2, self.y + self.height - 2]
        
        x_range_other = [other.x, other.x + other.width]
        y_range_other = [other.y, other.y + other.height]
        return self.overlap(x_range_self, x_range_other) and self.overlap(y_range_self, y_range_other)