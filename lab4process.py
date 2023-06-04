"""
Alex Hagemeister
Lab 4: Web API, Multithreading, Multiprocessing, OS, JSON Review, and GUI
CIS 41B, Spring 2023

lab4process.py:

This file is another modified version of lab4.py that utilizes multiprocessing for faster data retrieval.
It also includes the same GUI window class as lab4.py.

The tasks in lab4process.py include:
    - Replacing the multithreading code with multiprocessing Pool to make API calls concurrently.
    - Displaying the status message (state name and number of parks) as each process finishes fetching data.
    - Recording the time taken to retrieve data for the same states as in lab4.py and lab4thread.py.
    - Refactoring the function that the processes run into a global function to facilitate multiprocessing.

Make a copy of lab4thread.py file and save it as lab4process.py, then change the code to use multiprocessing.

1. Change all multithreading code to multiprocessing code:
- Remove the multithreading code and replace with a multiprocessing Pool.
- To minimize the code dissection and keep the later part of the app the same, 
it would be best to store all the Response data in the same container that was used for lab4.py and lab4threading.py.

2. For the window, the label at the bottom is now the same “Fetching data for N states” as with lab4.py.

3. The function that the processes will run should be removed from the window class and turned into a global function
so that the process can access it.

4. Add code to record the time it takes to get the data from the NPS API, for the same states that you used in lab4.py
and lab4threading.py. Be careful where you put the timer code so that the time is for downloading the data from
the NPS.

---

## Step 5: Analysis

At the end of lab4process.py, add a comment block to discuss your time measurements:
- Show the order from slowest to fastest between the 3 ways to fetch data: serial, threads, processes.
- Explain why they are in that order.

"""

import tkinter as tk
from tkinter import messagebox, filedialog
import urllib.request, json
import time
import os
from multiprocessing import Pool
