
from treeLinkedList import TreeLinkedList
import pygame
import time

#inicializar modulo pygame
pygame.init()
window_width=1000
window_height=600
BLACK=(0,0,0)
WHITE=(255,255,255)
GREEN=(0,255,0)
RED=(255,0,0)
GRAY=(10,10,10)

#crear variable que recibe alto y ancho de la pantalla
display_game= pygame.display.set_mode((window_width,window_height))
pygame.display.set_caption("Arboles binarios: JUAN_CAMILO")
inicio=pygame.time.get_ticks()/1000
#variable que permitira mantener el display activo
display_game.fill(WHITE)

fuente1=pygame.font.SysFont("Arial",20)
texto1=fuente1.render("Recorridos :",0,GRAY)
texto2=fuente1.render("tecla arriba para amplitud ",0,GRAY)
texto3=fuente1.render("tecla abajo para profundidad preorder ",0,GRAY)
texto4=fuente1.render("tecla derecha para profundidad inorder ",0,GRAY)
texto5=fuente1.render("tecla izquierda para profundidad postorder ",0,GRAY)


display_game.blit(texto1,(25,15))
display_game.blit(texto2,(25,40))
display_game.blit(texto3,(25,65))
display_game.blit(texto4,(25,90))
display_game.blit(texto5,(25,115))

b1=TreeLinkedList(display_game)
b1.add_node(60,480,51)
b1.add_node(41,356,154)
b1.add_node(16,200,248)
b1.add_node(25,231,346)
b1.add_node(53,356,248)
b1.add_node(46,318,346)
b1.add_node(42,300,443)
b1.add_node(55,431,346)
b1.add_node(74,637,154)
b1.add_node(65,623,248)
b1.add_node(63,570,346)
b1.add_node(62,525,443)
b1.add_node(64,604,443)
b1.add_node(70,718,346)


b1PreorderList=b1.preorder()
print(b1PreorderList)
b1InorderList=b1.inorder()
print(b1InorderList)
b1PostorderList=b1.postorder()
print(b1PostorderList)
b1Amplitud=b1.breadth_first_search()
print(b1Amplitud)

                
running=True 
bandera1=False
bandera2=False
bandera3=False
bandera4=False
i=0
j=0
while (running):
    if bandera1==True:
        if i<len(b1PreorderList):
                b1.find(b1PreorderList[i])
                i+=1
                time.sleep(1)
        else:
            
            if j<len(b1PreorderList):
                b1.limpiarRecorrido(b1PreorderList[j])
                j+=1
            else:
                bandera1=False
                i=0
                j=0
        
            
    if bandera2 ==True:
        if i<len(b1InorderList):
                b1.find(b1InorderList[i])
                i+=1
                time.sleep(1)
        else:
            
            if j<len(b1InorderList):
                b1.limpiarRecorrido(b1InorderList[j])
                j+=1
            else:
                bandera2=False
                i=0
                j=0
                
                
    if bandera3 ==True:
        if i<len(b1PostorderList):
                b1.find(b1PostorderList[i])
                i+=1
                time.sleep(1)
        else:
            
            if j<len(b1PostorderList):
                b1.limpiarRecorrido(b1PostorderList[j])
                j+=1
            else:
                bandera3=False
                i=0
                j=0
    if bandera4 ==True:
        if i<len(b1Amplitud):
                b1.find(b1Amplitud[i])
                i+=1
                time.sleep(1)
        else:
            
            if j<len(b1Amplitud):
                b1.limpiarRecorrido(b1Amplitud[j])
                j+=1
            else:
                bandera4=False
                i=0
                j=0
    
    for event in pygame.event.get():
        if event.type==pygame.KEYDOWN:
            if event.key== pygame.K_DOWN:
                bandera1=True
                print(f"bandera1 {bandera1}")
            if event.key==pygame.K_RIGHT:
                bandera2=True
                print(f"bandera2 {bandera2}")
            if event.key==pygame.K_LEFT:
                bandera3=True
                print(f"bandera3 {bandera3}")
            if event.key==pygame.K_UP:
                bandera4=True
                print(f"bandera4 {bandera4}")
        if event.type== pygame.QUIT:
            running=False
    pygame.display.update()    
pygame.mainloop()
pygame.quit() 