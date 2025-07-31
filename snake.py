import pygame
import time
import random
import os
import colorsys

pygame.init()

# Window settings
dis_width = 600
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('🐍 Sweet Snake Game 🍭')

clock = pygame.time.Clock()

snake_block = 10
snake_speed = 12

# Fonts
font_style = pygame.font.SysFont("comicsansms", 25)
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
    value = score_font.render(f"Score: {score}  High Score: {high_score}", True, (255,255,255))
    dis.blit(value, [10, 10])

def draw_gradient_background():
    for y in range(dis_height):
        r = int(100 + (155 * y / dis_height))
        g = int(100 + (80 * y / dis_height))
        b = int(200 - (150 * y / dis_height))
        pygame.draw.line(dis, (r, g, b), (0, y), (dis_width, y))

def our_snake(snake_list):
    for pos in snake_list:
        pygame.draw.rect(dis, (0,0,0), [pos[0], pos[1], snake_block, snake_block])

def message(msg, color):
    mesg = font_style.render(msg, True, color)
    rect = mesg.get_rect(center=(dis_width/2, dis_height/2))
    dis.blit(mesg, rect)

def wait_for_key(msg="Press any key to start"):
    draw_gradient_background()
    message(msg, (255,255,255))
    pygame.display.update()
    waiting = True
    while waiting:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                waiting = False

def gameLoop():
    game_over = False
    pause = False

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

    wait_for_key()

    while not game_over:
        while pause:
            draw_gradient_background()
            message("Paused - Press any key to resume", (255,255,255))
            pygame.display.update()
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    pygame.quit()
                    quit()
                if event.type == pygame.KEYDOWN:
                    pause = False

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if x1_change == 0 and event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif x1_change == 0 and event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif y1_change == 0 and event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif y1_change == 0 and event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0
                elif event.key != pygame.K_LEFT and event.key != pygame.K_RIGHT and event.key != pygame.K_UP and event.key != pygame.K_DOWN:
                    pause = True  # Press any other key to pause

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_over = True

        x1 += x1_change
        y1 += y1_change

        draw_gradient_background()

        # Draw food
        if special_food:
            pygame.draw.rect(dis, (255,0,0), [special_food[0], special_food[1], snake_block, snake_block])
        else:
            pygame.draw.rect(dis, (0,255,0), [foodx, foody, snake_block, snake_block])

        snake_Head = [x1, y1]
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_over = True

        current_score = Length_of_snake - 1
        if current_score > high_score:
            high_score = current_score
            save_high_score(high_score)

        our_snake(snake_List)
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

    draw_gradient_background()
    message("Game Over! Press any key to play again", (255,0,0))
    pygame.display.update()
    
    wait_for_key()
    gameLoop()

gameLoop()
