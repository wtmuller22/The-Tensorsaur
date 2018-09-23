'''
Created on Sep 7, 2018

@author: wtmul
'''
import pyglet, math, ground
from ground import Ground
from pyglet import image
import physicalobject
import scoreboard
from scoreboard import Score
from pyglet.window import key

#Loads and instantiates running dino
dinoRunning = image.load_animation('Dinomation.gif', None, None)
myBin = image.atlas.TextureBin()
dinoRunning.add_to_texture_bin(myBin)
dino = physicalobject.PhysicalObject(img=dinoRunning)

#Batch of objects for convenient updating
game_objects = [dino]

#Creates score board
score0 = Score(0, img=pyglet.image.load('sprites/0.png'), x=500, y=300)
score1 = Score(1, img=pyglet.image.load('sprites/0.png'), x=480, y=300)
score2 = Score(2, img=pyglet.image.load('sprites/0.png'), x=460, y=300)
score3 = Score(3, img=pyglet.image.load('sprites/0.png'), x=440, y=300)
score4 = Score(4, img=pyglet.image.load('sprites/0.png'), x=420, y=300)
score_board = [score0, score1, score2, score3, score4]

#Creates ground
movingGround = Ground(True, True, img=(pyglet.image.load('sprites/ground.png').get_region(0, 0, 1280, 28)), x=0, y=0)
movingGround2 = Ground(False, False, img=(pyglet.image.load('sprites/ground.png').get_region(0, 0, 2, 28)), x=1280, y=0)

#Calls an update to the whole batch
def update(dt):
    physicalobject.PhysicalObject.current_ground_speed -= 5 #Slowly increases speed
    for obj in game_objects:
        obj.update(dt)
    dino_distance(dt)
    for score in score_board:
        score.update_score()
    #Prevents gap from updating in wrong order
    if movingGround.atOrigin:
        movingGround.update_ground(dt)
        movingGround2.update_ground(dt)
    else:
        movingGround2.update_ground(dt)
        movingGround.update_ground(dt)
        
#Updates distance dino has traveled
def dino_distance(dt):
    physicalobject.PhysicalObject.dinoDist += (math.fabs(movingGround.current_ground_speed * dt)) / 100

#Creates a window of a specific size
window = pyglet.window.Window(1280, 720)

@window.event
def on_draw():
    window.clear()
    
    movingGround.draw()
    movingGround2.draw()
    for object in game_objects:
        object.draw()
    for score in score_board:
        score.draw()
    
@window.event
def on_key_press(symbol, modifiers):
    if (symbol == key.UP) and (dino.y == 0):
        dino.y = 1
        dino.velocity_y = 1000
        dino.isJumping = True
    
pyglet.clock.schedule_interval(update, 1/120.0)
pyglet.app.run()