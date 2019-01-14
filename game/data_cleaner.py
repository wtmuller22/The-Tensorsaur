'''
Created on Jan 13, 2019

@author: cpendery
'''

import csv, random, os

class DataPiece():
    def __init__(self):
        self.array = [0,0,0,0,0,0,0,9]
    def set_DTO(self, var):
        self.array[0] = var
    def set_HOO(self, var):
        self.array[1] = var
    def set_WOO(self, var):
        self.array[2] = var
    def set_OYP(self, var):
        self.array[3] = var
    def set_S(self, var):
        self.array[4] = var
    def set_PYP(self, var):
        self.array[5] = var
    def set_GBO(self, var):
        self.array[6] = var
    def set_PS(self, var):
        self.array[7] = var
    
def sort_data(var):
    return var.array[7]

def find_smallest(var1, var2, var3):
    Min = var1
    if var2 < Min:
        Min = var2  
    if var3 < Min:
        Min = var3
    if var2 < var3:
        Min = var2
    return Min
        
class DataCleaner():
    
    def __init__(self):
        self.data_pieces = []
        self.count0 = 0
        self.count1 = 0
        self.count2 = 0
        
    #cleans and rewrites the cleaned data
    def clean_data(self):
        self.read_in_data()
        self.remove_data()
        self.write_data()
        
    def read_in_data(self):
        #brings in the all the data pieces filling the first value
        with open('logs/distanceToObstacle.txt', 'r') as f:
            reader = csv.reader(f, dialect='excel', delimiter=',')
            for row in reader:
                for val in row:
                    d = DataPiece()
                    d.set_DTO(val)
                    self.data_pieces.append(d)
        #changes the value in all the filled data pieces
        with open('logs/heightOfObstacle.txt', 'r') as f:
                reader = csv.reader(f, dialect='excel', delimiter=',')
                for row in reader:
                    for idx, val in enumerate(row):
                        self.data_pieces[idx].set_HOO(val)
                        
        with open('logs/widthOfObstacle.txt', 'r') as f:
                reader = csv.reader(f, dialect='excel', delimiter=',')
                for row in reader:
                    for idx, val in enumerate(row):
                        self.data_pieces[idx].set_WOO(val)
                        
        with open('logs/obstacleYPosition.txt', 'r') as f:
                reader = csv.reader(f, dialect='excel', delimiter=',')
                for row in reader:
                    for idx, val in enumerate(row):
                        self.data_pieces[idx].set_OYP(val)
                        
        with open('logs/speed.txt', 'r') as f:
                reader = csv.reader(f, dialect='excel', delimiter=',')
                for row in reader:
                    for idx, val in enumerate(row):
                        self.data_pieces[idx].set_S(val)
                        
        with open('logs/playerYPosition.txt', 'r') as f:
                reader = csv.reader(f, dialect='excel', delimiter=',')
                for row in reader:
                    for idx, val in enumerate(row):
                        self.data_pieces[idx].set_PYP(val)
                        
        with open('logs/gapBetweenObstacles.txt', 'r') as f:
                reader = csv.reader(f, dialect='excel', delimiter=',')
                for row in reader:
                    for idx, val in enumerate(row):
                        self.data_pieces[idx].set_GBO(val)
                        
        with open('logs/playerState.txt', 'r') as f:
                reader = csv.reader(f, dialect='excel', delimiter=',')
                for row in reader:
                    for idx, val in enumerate(row):
                        self.data_pieces[idx].set_PS(val)
                        
                        if (val == '0'):
                            self.count0 += 1
                        elif (val == '1'):
                            self.count1 += 1
                        elif (val == '2'):
                            self.count2 += 1
                        
        #removing the end data piece that is empty
        self.data_pieces.pop()
        #sorting the array according to the player state
        self.data_pieces.sort(key=sort_data)
                    
            
    def remove_data(self):
        #finds the lowest number of 0, 1, or 2's
        smallest = find_smallest(self.count0, self.count1, self.count2)
        while(self.count0 > smallest):
            self.random_remove(0)
        while(self.count1 > smallest):
            self.random_remove(1)
        while(self.count2 > smallest):
            self.random_remove(2)
            
            
    #removes a random entry from the player_state given in the 
    #data collected for that state
    def random_remove(self, player_state):
        if(player_state == 0):
            toRemove = random.randint(0, self.count0 - 1)
            del(self.data_pieces[toRemove])
            self.count0 -= 1
        elif(player_state == 1):
            toRemove = random.randint(self.count0, self.count0 + self.count1 - 1)
            del(self.data_pieces[toRemove])
            self.count1 -= 1
        else:
            toRemove = random.randint(self.count0 + self.count1, self.count0 + self.count1 + self.count2 - 1)
            del(self.data_pieces[toRemove])
            self.count2 -= 1
            
    def remove_prev_files(self):
        os.remove("logs/distanceToObstacle.txt")
        os.remove("logs/heightOfObstacle.txt")
        os.remove("logs/widthOfObstacle.txt")
        os.remove("logs/obstacleYPosition.txt")
        os.remove("logs/speed.txt")
        os.remove("logs/playerYPosition.txt")
        os.remove("logs/gapBetweenObstacles.txt")
        os.remove("logs/playerState.txt")
        
    def write_data(self):
        self.remove_prev_files()
        
        dto = open("logs/distanceToObstacle.txt", 'a+')
        hoo = open("logs/heightOfObstacle.txt", 'a+')
        woo = open("logs/widthOfObstacle.txt", 'a+')
        oyp = open("logs/obstacleYPosition.txt", 'a+')
        s = open("logs/speed.txt", 'a+')
        pyp = open("logs/playerYPosition.txt", 'a+')
        gbo = open("logs/gapBetweenObstacles.txt", 'a+')
        ps = open("logs/playerState.txt", 'a+')
        
        for d in self.data_pieces:
            dto.write("%s," % d.array[0])
        for d in self.data_pieces:
            hoo.write("%s," % d.array[1])
        for d in self.data_pieces:
            woo.write("%s," % d.array[2])
        for d in self.data_pieces:
            oyp.write("%s," % d.array[3])
        for d in self.data_pieces:
            s.write("%s," % d.array[4])
        for d in self.data_pieces:
            pyp.write("%s," % d.array[5])
        for d in self.data_pieces:
            gbo.write("%s," % d.array[6])
        for d in self.data_pieces:
            ps.write("%s," % d.array[7])
            
        dto.close()
        hoo.close()
        woo.close()
        oyp.close()
        s.close()
        pyp.close()
        gbo.close()
        ps.close()
        
            
d = DataCleaner()
d.clean_data()