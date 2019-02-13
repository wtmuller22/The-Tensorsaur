import gameboard, math, pyglet
from pyglet import image
'''
Created on Sep 21, 2018

@author: wtmuller, cpendery
'''

#Ground class
class Ground(pyglet.sprite.Sprite):
    
    FRAMES = 60 #per second
    
    
    
    #converts to fps for code
    FRAMES = 1.0/FRAMES
    current_ground_speed = (-800.0/60) / FRAMES
    
    def __init__(self, vis, at, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.isVisible = vis
        self.atOrigin = at
        self.start = 0
        self.length = gameboard.window.width
    
    def update_ground(self, dt):
        whole_ground = image.load('sprites/ground.png')
        if self.isVisible and self.atOrigin:
            if self.start + (math.floor(math.fabs(self.current_ground_speed * dt))) >= 2402:
                self.isVisible = False
                self.atOrigin = False
                self.x = gameboard.window.width
                self.start = 0
                self.length = 2
            else:
                self.start += math.floor(math.fabs(self.current_ground_speed * dt))
                self.length = gameboard.window.width
                if self.start + self.length >= 2402:
                    self.length = 2402 - self.start
                    if self != gameboard.moving_ground:
                        gameboard.moving_ground.isVisible = True
                    else:
                        gameboard.moving_ground_2.isVisible = True
                self.image = whole_ground.get_region(self.start, 0, self.length, 28)
        elif self.isVisible:
            if (self == gameboard.moving_ground and not gameboard.moving_ground_2.isVisible) or (self == gameboard.moving_ground_2 and not gameboard.moving_ground.isVisible):
                self.atOrigin = True
                self.x = 0
            if self == gameboard.moving_ground:
                self.length = gameboard.window.width - gameboard.moving_ground_2.length
                if self.length <= 0:
                    self.length = 1
                self.image = whole_ground.get_region(0, 0, self.length, 28)
                self.x = gameboard.moving_ground_2.length
            elif self == gameboard.moving_ground_2:
                self.length = gameboard.window.width - gameboard.moving_ground.length
                if self.length <= 0:
                    self.length = 1
                self.image = whole_ground.get_region(0, 0, self.length, 28)
                self.x = gameboard.moving_ground.length