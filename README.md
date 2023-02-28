# language_robot_control
Using language for robot control.

To get started, create a file `openai_api_key.txt` and paste your key. Make sure this file is saved as per this exact file name (as this is what is included in `.gitigore`), as you would **never** want to push your API key to a public repository! You can also save this somewhere else (e.g. your Desktop) and modify the script accordingly. 

Once you have an API key set up, you can then run example.py to test the language controller on a dummy 2D grid environment. This dummy environment simply consists of an agent and a goal randomly placed on a grid, and policy options for `(move up, move down, move left, move right)`. In most cases, the answer should be correct! Although the LLM is not guaranteed to provide a correct answer, particularly for long sequences (this example is open-loop control in language space, but we could modify it to do closed-loop control). A sample output for this environment is (including the full `Response` returned by the OpenAI API):

![language_control_grid](https://user-images.githubusercontent.com/46450880/221913170-4b85cd52-eadf-41cb-9a25-3b6e3fa15063.png)
