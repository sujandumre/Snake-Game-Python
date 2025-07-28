import pygame
import time
import random
import os

pygame.init()

# Colors
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

# Display settings
dis_width = 600
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Snake Game')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 10

# Fonts
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 30)

# High score file
high_score_file = "high_score.txt"

def get_high_score():
    if not os.path.exists(high_score_file):
        with open(high_score_file, "w") as f:
            f.write("0")
    with open(high_score_file, "r") as f:
        return int(f.read())

def save_high_score(score):
    with open(high_score_file, "w") as f:
        f.write(str(score))

def Your_score(score, high_score):
    value = score_font.render(f"Score: {score}  High Score: {high_score}", True, yellow)
    dis.blit(value, [10, 10])

def our_snake(snake_block, snake_list):
    for x in snake_list:
        pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])

def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    high_score = get_high_score()

    foods_eaten = 0
    special_food = None
    special_food_value = 3

    while not game_over:

        while game_close:
            dis.fill(blue)
            message("You Lost! Press C-Play Again or Q-Quit", red)
            Your_score(Length_of_snake - 1, high_score)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT and x1_change == 0:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT and x1_change == 0:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP and y1_change == 0:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN and y1_change == 0:
                    y1_change = snake_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True

        x1 += x1_change
        y1 += y1_change
        dis.fill(blue)

        # Draw food
        if special_food:
            pygame.draw.rect(dis, red, [special_food[0], special_food[1], snake_block, snake_block])
        else:
            pygame.draw.rect(dis, green, [foodx, foody, snake_block, snake_block])

        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        current_score = Length_of_snake - 1
        if current_score > high_score:
            high_score = current_score
            save_high_score(high_score)

        our_snake(snake_block, snake_List)
        Your_score(current_score, high_score)

        pygame.display.update()

        # Check food eaten
        if special_food and x1 == special_food[0] and y1 == special_food[1]:
            Length_of_snake += special_food_value
            foods_eaten = 0
            special_food = None
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
        elif not special_food and x1 == foodx and y1 == foody:
            foods_eaten += 1
            Length_of_snake += 1
            if foods_eaten % 4 == 0:
                special_food = [
                    round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0,
                    round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
                ]
                foodx, foody = None, None
            else:
                foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
                foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
