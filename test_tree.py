from random import shuffle
from AVLTree import AVLTree
insert_seq = [2,9,4,8,7,5,6,0,1,3]
tree = AVLTree()
for i in range(len(insert_seq)):
    tree.insert(insert_seq[i], 'hi')
print('********')
tree.root.display()