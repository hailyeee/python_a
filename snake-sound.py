import turtle
import random
import winsound  # Windows-specific sound module

# Set up the game window
window = turtle.Screen()
window.bgcolor("black")
window.title("Snake Game")

# Create the snake
snake = turtle.Turtle()
snake.speed(0)
snake.shape("square")
snake.color("white")
snake.penup()
snake.goto(0, 0)
snake.direction = "stop"
segments = []

# Create the food
food = turtle.Turtle()
food.speed(0)
food.shape("circle")
food.color("red")
food.penup()
food.goto(0, 100)

# Keep track of the score
score = 0
high_score = 0
score_pen = turtle.Turtle()
score_pen.speed(0)
score_pen.color("white")
score_pen.penup()
score_pen.goto(0, 260)
score_pen.write("Score: 0  High Score: 0", align="center", font=("Courier", 24, "normal"))

# Functions to move the snake
def go_up():
    if snake.direction != "down":
        snake.direction = "up"

def go_down():
    if snake.direction != "up":
        snake.direction = "down"

def go_left():
    if snake.direction != "right":
        snake.direction = "left"

def go_right():
    if snake.direction != "left":
        snake.direction = "right"

def move():
    if snake.direction == "up":
        y = snake.ycor()
        snake.sety(y + 20)
    if snake.direction == "down":
        y = snake.ycor()
        snake.sety(y - 20)
    if snake.direction == "left":
        x = snake.xcor()
        snake.setx(x - 20)
    if snake.direction == "right":
        x = snake.xcor()
        snake.setx(x + 20)

    # Move the end segments first in reverse order
    for index in range(len(segments)-1, 0, -1):
        x = segments[index-1].xcor()
        y = segments[index-1].ycor()
        segments[index].goto(x, y)

    # Move the segment at the front of the snake
    if len(segments) > 0:
        x = snake.xcor()
        y = snake.ycor()
        segments[0].goto(x, y)

    # Play a sound effect when the snake moves
    winsound.PlaySound("SystemExit", winsound.SND_ALIAS)

# Keyboard bindings
window.listen()
window.onkey(go_up, "Up")
window.onkey(go_down, "Down")
window.onkey(go_left, "Left")
window.onkey(go_right, "Right")

# Main game loop
while True:
    window.update()

    # Check for a collision with the border
    if snake.xcor() > 290 or snake.xcor() < -290 or snake.ycor() > 290 or snake.ycor() < -290:
        snake.goto(0, 0)
        snake.direction = "stop"
        for segment in segments:
            segment.goto(1000, 1000)
        segments.clear()
        score = 0
        score_pen.clear()
        score_pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    # Check for a collision with the food
    if snake.distance(food) < 20:
        # Play a sound effect when the snake eats the food
        winsound.PlaySound("SystemExit", winsound.SND_ALIAS | winsound.SND_LOOP)

        x = random.randint(-270, 270)
        y = random.randint(-270, 270)
        food.goto(x, y)
        new_segment = turtle.Turtle()
        new_segment.speed(0)
        new_segment.shape("square")
        new_segment.color("white")
        new_segment.penup()
        segments.append(new_segment)
        score += 10
        if score > high_score:
            high_score = score
        score_pen.clear()
        score_pen.write(f"Score: {score}  High Score: {high_score}", align="center", font=("Courier", 24, "normal"))

    # Move the snake
    move()

    # Only add a new segment when the snake eats the food
    if len(segments) > 0:
        for index in range(len(segments)-1, 0, -1):
            x = segments[index-1].xcor()
            y = segments[index-1].ycor()
            segments[index].goto(x, y)

    # Delay
    turtle.time.sleep(0.1)