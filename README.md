# language_robot_control
Using language for robot control.

To get started, create a file `openai_api_key.txt` and paste your key. Make sure this file is saved as per this exact file name (as this is what is included in `.gitigore`), as you would **never** want to push your API key to a public repository! You can also save this somewhere else (e.g. your Desktop) and modify the script accordingly. 

Once you have an API key set up, you can then test some of the examples below.

### Open-loop control
Run `example.py` to test the language controller on a dummy 2D grid environment doing open-loop control. This dummy environment simply consists of an agent and a goal randomly placed on a grid, and policy options for `(move up, move down, move left, move right)`. In most cases, the answer should be correct! Although the LLM is not guaranteed to provide a correct answer, particularly for long sequences (in this example we open-loop control in language space, but we could modify it to do closed-loop control). A sample output for this environment is (including the full `Response` returned by the OpenAI API):

![language_control_grid](https://user-images.githubusercontent.com/46450880/221913170-4b85cd52-eadf-41cb-9a25-3b6e3fa15063.png)

As you can see, the robot reaches the goal by following the open-loop plan!

### Closed-loop control
We can also run `example_closed_loop.py` to run the dummy 2D grid environment doing closed-loop control in language space. To do this, we query the LLM to produce a high-level plan at every environment step (instead of only quering the model at the initial step), and at each step we execute the first step in the plan only. Here is an example of the output should should expect (replanning at each step makes the output very long! and the script more costly to run!):

![language_control_grid_closed_loop1](https://user-images.githubusercontent.com/46450880/221918994-61f07fc0-9c20-4ce7-b97f-b34d8add984a.png)
![language_control_grid_closed_loop2](https://user-images.githubusercontent.com/46450880/221919037-be082811-9903-4bcc-b80a-c4b975ef7f18.png)

As you can see, the robot also reaches the goal. Quering the LLM for a high-level plan does not always yield the correct answer, therefore doing closed-loop control might not yield an optimal solution in terms of minimum number of steps, but it should be more robust to incorrect high-level plans provided by the LLM as it can re-plan at every step.  
