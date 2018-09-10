'''
Created on Sep 7, 2018

@author: wtmul
'''
import pyglet, math
from pyglet import image
import physicalobject
import scoreboard
from scoreboard import Score
from pyglet.window import key

#Standing dino image
dinoStand = pyglet.resource.image('dinoStand.png')

#Loads and instantiates running dino
dinoRunning = image.load_animation('Dinomation.gif', None, None)
myBin = image.atlas.TextureBin()
dinoRunning.add_to_texture_bin(myBin)
dino = physicalobject.PhysicalObject(img=dinoRunning)

#Loads ground.gif
grd = image.load_animation('ground.gif', None, None)

#Instantiates first ground object
movingGround = physicalobject.PhysicalObject(img=grd)
movingGround.velocity_x = -500.0

#Instantiates second ground object
movingGround2 = physicalobject.PhysicalObject(img=grd)
movingGround2.x = 1280
movingGround2.isVisible = False

#Tells which ground is to follow the visible one
def cycleGround():
    if movingGround.isVisible:
        movingGround2.velocity_x = movingGround.current_ground_speed
        movingGround2.isVisible = True
    else:
        movingGround.x = 1272 #Manually Adjusting Gap Issue
        movingGround.velocity_x = movingGround.current_ground_speed
        movingGround.isVisible = True

#Batch of objects for convenient updating
game_objects = [movingGround, movingGround2, dino]

#Creates score board
score0 = Score(0, img=pyglet.image.load('sprites/0.png'), x=500, y=300)
score1 = Score(1, img=pyglet.image.load('sprites/0.png'), x=480, y=300)
score2 = Score(2, img=pyglet.image.load('sprites/0.png'), x=460, y=300)
score3 = Score(3, img=pyglet.image.load('sprites/0.png'), x=440, y=300)
score4 = Score(4, img=pyglet.image.load('sprites/0.png'), x=420, y=300)
score_board = [score0, score1, score2, score3, score4]

#Calls an update to the whole batch
def update(dt):
    for obj in game_objects:
        obj.update(dt)
    dino_distance(dt)
    for score in score_board:
        score.update_score()
        
#Updates distance dino has traveled
def dino_distance(dt):
    physicalobject.PhysicalObject.dinoDist += (math.fabs(movingGround.current_ground_speed * dt)) / 100

#Creates a window of a specific size
window = pyglet.window.Window(1280, 720)

@window.event
def on_draw():
    window.clear()
    
    for object in game_objects:
        object.draw()
    for score in score_board:
        score.draw()
    
@window.event
def on_key_press(symbol, modifiers):
    if (symbol == key.UP) and (dino.y == 0):
        dino.y = 1
        dino.velocity_y = 1000
    
pyglet.clock.schedule_interval(update, 1/120.0)
pyglet.app.run()