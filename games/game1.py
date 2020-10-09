import pygame
import random
pygame.mixer.init()
pygame.mixer.music.load('game_song.mp3.mp3')
pygame.mixer.music.play()

pygame.init()

#Game display color

white = (255,255,255)
red = (255,0,0)
black = (0,0,0)
screen_hieght = 600
screen_wiegth = 800

#creating game display
gamewindow=pygame.display.set_mode((screen_wiegth,screen_hieght))

#Titel
pygame.display.set_caption("Supper Snake")
pygame.display.update()

#Game variables

clock = pygame.time.Clock()
font = pygame.font.SysFont(None,40)

def screen_score(text , color , x , y):
    screen_text = font.render(text,True,color)
    gamewindow.blit(screen_text,[x , y])

def plot_snake(gamewindow,color,snk_list,snake_size):
    for x,y in snk_list:
        pygame.draw.rect(gamewindow, color , [x,y, snake_size, snake_size])

def welcome():
    exit_game = False
    while not exit_game:
        gamewindow.fill((229,220,230))
        screen_score("Developed by Smit",(150,10,15),10,10)
        screen_score("Welcome To Supper Snake",black,225,240)
        screen_score("[Press Spacebar To Play]", black, 243,500)
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                exit_game = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_SPACE:
                    gameloop()
        pygame.display.update()
        clock.tick(60)



#Game loop
def gameloop():
    exit_game = False
    game_over = False
    snake_x = 45
    snake_y = 55
    score = 0
    food_x = random.randint(0,screen_wiegth/2)
    food_y = random.randint(0,screen_hieght/2)
    velocity_x = 0
    velocity_y = 0
    snake_size = 15
    speed =4
    fps = 60
    snk_list = []
    snk_length = 1
    while  not exit_game:
        if game_over:
            gamewindow.fill(white)
            screen_score("Game Over! press Enter to continue",red,150,250)
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RETURN:
                        welcome()

        else:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    exit_game = True

                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_RIGHT:
                        velocity_x = speed
                        velocity_y = 0

                    if event.key == pygame.K_LEFT:
                        velocity_x = - speed
                        velocity_y = 0

                    if event.key == pygame.K_UP:
                        velocity_y = - speed
                        velocity_x = 0
                    if event.key == pygame.K_DOWN:
                        velocity_y = speed
                        velocity_x = 0

            snake_y = snake_y + velocity_y
            snake_x = snake_x + velocity_x

        #snake eat food here
            if abs(snake_x-food_x)<8 and abs(snake_y-food_y)<8:
                score += 1
                food_x = random.randint(0, 300)
                food_y = random.randint(0, 400)
                snk_length+=5


            gamewindow.fill(white)
            screen_score("score: " + str(score * 10), red, 5, 5)
            pygame.draw.rect(gamewindow, (75,225,130), [food_x, food_y, 15, 15])

            head = []
            head.append(snake_x)
            head.append(snake_y)
            snk_list.append(head)

            if len(snk_list)>(snk_length):
                del snk_list[0]
            if head in snk_list[:-1]:
                game_over = True

            if snake_x<0 or snake_x>screen_wiegth or snake_y<0 or snake_y>screen_hieght:
                game_over = True
                print("game Over!")
            # pygame.draw.rect(gamewindow,black,[snake_x,snake_y,snake_size,snake_size])
            plot_snake(gamewindow,black,snk_list,snake_size)
        pygame.display.update()
        clock.tick(fps)

    pygame.quit()
    quit()
welcome()
