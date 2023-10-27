import pygame
import random
def draw_grid(rowC,colC,screen, color,cellW, cellH):
    for row in range(rowC):
        for col in range(colC):
            pygame.draw.rect(screen ,color ,
                             (col * cellW ,row * cellH ,
                              cellW ,cellH) ,1)



