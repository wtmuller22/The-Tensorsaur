import math
import gym
from gym import spaces, logger
from gym.utils import seeding
import numpy as np
import pdb
#from dino_dynam import Dinosaur

class DinoEnv(gym.Env):
    """ Actions:
        Type: Discrete(2)
        Num Action
        0   Stay
        1   Jump 

        Obstacles:
        Type: Tall(0), Long(1)
        Parameters as Tuple:
        (type, x-coord, y-coord, height, width) 

        Jumps are only possible on the ground, if not on the ground, then points are reduced """
    metadata = {
        'render.modes': ['human', 'rgb_array'],
        'video.frames_per_second' : 50
    }

    def __init__(self):
        self.obstacle_speed = 20
        self.gravity = 3.1 #random value
        self.massdino = 1.0
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

        self.dinowidth = 30.0
        self.dinoheight = 60.0

        self.time = 0

    def seed(self, seed=None):
        self.np_random, seed = seeding.np_random(seed)
        return [seed]

    def step(self, action):
        print('hi')

    def reset(self):
        self.state = self.np_random.uniform(low=-0.05, high=0.05, size=(4,))
        self.steps_beyond_done = None
        return np.array(self.state)

    def render(self, mode='human'):
        screen_width = 600
        screen_height = 400

        world_width = 60
        scale = screen_width/world_width

        if self.viewer is None:
            from gym.envs.classic_control import rendering
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
        #self.poletrans.set_rotation(-x[2])

        return self.viewer.render(return_rgb_array = mode=='rgb_array')


    def create_state(action):
        reward = 1.0
        #if asking to jump
        if(action == 1):
            #check if on ground,
            if(self.dinoy == 70):
                reward = -.3
            #if not, nothing
            else:
                self.dinoay = 12
                self.dinovy = 2
                self.dinoy = 71 #small movement to help me
                                #with future checks
                reward = 1
        #choosing to stay on the ground, so nothing changes

        #checking with obstacles, To-Do
        for obsta in self.obstacles:
            if(collision(obsta)):
                reward = -20

        #returning the state
        self.state = ()
        return reward

    #updates the physics for the dino
    def update_physics():
        if(self.dinoy == 70):
            self.dinoy = 70
            self.dinovy = 0
            self.dinoay = 0
        else:
            self.dinoy = self.dinoy + dinovy
            self.dinovy = self.dinovy + dinoay
            self.dinoay = self.dinoay + self.gravity

    def update_obstacles():

        #moves the current obstacles
        for obsta in self.obstacles:
            obsta[1] = obsta[1] - self.obstacle_speed

        #generates new obstacles
        if(self.time == 100): #every 2 seconds
            obType = randint(0,2) #0 or 1
            width = 0
            height = 0
            if(obType == 1):
                width = 30
                height = 60
            else:
                width = 50
                height = 20
            self.obstacles.append([obType, 600, 30, height, width])
            self.time = 0
        else:
            self.time = self.time + 1

    def collision(obstacle):
        return (self.dinox <= obstacle[1]+obstacle[4]) and (obstacle[1] <= self.dionx + self.width) or (self.dinoy <= obstacle[2]+obstacle[3]) and (obstacle[2] <= self.dinoy + self.height)

    def close(self):
        if self.viewer:
            self.viewer.close()
            self.viewer = None
