# In questi alberi in nodo principale è il più grande di quello alla sua sinistra, ma è più piccolo di quello
# alla sua destra
#
#                                 4
#                              3     5
#                            2    4.5  6
#               
#
# {4:[3,5] , 3:[2,None] , 5:[4.5,6] , 2:[None,None] , 4.5:[None,None] , 6:[None,None]}


def search(array: list[int] , x: int) -> int :
    for i in range(len(array)):
        if array[i] == x:
            return x
    
    #se una lista non è ordinara per cercare x conviene fare questo,
    #perchè ordinare una lista richiede un numero di operazioni lunghe quanto la lista

    return None

# Seguendo questa funzione  len(erray) fa 10.000 iterazioni
# mentre così ne farebbe solo 14 log_2(len(array))   


# array = [-1 ,0 ,1 ,5 ,65 ,67 ,99 ,912 ,1207]
# x = 912

def binary_search(array: list[int] , x: int) -> int:
    
    low = 0
    high = len(array)

    while low < high:
        mid = (low + high) // 2
        if array[mid] == x:
            return mid
        else:
            if x > array[mid]:
                low = mid + 1
            else:
                high = mid - 1
    
    #Queste due funzioni scritte, posso semplicemnte essere sostituite con array.index(x)

    return None


def __binary_search_recursive(array: list[int] , x: int ,
                              low: int , high: int ) -> int:
   
    mid = (low + high) // 2

    if x == array[mid]:
        return mid
    elif x > array[mid]:
        return __binary_search_recursive(array ,x ,mid + 1 ,high)
    else:
        return __binary_search_recursive(array ,x ,low ,mid - 1)

def binary_search_recursive(array: list[int] , x: int) ->int:
    return __binary_search_recursive(array ,x ,0 ,len(array))


def visit_tree(tree:dict[int ,list[int]] , node:int):
    
    print(node)
    
    left_child, right_child = tree.get(node, [None, None])

    if left_child: #messo così è is not None
        visit_tree(tree, left_child)
    
    if right_child: #idem
        visit_tree(tree, right_child)

tree = {4:[3,5] , 3:[2,None] , 5:[4.5,6] , 2:[None,None] , 4.5:[None,None] , 6:[None,None]}
visit_tree(tree,4)

print("\nSPAZIATORE\n")

def visit_tree_iterative(tree: dict[int, list[int]], root: int):
    
    stack: list[int] = [root]
    while stack: #messo così viene len(stack) > 0
        curr_node = stack.pop(0) #mettendo uno zero qua fa vedere subito i figli del ramo madre e poi il figlio
        print(curr_node)         #del ramo di destra perchè in questo caso abbiamo iniziato l'if da destra
        left_child, right_child = tree.get(curr_node, [None, None])
        if right_child:
            stack.append(right_child)
        if left_child:   
            stack.append(left_child)

tree = {4:[3,5] , 3:[2,None] , 5:[4.5,6] , 2:[None,None] , 4.5:[None,None] , 6:[None,None]}
visit_tree_iterative(tree,4)
print("\nSPAZIATORE\n")

def visit_tree_medium(tree: dict[int, list[int]], root: int):
    
    dict_media:dict = {}
    nodi_per_livello:dict = {}
    
    stack: list[int] = [(root, 0)]
    
    while stack: #messo così viene len(stack) > 0
        curr_node, curr_level = stack.pop(0) 
        
        print(curr_node)         
        print(dict_media)
        left_child, right_child = tree.get(curr_node, [None, None])
        
        if right_child:
            stack.append((right_child, curr_level+1))
            dict_media[curr_level] = dict_media.get(curr_level, 0) + right_child
        if left_child:   
            stack.append((left_child, curr_level+1))
            dict_media[curr_level] = dict_media.get(curr_level, 0) + left_child
    
    for i in dict_media:
        dict_media[i] /= nodi_per_livello[i]

tree = {4:[3,5] , 3:[2,None] , 5:[4.5,6] , 2:[None,None] , 4.5:[None,None] , 6:[None,None]}
visit_tree_medium(tree,4)
#DA VEDERE DA UN ERRORE
    