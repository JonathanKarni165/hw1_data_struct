import AVLTree
from AVLTree import AVLNode
from AVLTree import AVLTree
'''
root = AVLNode(10, "ten")
root.height = 0

root.left = AVLNode(5, "five")
root.left.parent = root
root.left.height = 0

root.right = AVLNode(15, "fifteen")
root.right.parent = root
root.right.height = 0

root.left.left = AVLNode(2, "two")
root.left.left.parent = root.left
root.left.left.height = 0

root.left.right = AVLNode(7, "seven")
root.left.right.parent = root.left
root.left.right.height = 0

root.right.right = AVLNode(20, "twenty")
root.right.right.parent = root.right
root.right.right.height = 0
'''
tree = AVLTree()
print(tree.avl_to_array())
print(tree.size())
tree.insert(5, 'hi', 'max')

print('************************************\n\n')
tree.insert(50, "he", 'max')

print('************************************\n\n')
tree.insert(15, "ho", 'max')

print('************************************\n\n')
tree.insert(7, "hu", 'max')

print('************************************\n\n')
tree.insert(55, "ha", 'max')

print('************************************\n\n')
tree.insert(60, 'blabla')

print('************************************\n\n')
tree.insert(70, 'kaaa')

print('************************************\n\n')
tree.insert(65, 'blab')

print('************************************\n\n')

tree.delete(tree.search(15))

# print('************************************\n\n')
# tree.delete(tree.search(7))

print('************************************\n\n')


#tree.in_order()

# print(tree.avl_to_array())


# def test_amir_balance_factor():
#      """Test Amir's balance factor."""
#      tree1 = AVLTree()
#      print(tree1.get_amir_balance_factor())
#      tree1.insert(10, "ten")
#      tree1.insert(20, "twenty")
#      tree1.insert(5, "five")
#      print(tree1.get_amir_balance_factor())

# test_amir_balance_factor()