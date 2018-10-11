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
        if (self != gameboard.dino):
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
                
    #[num1, num2] lower value in the left, higher value in the right
    def overlap(self, range1:list, range2:list):
        return range1[0] <= range2[1] and range2[0] <= range1[1]
                
    #checks if the self, the dino, is in a state of collision with the
    #other physical object
    def collision(self, other) -> bool:
        #little adjustments for the dinosaur as it will always be self
        xRangeSelf = [self.x - 15, self.x + self.width - 15]
        yRangeSelf = [self.y - 2, self.y + self.height - 2]
        
        xRangeOther = [other.x, other.x + other.width]
        yRangeOther = [other.y, other.y + other.height]
        return self.overlap(xRangeSelf, xRangeOther) and self.overlap(yRangeSelf, yRangeOther)