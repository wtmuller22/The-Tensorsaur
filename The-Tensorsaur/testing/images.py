import pyglet
'''
Created on Aug 30, 2018

@author: 17cha
'''
window = pyglet.window.Window()

from pyglet.window import key
@window.event
def on_key_press(symbol, modifiers):
    if symbol == key.UP:
        print("up arrow")
    elif symbol == key.DOWN:
        print("down arrow")

@window.event
def on_draw():
    window.clear()
 
pyglet.app.run()