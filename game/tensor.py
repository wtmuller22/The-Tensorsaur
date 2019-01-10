'''
Created on Dec 31, 2018

@author:  cpendery, wmuller
'''


import tensorflow as tf
import numpy as np
import pandas as pd

distance_file = open("logs/distanceToObstacle.txt", 'r')
result_1 = [line.split(',') for line in distance_file]
height_file = open("logs/heightOfObstacle.txt", 'r')
result_2 = [line.split(',') for line in height_file]
width_file = open("logs/widthOfObstacle.txt", 'r')
result_3 = [line.split(',') for line in width_file]
obstacle_y_file = open("logs/obstacleYPosition.txt", 'r')
result_4 = [line.split(',') for line in obstacle_y_file]
speed_file = open("logs/speed.txt", 'r')
result_5 = [line.split(',') for line in speed_file]
player_y_file = open("logs/playerYPosition.txt", 'r')
result_6 = [line.split(',') for line in player_y_file]
gap_file = open("logs/gapBetweenObstacles.txt", 'r')
result_7 = [line.split(',') for line in gap_file]
state_file = open("logs/playerState.txt", 'r')
result_8 = [line.split(',') for line in state_file]
#7 params
#{distance to ob, height of ob, width of ob, bird height, speed, player y pos, gap between obs}
#3 lables
#0 = stay, 1 = jump, 2 = duck
distance_to = pd.Series([float(num) for num in result_1[0]])
height_of = pd.Series([float(num) for num in result_2[0]])
width_of = pd.Series([float(num) for num in result_3[0]])
obstacle_y = pd.Series([float(num) for num in result_4[0]])
speed = pd.Series([float(num) for num in result_5[0]])
player_y = pd.Series([float(num) for num in result_6[0]])
obstacle_gap = pd.Series([float(num) for num in result_7[0]])
labels = pd.Series([int(num) for num in result_8[0]])

playing_data = pd.DataFrame({ 'Distance to Obstacle': distance_to, 'Height of Obstacle': height_of,
                             'Width of Obstacle': width_of, 'Obstacle y Position': obstacle_y, 
                             'Speed': speed, 'Player y Position': player_y, 
                             'Gap Between Obstacles': obstacle_gap, 'Player State': labels})
print(playing_data)