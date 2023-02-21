import numpy as np
from robots.dummy import FourDirectionRobotManager

# Read the API key from a text file
with open("openai_api_key.txt", "r") as f:
    api_key = f.read().strip()

# Instantiate the FourDirectionRobotManager class
robot_manager = FourDirectionRobotManager(api_key=api_key)

# Define the high-level goal
goal = "Reach the goal location"

# Define the grid size
grid_size = 6

# Randomly place the robot and the goal in the grid
robot_position = np.random.randint(grid_size, size=2)
goal_position = np.random.randint(grid_size, size=2)

# Describe the goal location relative to the robot in natural language
if goal_position[0] < robot_position[0]:
    vert_direction = "up"
elif goal_position[0] > robot_position[0]:
    vert_direction = "down"
if goal_position[1] < robot_position[1]:
    horiz_direction = "left"
elif goal_position[1] > robot_position[1]:
    horiz_direction = "right"

if goal_position[0]==robot_position[0]:
    vert_direction = "away"
if goal_position[1]==robot_position[1]:
    horiz_direction = "away"

# environment_description = f"The robot is at position {robot_position} and the goal is at position {goal_position}."
goal_description = f"The goal is {abs(goal_position[0] - robot_position[0])} steps {vert_direction} and {abs(goal_position[1] - robot_position[1])} steps {horiz_direction} from the robot."
if vert_direction=="away" and horiz_direction=="away":
    goal_description = f"The goal is at the robot's current position."

# Generate a list of low-level steps to achieve the high-level goal
# steps = robot_manager.generate_steps(environment_description, goal)
steps = robot_manager.generate_steps(goal_description, goal)
# steps = robot_manager.generate_steps(environment_description+goal_description, goal)

# Print the initial grid
grid = np.zeros((grid_size, grid_size), dtype=str)
grid[robot_position[0], robot_position[1]] = "o"
grid[goal_position[0], goal_position[1]] = "x"
print("Initial grid:")
print(grid)

def step_robot_position(robot_position, step):
    """
    Update the robot's position based on the low-level step taken.

    Args:
        robot_position (ndarray): The robot's current position.
        step (str): The low-level step taken.

    Returns:
        list: The robot's updated position.
    """
    if step == "Move the robot up":
        robot_position[0] -= 1
    elif step == "Move the robot down":
        robot_position[0] += 1
    elif step == "Move the robot left":
        robot_position[1] -= 1
    elif step == "Move the robot right":
        robot_position[1] += 1
    return robot_position

# Take each step and print the updated grid
for step in steps:
    robot_manager.execute_step(step)
    robot_position = step_robot_position(robot_position, step)
    grid = np.zeros((grid_size, grid_size), dtype=str)
    grid[robot_position[0], robot_position[1]] = "o"
    grid[goal_position[0], goal_position[1]] = "x"
    print(f"Grid after taking step '{step}':")
    print(grid)
