import random
from typing import List

# Define a class for a sample nevironment
class SampleEnvironment:
    def __init__(self):
        """
        Initialize the environment with a predefined number of steps.
        """
        self.steps_left = 20 # Total steps available in the environment

    def get_observation(self)->List[float]:
        """
        Return the list of possible actions in the environment.
        In this case, there are two possible actions: 0 and 1.
        """
        return[0.0, 0.0, 0.0] # List of possible actions
    def get_actions(self)->List[int]:
        """
        Return the list of possible actions in the environment.
        In this case, there are two possible actions: 0 and 1.
        """
        return[0, 1]
    def is_done(self)->bool:
        """
        Check if the environment is finished.
        The environment is done when no steps are left.
        """
        return self.steps_left == 0 # Return True if no steps are left
    def action(self, action:int)->float:
        """
        Perform an action in the environment and return a reward.
        If the environment is already done, raise an exception.
        Otherwise, decrement the steps left and return a random reward.
        
        :param action: The action to be taken
        :return: A random float value as the reward
        """

        if self.is_done():
            raise Exception("Game is over")  # Raise an exception if no steps are left
        self.steps_left -= 1
        return random.random() # Return a random reward between 0 and 1
    

# Define a class for an agent that interacts with the environment
class Agent:
    def __init__(self):
        """
        Initialize the agent with a total reward of 0.0.
        """
        self.total_reward = 0.0 # Initialize total reward

    def steps(self, env:SampleEnvironment):
        """
        Perform a single step in the environment.
        This includes observing the environment, deciding an action,
        executing it, and updating the total reward.

        :param env: The environment in which the agent is acting
        """
        # Get the current observation from the environment
        current_obs = env.get_observation()
        print("Observation", current_obs) # Print the current observation

        # Get the list of possible actions from the environment
        actions = env.get_actions()
        print(actions) # Print the possible actions

        reward = env.action(random.choice(actions))

        # Add the received reward to the agent's total reward
        self.total_reward += reward
        print(f"Reward received this step: {reward:.4f}")

if __name__ == "__main__":
    """
    Entry point of the program. Initializes the environment and the agent,
    and runs the agent in the environment until the environment is done.
    """
    # Create an instance of the environment
    env = SampleEnvironment()

    # Create an instance of the Agent
    agent = Agent()

    i = 0

    # Run the agent in the environment until the environment signals it's done
    while not env.is_done():
        i = i+1
        print("Steps {}".format(i))
        # Perform a step in the environment
        agent.steps(env)
        # Print cumulative total reward
        print(f"Total reward so far: {agent.total_reward:.4f}\n")

    # Print the total reward accumulated by the agent
    print("Total reward got: %.4f" % agent.total_reward)