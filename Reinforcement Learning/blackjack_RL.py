import gym
from gym import wrappers
env = gym.make('Blackjack-v0')
from agent_rl import *

num_rounds = 1000 
num_samples = 50 


num_episodes_values = range(200, 2200, 200)
               
for num_episodes_value in num_episodes_values:
    total_payout = 0 
    average_payouts = [] 
    agent = Agent(env=env, epsilon=1.0, alpha=0.8, gamma=0.9, num_episodes_to_train=num_episodes_value)

    observation = env.reset()
    for sample in range(num_samples):
        round = 1
        
        while round <= num_rounds:
            action = agent.choose_action(observation)
            next_observation, payout, is_done, _ = env.step(action)
            agent.learn(observation, action, payout, next_observation)
            total_payout += payout
            observation = next_observation
            if is_done:
                observation = env.reset()
                round += 1
                average_payouts.append(total_payout/(sample*num_rounds + round))

        print ("Average payout after {} rounds after training for {} episodes is {}".format(num_rounds, num_episodes_value, total_payout/(num_samples)))


env.close()