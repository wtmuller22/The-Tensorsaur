import pyglet
import gameboard
'''
Created on Dec 24, 2018

@author: wtmuller, cpendery
'''

class Lose(pyglet.sprite.Sprite):

    def __init__(self):
        super().__init__(img=pyglet.image.load('sprites/gameOver.png'))
        self.x = (gameboard.window.width/2 - 200)
        self.y = (gameboard.window.height/2 + 50)
        self.opacity = 0
        
class Restart(pyglet.sprite.Sprite):
    
    def __init__(self):
        super().__init__(img=pyglet.image.load('sprites/restartButton.png'))
        self.x = (gameboard.window.width/2 - 50)
        self.y = (gameboard.window.height/2 - 50)
        self.opacity = 0
        
    def collision(self, otherX, otherY):
        x_range_self = [self.x, self.x + self.width]
        y_range_self = [self.y, self.y + self.height]

        if(x_range_self[0] <= otherX < x_range_self[1] and y_range_self[0] <= otherY < y_range_self[1]):
            return True
        return False