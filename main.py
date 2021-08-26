#import packages
import pygame 
import random
import time

pygame.init()
#colors used
white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)

#dimensions of the display
dis_width = 600
dis_height = 400
dis = pygame.display.set_mode((dis_width, dis_height))
#captions for the game
pygame.display.set_caption("snake")
#timer for the game
clock = pygame.time.Clock()
#snake
snake_block = 10
snake_speed = 15
#font
font_style = pygame.font.SysFont("bahnschrift", 25)
score_font = pygame.font.SysFont("comicsansms", 35, True)

#The score of the game
def Your_score(score):
  value = score_font.render("Your score: "+ str(score), True, yellow)
  dis.blit(value, [0,0])

#appearance of the snake
def our_snake(snake_block, snake_list):
  for x in snake_list:
    pygame.draw.rect(dis, black, [x[0], x[1], snake_block, snake_block])

#messages for the game
def message(msg, color):
  mesg = font_style.render(msg, True, color)
  dis.blit(mesg, [dis_width / 6, dis_height / 3])

#the main piece of code to run the game
def gameLoop():
    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    snake_List = []
    Length_of_snake = 1

    #randomly places food in different areas of the grid
    foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
    foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0

    #code for quit game
    while not game_over:
        while game_close == True:
            dis.fill(green)
            message("Press 'C' to Play Again or Press 'Q' to Quit", blue)
            Your_score(Length_of_snake - 1)
            pygame.display.update()

            #setting up keys to move the snake
            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_q:
                        game_over = True
                        game_close = False
                    if event.key == pygame.K_c:
                        gameLoop()

        #setting up movement keys
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -snake_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = snake_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -snake_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = snake_block
                    x1_change = 0

        #the movement of the snake
        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            if x1 >= dis_width:
                x1 = 0
            elif x1 < 0:
                x1 = dis_width
            elif y1 >= dis_height:
                y1 = 0
            elif y1 < 0:
                y1 = dis_height

            #game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.fill(green)
        pygame.draw.rect(dis, red, [foodx, foody, snake_block, snake_block])
        snake_Head = []
        snake_Head.append(x1)
        snake_Head.append(y1)
        snake_List.append(snake_Head)
        if len(snake_List) > Length_of_snake:
            del snake_List[0]

        for x in snake_List[:-1]:
            if x == snake_Head:
                game_close = True

        our_snake(snake_block, snake_List)
        Your_score(Length_of_snake - 1)
        

        pygame.display.update()

        if x1 == foodx and y1 == foody:
            foodx = round(random.randrange(0, dis_width - snake_block) / 10.0) * 10.0
            foody = round(random.randrange(0, dis_height - snake_block) / 10.0) * 10.0
            Length_of_snake += 1

        clock.tick(snake_speed)

    pygame.quit()
    quit()

gameLoop()
