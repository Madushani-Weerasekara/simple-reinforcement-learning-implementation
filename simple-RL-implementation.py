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
        return[0, 1] # List of possible actions
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
        self.steps_left -+ 1
        return random.random() # Return a random reward between 0 and 1
    
         