from random import shuffle
from AVLTree import AVLTree
insert_seq = [10,7,12,6,8,13,5]

print(insert_seq)

tree = AVLTree()
for i in range(len(insert_seq)):
    tree.insert(insert_seq[i], 'hi','max')
print('********')
tree.root.display()
print('******** test delete *****')

del_seq = [13]

print(del_seq)
while True:
    print("\nchoose node to delete:")
    key_to_delete = int(input())
    tree.delete(tree.search(key_to_delete))
    print('\n############################\n\n')
    tree.root.display()
    #[4, 8, 1, 2, 9, 6, 3, 7, 5, 0]
    #[8, 6, 2, 5, 7, 9, 1, 0, 3, 4]
input()