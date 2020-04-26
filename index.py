import numpy as np
import pygame
import time

#Define variables for screan
width, height = 700, 700
nxC, nyC = 25, 25
dimCW  = width / nxC
dimCH  = height / nyC
#Screan color
bg = 25, 25, 25
bg_poly_dead = 128, 128, 128
bg_poly_alive = 255, 255, 255
#game state
gameState = np.zeros((nxC, nyC))

#Set state example
gameState[5, 3] = 1
gameState[5, 4] = 1
gameState[5, 5] = 1

gameState[21, 21] = 1
gameState[22, 22] = 1
gameState[23, 23] = 1
gameState[22, 23] = 1
gameState[21, 23] = 1

#pygame.init()
screan = pygame.display.set_mode((width, height))

screan.fill(bg)

while True:
    #copy state
    newGameState = np.copy(gameState)

    #Clean the screan
    screan.fill(bg)
    time.sleep(0.2)

    for i in range(0, nyC):
        for j in range(0, nxC):
            n_neigh =   gameState[(i - 1) % nxC, (j - 1) % nyC] + \
                gameState[(i) % nxC, (j - 1) % nyC] + \
                gameState[(i + 1) % nxC, (j - 1) % nyC] + \
                gameState[(i - 1) % nxC, (j) % nyC] + \
                gameState[(i + 1) % nxC, (j) % nyC] + \
                gameState[(i - 1) % nxC, (j + 1) % nyC] + \
                gameState[(i) % nxC, (j + 1) % nyC] + \
                gameState[(i + 1) % nxC, (j + 1) % nyC]

            if gameState[i, j] == 0 and n_neigh == 3:
                newGameState[i, j] = 1

            elif gameState[i, j] == 1 and (n_neigh < 2 or n_neigh >3):
                newGameState[i, j] = 0

            #Create polygon
            poly = [
                (j * dimCW, i * dimCH),
                ((j + 1) * dimCW, i * dimCH),
                ((j + 1) * dimCW, (i + 1) * dimCH),
                (j * dimCW, (i + 1) * dimCH),
            ]
            #draw dead polygon
            if gameState[i, j] == 0:
                pygame.draw.polygon(screan, bg_poly_dead, poly, 1)
            #draw alive polygon
            else:
                pygame.draw.polygon(screan, bg_poly_alive, poly, 0)
    gameState = np.copy(newGameState)
    #refresh the screan
    pygame.display.flip()