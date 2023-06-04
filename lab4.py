"""
Alex Hagemeister
Lab 4: Web API, Multithreading, Multiprocessing, OS, JSON Review, and GUI
CIS 41B, Spring 2023

lab4.py:

The starting point and the base implementation of the application. 
It contains a GUI window class that allows the user to select states and parks for their vacation planning.

Tasks: 
    - Presenting a list of states for the user to choose from (up to 5 states).
    - Displaying a list of parks in the selected states for the user to choose from.
    - Saving the chosen park data of each state in separate files named after the states.
    - Providing error handling for invalid user inputs.
    - Recording the time taken to retrieve data for specific states.

### A. Overview

Lab4.py has one GUI window class which is a Tk window.
The window does 3 tasks one after another:
- present the user with a list of states so the user can choose up to 5 states
- for all states that the user chooses, present the user with a list of parks in the states 
  so the user can choose their parks
- save data of the chosen parks of each state in a file that’s the state name

Before diving into multithreading and multiprocessing, it’s best to get the lab to work in a single thread first.

### B. Details

1. Let the user choose 1-5 states. The window has these components:

- A title for the window, such as NPS or Parks, etc.
- A name for the app. Feel free to use your own wording, font type, color, size ,etc.
- A prompt that asks the user to select up to 5 states from the listbox. 
    - Make the 5 a class attribute so it can be changed easily.
- The listbox can display 10 items at a time and is 40-50 chars in width.
    - It has a scrollbar so the user can scroll through all 50 states.
    - The state names come from the states_hash.json file.
- The user clicks the Submit button to lock in the choice of states. 
    - Feel free to change the text, font, color for the button.
- A blank label at the bottom for status messages later.  


2. When the user clicks the Submit button, check that the user has made 1 - 5 choices, inclusive, from the listbox.
If there are not 1-5 choices, pop up a messagebox to display an error message, then wait for the user to choose
again.

3. When the user has submitted 1-5 choices, make the API call for each choice, and save the Response data of all the
chosen states in a container of your choice.

4. Let the user choose their parks from your data container.
Some of the window widgets change to show the parks:
   - The prompt now asks the user to select one or more parks.
   - The listbox shows all the parks for each state that the user chose. 
     - The format is: state name: park name
     - The park name is the “name” field of the NPS JSON structure.
   - The button text changes to let the user know it’s for saving data to file.
   - The label shows that 2 states were chosen.  
  

`(Hint while debugging: the 2 example states only have a few parks, so you can easily view both in the listbox)`


5. When the user clicks the Save button, check that there is at least 1 choice from the listbox.
If not, pop up a messagebox to display a “no park chosen” message, then wait for the user to choose again.

6. If the user makes at least 1 choice, pop up a file dialog window to let the user choose a directory to save the output
file. The default directory of the file dialog window is the user’s current directory.

7. If the user doesn’t choose a directory, clear the user’s selection from the listbox and wait for the user to choose
their parks again.

To clear the listbox, use: LB.selection_clear(0, tk.END) where LB is the listbox object.

8. If the user chooses a directory, create a JSON file for each state that the user chose:
   - The name of the file is the state name.
   - In each JSON file is a list of the parks that the user chose.
   - Each park is a dictionary with the following fields (from the NPS JSON file):
     - full name
     - description
     - activities (as a comma separated list)
     - url

10. After the file(s) are written, show a confirmation messagebox to let the user know the filename(s).
- Confirmation messagebox after the user chose parks from Nevada and New Hampshire.

When the user clicks OK on the messagebox or clicks to close the messagebox, the app ends.

11.  Add code to record the time it takes to get the data from the NPS API, for 3-5 of states. 
- Be careful where you put the timer code so that the time is only for downloading the data from the NPS.

While working with the listbox, there are 2 more listbox methods that could be useful, in addition to the ones
already in the class notes: 
- LB.selection_clear(0, tk.END) to clear the user selections in the listbox
- LB.get(0, tk.END) to get all the items that are shown in the listbox

"""

import tkinter as tk
from tkinter import messagebox, filedialog
import urllib.request, json
import time
import os

# Configure API request
endpoint = "https://developer.nps.gov/api/v1/parks?stateCode=me"
HEADERS = {"X-Api-Key":"UpWtvWDtfA5WOBOzzSpvzId1FHi6MbLjdzhXpK3I"}
req = urllib.request.Request(endpoint,headers=HEADERS)
