import math
import gym
from gym import spaces, logger
from gym.utils import seeding
import numpy as np
import pdb
import random
from gym.envs.classic_control import rendering
#from dino_dynam import Dinosaur

class DinoEnv(gym.Env):
    #-.02, 6
    """ Actions:
        Type: Discrete(2)
        Num Action
        0   Stay
        1   Jump 

        Obstacles:
        Type: Tall(0), Long(1)
        hasBeenCollidedWith: No(0), Yes(1)
        Parameters as Tuple:
        (type, x-coord, y-coord, height, width, hasBeenCollidedWith, obsId) 

        Jumps are only possible on the ground, if not on the ground, then points are reduced """
    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'video.frames_per_second' : 50
    }

    def __init__(self):
        self.obsId = 0
        self.obstacle_speed = 4
        self.gravity = -.02 #random value
        self.tau = 0.02  # seconds between state updates
        self.kinematics_integrator = 'euler'
        self.action_space = spaces.Discrete(2)
        # self.observation_space = spaces.Box(-high, high, dtype=np.float32)

        self.seed()
        self.viewer = None
        self.state = None

        self.steps_beyond_done = None

        self.dinox = 100
        self.dinoy = 70
        self.dinovy = 0
        self.dinoay = 0

        self.obstacles = []
        self.obstacletrans = []

        self.dinowidth = 30.0
        self.dinoheight = 60.0

        self.time = 0

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, action):
        self.update_physics()
        self.update_obstacles()
        reward = self.create_state(action)
        done = False
        if(reward < -60):
            done = True
        return self.state, reward, done, {}

    def reset(self):
        self.state = self.np_random.uniform(low=-0.05, high=0.05, size=(4,))
        self.steps_beyond_done = None
        return np.array(self.state)

    def render(self, mode='human'):
        screen_width = 600
        screen_height = 400

        world_width = 60
        scale = screen_width/world_width

        #the renderer creation
        if self.viewer is None:
            self.viewer = rendering.Viewer(screen_width, screen_height)
            l,r,t,b = -self.dinowidth/2, self.dinowidth/2, self.dinoheight/2, -self.dinoheight/2
            dino = rendering.FilledPolygon([(l,b), (l,t), (r,t), (r,b)])
            self.dinostrans = rendering.Transform()
            dino.add_attr(self.dinostrans)
            self.viewer.add_geom(dino)
            self.track = rendering.Line((0,40), (screen_width,40))
            self.track.set_color(0,0,0)
            self.viewer.add_geom(self.track)

        if self.state is None: return None

        self.dinox = screen_width/6.0 -30
        self.dinostrans.set_translation(self.dinox, self.dinoy)
        
        #render the obstacles
        for obs in self.obstacles:
            l,r,t,b = -obs[4]/2, obs[4]/2, obs[3]/2, -obs[3]/2
            obsrender = rendering.FilledPolygon([(l,b), (l,t), (r,t), (r,b)])
            obstrans = rendering.Transform()
            obsrender.add_attr(obstrans)
            obstrans.set_translation(obs[1],obs[2])
            self.viewer.add_onetime(obsrender)
            
        return self.viewer.render(return_rgb_array = mode=='rgb_array')


    def create_state(self, action):
        reward = 1.0
        #if asking to jump
        if(action == 1):
            #check if on ground,
            if(not(self.dinoy == 70)):
                reward = -.3
            #if not, nothing
            else:
                self.dinoay = 0
                self.dinovy = 6
                self.dinoy = 71 #small movement to help me
                                #with future checks
                reward = 1
        #choosing to stay on the ground, so nothing changes

        #checking with obstacles
        for obsta in self.obstacles:
            if(self.collision(obsta) and obsta[5] == 0):
                reward = -20
                obsta[5] = 1

        #returning the state
        self.state = [self.dinox, self.dinoy, self.obstacles]
        return reward

    #updates the physics for the dino
    def update_physics(self):
        if(self.dinoy == 70):
            self.dinoy = 70
            self.dinovy = 0
            self.dinoay = 0
        else:
            self.dinoy = self.dinoy + self.dinovy
            self.dinovy = self.dinovy + self.dinoay
            self.dinoay = self.dinoay + self.gravity
            if(self.dinoy < 70):
                self.dinoy = 70

    def update_obstacles(self):

        #clears old obstacles
        for obsta in self.obstacles:
            if(obsta[1] + obsta[4] < 0):
                self.obstacles.remove(obsta)

        #moves the current obstacles
        for obsta in self.obstacles:
            obsta[1] = obsta[1] - self.obstacle_speed

        #generates new obstacles
        if(self.time == 100): #every 2 seconds
            obType = random.randint(0,2) #0 or 1
            width = 0
            height = 0
            ycoord = 30
            if(obType == 1):
                width = 30
                height = 60
                ycoord = 70
            else:
                width = 50
                height = 30
                ycoord = 55
            self.obstacles.append([obType, 600, ycoord, height, width, 0, self.obsId])
            self.time = 0
            self.obsId = self.obsId + 1
        else:
            self.time = self.time + 1

    def collision(self, obstacle):
        sX = (self.dinox, self.dinox+self.dinowidth)
        sY = (self.dinoy, self.dinox+self.dinoheight)
        oX = (obstacle[1],obstacle[1]+obstacle[4])
        oY = (obstacle[2],obstacle[2]+obstacle[3])
        #intersections
        xCollision = sX[0] <= oX[1] and oX[0] <= sX[1]
        yCollision = sY[0] <= oY[1] and oY[0] <= sY[1]
        return xCollision and yCollision

    def close(self):
        if self.viewer:
            self.viewer.close()
            self.viewer = None
