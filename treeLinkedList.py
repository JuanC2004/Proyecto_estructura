from bolitas import bolita
from rayita import Rayita
import pygame

class TreeLinkedList:
    
    class Node:
        def __init__(self,value,x,y):
            self.value=value
            self.right_node=None
            self.left_node=None
            self.miBola=None
            self.miRayaIz=None
            self.miRayaDer=None
            self.x=x
            self.y=y
    
    def __init__(self,display):
        self.root=None
        self.length=0
        self.display=display
        self.COLORBOLITAS=(204,255,0)
        self.ColorEncontrado=(0,190,21)
        
        
    def add_node(self,value,x,y):
        new_node=self.Node(value,x,y)
        new_node.miBola=bolita(self.display,self.COLORBOLITAS,value,x,y).crear()
        
        if self.root==None:
            self.root=new_node
        else:
            def recorrer(value,node):
                if value==node.value:
                    return "el elemento ya existe"
                elif value < node.value:
                    if node.left_node == None:
                        node.left_node=new_node
                        return True
                    else:
                        return recorrer(value,node.left_node)
                elif value > node.value:
                    if node.right_node == None:
                        node.right_node = new_node
                        return True
                    else:
                        
                        return recorrer(value, node.right_node)
            recorrer(value,self.root)
    
    def find (self, value):
        def recorrer(value, node):
            if value == node.value:
                node.miBola=bolita(self.display,self.ColorEncontrado,value,node.x,node.y).crear()
                
                return node.value
            elif value < node.value:
                if node.left_node == None:
                    return "No existe el elemento buscado"
                else:
                    node.miRayaIz=Rayita(self.display,self.ColorEncontrado,node.x,node.y,node.left_node.x,node.left_node.y).crear()
                    return recorrer(value, node.left_node)

            else:
                if node.right_node == None:
                    return "No existe el elemento buscado"
                else:
                    node.miRayaIz=Rayita(self.display,self.ColorEncontrado,node.x,node.y,node.right_node.x,node.right_node.y).crear()
                    return recorrer(value, node.right_node)
        nodo_encontrado = recorrer(value, self.root)
        return print(nodo_encontrado)
    
    def preorder (self):
        #RID(Raíz, izquierda, derecha)
        container = []
        def recorrer(node):
            
            container.append(node.value)
            if node.left_node != None:
                recorrer(node.left_node)
            if node.right_node != None:
                recorrer(node.right_node)
        recorrer(self.root)
        return (container)
    
    def inorder(self):
        #IRD (Izquierda, raíz, derecha)
        container = []
        def recorrer(node):
            if node.left_node != None:
                node.miRayaIz=Rayita(self.display,self.COLORBOLITAS,node.x,node.y,node.left_node.x,node.left_node.y).crear()
                recorrer(node.left_node)
            container.append(node.value)
            if node.right_node != None:
                node.miRayaDer=Rayita(self.display,self.COLORBOLITAS,node.x,node.y,node.right_node.x,node.right_node.y).crear()
                recorrer(node.right_node)
        recorrer(self.root)
        return (container)
    
    def postorder(self):
        #IDR(Izquierda, derecha, raíz)
        container = []
        def recorrer (node):
            if node.left_node != None:
                recorrer(node.left_node)
            if node.right_node != None:
                recorrer(node.right_node)
            container.append(node.value)
        recorrer(self.root)
        return (container)
    
    def breadth_first_search(self):
        contenedor_1=[self.root]
        contenedor_2=[self.root.value]
        while len(contenedor_1)!=0:
            node=contenedor_1[0]
            if node.left_node != None:
                contenedor_1.append(node.left_node)
                contenedor_2.append(node.left_node.value)
            if node.right_node !=None:
                contenedor_1.append(node.right_node)
                contenedor_2.append(node.right_node.value)
            contenedor_1.pop(0)
        return (contenedor_2)
    def limpiarRecorrido (self, value):
        def recorrer(value, node):
            if value == node.value:
                node.miBola=bolita(self.display,self.COLORBOLITAS,value,node.x,node.y).crear()
                return node.value
            elif value < node.value:
                if node.left_node == None:
                    return "No existe el elemento buscado"
                else:
                    node.miRayaIz=Rayita(self.display,self.COLORBOLITAS,node.x,node.y,node.left_node.x,node.left_node.y).crear()
                    return recorrer(value, node.left_node)
            else:
                if node.right_node == None:
                    return "No existe el elemento buscado"
                else:
                    node.miRayaDer=Rayita(self.display,self.COLORBOLITAS,node.x,node.y,node.right_node.x,node.right_node.y).crear()
                    return recorrer(value, node.right_node)
        nodo_encontrado = recorrer(value, self.root)
        return print(nodo_encontrado)
    
                        