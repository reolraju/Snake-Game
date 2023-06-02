from turtle import Screen
from snake import Snake
from food import Food
from score import Score
import time

screen = Screen()
screen.bgcolor("black")
screen.setup(600, 600)
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Score()

screen.listen()

screen.onkey(snake.right, "Right")
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.down, "Down")

is_move = True

while is_move:
    screen.update()
    time.sleep(0.1)
    snake.move()

    if snake.head.distance(food) < 15:
        print("nom nom nom")
        food.refresh()
        score.inc_score()
        snake.extend()

    if snake.head.xcor() < -290 or snake.head.xcor() > 290 or snake.head.ycor() < -290 or snake.head.ycor() > 290:
        score.reset()
        snake.reset()


    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            score.reset()
            snake.reset()



screen.exitonclick()
