import pyglet, gameboard, physicalobject, math
from physicalobject import PhysicalObject
from pyglet import image
'''
Created on Sep 21, 2018

@author: wtmul
'''

#Ground class
class Ground(PhysicalObject):
    
    def __init__(self, vis, at, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.isVisible = vis
        self.atOrigin = at
        self.start = 0
        self.length = gameboard.window.width
    
    def update_ground(self, dt):
        wholeGround = image.load('sprites/ground.png')
        if self.isVisible and self.atOrigin:
            if self.start + (math.floor(math.fabs(self.current_ground_speed * dt)) / 2) >= 2402:
                self.isVisible = False
                self.atOrigin = False
                self.x = gameboard.window.width
                self.start = 0
                self.length = 2
            else:
                self.start += math.floor(math.fabs(self.current_ground_speed * dt) / 2)
                self.length = gameboard.window.width
                if self.start + self.length >= 2402:
                    self.length = 2402 - self.start
                    if self != gameboard.movingGround:
                        gameboard.movingGround.isVisible = True
                    else:
                        gameboard.movingGround2.isVisible = True
                self.image = wholeGround.get_region(self.start, 0, self.length, 28)
        elif self.isVisible:
            if (self == gameboard.movingGround and not gameboard.movingGround2.isVisible) or (self == gameboard.movingGround2 and not gameboard.movingGround.isVisible):
                self.atOrigin = True
                self.x = 0
            if self == gameboard.movingGround:
                self.length = gameboard.window.width - gameboard.movingGround2.length
                if self.length <= 0:
                    self.length = 1
                self.image = wholeGround.get_region(0, 0, self.length, 28)
                self.x = gameboard.movingGround2.length
            elif self == gameboard.movingGround2:
                self.length = gameboard.window.width - gameboard.movingGround.length
                if self.length <= 0:
                    self.length = 1
                self.image = wholeGround.get_region(0, 0, self.length, 28)
                self.x = gameboard.movingGround.length