import gym
import numpy as np
import matplotlib.pyplot as plt
import time 

def get_action(observation, agent): 
    product = observation.dot(agent) # [1,2,3,4] * [1,1,1,1] = 1 + 2 + 3 + 4 = 10
    return 1 if product > 0 else 0 

def play_one_episode(agent, env):
    # Variables
    total_reward = 0
    run = 0 
    observation, info = env.reset(seed=42)
    terminated = False

    while not terminated and run < 100:
        action = get_action(observation, agent)
        observation, reward, terminated, truncated, info = env.step(action)
        
        total_reward += reward
        run += 1
        
        if terminated or truncated: 
            env.reset()

    print(f'terminated with a score of: {total_reward}')
    return total_reward

def train(env): 
    best_agent = None
    high_score = 0

    for _ in range(3):
        new_agent = new_agent = np.random.random(4)*2 - 1
        reward = play_one_episode(agent=new_agent, env=env)
        
        if(reward > high_score):
            high_score = reward 
            best_agent = new_agent

    return best_agent, high_score

env = gym.make("CartPole-v1", render_mode="human")
best_agent, high_score = train(env)
print(best_agent, high_score)

print("Playing with best agent")
time.sleep(5)
play_one_episode(best_agent,env=env)