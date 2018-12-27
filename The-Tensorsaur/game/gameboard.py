'''
Created on Sep 7, 2018

@author: wmuller, cpendery
'''
import pyglet, math, random
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
score_board = Scoreboard()
high_score = Scoreboard()
game_objects = [dino]
moving_ground = Ground(True, True, img=(pyglet.image.load('sprites/ground.png').get_region(0, 0, window.width, 28)), x=0, y=0)
moving_ground_2 = Ground(False, False, img=(pyglet.image.load('sprites/ground.png').get_region(0, 0, 2, 28)), x=window.width, y=0)

#Sets up high score
high = pyglet.sprite.Sprite(img=image.load('sprites/highScore.png'), x=(window.width/2 - 100), y=(window.height - 150))
high.opacity = 0
for score in high_score.board:
    score.y = window.height - 150
    score.x = score.x + 20
    score.opacity = 0

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
    #Sets high score
        if Dinosaur.dino_dist > Dinosaur.high_score:
            Dinosaur.high_score = Dinosaur.dino_dist
            high.opacity = 255
            for score in high_score.board:
                score.opacity = 255
                score.update_score()
        dino.image = Dinosaur.dino_dead
        pyglet.clock.schedule_once(game_over_visible, 1.0)
        pyglet.clock.unschedule(update)
        pyglet.clock.unschedule(spawn)
    #Stops bird flapping
        obstacles = game_objects[1:]
        for obs in obstacles:
            if isinstance(obs, Bird):
                obs.image = Bird.bird_flapped
                
def game_over_visible(dt):
    game_over.opacity = 255
        
def spawn(dt):
    if Dinosaur.dino_dist < 100:
        game_objects.append(Cactus())
    else:
        decide = random.randint(1, 6)
        if decide == 1 or decide == 2:
            game_objects.append(Bird())
        else:
            game_objects.append(Cactus())
    num = random.randint(90, 126)
    pyglet.clock.schedule_once(spawn, num / 100)
        
    
#returns false if the dino is not in collision
def checkCollisions(dino, game_objects):
    for obj in game_objects:
        if dino != obj and dino.collision(obj):
            return True
    return False

def restart():
    Dinosaur.dino_dist = 0.0
    Ground.current_ground_speed = -800.0
    obstacles = game_objects[1:]
    for obs in obstacles:
        obs.delete()
        game_objects.remove(obs)
    game_over.opacity = 0
    dino.y = 0
    dino.velocity_y = 0
    dino.image = Dinosaur.dino_running
    pyglet.clock.schedule_once(spawn, 2.0)
    pyglet.clock.schedule_interval(update, 1/30.0)
            
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
    for score in high_score.board:
        score.draw()
    high.draw()
    game_over.draw()
    
@window.event
def on_key_press(symbol, modifiers):
    if dino.image == Dinosaur.dino_running or dino.image == Dinosaur.dino_down:
        if (symbol == key.UP or symbol == key.SPACE) and (dino.y == 0):
            dino.y = 1
            dino.velocity_y = 1200
            dino.isJumping = True
            dino.image = pyglet.image.load('sprites/dinoStand.png')
        elif (symbol == key.DOWN) and (dino.y == 0):
            dino.image = Dinosaur.dino_down
    if (game_over.opacity == 255):
        restart()
        
@window.event
def on_key_release(symbol, modifiers):
    if (symbol == key.DOWN) and (dino.image == Dinosaur.dino_down):
        dino.image = Dinosaur.dino_running
    
pyglet.clock.schedule_once(spawn, 2.0)
pyglet.clock.schedule_interval(update, 1/60.0)
pyglet.app.run()