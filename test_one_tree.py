from AVLTree import AVLTree
from AVLTree import AVLNode
insert_seq = [2, 9, 4, 8, 7, 5, 6, 0, 1, 3]
tree = AVLTree()
for i in range(len(insert_seq)):
    tree.insert(insert_seq[i], 'hi')
    print('********************\n\n')
    tree.root.display()