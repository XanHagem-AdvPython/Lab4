"""
Alex Hagemeister
Lab 4: Web API, Multithreading, Multiprocessing, OS, JSON Review, and GUI
CIS 41B, Spring 2023

lab4thread.py:

This file is a modified version of lab4.py that introduces multithreading to improve performance.
It includes the same GUI window class as lab4.py.

The tasks in lab4thread.py include:
    - Utilizing multithreading to make API calls for each state simultaneously.
    - Displaying the status message (state name and number of parks) as each thread finishes fetching data.
    - Recording the time taken to retrieve data for the same states as in lab4.py.

After lab4.py works to specs, make a copy of it and name it lab4thread.py, then change the code to use multithreading.

1. For each API call in step 3 of lab4.py above:
- Create a thread to request data from the API.
- Save the Response data in the same container as lab4.py


2. As each thread finished fetching the data, use the label at the bottom of the window to display the state name and
the number of parks there are in the state.
- The number of parks is the “total” field in the NPS JSON structure.
- Note that the status message for each state should show up as each thread is finished, don't print all the status
messages at the very end when all threads are done.

Window A

The user chose California and Delaware, 
and because California appears before Delaware 
in the list of states, the thread for California
started before the thread for Delaware.

window B 

Yet Delaware status appears first because Delaware has fewer parks
and can finish faster than California

3. Add code to record the time it takes to get the data from the NPS API, for the same states that you used in lab4.py.
Be careful where you put the timer code so that the time is for downloading the data from the NPS.
    
"""

import tkinter as tk
from tkinter import messagebox, filedialog
import urllib.request, json
import time
import os
import threading
