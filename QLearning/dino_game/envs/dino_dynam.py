# import Box2D# from Box2D import *# world = b2World((0, -10)) #default values# #creates the ground# groundBody = world.CreateStaticBody(#     position=(0,-10),
#     shapes=b2PolygonShape(box=(50,10)),#     )# #creating a dynamic body# body = world.CreateDynamicBody(position=(0,4))# #attach polygon fixture
# box = body.CreatePolygonFixture(box=(1,1), density=1)# # Prepare for simulation. Typically we use a time step of 1/60 of a# # second (60Hz) and 6 velocity/2 position iterations. This provides a # # high quality simulation in most game scenarios.
# timeStep = 1.0 / 60# #iteration for values# vel_iters, pos_iters = 6, 2# # This is our little game loop.# for i in range(60):
#     # Instruct the world to perform a single step of simulation. It is#     # generally best to keep the time step and iterations fixed.#     world.Step(timeStep, vel_iters, pos_iters)
#     # Clear applied body forces. We didn't apply any forces, but you
#     # should know about this function.#     world.ClearForces()#     # Now print the position and angle of the body.#     print body.position, body.angle

class Dino:
	def __init__(self, world):
		print('created')

	#draws the dinosaur
	def draw(self, viewer, draw_particles=True):
        for obj in self.drawlist:
            for f in obj.fixtures:
                trans = f.body.transform
                path = [trans*v for v in f.shape.vertices]
                viewer.draw_polygon(path, color=obj.color)
                if "phase" not in obj.__dict__: continue
                a1 = obj.phase
                a2 = obj.phase + 1.2  # radians
                s1 = math.sin(a1)
                s2 = math.sin(a2)
                c1 = math.cos(a1)
                c2 = math.cos(a2)
