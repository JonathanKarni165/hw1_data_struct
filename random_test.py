from AVLTree import AVLTree
from AVLTree import AVLNode
from random import shuffle

lst = list(range(0,10))
for i in range(10):
    shuffle(lst)
    
    print(lst)
    print('makes tree:\n')
    tree = AVLTree()
    for j in range(0,10):
        tree.insert(lst[j],f'node_({i},{j})')
    tree.root.display()
    print('*********************\n\n')

input()