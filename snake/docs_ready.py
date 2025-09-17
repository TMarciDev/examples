import msvcrt
import os
import random
from time import sleep

# Clean up the console
os.system("cls" if os.name == "nt" else "clear")

# Get a random value between 1 and 10
x = random.randint(1, 10)

# Reading the arrow buttons
direction = None
while msvcrt.kbhit():
    key = msvcrt.getch()
    if key in (b'\x00', b'\xe0'):
        last_key = msvcrt.getch()
        direction = None
        if last_key == b'H':  # Up arrow
            direction = "Up arrow was pressed"
        elif last_key == b'P':  # Down arrow
            direction = "Down arrow was pressed"
        elif last_key == b'K':  # Left arrow
            direction = "Left arrow was pressed"
        elif last_key == b'M':  # Right arrow
            direction = "Right arrow was pressed"
print(direction)

# way to time out, set the "framerate"
sleep(0.1)
