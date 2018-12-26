import pyglet
from pyglet import image
'''
Created on Sep 7, 2018

@author: 17cha
'''
#Dino Class
class Dinosaur(pyglet.sprite.Sprite):
    
    high_score = 0.0
    dino_dist = 0.0
    dino_running = image.load_animation('sprites/dinomation.gif', None, None)
    dino_down = image.load_animation('sprites/downDinomation.gif', None, None)
    dino_dead = img=pyglet.image.load('sprites/dinoDead.png', None, None)
    
    def __init__(self):
        super().__init__(img=Dinosaur.dino_running)
        self.velocity_y = 0.0
        self.acceleration_y = -3500
        self.isJumping = False
        self.x = 20
    
    def update(self, dt):
        if (self.y > 0):
            self.velocity_y += self.acceleration_y * dt
            if (self.y + self.velocity_y * dt) < 0:
                self.velocity_y = 0
                self.y = 0
                self.image = Dinosaur.dino_running
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
#End of Class