'''
Created on Sep 7, 2018

@author: wtmul, cpendery
'''
import pyglet, math, ground
from ground import Ground
from pyglet import image
import physicalobject
import scoreboard
from scoreboard import Score
from pyglet.window import key
from pyglet.gl.base import ObjectSpace

#Creates a window of a specific size
window = pyglet.window.Window(960, 540)
#Sets default window color to white
pyglet.gl.glClearColor(1, 1, 1, 1)

#Loads and instantiates dino
dino_running = image.load_animation('sprites/dinomation.gif', None, None)
dino_down = image.load_animation('sprites/downDinomation.gif', None, None)
dino_dead = img=pyglet.image.load('sprites/dinoDead.png', None, None)

game_over = pyglet.sprite.Sprite(img=pyglet.image.load('sprites/gameOver.png'))
game_over.x = (window.width/5 - 100)
game_over.y = (window.height/5)
game_over.opacity = 0

my_bin = image.atlas.TextureBin()
dino_running.add_to_texture_bin(my_bin)
dino = physicalobject.PhysicalObject(img=dino_running)

#adding in the big cactus
big_cact = img=pyglet.image.load('sprites/bigCactus.png', None, None)
cactus = physicalobject.PhysicalObject(img=big_cact)
cactus.x = 2000

#adding in a bird
bird_flap = image.load_animation('sprites/birdomation.gif', None, None)
bird_flap.add_to_texture_bin(my_bin)
bird = physicalobject.PhysicalObject(img=bird_flap)
bird.setBird(True)
bird.x = 500
#70 for hits, 100 for no need to duck (will not have low jumps for birds)
bird.y = 100

#Batch of objects for convenient updating
game_objects = [dino, cactus, bird]

#Creates score board
score0 = Score(0, img=pyglet.image.load('sprites/0.png'), x=(window.width/2 + 30), y=(window.height/2 - 20))
score1 = Score(1, img=pyglet.image.load('sprites/0.png'), x=(window.width/2 + 10), y=(window.height/2 - 20))
score2 = Score(2, img=pyglet.image.load('sprites/0.png'), x=(window.width/2 - 10), y=(window.height/2 - 20))
score3 = Score(3, img=pyglet.image.load('sprites/0.png'), x=(window.width/2 - 30), y=(window.height/2 - 20))
score4 = Score(4, img=pyglet.image.load('sprites/0.png'), x=(window.width/2 - 50), y=(window.height/2 - 20))
score_board = [score0, score1, score2, score3, score4]

#Creates ground
moving_ground = Ground(True, True, img=(pyglet.image.load('sprites/ground.png').get_region(0, 0, window.width, 28)), x=0, y=0)
moving_ground_2 = Ground(False, False, img=(pyglet.image.load('sprites/ground.png').get_region(0, 0, 2, 28)), x=window.width, y=0)

#Calls an update to the whole batch
def update(dt):
    if(not checkCollisions(dino, game_objects)):
        physicalobject.PhysicalObject.current_ground_speed -= 5 #Slowly increases speed
        for obj in game_objects:
            obj.update(dt)
        dino_distance(dt)
        for score in score_board:
            score.update_score()
    #Prevents gap from updating in wrong order
        if moving_ground.atOrigin:
            moving_ground.update_ground(dt)
            moving_ground_2.update_ground(dt)
        else:
            moving_ground_2.update_ground(dt)
            moving_ground.update_ground(dt)
    else:
        dino.image = dino_dead
        game_over.opacity = 255
        
        
#Updates distance dino has traveled
def dino_distance(dt):
    physicalobject.PhysicalObject.dino_dist += (math.fabs(moving_ground.current_ground_speed * dt)) / 100
    
#returns false if the dino is not in collision
def checkCollisions(dino, game_objects):
    for obj in game_objects:
        if dino != obj and dino.collision(obj):
            return True
    return False
            
@window.event
def on_draw():
    window.clear()
    
    pyglet.sprite.Sprite(pyglet.image.load('sprites/ground.png')).draw()
    moving_ground.draw()
    moving_ground_2.draw()
    for object in game_objects:
        object.draw()
    for score in score_board:
        score.draw()
    game_over.draw()
    
@window.event
def on_key_press(symbol, modifiers):
    if (symbol == key.UP or symbol == key.SPACE) and (dino.y == 0):
        dino.y = 1
        dino.velocity_y = 1000
        dino.isJumping = True
        dino.image = pyglet.image.load('sprites/dinoStand.png')
    elif (symbol == key.DOWN) and (dino.y == 0):
        dino.image = dino_down
        
@window.event
def on_key_release(symbol, modifiers):
    if (symbol == key.DOWN):
        dino.image = dino_running
    
pyglet.clock.schedule_interval(update, 1/30.0)
pyglet.app.run()