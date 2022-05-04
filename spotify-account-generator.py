import os
import time
import string
from termcolor import colored
from os import system
from time import sleep
try:
 import pynput
except ImportError:
  os.system('python -m pip install pynput')
import pynput
from pynput.keyboard import Key, Controller

system("title " + "Spotify Account Generator - Deep Tools©")

def clearConsole():
    command = 'clear'
    if os.name in ('nt', 'dos'):  
        command = 'cls'
    os.system(command)

clearConsole()

print("")
time.sleep(0.03)
print("")
time.sleep(0.03)
print(colored("              ██████╗ ███████╗███████╗██████╗   ████████╗ █████╗  █████╗ ██╗      ██████╗","red"))
time.sleep(0.03)
print(colored("              ██╔══██╗██╔════╝██╔════╝██╔══██╗  ╚══██╔══╝██╔══██╗██╔══██╗██║     ██╔════╝","red"))
time.sleep(0.03)
print(colored("              ██║  ██║█████╗  █████╗  ██████╔╝     ██║   ██║  ██║██║  ██║██║     ╚█████╗    ","red"))
time.sleep(0.03)
print(colored("              ██║  ██║██╔══╝  ██╔══╝  ██╔═══╝      ██║   ██║  ██║██║  ██║██║      ╚═══██╗   ","red"))
time.sleep(0.03)
print(colored("              ██████╔╝███████╗███████╗██║          ██║   ╚█████╔╝╚█████╔╝███████╗██████╔╝   ","red"))
time.sleep(0.03)
print(colored("              ╚═════╝ ╚══════╝╚══════╝╚═╝          ╚═╝    ╚════╝  ╚════╝ ╚══════╝╚═════╝    ","red"))
time.sleep(0.03)
print("")
time.sleep(0.03)
print("")

print(colored(" Buy Here: https://deeptools.xyz/ ","red"))
print("")
print(colored(" Discord / Support Server: https://discord.gg/JYvpJ6dh5D ","red"))

os.system("start \"\" https://deeptools.xyz/")