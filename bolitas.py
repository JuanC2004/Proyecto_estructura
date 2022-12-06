import pygame
class bolita:
    def __init__(self,display,color,valor,x,y):
        self.display_game=display
        self.valor=valor
        self.color=color
        self.coordenada=x,y
        self.x=x-12
        self.y=y-17
           
    def crear(self):
        textoNodo=str(self.valor)
        BLACK=(0,0,0)
        pygame.draw.circle(self.display_game,self.color,self.coordenada,30)
        fuente1=pygame.font.SysFont("Arial",30)
        texto1=fuente1.render(textoNodo,0,BLACK)
        self.display_game.blit(texto1,(self.x,self.y))
        