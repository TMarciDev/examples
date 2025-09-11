import msvcrt
import os
import random
from time import sleep

# Clean up the console
os.system("cls" if os.name == "nt" else "clear")

# Get a random value between 1 and 10
x = random.randint(1, 10)

# Reading the arrow buttons
# Drain the buffer so only the latest keypress is processed
while msvcrt.kbhit():
    key = msvcrt.getch()
    if key in (b'\x00', b'\xe0'):
        last_key = msvcrt.getch()
        direction = None
        if last_key == b'H':  # Up arrow
            pass
        elif last_key == b'P':  # Down arrow
            pass
        elif last_key == b'K':  # Left arrow
            pass
        elif last_key == b'M':  # Right arrow
            pass
# Only return the last detected direction in the buffer
new_dir = direction if 'direction' in locals() else None

# if you want to reassign a value to an external variable
def func():
    global variable

# way to time out, "framerate"
sleep(0.1)
