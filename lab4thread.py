import threading
import tkinter as tk
import tkinter.messagebox as tkmb
import sqlite3
import webbrowser
import numpy as np
import requests
from bs4 import BeautifulSoup
import json
import sqlite3
from collections import defaultdict
import os
import multiprocessing as mp
import urllib.request, json


# Configure API request
endpoint = "https://developer.nps.gov/api/v1/parks?stateCode=me"
HEADERS = {"X-Api-Key":"UpWtvWDtfA5WOBOzzSpvzId1FHi6MbLjdzhXpK3I"}
req = urllib.request.Request(endpoint,headers=HEADERS)
# Additional code would follow