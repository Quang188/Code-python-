import pygame
import time
import random

pygame.init()

white = (255, 255, 255)
yellow = (255, 255, 102)
black = (0, 0, 0)
red = (213, 50, 80)
green = (0, 255, 0)
blue = (50, 153, 213)
dis_width = 800
dis_height = 600

dis = pygame.display.set_mode((dis_width, dis_height))
pygame.display.set_caption('Robot  ')

clock = pygame.time.Clock()

background_image = pygame.image.load('assets/background.jpg')
background_image = pygame.transform.scale(background_image, (dis_width, dis_height))

robot_image = pygame.image.load('assets/robot0.png')
robot_image = pygame.transform.scale(robot_image, (25, 25))

target_image = pygame.image.load('assets/A+.png')
robot_block = 25
target_image = pygame.transform.scale(target_image, (robot_block, robot_block))

robot_speed = 10

font_style = pygame.font.SysFont("Times New Roman", 25)
score_font = pygame.font.SysFont("Times New Roman", 15)


def Your_score(score):
    value = score_font.render("Score: " + str(score), True, yellow)
    dis.blit(value, [0, 0])


def our_robot(robot_image, robot_list):
    for x in robot_list:
        dis.blit(robot_image, (x[0], x[1]))


def message(msg, color):
    mesg = font_style.render(msg, True, color)
    dis.blit(mesg, [dis_width / 6, dis_height / 3])


def game_intro():
    intro = True
    while intro:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()

        dis.blit(background_image, (0, 0))

        font = pygame.font.SysFont("comicsansms", 70)
        title = font.render("Catch Target ", True, white)
        dis.blit(title, (dis_width / 4, dis_height / 4))

        pygame.draw.rect(dis, green, (300, 400, 200, 50))
        font = pygame.font.SysFont("comicsansms", 30)
        start_text = font.render("Start", True, black)
        dis.blit(start_text, (350, 410))

        pygame.display.update()

        mouse = pygame.mouse.get_pos()
        click = pygame.mouse.get_pressed()

        if 300 < mouse[0] < 500 and 400 < mouse[1] < 450:
            if click[0] == 1:
                intro = False


def gameLoop():
    game_intro()

    game_over = False
    game_close = False

    x1 = dis_width / 2
    y1 = dis_height / 2

    x1_change = 0
    y1_change = 0

    robot_List = []
    Length_of_robot = 1

    targetx = round(random.randrange(0, dis_width - robot_block) / robot_block) * robot_block
    targety = round(random.randrange(0, dis_height - robot_block) / robot_block) * robot_block

    while not game_over:

        while game_close:
            dis.fill(green)
            message("Bạn đã thua rồi! Nhấn (R)-Chơi lại or (E)-Thoát", red)
            Your_score(Length_of_robot - 1)
            pygame.display.update()

            for event in pygame.event.get():
                if event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_e:
                        pygame.quit()
                        quit()
                    if event.key == pygame.K_r:
                        gameLoop()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                quit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_LEFT:
                    x1_change = -robot_block
                    y1_change = 0
                elif event.key == pygame.K_RIGHT:
                    x1_change = robot_block
                    y1_change = 0
                elif event.key == pygame.K_UP:
                    y1_change = -robot_block
                    x1_change = 0
                elif event.key == pygame.K_DOWN:
                    y1_change = robot_block
                    x1_change = 0

        if x1 >= dis_width or x1 < 0 or y1 >= dis_height or y1 < 0:
            game_close = True
        x1 += x1_change
        y1 += y1_change
        dis.blit(background_image, (0, 0))

        dis.blit(target_image, (targetx, targety))

        robot_Head = []
        robot_Head.append(x1)
        robot_Head.append(y1)
        robot_List.append(robot_Head)
        if len(robot_List) > Length_of_robot:
            del robot_List[0]

        for x in robot_List[:-1]:
            if x == robot_Head:
                game_close = True

        our_robot(robot_image, robot_List)
        Your_score(Length_of_robot - 1)

        pygame.display.update()

        if x1 == targetx and y1 == targety:
            targetx = round(random.randrange(0, dis_width - robot_block) / robot_block) * robot_block
            targety = round(random.randrange(0, dis_height - robot_block) / robot_block) * robot_block
            Length_of_robot += 1

        clock.tick(robot_speed)

    pygame.quit()
    quit()


gameLoop()
