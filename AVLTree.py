# username - yonatankarni
# id1      - 214411571
# name1    - יונתן קרני
# id2      - 214701344
# name2    - שחר בן-דוד


"""A class represnting a node in an AVL tree"""


class AVLNode(object):
    """Constructor, you are allowed to add more fields.

    @type key: int or None
    @param key: key of your node
    @type value: string
    @param value: data of your node
    """

    def __init__(self, key=None, value=None, is_real=True):
        self.key = key
        self.value = value
        self.left: AVLNode = None
        self.right: AVLNode = None
        self.parent: AVLNode = None
        self.height = -1

    def has_right(self):
        return self.right.key is not None

    def has_left(self):
        return self.left.key is not None

    def has_parent(self):
        return self.parent is not None

    def is_leaf(self):
        return (not self.has_right()) and (not self.has_left())

    def get_BF(self):
        return self.left.height - self.right.height

    """returns whether self is not a virtual node

	@rtype: bool
	@returns: False if self is a virtual node, True otherwise.
	"""

    def is_real_node(self):
        return self.key == None

    def display(self):
        lines, *_ = self._display_aux()
        for line in lines:
            print(line)

    def _display_aux(self):
        """Returns list of strings, width, height, and horizontal coordinate of the root."""
        # No child.
        if self.right is None and self.left is None:
            line = '%s' % self.key
            width = len(line)
            height = 1
            middle = width // 2
            return [line], width, height, middle

        # Only left child.
        if self.right is None:
            lines, n, p, x = self.left._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = (x + 1) * ' ' + (n - x - 1) * '_' + s
            second_line = x * ' ' + '/' + (n - x - 1 + u) * ' '
            shifted_lines = [line + u * ' ' for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, n + u // 2

        # Only right child.
        if self.left is None:
            lines, n, p, x = self.right._display_aux()
            s = '%s' % self.key
            u = len(s)
            first_line = s + x * '_' + (n - x) * ' '
            second_line = (u + x) * ' ' + '\\' + (n - x - 1) * ' '
            shifted_lines = [u * ' ' + line for line in lines]
            return [first_line, second_line] + shifted_lines, n + u, p + 2, u // 2

        # Two children.
        left, n, p, x = self.left._display_aux()
        right, m, q, y = self.right._display_aux()
        s = '%s' % self.key
        u = len(s)
        first_line = (x + 1) * ' ' + (n - x - 1) * \
            '_' + s + y * '_' + (m - y) * ' '
        second_line = x * ' ' + '/' + \
            (n - x - 1 + u + y) * ' ' + '\\' + (m - y - 1) * ' '
        if p < q:
            left += [n * ' '] * (q - p)
        elif q < p:
            right += [m * ' '] * (p - q)
        zipped_lines = zip(left, right)
        lines = [first_line, second_line] + \
            [a + u * ' ' + b for a, b in zipped_lines]
        return lines, n + m + u, max(p, q) + 2, n + u // 2


"""
A class implementing an AVL tree.
"""


class AVLTree(object):

    """
    Constructor, you are allowed to add more fields.

    """

    def __init__(self, root=None):
        self.root = root
        self.max = None
    """searches for a node in the dictionary corresponding to the key

	@type key: int
	@param key: a key to be searched
	@rtype: AVLNode
	@returns: node corresponding to key
	"""

    def search(self, key):
        '''
        cur_node: AVLNode = self.root
        while cur_node is not None:
            if cur_node.key == key:
                return cur_node
            if cur_node.key < key:
                cur_node = cur_node.right
            else:
                cur_node = cur_node.left
        '''
        return self.generic_search(self.root, key, True)

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

        new_node = self.init_new_real_node(key, val)
        new_node.height = 0
        if self.root == None:
            self.root = new_node
            self.max = new_node
            return
        # find where to insert
        parent = None
        if start == 'root':
            parent = self.generic_search(self.root, key, False)
        elif start == 'max':
            parent = self.get_parent_to_insert_from_max(key)

        if key < parent.key:
            parent.left = new_node
        else:
            parent.right = new_node
        new_node.parent = parent

        if key > self.max.key:
            self.max = new_node
        # update height
        cur_node = new_node
        while cur_node.has_parent():
            cur_node = cur_node.parent
            cur_node.height = max(cur_node.left.height,
                                  cur_node.right.height) + 1

        # find errors and fix
        return self.fix_tree(new_node)

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

    def rotate(self, dir, root: AVLNode):
        self.root.display()
        #  rotate subtree left or right
        if dir == 'R':
            if not root.has_left():
                # TODO remove print when done
                print('rotate: not the tree i expect')
                return None

            b: AVLNode = root
            a: AVLNode = root.left
            b.left = a.right
            print(b.left.height)
            if b.has_left():
                b.left.parent = b
            a.right = b

        elif dir == 'L':
            if not root.has_right():
                # TODO remove print when done
                print('rotate: not the tree i expect')
                return None

            b: AVLNode = root
            a: AVLNode = root.right
            print(str(a.left.height), "ssssss")
            b.right = a.left
            print(b.right.height)
            if b.has_right():
                b.right.parent = b
            a.left = b

        a.parent = b.parent
        if b != self.root:
            if a.parent.right == b:
                a.parent.right = a
            else:
                a.parent.left = a

        else:
            self.root = a
        b.parent = a

        b.height = max(b.left.height, b.right.height) + 1
        a.height = max(a.left.height, a.right.height) + 1
        self.root.display()

        return a

    """
    --helper method--
	return node if it in the tree and if not return where to insert it
    @param new_node: new node to insert from max
	"""

    def generic_search(self, start, key, is_in_tree):
        cur_node: AVLNode = start
        prev_node: AVLNode = cur_node
        while cur_node.key is not None:
            if cur_node.key == key and is_in_tree:
                return cur_node
            prev_node = cur_node
            if cur_node.key < key:
                cur_node = cur_node.right
            else:
                cur_node = cur_node.left

        if not is_in_tree:
            return prev_node
        return None

    """
    --helper method--
	insert from max WITHOUT fixing tree
    @param key
	"""

    def get_parent_to_insert_from_max(self, key: AVLNode):
        cur_node: AVLNode = self.max

        # go up until reaching parent of new node
        while cur_node.has_parent() and key < cur_node.key:
            cur_node = cur_node.parent
        # insert from parent
        return self.generic_search(cur_node, key, False)

    """
    --helper method--
	find avl errors and fix with rotations 
    @param start_node : position to start search for avl error
	"""

    def fix_tree(self, start_node: AVLNode):
        count_rotations = 0
        cur_node = start_node
        while not cur_node is None:
            print('node: ', cur_node.key,
                  'with bf: ', cur_node.get_BF())
            if cur_node.get_BF() == 2:
                # left height is 1 -> rotate R
                if cur_node.left.get_BF() == 1:
                    self.rotate('R', cur_node)
                    count_rotations += 1
                # left height is -1 -> rotate LR
                else:
                    self.rotate('L', cur_node.left)
                    self.rotate('R', cur_node)
                    count_rotations += 2
            if cur_node.get_BF() == -2:
                print("ahhhhhhhhhhhhhh")
                # left height is -1 -> rotate L
                if cur_node.right.get_BF() == -1:
                    self.rotate('L', cur_node)
                    count_rotations += 1
                # left height is 1 -> rotate RL
                else:
                    self.rotate('R', cur_node.right)
                    self.rotate('L', cur_node)
                    count_rotations += 2
            cur_node = cur_node.parent

        return count_rotations

    """deletes node from the dictionary

	@type node: AVLNode
	@pre: node is a real pointer to a node in self
	@rtype: int
	@returns: the number of rebalancing operation due to AVL rebalancing
	"""

    def delete(self, node):
        """need to fix height and gilgoolim
        
        
        """
        if self.search(node.key) is None:
            return 0
        
        if (node.has_left and not node.has_right) or (node.has_right and not node.has_left):
            self.delete_with_one_son(node)

        elif not node.has_left and not node.has_right:
            self.delete_with_zero_sons(node)
        
        else:
            succ_node = self.successor(node)
            # succ cant be the root since node have 2 children

            if (succ_node.has_left and not succ_node.has_right) or (succ_node.has_right and not succ_node.has_left):
                self.delete_with_one_son(succ_node)
                
            elif not succ_node.has_left and not succ_node.has_right:
                self.delete_with_zero_sons(succ_node)

            succ_node.left = node.left
            node.left.parent = succ_node

            succ_node.right = node.right
            node.right.parent = succ_node
            succ_node.parent = node.parent


            if self.root == node:
                self.root = succ_node
            
            

            

        return -1
    


    def delete_with_one_son(self, node: AVLNode):
        if node.has_left and not node.has_right:
            if node.parent is not None:
                if node.parent.left == node:
                    node.parent.left = node.left
                    node.left.parent = node.parent
                    # maybe change node to None???
                elif node.parent.right == node:
                    node.parent.right = node.left
                    node.left.parent = node.parent
                    # maybe change node to None???
            else:
                self.root = node.left
                node.left.parent = None
        
        elif node.has_right and not node.has_left:
            if node.parent is not None:
                if node.parent.left == node:
                    node.parent.left = node.right
                    node.right.parent = node.parent
                    # maybe change node to None???
                elif node.parent.right == node:
                    node.parent.right = node.right
                    node.right.parent = node.parent
                    # maybe change node to None???  
            else:
                self.root = node.right
                node.right.parent = None



    def delete_with_zero_sons(self, node: AVLNode):
        if node.parent is not None:
            if node.parent.left == node:
                node.parent.left = node.left # ghost node
            elif node.parent.right == node:
                node.parent.right = node.right # ghost node
        else:
            self.root = None
            


    """returns an array representing dictionary

	@rtype: list
	@returns: a sorted list according to key of touples (key, value) representing the data structure
	"""

    def avl_to_array(self):
        # print("pppppppppppp " + str(self.max.has_right()))
        return self.rec_avl_to_array(self.root)

    """
    --helper method--
	gets current node and creates the in-order array recursively
    @param t: current node in the reccursion
	"""

    def rec_avl_to_array(self, t: AVLNode):
        if t is None or t.key is None:
            return []

        return self.rec_avl_to_array(t.left) + [(t.key, t.value)] + self.rec_avl_to_array(t.right)

    """returns the number of items in dictionary

	@rtype: int
	@returns: the number of items in dictionary
	"""

    def size(self):
        return len(self.avl_to_array())

    """returns the root of the tree representing the dictionary

	@rtype: AVLNode
	@returns: the root, None if the dictionary is empty
	"""

    def get_root(self):
        return self.root

    '''@returns: the number of nodes which have balance factor equals to 0 devided by the total number of nodes'''

    def get_amir_balance_factor(self):
        balance_array = [self.search(t[0]).get_BF() for t in self.avl_to_array()]
        zeros = balance_array.count(0)
        if self.size() > 0:
            return zeros/self.size()
        return 0

    def in_order(self):
        self.rec_in_order(self.root)

    def rec_in_order(self, t: AVLNode):
        if t.key is not None:
            self.rec_in_order(t.left)
            print(t.key, ' height is: ', t.height)
            self.rec_in_order(t.right)

    def print_tree_2(self, node: AVLNode, level=0, label="Root"):
        if node is not None:
            self.print_tree(node.right, level + 1, "R")
            print("    " * level + f"{label}: ({node.key}, {node.value})")
            self.print_tree(node.left, level + 1, "L")

    def init_new_real_node(self, key, value: int):
        new_real_node = AVLNode(key, value)
        left_ghost = AVLNode()
        right_ghost = AVLNode()

        new_real_node.right = right_ghost
        new_real_node.left = left_ghost
        right_ghost.parent = new_real_node
        left_ghost.parent = new_real_node

        return new_real_node
    
    def successor(self, node: AVLNode):
        if node.right.key is not None:
            ret = node.right
            while ret.left.key is not None:
                ret = ret.left.key
        else:
            ret = node
            while ret.parent is not None and ret.parent.key < ret.key:
                ret = ret.parent
            if ret.parent is None:
                ret = None
        return ret