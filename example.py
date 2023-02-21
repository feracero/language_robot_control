import numpy as np
from robot_manager import FourDirectionRobotManager

# Read the API key from a text file
with open("openai_api_key.txt", "r") as f:
    api_key = f.read().strip()

# Instantiate the FourDirectionRobotManager class
robot_manager = FourDirectionRobotManager(api_key=api_key)

# Define the high-level goal
goal = "Reach the goal location"

# Define the grid size
grid_size = 5

# Randomly place the robot and the goal in the grid
robot_position = np.random.randint(grid_size, size=2)
goal_position = np.random.randint(grid_size, size=2)

# Describe the goal location relative to the robot in natural language
if goal_position[0] < robot_position[0]:
    direction = "up"
elif goal_position[0] > robot_position[0]:
    direction = "down"
elif goal_position[1] < robot_position[1]:
    direction = "left"
elif goal_position[1] > robot_position[1]:
    direction = "right"
else:
    direction = "at"

goal_description = f"The goal is {abs(goal_position[0] - robot_position[0])} steps {direction} and {abs(goal_position[1] - robot_position[1])} steps away from the robot."

# Generate a list of low-level steps to achieve the high-level goal
steps = robot_manager.generate_steps(goal)

# Print the goal and the list of steps
print(goal)
print(goal_description)
print("Steps:")
for step in steps:
    print(step)
