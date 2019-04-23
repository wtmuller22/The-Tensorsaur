import gym,time, random
import numpy as np
env = gym.make('CartPole-v0')

q_table = np.zeros([env.observation_space.n, env.action_space.n])
#Training the agent
#Hyperparameters
alpha = 0.2
gamma = 0.6
epsilon = 0

for i in range(1, 10001):
    state = env.reset()

    epochs, penalties, reward, = 0, 0, 0
    done = False

    while not done:
        env.render()
        if random.uniform(0, 1) < epsilon:
            action = env.action_space.sample() # Explore action space
        else:
            action = np.argmax(q_table[state]) # Exploit learned values

        next_state, reward, done, info = env.step(action)

        old_value = q_table[state, action]
        next_max = np.max(q_table[next_state])

        new_value = (1 - alpha) * old_value + alpha * (reward + gamma * next_max)
        q_table[state, action] = new_value

        if reward < 0:
            penalties += 1

        state = next_state
        epochs += 1

"""
#in frame 200, jump
for i in range(500):
    if(i == 204):
        env.step(1)
    elif(i >= 300 and i < 350):
        env.step(2)
    else:
        env.step(0)
    env.render()
"""
