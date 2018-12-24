from collections import deque
import math

class Node:
    def __init__(self, data):
        self.value = data
        self.left = None
        self.right = None

class BinarySearchTree:
    """
    Author: Teddy

    This is an implementation of Binary Search Tree with useful methods including common operations (insert, delete, search, and traversal) 
    """
    def __init__(self):
        self.root = None
        self.type_of_data = type(self.root.value) if self.root else None
        self.count = 0
    # need to implement dunder methods like:
    # __len__ : to return the height
    # __getitem__ : to print out data of tree using one of the traversal methods

    def __len__(self):
        return self.count

    def insert(self, value):
        # PRE: value(s) has/have passed the custom type checks for type T (tree)
        # POST: value(s) is/are added onto the BST
        if self.root is None:
            self.root = Node(value)
            self.count +=1
        else:
            self._insert_node(self.root, value)

    def _insert_node(self, current, value):
        if value <= current.value:
            if current.left is None:
                current.left = Node(value)
                self.count += 1
            else:
                return self._insert_node(current.left, value)
        else:
            if current.right is None:
                current.right = Node(value)
                self.count += 1
            else:
                return self._insert_node(current.right, value)
    
    def delete(self, value):
        """
        PRE: 'value' is the value of the node we'd like to delete 
        POST: the 'value' is deleted and tree is organized which yields True, otherwise yields False
        """
        assert (self.root is not None), "Root is None and '_find_node_rref(...)' can't be used" # waiting for implementation of is_empty()
        node_to_remove = self.find_node(value)
        if node_to_remove is None:
            return False
        parent = self.find_parent(value)
        
        if node_to_remove.left is None and node_to_remove.right is None:
            # case 1: the value to remove is a leaf node
            if node_to_remove.value == self.root.value and parent is None:
                # special case: where the root node is the only node
                self.root = None
            elif node_to_remove.value < parent.value:
                # leaf node to delete is left of parent
                parent.left = None
            else:
                # leaf node to delete is right of parent
                parent.right = None
        elif node_to_remove.left is None and node_to_remove.right is not None:
            # case 2: the value to remove has a right subtree, no left subtree
            if node_to_remove.value < parent.value:
                parent.left = node_to_remove.right
            else:
                parent.right = node_to_remove.right
        elif node_to_remove.left is not None and node_to_remove.right is None:
            # case 3: the value to remove has a left subtree, no right subtree
            if node_to_remove.value < parent.value:
                parent.left = node_to_remove.left
            else:
                parent.right = node_to_remove.left
        else:
            # case 4: the value to remove has both left and right subtrees, in
            # which case we promote the largest value in the left subtree

            # Find node directly to the left of the node to remove
            largest_value = node_to_remove.left

            # traverse right of the left subtree until u find largest node in the led
            while largest_value.right is not None:
                largest_value = largest_value.right
            # dereference the largest value so that it could be promoted
            find_parent(largest_value.value).right = None
            node_to_remove.value = largest_value.value
        self.count -= 1
        return True

    def contains(self, value):
        """ 
        PRE: 'root' is the root of the tree, 'value' is the value we want to locate
        POST: we return true if the value is in the tree, false otherwise
        """
        return self._search_rbool(self.root, value)

    def find_parent(self, value):
        return self._find_parent(self.root, value)

    def _find_parent(self, root, value):
        """
        PRE: 'root' is a parent node of the BST (it cannot be None), 'value' is value of the node whose parent node we want to find
        POST: return the reference to the parent node for the 'value', or return None

        Important Note: If the value does not exist in the BST, this method returns None. Callers for this method should consider this
        """

        assert (root is not None), "Root is None and '_find_parent(...)' can't be used" # waiting for implementation of is_empty()
        
        if root.value == value:
            return None

        if root.value <= value:
            if root.left is None:
                return None
            elif root.left.value == value:
                return root
            else:
                return self._find_parent(root.left, value)
        else:
            if root.right is None:
                return None
            elif root.right.value == value:
                return root
            else:
                return self._find_parent(root.right, value)

    def _search_rbool(self, current, value):
        """
        Helper method to search for value and return a boolean
        """
        # case 1: root is None
        if current is None:
            return False
        # case 2: root equals the value
        if current.value == value:
            return True
        elif current.value <= value:
            # case 3: root.value <= value, we check the left subtree
            return self._search_rbool(current.left, value)
        else:
            # case 4: root.value > value, we check the right subtree
            return self._search_rbool(current.right, value)

    def find_node(self, value):
        return self._search_rref(self.root, value)

    def _search_rref(self, current, value):
        """
        Helper method to search for value and return a reference to node with that value
        """
        if current is None:
            return None
        # case 2: root equals the value
        if current.value == value:
            return current
        elif current.value <= value:
            # case 3: root.value <= value, we check the left subtree
            return self._search_rbool(current.left, value)
        else:
            # case 4: root.value > value, we check the right subtree
            return self._search_rbool(current.right, value)

    def is_empty(self):
        if self.root:
            return False
        return True

    def _helper_height(self, node)
        if node is None:
            return None
        return max(self.height(node.left), self.height(node.right)) + 1

    def height(self, node):
        #if self.root is None:
        #    return None
        return self._helper_height(self.root)

    def levels(self):
        print("# OF LEVELS:", math.floor(math.log2(self.count) + 1), sep=' ')

    
    # traversal strategies: pre-order, post-order, in-order, level order

    def _helper_pre(self, root):
        if root is not None:
            print(root.value)
            self._helper_pre(root.left)
            self._helper_pre(root.right)
        
    def pre_order(self):
        return self._helper_pre(self.root)

    def _helper_post(self,root):
        if root is not None:
            self._helper_post(root.left)
            print(root.value)
            self._helper_post(root.right)
        
    def post_order(self):
        return self._helper_post(self.root)

    def _helper_in(self, root):
        if root is not None:
            self._helper_in(root.left)
            self._helper_in(root.right)
            print(root.value)

    def in_order(self):
        return self._helper_in(self.root) 

    def _helper_level(self, root):
        if root:
            queue = deque()
            queue.append(root)
            while len(queue) > 0:
                rt = queue.popleft()
                print(rt.value)
                if rt.left:
                    queue.append(rt.left)
                if rt.right:
                    queue.append(rt.right)

    def level_order(self):
        return self._helper_level(self.root)

# Test Cases:
t1 = [4, 3 ,5, 1, 2, 9]

BST = BinarySearchTree()
for i in t1:
    BST.insert(i)

