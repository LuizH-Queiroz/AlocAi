import os
import time

def clear_sleep(t=0.5):
  time.sleep(t)
  os.system('cls' if os.name == 'nt' else 'clear')