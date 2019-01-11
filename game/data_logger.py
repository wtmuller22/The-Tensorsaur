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
            
    def clear_queue(self):
        while(not self.dataQ.empty()):
            self.dataQ._get()
    
    #writes the data to the proper .txt files
    def write_data(self, toLog):
        if(not(self.txt_open)):
            self.open_txt()
            self.txt_open = True
            
        self.txt_list[0].write("%.2f," % self.new_list[0])
        self.txt_list[1].write("%.2f," % self.new_list[1])
        self.txt_list[2].write("%.2f," % self.new_list[2])
        self.txt_list[3].write("%.2f," % self.new_list[3])
        self.txt_list[4].write("%i," % self.new_list[4])
        self.txt_list[5].write("%.2f," % self.new_list[5])
        self.txt_list[6].write("%.2f," % self.new_list[6])
        self.txt_list[7].write("%i," % self.new_list[7])
        
    def open_txt(self):
        self.txt_list.append(open("logs/distanceToObstacle.txt", 'a'))
        self.txt_list.append(open("logs/heightOfObstacle.txt", 'a'))
        self.txt_list.append(open("logs/widthOfObstacle.txt", 'a'))
        self.txt_list.append(open("logs/obstacleYPosition.txt", 'a'))
        self.txt_list.append(open("logs/speed.txt", 'a'))
        self.txt_list.append(open("logs/playerYPosition.txt", 'a'))
        self.txt_list.append(open("logs/gapBetweenObstacles.txt", 'a'))
        self.txt_list.append(open("logs/playerState.txt", 'a'))
        
    def clear_logs(self):
        self.txt_list.append(open("logs/distanceToObstacle.txt", 'w'))
        self.txt_list.append(open("logs/heightOfObstacle.txt", 'w'))
        self.txt_list.append(open("logs/widthOfObstacle.txt", 'w'))
        self.txt_list.append(open("logs/obstacleYPosition.txt", 'w'))
        self.txt_list.append(open("logs/speed.txt", 'w'))
        self.txt_list.append(open("logs/playerYPosition.txt", 'w'))
        self.txt_list.append(open("logs/gapBetweenObstacles.txt", 'w'))
        self.txt_list.append(open("logs/playerState.txt", 'w'))
        
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
        
    def set_new_list(self,var):
        self.new_list = var