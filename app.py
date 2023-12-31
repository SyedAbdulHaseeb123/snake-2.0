from tkinter import *
import random

GAME_WIDTH = 500
GAME_HEIGHT = 500
SPEED = 200
SPACE_SIZE = 50
BODY_PARTS = 3
SNAKE_COLOUR = 'green'
FOOD_COLOUR = 'red'
BACKGROUND_COLOUR = 'black'

class Snake:
    def __init__(self):
        self.body_size = BODY_PARTS
        self.coordinates = [(0, 0) for _ in range(BODY_PARTS)]
        self.squares = [canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOUR, tags='snake') for x, y in self.coordinates]

class Food:
    def __init__(self):
        x = random.randint(0, (GAME_WIDTH // SPACE_SIZE) - 1) * SPACE_SIZE
        y = random.randint(0, (GAME_HEIGHT // SPACE_SIZE) - 1) * SPACE_SIZE
        self.coordinates = [x, y]
        canvas.create_oval(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=FOOD_COLOUR, tags='food')

def next_turn(snake, food):
    x, y = snake.coordinates[0]

    if direction == 'up':
        y -= SPACE_SIZE
    elif direction == 'down':
        y += SPACE_SIZE
    elif direction == 'left':
        x -= SPACE_SIZE
    elif direction == 'right':
        x += SPACE_SIZE

    snake.coordinates.insert(0, (x, y))
    square = canvas.create_rectangle(x, y, x + SPACE_SIZE, y + SPACE_SIZE, fill=SNAKE_COLOUR)
    snake.squares.insert(0, square)

    if x == food.coordinates[0] and y == food.coordinates[1]:
        global score
        score += 1
        label.config(text=f'Score: {score}')
        canvas.delete('food')

        food = Food()
    else:
        del snake.coordinates[-1]
        canvas.delete(snake.squares[-1])
        del snake.squares[-1]

    if check_collisions(snake):
        game_over()
    else:
        window.after(SPEED, next_turn, snake, food)

def change_direction(new_direction):
    global direction
    if new_direction in {'up', 'down', 'left', 'right'}:
        if (new_direction == 'left' and direction != 'right') or \
           (new_direction == 'right' and direction != 'left') or \
           (new_direction == 'up' and direction != 'down') or \
           (new_direction == 'down' and direction != 'up'):
            direction = new_direction

def check_collisions(snake):
    x, y = snake.coordinates[0]
    if x < 0 or x >= GAME_WIDTH or y < 0 or y >= GAME_HEIGHT:
        print('game over')
        return True
    return False

def game_over():
    pass

window = Tk()
window.title('Snakegame')

score = 0
direction = 'down'

label = Label(window, text=f'Score: {score}')
label.pack()

canvas = Canvas(window, bg=BACKGROUND_COLOUR, height=GAME_HEIGHT, width=GAME_WIDTH)
canvas.pack()

window.update()

window_width = window.winfo_width()
window_height = window.winfo_height()
screen_width = window.winfo_screenwidth()
screen_height = window.winfo_screenheight()

x = int((screen_width / 4) - (window_width / 4))
y = int((screen_height / 4) - (window_height / 4))

window.bind('<Left>', lambda event: change_direction('left'))
window.bind('<Right>', lambda event: change_direction('right'))
window.bind('<Up>', lambda event: change_direction('up'))
window.bind('<Down>', lambda event: change_direction('down'))

snake = Snake()
food = Food()
next_turn(snake, food)

window.mainloop()