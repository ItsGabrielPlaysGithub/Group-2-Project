import pygame
import random

pygame.init()
screen = pygame.display.set_mode((800,600))

gamerun = True

# ======== Player 1 and 2 images ========== #
player1png = pygame.image.load("tray.png")
player1x = 0
player1y = 268
player1yd = 0
def player1(x,y):
    screen.blit(player1png, (x,y))

player2png = pygame.image.load("tray.png")
player2x = 736
player2y = 268
player2yd = 0
def player2(x,y):
    screen.blit(player1png, (x,y))

# ======== Ball images ========== #
ballpng = pygame.image.load("ball.png")
ballx = 386
bally = 286
ballxd = -0.1
ballyd = -0.1
def ball(x,y):
    screen.blit(ballpng,(x,y))
def corner(y):
    global ballyd
    if y <= 0 or y >= 568:
        ballyd *= -1
    return ballyd
def bounce():
    global player1x,player1y,player2x,player2y,ballx,bally,ballxd,ballyd
    if ((ballx <= player1x + 37)and(ballx >= player1x + 28)) and ((bally+28 >= player1y)and(bally <= player1y + 64)):
        ballx = 37
        ballxd *= -1
        if ((bally + 28 >= player1y + 24) and (bally <= player1y + 40)):
            anglenear = [0.03,-0.03,0.05,-0.05]
            ballyd = random.choice(anglenear)
            print(ballyd)
        elif ((bally+28 >= player1y)and(bally <= player1y + 64)):
            anglefar = [0.1,-0.1,0.15,-0.15]
            ballyd = random.choice(anglefar)
            print(ballyd)

    br = 28 # br means "bottom right"
    if ((ballx+br <= player2x + 37)and(ballx+br >= player2x + 28)) and ((bally+28 >= player2y)and(bally <= player2y + 64)):
        ballx = 735
        ballxd *= -1
        if ((bally + 28 >= player2y + 24) and (bally <= player2y + 40)):
            anglenear = [0.03, -0.03, 0.05, -0.05]
            ballyd = random.choice(anglenear)
            print(ballyd)
        elif ((bally+28 >= player2y)and(bally <= player2y + 64)):
            anglefar = [0.1, -0.1, 0.15, -0.15]
            ballyd = random.choice(anglefar)
            print(ballyd)

    return ballyd,ballxd


while gamerun == True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            gamerun = False

        # ======== pressed button ======== #
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_w:
                player1yd = -0.2
            if event.key == pygame.K_UP:
                player2yd = -0.2

            if event.key == pygame.K_s:
                player1yd = 0.2
            if event.key == pygame.K_DOWN:
                player2yd = 0.2

        # ======== released button ======== #
        if event.type == pygame.KEYUP:
            if event.key == pygame.K_w or event.key == pygame.K_s:
                player1yd = 0
            if event.key == pygame.K_UP or event.key == pygame.K_DOWN:
                player2yd = 0

    screen.fill((0,0,0))

    # display ball and its changed position #
    ballx += ballxd
    bally += ballyd
    corner(bally)
    bounce()
    ball(ballx, bally)

    # display score system #


    # display player 1 and 2 and its changed position #
    player1y += player1yd
    player2y += player2yd
    if player1y < 0:
        player1y = 0
    elif 536 < player1y:
        player1y = 536
    if player2y < 0:
        player2y = 0
    elif 536 < player2y:
        player2y = 536
    player1(player1x, player1y)
    player2(player2x, player2y)
    pygame.display.update()
