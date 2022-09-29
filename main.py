import pygame
from pygame.locals import *
from os import system
from sys import exit

from board import Board, Player

system("cls")
cont = True
immune = False
while cont:
    
    pygame.init()

    def checkAllowed(player, dir):
        if dir == "RIGHT" and player.dir == "LEFT":
            return False
        elif dir == "LEFT" and player.dir == "RIGHT":
            return False
        elif dir == "UP" and player.dir == "DOWN":
            return False
        elif dir == "DOWN" and player.dir == "UP":
            return False
        return True


    windowWidth, windowHeight = 1000, 1000
    window = pygame.display.set_mode([windowWidth, windowHeight])
    pygame.display.set_caption("Tron by Patrick Russell no rights reserved")

    window.fill((10, 10, 10))

    winner = ""
    board = Board(window, (windowWidth, windowHeight), 10)
    player1 = Player(board, (100, 100), 1)
    player2 = Player(board, (100, 900), 2)

    timer = 0
    mod1 = 5
    mod2 = 5

    running = True
    while running:
        pygame.time.delay(1)
        timer += 1
        window.fill((30, 30, 30))
        if not winner:
            if timer%mod1 == 0:
                player1.move()
                board.expire()
                if board.checkCollision(player1) and not immune:
                    winner = "Player 2"
                    mod = 100
                    timer = 1
            if timer%mod2 == 0:
                player2.move()
                if board.checkCollision(player2) and not immune:
                    winner = "Player 1"
                    mod = 10
                    timer = 1
        else:
            if timer%mod == 0:
                running = False
        
        board.draw()

        for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    running = False
                    cont = False
                if event.type == KEYDOWN:
                    if event.key == K_ESCAPE:
                        running = False
                        cont = False
                    if event.key == K_RIGHT:
                        if checkAllowed(player1, "RIGHT"):
                            player1.dir = "RIGHT"
                    if event.key == K_LEFT:
                        if checkAllowed(player1, "LEFT"):
                            player1.dir = "LEFT"
                    if event.key == K_UP:
                        if checkAllowed(player1, "UP"):
                            player1.dir = "UP"
                    if event.key == K_DOWN:
                        if checkAllowed(player1, "DOWN"):
                            player1.dir = "DOWN"
                    

                    if event.key == K_d:
                        if checkAllowed(player2, "RIGHT"):
                            player2.dir = "RIGHT"
                    if event.key == K_a:
                        if checkAllowed(player2, "LEFT"):
                            player2.dir = "LEFT"
                    if event.key == K_w:
                        if checkAllowed(player2, "UP"):
                            player2.dir = "UP"
                    if event.key == K_s:
                        if checkAllowed(player2, "DOWN"):
                            player2.dir = "DOWN"
                    if event.key == K_g:
                        immune = True
                    

                    if event.key == K_c:
                        if mod2 == 5:
                            mod2 = 2
                        else:
                            mod2 = 5
                    if event.key == K_HASH:
                        if mod1 == 5:
                            mod1 = 0.5
                        else:#a
                            mod1 = 5
        keys = pygame.key.get_pressed()
        
        pygame.display.flip()

    if winner:
        print("Winner is", winner)

    pygame.quit()


exit()