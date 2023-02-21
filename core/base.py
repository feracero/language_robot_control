import openai
from abc import ABC, abstractmethod

class RobotManager(ABC):
    """
    An abstract base class for managing high-level control of robots using OpenAI's language model.
    """

    def __init__(self, api_key):
        """
        Initialize the RobotManager with the OpenAI API key.
        """
        openai.api_key = api_key

    @abstractmethod
    def generate_steps(self, goal):
        """
        Generate a list of low-level steps to achieve a high-level goal using OpenAI's language model.

        Args:
            goal (str): The high-level goal to achieve.

        Returns:
            list: A list of low-level steps to achieve the high-level goal.
        """
        pass

    @abstractmethod
    def execute_step(self, step):
        """
        Execute a low-level step to achieve a high-level goal.

        Args:
            step (str): The low-level step to execute.
        """
        pass

    def achieve_goal(self, goal):
        """
        Break down a high-level goal into low-level steps and execute them to achieve the goal.

        Args:
            goal (str): The high-level goal to achieve.
        """
        # Generate the list of low-level steps to achieve the goal
        steps = self.generate_steps(goal)

        # Execute each step in order
        for step in steps:
            self.execute_step(step)
