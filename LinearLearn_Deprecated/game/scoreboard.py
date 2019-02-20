import pyglet, math, gameboard
from dinosaur import Dinosaur
'''
Created on Sep 7, 2018

@author: wmuller, cpendery
'''

#Score Class
class Score(pyglet.sprite.Sprite):
    
    def __init__(self, num, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.number = num
        self.isFlashing = False

    def update_score(self):
        self.image = Scoreboard.digitArray[math.floor((Dinosaur.dino_dist / (10**self.number)) % 10)]
        
        #updating based on the parameter, not the distance
    def update_score_p(self, highscore):
        self.image = Scoreboard.digitArray[math.floor((highscore / (10**self.number)) % 10)]
            
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

#Score board class
class Scoreboard:
    
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
    
    def __init__(self):
        #diff of 20 for spacing
        score0 = Score(0, img=pyglet.image.load('sprites/0.png'), x=(gameboard.window.width - 60), y=(gameboard.window.height/2 - 20))
        score1 = Score(1, img=pyglet.image.load('sprites/0.png'), x=(gameboard.window.width - 80), y=(gameboard.window.height/2 - 20))
        score2 = Score(2, img=pyglet.image.load('sprites/0.png'), x=(gameboard.window.width - 100), y=(gameboard.window.height/2 - 20))
        score3 = Score(3, img=pyglet.image.load('sprites/0.png'), x=(gameboard.window.width - 120), y=(gameboard.window.height/2 - 20))
        score4 = Score(4, img=pyglet.image.load('sprites/0.png'), x=(gameboard.window.width - 140), y=(gameboard.window.height/2 - 20))
        self.board = [score0, score1, score2, score3, score4]
        
class HighScoreboard:
    
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
    
    def __init__(self):
        #diff of 20 for spacing
        score0 = Score(0, img=pyglet.image.load('sprites/0.png'), x=(gameboard.window.width - 60), y=(gameboard.window.height/2 + 20))
        score1 = Score(1, img=pyglet.image.load('sprites/0.png'), x=(gameboard.window.width - 80), y=(gameboard.window.height/2 + 20))
        score2 = Score(2, img=pyglet.image.load('sprites/0.png'), x=(gameboard.window.width - 100), y=(gameboard.window.height/2 + 20))
        score3 = Score(3, img=pyglet.image.load('sprites/0.png'), x=(gameboard.window.width - 120), y=(gameboard.window.height/2 + 20))
        score4 = Score(4, img=pyglet.image.load('sprites/0.png'), x=(gameboard.window.width - 140), y=(gameboard.window.height/2 + 20))
        self.board = [score0, score1, score2, score3, score4]
        
#end of Score board class