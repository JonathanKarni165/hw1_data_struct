from AVLTree import AVLTree

from AVLTree import BST
tree = BST()
while True:
    print('\n\n')
    print('what to do? \ninsert : i \ndelete : d \ninsert_max : im \nprint_tree : p \nsize : s \nmax : m \namir_balance : a \navl_array : ar \ninsert_bst : in')
    command = input()
    
    if command == 'in':
        print('what key to insert?')
        key = int(input())
        tree.insert_naive(key, str(key))

    if command == 'i':
        print('what key to insert?')
        key = int(input())
        tree.insert(key, str(key))

    if command == 'im':
        print('what key to insert?')
        key = int(input())
        tree.insert(key, str(key)+'fm', 'max')
    
    if command == 'd':
        print('what key to delete?')
        key = int(input())
        tree.delete(tree.search(key))
    
    if command == 'm':
        print(tree.max.key)

    if command == 's':
        print(tree.size())
    
    if command == 'a':
        print(tree.get_amir_balance_factor())

    if command == 'ar':
        print(tree.avl_to_array())
        
    if command == 'p':
        print('\n###################\n')
        tree.root.display()
        print('\n###################\n')

    


