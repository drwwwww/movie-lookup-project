import requests
from colorama import init, Fore, Back, Style
import json
import os
from dotenv import load_dotenv

init()

load_dotenv

key = os.getenv("OMDbkey")
