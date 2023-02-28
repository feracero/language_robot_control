import openai
from core.base import RobotManager

class FourDirectionRobotManager(RobotManager):
    """
    A class for managing high-level control of a robot that can move in four directions using OpenAI's language model.
    """

    def __init__(self, api_key):
        super().__init__(api_key)

        # Initialize the low-level policies and goals for the robot
        self.policies = {
            "move_up": "Move the robot up",
            "move_down": "Move the robot down",
            "move_left": "Move the robot left",
            "move_right": "Move the robot right",
        }
        self.goals = {
            "reach_goal": "Reach the goal location",
        }

    def generate_steps(self, environment, goal):
        """
        Generate a list of low-level steps to achieve a high-level goal using OpenAI's language model.

        Args:
            environment (str): The description of the environment state.
            goal (str): The high-level goal to achieve.

        Returns:
            list: A list of low-level steps to achieve the high-level goal.
        """
        # Create a prompt that lists the available low-level policies as options for each step
        prompt = f"Consider the following environment: '{environment}'.\n"
        prompt += "List all the steps required to achieve the robot to arrive to the goal location. For each step, choose one of the following policies: \n"
        prompt += "\n".join([f"{i+1}. {policy}" for i, policy in enumerate(self.policies.values())])
        prompt += "\n"
        prompt += "Make sure you provide sufficient steps for the robot to achieve the goal."

        print("Prompt: ", prompt)

        # Use OpenAI's language model to generate a list of steps for achieving the goal
        response = openai.Completion.create(
            engine="text-davinci-002", 
            # # engine="text-curie-001", 
            prompt=prompt,
            max_tokens=1024,
            n=1,
            stop=None,
            temperature=0.5,
        )

        print("Response: ", response)

        # Extract the generated steps from the response
        steps = response.choices[0].text.strip().split("\n")

        # Remove the policy choices from the generated steps
        steps = [step.split(".", 1)[1].strip() for step in steps]

        # Return the list of generated steps
        return steps

    def execute_step(self, step):
        """
        Execute a low-level step to achieve a high-level goal.

        Args:
            step (str): The low-level step to execute.
        """
        # Execute the appropriate low-level policy for the step
        if step == self.policies["move_up"]:
            self.move_up()
        elif step == self.policies["move_down"]:
            self.move_down()
        elif step == self.policies["move_left"]:
            self.move_left()
        elif step == self.policies["move_right"]:
            self.move_right()

    def move_up(self):
        """
        Move the robot up.
        """
        print("Moving the robot up.")

    def move_down(self):
        """
        Move the robot down.
        """
        print("Moving the robot down.")

    def move_left(self):
        """
        Move the robot left.
        """
        print("Moving the robot left.")

    def move_right(self):
        """
        Move the robot right.
        """
        print("Moving the robot right.")
