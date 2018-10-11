import pyglet, gameboard, physicalobject, math
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
                       
#end of score class