'''
Created on Jan 10, 2019

@author: cpendery
'''

import  queue

class DataLogger():    
    def __init__(self, queueLength):
        self.dataQ = queue.Queue(queueLength)
        self.new_list = []
        self.txt_open = False
        self.txt_list = []
    
    def log_data(self):
        if(self.dataQ.full()):
            toLog = self.dataQ._get()
            self.write_data(toLog)
            self.dataQ.put(self.new_list)
        else:
            self.dataQ.put(self.new_list)
    
    #writes the data to the proper .txt files
    def write_data(self, toLog):
        if(not(self.txt_open)):
            self.open_txt()
            self.txt_open = True
            
        self.txt_list[0].write("%s," % self.new_list[0])
        self.txt_list[1].write("%s," % self.new_list[1])
        self.txt_list[2].write("%s," % self.new_list[2])
        self.txt_list[3].write("%s," % self.new_list[3])
        self.txt_list[4].write("%s," % self.new_list[4])
        self.txt_list[5].write("%s," % self.new_list[5])
        self.txt_list[6].write("%s," % self.new_list[6])
        self.txt_list[7].write("%s," % self.new_list[7])
        
    def open_txt(self):
        self.txt_list[0] = open("logs/distanceToObstacle.txt", 'a+')
        self.txt_list[1] = open("logs/heightOfObstacle.txt", 'a+')
        self.txt_list[2] = open("logs/widthOfObstacle.txt", 'a+')
        self.txt_list[3] = open("logs/obstacleYPosition.txt", 'a+')
        self.txt_list[4] = open("logs/speed.txt", 'a+')
        self.txt_list[5] = open("logs/distanceToObstacle.txt", 'a+')
        self.txt_list[6] = open("logs/gapBetweenObstacles.txt", 'a+')
        self.txt_list[7] = open("logs/playerState.txt", 'a+')
        
    def close_txt(self):
        self.txt_list[0].close()
        self.txt_list[1].close()
        self.txt_list[2].close()
        self.txt_list[3].close()
        self.txt_list[4].close()
        self.txt_list[5].close()
        self.txt_list[6].close()
        self.txt_list[7].close()
        
        #adds the the value to the list for the data
    def add_distance_to_obstacle(self, var):
        self.new_list[0] = var
    def add_height_of_obstacle(self, var):
        self.new_list[1] = var
    def add_width_of_obstacle(self, var):
        self.new_list[2] = var
    def add_obstacle_y_position(self, var):
        self.new_list[3] = var
    def add_speed(self, var):
        self.new_list[4] = var
    def add_player_y_position(self, var):
        self.new_list[5] = var
    def add_gap_between_obstacles(self, var):
        self.new_list[6] = var
    def add_player_state(self,var):
        self.new_list[7] = var