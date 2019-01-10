'''
Created on Dec 31, 2018

@author:  cpendery, wmuller
'''


import tensorflow as tf
import numpy as np
import pandas as pd

#7 params
#{distance to ob, height of ob, width of ob, bird height, speed, player y pos, gap between obs}
#3 lables
#0 = stay, 1 = jump, 2 = duck
distance_to = pd.Series([])
height_of = pd.Series([])
width_of = pd.Series([])
obstacle_y = pd.Series([])
speed = pd.Series([])
player_y = pd.Series([])
obstacle_gap = pd.Series([])
labels = pd.Series([])

playing_data = pd.DataFrame({ 'Distance to Obstacle': distance_to, 'Height of Obstacle': height_of,
                             'Width of Obstacle': width_of, 'Obstacle y Position': obstacle_y, 
                             'Speed': speed, 'Player y Position': player_y, 
                             'Gap Between Obstacles': obstacle_gap, 'Player State': labels})
playing_data