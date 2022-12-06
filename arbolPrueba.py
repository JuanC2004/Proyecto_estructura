class treeNodes:
    class Node:
        def _init_(self,value):
            self.value = value
            self.left_node = None
            self.right_node = None
            
    def _init_(self):
        self.root = None
        self.lenght_nodes = 0 
        
    def add(self, value):
        new_node = self.Node(value)
        if self.root == None:
            self.root = new_node
        else:
            def recorrer (value, node):
                if value == node.value:
                    return "El elemento ya existe"
                elif value < node.value:
                    if node.left_node == None:
                        node.left_node = new_node
                        return True
                    else:
                        return recorrer(value, node.left_node)
                elif value > node.value:
                    if node.right_node == None:
                        node.right_node = new_node
                        return True
                    else:
                        return recorrer(value, node.right_node)
            recorrer(value, self.root)
                    
    def find (self, value):
        def recorrer(value, node):
            if value == node.value:
                return node.value
            elif value < node.value:
                if node.left_node == None:
                    return "No existe el elemento buscado"
                else:
                    return recorrer(value, node.left_node)
            else:
                if node.right_node == None:
                    return "No existe el elemento buscado"
                else:
                    return recorrer(value, node.right_node)
        nodo_encontrado = recorrer(value, self.root)
        return print(nodo_encontrado.value)
        
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
        return print(container)
    
    def inorder(self):
        #IRD (Izquierda, raíz, derecha)
        container = []
        def recorrer(node):
            if node.left_node != None:
                recorrer(node.left_node)
            container.append(node.value)
            if node.right_node != None:
                recorrer(node.right_node)
        recorrer(self.root)
        return print(container)
    
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
        return print(container)
            
    def breadth_first_search(self):
        #si el contenedor 1 tiene como longitud 1 quiere decir que el arbol al menos tiene un nodo que es la raíz
        container_1 = [self.root]
        container_2 = [self.root.value]
        while len(container_1) != 0:
            node = container_1[0]
            if node.left_node != None:
                container_1.append(node.left_node)
                container_2.append(node.left_node.value)
            if node.right_node != None:
                container_1.append(node.right_node)
                container_2.append(node.right_node.value)
            container_1.pop(0)
        return print(container_2)
    
    def delete(self, value):
        def recorrer(value, node, previous_node):
            if value == node.value:
                ''' 
                Valido si el node que quiero eliminar es una hoja
                El node que se va a eliminar no tiene hijo, es una hoja.
                '''
                if node.left_node == None and node.right_node == None:
                    if previous_node.left_node != None:
                        if previous_node.left_node.value == node.value:
                            previous_node.left_node = None
                    if previous_node.right_node != None:
                        if previous_node.right_node.value == node.value:
                            previous_node.right_node = None
                    node = None
                    '''
                    El node que se va a eliminar tiene un solo hijo 
                    El hijo esta a la derecha
                    '''
                elif node.left_node == None and node.right_node != None:
                    if previous_node.left_node != None:
                        if previous_node.left_node.value == node.value:        
                            previous_node.left_node = node.right_node
                    if previous_node.right_node != None:
                        if previous_node.right_node.value == node.value:
                            previous_node.right_node = node.right_node
                    '''
                    El node que se va a eliminar tiene un solo hijo 
                    El hijo esta a la izquierda
                    '''
                elif node.right_node == None and node.left_node != None:
                    if previous_node.left_node != None:
                        if previous_node.left_node.value == node.value:
                            previous_node.left_node = node.left_node
                    if previous_node.right_node != None:
                        if previous_node.right_node.value == node.value:
                            previous_node.right_node = node.left_node
              
        recorrer(value, self.root, self.root)