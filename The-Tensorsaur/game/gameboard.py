'''
Created on Sep 7, 2018

@author: wtmul
'''
import pyglet
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
#sprite = pyglet.sprite.Sprite(img=dinoRunning)
dino = physicalobject.PhysicalObject(img=dinoRunning)

#Loads ground.gif
grd = image.load_animation('ground.gif', None, None)
#ground = pyglet.sprite.Sprite(img=grd)

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
        movingGround2.velocity_x = -500.0
        movingGround2.isVisible = True
    else:
        movingGround.x = 1272 #Manually Adjusting Gap Issue
        movingGround.velocity_x = -500.0
        movingGround.isVisible = True

#Batch of objects for convenient updating
game_objects = [movingGround, movingGround2, dino]

#Calls an update to the whole batch
def update(dt):
    for obj in game_objects:
        obj.update(dt)

#Creates a window of a specific size
window = pyglet.window.Window(1280, 720)
score = Score()

@window.event
def on_draw():
    window.clear()
    
    movingGround2.draw()
    movingGround.draw()
    dino.draw()
    score.batch.draw()
    
@window.event
def on_key_press(symbol, modifiers):
    if (symbol == key.UP) and (dino.y == 0):
        dino.y = 1
        dino.velocity_y = 1000
    
pyglet.clock.schedule_interval(update, 1/120.0)
pyglet.app.run()