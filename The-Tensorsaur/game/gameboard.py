'''
Created on Sep 7, 2018

@author: wtmul, cpendery
'''
import pyglet, math
from ground import Ground
from pyglet import image
from scoreboard import Score
from scoreboard import Scoreboard
from pyglet.window import key
from pyglet.gl.base import ObjectSpace
from dinosaur import Dinosaur
from cactus import Cactus
from bird import Bird
from lose import Lose

#Creates a white window of a specific size
window = pyglet.window.Window(960, 540)
pyglet.gl.glClearColor(1, 1, 1, 1)

#Loads and instantiates objects
game_over = Lose()
dino = Dinosaur()
cactus = Cactus()
bird = Bird()
score_board = Scoreboard()
game_objects = [dino, cactus, bird]
moving_ground = Ground(True, True, img=(pyglet.image.load('sprites/ground.png').get_region(0, 0, window.width, 28)), x=0, y=0)
moving_ground_2 = Ground(False, False, img=(pyglet.image.load('sprites/ground.png').get_region(0, 0, 2, 28)), x=window.width, y=0)

def update(dt):
#Updates batch
    for obj in game_objects:
        obj.update(dt)
#Updates distance traveled
    Dinosaur.dino_dist += (math.fabs(Ground.current_ground_speed * dt)) / 100
#Updates/Flashes score
    for score in score_board.board:
        if not score.isFlashing:
            score.update_score()
        if (not score.isFlashing and not math.floor(Dinosaur.dino_dist) == 0 and
                math.floor(Dinosaur.dino_dist % 100) == 0):
            score.isFlashing = True
            Ground.current_ground_speed -= 10 #Increases speed
            score.flashing()
#Prevents gap from updating in wrong order
    if moving_ground.atOrigin:
        moving_ground.update_ground(dt)
        moving_ground_2.update_ground(dt)
    else:
        moving_ground_2.update_ground(dt)
        moving_ground.update_ground(dt)
#Checks if game is over
    if(checkCollisions(dino, game_objects)):
        dino.image = Dinosaur.dino_dead
        bird.image = pyglet.image.load('sprites/birdFlapped.png', None, None)
        game_over.opacity = 255
        pyglet.clock.unschedule(update)
    
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
    for score in score_board.board:
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
        dino.image = Dinosaur.dino_down
        
@window.event
def on_key_release(symbol, modifiers):
    if (symbol == key.DOWN):
        dino.image = Dinosaur.dino_running
    
pyglet.clock.schedule_interval(update, 1/30.0)
pyglet.app.run()