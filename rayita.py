import pygame
class Rayita:
    def __init__(self,display,color,x1,y1,x2,y2):
        self.display_game=display
        self.color=color
        self.coordenada1=x1,y1
        self.coordenada2=x2,y2
        self.x1=x1
        self.y1=y1
        self.x2=x2
        self.y2=y2
    def crear(self):
        BLACK=(0,0,0)
        pygame.draw.line(self.display_game, self.color, (self.coordenada1), (self.coordenada2))

    