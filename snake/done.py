import msvcrt
import os
import random
from time import sleep

SIZE_X = 30
SIZE_Y = 20

def initialize_map():
    """Initialize the map for word tracking."""
    map: list[list[str]] = []

    for y in range(SIZE_Y):
        row: list[str] = []
        for x in range(SIZE_X):
            if y == 0 or y == SIZE_Y - 1 or x == 0 or x == SIZE_X - 1:
                row.append("#")
            else:
                row.append(" ")
        map.append(row)

    return map


def print_game():
    os.system("cls" if os.name == "nt" else "clear")
    for y in range(SIZE_Y):
        for x in range(SIZE_X):
            if (x, y) == fruit_position:
                print("X", end="")
            elif (x, y) in snake:
                print("O", end="")
            else:
                print(map[y][x], end="")
        print()


def select_fruit_position():
    while True:
        x = random.randint(1, SIZE_X - 2)
        y = random.randint(1, SIZE_Y - 2)
        if map[y][x] == " " and (x, y) not in snake:
            return (x, y)


def get_direction():
    # Drain the buffer so only the latest keypress is processed
    while msvcrt.kbhit():
        key = msvcrt.getch()
        if key in (b'\x00', b'\xe0'):
            last_key = msvcrt.getch()
            direction = None
            if last_key == b'H':
                direction = (0, -1)
            elif last_key == b'P':
                direction = (0, 1)
            elif last_key == b'K':
                direction = (-1, 0)
            elif last_key == b'M':
                direction = (1, 0)
    # Only return the last detected direction in the buffer
    return direction if 'direction' in locals() else None


def update():
    global fruit_position
    current_head = snake[0]
    new_head = (current_head[0] + direction[0], current_head[1] + direction[1])

    if (
        new_head[0] <= 0
        or new_head[0] >= SIZE_X - 1
        or new_head[1] <= 0
        or new_head[1] >= SIZE_Y - 1
        or new_head in snake
    ):
        print("Game Over!")
        exit()

    snake.insert(0, new_head)

    if new_head == fruit_position:
        fruit_position = select_fruit_position()
    else:
        snake.pop()


map = initialize_map()
snake_head_start_pos = (SIZE_X // 2, SIZE_Y // 2)
snake: list[tuple[int, int]] = [snake_head_start_pos, (snake_head_start_pos[0], snake_head_start_pos[1] - 1)]
direction = (-1, 0)  # Moving up initially
fruit_position = select_fruit_position()


while True:
    new_dir = get_direction()
    if new_dir and new_dir != direction:
        direction = new_dir
    update()
    print_game()
    sleep(0.1)
