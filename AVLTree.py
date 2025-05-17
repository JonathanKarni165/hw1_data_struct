# username - complete info
# id1      - complete info
# name1    - complete info
# id2      - complete info
# name2    - complete info


"""A class represnting a node in an AVL tree"""


class AVLNode(object):
    """Constructor, you are allowed to add more fields.

    @type key: int or None
    @param key: key of your node
    @type value: string
    @param value: data of your node
    """

    def __init__(self, key, value: int):
        self.key = key
        self.value = value
        self.left: AVLNode = None
        self.right: AVLNode = None
        self.parent: AVLNode = None
        self.height = -1

    def has_right(self):
        return self.right is not None

    def has_left(self):
        return self.left is not None

    def is_leaf(self):
        return (not self.has_right()) and (not self.has_right())

    """returns whether self is not a virtual node

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""

    def is_real_node(self):
        return False


"""
A class implementing an AVL tree.
"""


class AVLTree(object):

    """
    Constructor, you are allowed to add more fields.

    """

    def __init__(self):
        self.root = None

    """searches for a node in the dictionary corresponding to the key

	@type key: int
	@param key: a key to be searched
	@rtype: AVLNode
	@returns: node corresponding to key
	"""

    def search(self, key):
        cur_node: AVLNode = self.root
        while cur_node is not None:
            if cur_node.key == key:
                return cur_node
            if cur_node.key < key:
                cur_node = cur_node.left
            else:
                cur_node = cur_node.right
        return None

    """inserts a new node into the dictionary with corresponding key and value

	@type key: int
	@pre: key currently does not appear in the dictionary
	@param key: key of item that is to be inserted to self
	@type val: string
	@param val: the value of the item
    @param start: can be either "root" or "max"
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""

    def insert(self, key, val, start="root"):
        return -1

    """
    --helper method--
	rotate tree right or left
	@param root: the root of the sub tree (or the whole tree)
		the sub tree has to have right or left child according to dir
    @param dir: gets the char R or L
    @param parent: parent node of root
    @returns : the new root of the tree after changes
			if the tree is not like expected the function returns None
            if dir is neither R or L also return None
	"""

    def rotate(self, dir, root: AVLNode, parent: AVLNode = None):
        #  rotate subtree left or right
        if dir == 'R':
            if root.left == None:
                # TODO remove print when done
                print('rotate: not the tree i expect')
                return None

            new_root: AVLNode = root.left
            root.left = new_root.right
            new_root.right = root

        elif dir == 'L':
            if root.right == None:
                # TODO remove print when done
                print('rotate: not the tree i expect')
                return None

            new_root: AVLNode = root.right
            root.right = new_root.left
            new_root.left = root

        # reconnect parent
        if parent == None:
            return new_root

        if parent.right == root:
            parent.right = new_root
        elif parent.left == root:
            parent.left = new_root
        else:
            return None

        return new_root

    def insert_from_root(self, new_node):
        new_key = new_node.key
        cur_node: AVLNode = self.root

    """deletes node from the dictionary

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""

    def delete(self, node):
        return -1

    """returns an array representing dictionary

	@rtype: list
	@returns: a sorted list according to key of touples (key, value) representing the data structure
	"""

    def avl_to_array(self):
        return None

    """returns the number of items in dictionary

	@rtype: int
	@returns: the number of items in dictionary
	"""

    def size(self):
        return -1

    """returns the root of the tree representing the dictionary

	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""

    def get_root(self):
        return None

    '''@returns: the number of nodes which have balance factor equals to 0 devided by the total number of nodes'''

    def get_amir_balance_factor(self):
        return None
