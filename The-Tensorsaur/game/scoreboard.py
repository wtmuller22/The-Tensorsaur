import pyglet, time, sched
from pyglet.window import key
'''
Created on Sep 7, 2018

@author: 17cha
'''

#Score Class
class Score:
    value = 0
    batch = pyglet.graphics.Batch()
    
    def __init__(self):
        digitArray = [pyglet.image.load('sprites/0.png'),
                      pyglet.image.load('sprites/1.png'),
                      pyglet.image.load('sprites/2.png'),
                      pyglet.image.load('sprites/3.png'),
                      pyglet.image.load('sprites/4.png'),
                      pyglet.image.load('sprites/5.png'),
                      pyglet.image.load('sprites/6.png'),
                      pyglet.image.load('sprites/7.png'),
                      pyglet.image.load('sprites/8.png'),
                      pyglet.image.load('sprites/9.png'),]
        digit1 = pyglet.image.Animation.from_image_sequence(digitArray, .1, True)
        digit2 = pyglet.image.Animation.from_image_sequence(digitArray, 1, True)
        digit3 = pyglet.image.Animation.from_image_sequence(digitArray, 10, True)
        digit4 = pyglet.image.Animation.from_image_sequence(digitArray, 100, True)
        digit5 = pyglet.image.Animation.from_image_sequence(digitArray, 1000, True)
        bin = pyglet.image.atlas.TextureBin()
        digit1.add_to_texture_bin(bin)
        digit2.add_to_texture_bin(bin)
        digit3.add_to_texture_bin(bin)
        digit4.add_to_texture_bin(bin)
        digit5.add_to_texture_bin(bin)
        scoreSprites = []
        scoreSprites.append(pyglet.sprite.Sprite(img=digit1, x=500, y=300, batch=self.batch))
        scoreSprites.append(pyglet.sprite.Sprite(img=digit2, x=480, y=300, batch=self.batch))
        scoreSprites.append(pyglet.sprite.Sprite(img=digit3, x=460, y=300, batch=self.batch))
        scoreSprites.append(pyglet.sprite.Sprite(img=digit4, x=440, y=300, batch=self.batch))
        scoreSprites.append(pyglet.sprite.Sprite(img=digit5, x=420, y=300, batch=self.batch))
    
#end of score class