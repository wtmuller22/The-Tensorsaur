import pyglet, math
from bird import Bird
from pyglet import image
from struct import unpack
'''
Created on Sep 7, 2018

@author: cpendery, wmuller
'''
#Dino Class
class Dinosaur(pyglet.sprite.Sprite):
    
    high_score = 0.0
    dino_dist = 0.0
    dino_running = image.load_animation('sprites/dinomation.gif', None, None)
    dino_down = image.load_animation('sprites/downDinomation.gif', None, None)
    dino_dead = img=pyglet.image.load('sprites/dinoDead.png', None, None)
    dino_pause_up = image.load('sprites/dinoLeftUp.png')
    dino_pause_down = image.load('sprites/dinoDownLeftUp.png')
    
    def __init__(self):
        super().__init__(img=Dinosaur.dino_running)
        self.velocity_y = 0.0
        self.acceleration_y = -3500
        self.isJumping = False
        self.x = 20
    
    def update(self, dt):
        if (self.y > 0):
            self.velocity_y += self.acceleration_y * dt
            if (self.y + self.velocity_y * dt) < 0:
                self.velocity_y = 0
                self.y = 0
                self.image = Dinosaur.dino_running
            else:
                self.y += self.velocity_y * dt
    
    #[num1, num2] lower value in the left, higher value in the right
    def overlap(self, range1:list, range2:list):
        return range1[0] <= range2[1] and range2[0] <= range1[1]

    #Decides if a collision has occurred
    def collision(self, other):
        x_range_self = [self.x, self.x + self.width]
        y_range_self = [self.y, self.y + self.height]
        
        x_range_other = [other.x, other.x + other.width]
        y_range_other = [other.y, other.y + other.height]
        #Only runs rest of code if general sprite boxes are overlapping
        #to improve efficiency.
        if self.overlap(x_range_self, x_range_other) and self.overlap(y_range_self, y_range_other):
            regions = Dinosaur.get_regions(self, other)
            sections = Dinosaur.get_sections(self, other, regions)
            set_one = Dinosaur.get_pixel_alpha_data(self, sections[0])
            set_two = Dinosaur.get_pixel_alpha_data(self, sections[1])
            if set_one == 0 or set_two == 0:
                return False
            min_len = min(len(set_one), len(set_two))
            for i in range(min_len):
                if set_one[i] > 200 and set_two[i] > 200:
                    return True
            return False
        else:
            return False

    #Returns a set of all the dimension ranges for
    #the exact overlapping rectangles within each 
    #sprite's image.
    def get_regions(self, other):
        x_range_self = [0, 0]
        y_range_self = [0, 0]
        
        x_range_other = [0, 0]
        y_range_other = [0, 0]
        
        if self.x > other.x:
            x_range_other = [math.ceil(self.x - other.x), other.width]
            x_range_self = [0, math.ceil(other.x + other.width - self.x)]
        else:
            x_range_self = [math.ceil(other.x - self.x), self.width]
            x_range_other = [0, math.ceil(self.x + self.width - other.x)]
        if self.y > other.y:
            y_range_other = [math.ceil(self.y - other.y), other.height]
            y_range_self = [0, math.ceil(other.y + other.height - self.y)]
        else:
            y_range_self = [math.ceil(other.y - self.y), self.height]
            y_range_other = [0, math.ceil(self.y + self.height - other.y)]
        return [x_range_self[0], 
                x_range_self[1], 
                x_range_other[0], 
                x_range_other[1], 
                y_range_self[0], 
                y_range_self[1], 
                y_range_other[0], 
                y_range_other[1]]

    #Returns a set consisting of the image regions
    #of sprites which are overlapping.
    def get_sections(self, other, ranges):
        self_section = None
        if self.image == Dinosaur.dino_running:
            self_section = Dinosaur.dino_pause_up.get_region(ranges[0], ranges[4], ranges[1], ranges[5])
            self_section.width = ranges[1] - ranges[0]
            self_section.height = ranges[5] - ranges[4]
        else:
            self_section = Dinosaur.dino_pause_down.get_region(ranges[0], ranges[4], ranges[1], ranges[5])
            self_section.width = ranges[1] - ranges[0]
            self_section.height = ranges[5] - ranges[4]
        other_section = None
        if other.image == Bird.bird_flapping:
            other_section = Bird.bird_flapped.get_region(ranges[2], ranges[6], ranges[3], ranges[7])
            other_section.width = ranges[3] - ranges[2]
            other_section.height = ranges[7] - ranges[6]
        else:
            other_section = other.image.get_region(ranges[2], ranges[6], ranges[3], ranges[7])
            other_section.width = ranges[3] - ranges[2]
            other_section.height = ranges[7] - ranges[6]
        return [self_section, other_section]
    
    #Returns a set of integers representing the 
    #alpha values for each pixel within the given section.
    def get_pixel_alpha_data(self, section):
        raw = section.get_image_data()
        raw.x = math.ceil(raw.x)
        raw.y = math.ceil(raw.y)
        raw.width = math.ceil(raw.width)
        raw.height = math.ceil(raw.height)
        pitch = raw.width * len('RGBA')
        if raw.width == 0:
            return 0
        pixels = raw.get_data('RGBA', pitch)
        data = unpack("%iB" % (len(pixels)), pixels)
        mask = data[3::4]
        return mask
    
#End of Class

