import pyglet, math
from physicalobject import PhysicalObject
'''
Created on Sep 7, 2018

@author: 17cha
'''

#Score Class
class Score(PhysicalObject):
    
    def __init__(self, num, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.number = num
        self.isFlashing = False

    def update_score(self):
        digitArray = [pyglet.image.load('sprites/0.png'),
                      pyglet.image.load('sprites/1.png'),
                      pyglet.image.load('sprites/2.png'),
                      pyglet.image.load('sprites/3.png'),
                      pyglet.image.load('sprites/4.png'),
                      pyglet.image.load('sprites/5.png'),
                      pyglet.image.load('sprites/6.png'),
                      pyglet.image.load('sprites/7.png'),
                      pyglet.image.load('sprites/8.png'),
                      pyglet.image.load('sprites/9.png')]
        
        self.image = digitArray[math.floor((self.dino_dist / (10**self.number)) % 10)]
        
    def flash(self, dt):
        if self.opacity == 0:
            self.opacity = 255
        else:
            self.opacity = 0
            
    def end_flashing(self, dt):
        self.isFlashing = False
        pyglet.clock.unschedule(self.flash)
        
    def flashing(self):
        pyglet.clock.schedule_interval(self.flash, 0.25)
        pyglet.clock.schedule_once(self.end_flashing, 1.75)
                       
#end of score class