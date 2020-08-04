""" Binary Search Tree """

# This BinarySearchTree works for unique values only


class BinarySearchTree:

    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

    """ Inserting Node """

    def insert(self, value):
        if not self.value:
            self.value = value
        else:
            if value < self.value:
                if not self.left:
                    self.left = BinarySearchTree(value)
                else:
                    self.left.insert(value)
            elif value > self.value:
                if not self.right:
                    self.right = BinarySearchTree(value)
                else:
                    self.right.insert(value)

    """ Search a Node """

    def search(self, value, parent=None):
        if value == self.value:
            return self, parent
        elif value < self.value:
            if not self.left:
                return None, None
            return self.left.search(value, self)
        elif value > self.value:
            if not self.right:
                return None, None
            return self.right.search(value, self)

    """ Number of childerns of particular node """

    def child_count(self):
        count = 0
        if self.left:
            count += 1
        if self.right:
            count += 1
        return count

    """ Delete node having 0 child """

    def delete_node_with_0_child(self, node, parent):
        if parent:
            if parent.right is node:
                parent.right = None
            elif parent.left is node:
                parent.left = None
            else:
                # Node not found
                return -1
            tmp = node
            del node
            return tmp
        else:
            if self == node:
                tmp = self
                del self
                return self
            # Node not found
            return -1

    """ Delete node having 1 child """

    def delete_node_with_1_child(self, node, parent):
        if node.left:
            child_node = node.left
        else:
            child_node = node.right

        if parent:
            if parent.left is node:
                parent.left = child_node
            else:
                parent.right = child_node
            tmp = node
            del node
            return tmp
        else:
            self.value = child_node.value
            self.left = child_node.left
            self.right = child_node.right
            tmp = self
            del self
            return tmp

    """ Copy dunder method """

    def __copy__(self):
        return self

    """ Delete node having 2 child """

    def delete_node_with_2_child(self, node, parent):
        tmp = node.value
        # If we assigned the node to tmp then changes in node will
        # affect value of tmp, to avoid that we are just assigning
        # node's value

        parent = node

        # Choosing the successor from right subtree
        successor = node.right

        # Finding the smallest node in left subtree of our successor
        while successor.left:
            parent = successor.left
            successor = successor.left

        # Replacing the node with successor value
        node.value = successor.value

        # if the successor is in left subtree of parent then making
        # the right subtree of successor as left subtree of parent
        if parent.left is successor:
            parent.left = successor.right
        else:
            # if the successor's right subree has only one node then
            # making that node as parent's right subtree
            parent.right = successor.right

        del node
        return tmp

    """ delete method can delete node with 0, 1, or 2 child(s) """

    def delete(self, node):
        node, parent = self.search(node)
        if node:
            num_of_child = node.child_count()
            if num_of_child == 0:
                return self.delete_node_with_0_child(node, parent)
            elif num_of_child == 1:
                return self.delete_node_with_1_child(node, parent)
            else:
                return self.delete_node_with_2_child(node, parent)

    """ Preorder """

    def preorder(self):
        print(self.value, end=" ")
        if self.left:
            self.left.preorder()
        if self.right:
            self.right.preorder()

    """ Inorder """

    def inorder(self):
        if self.left:
            self.left.inorder()
        print(self.value, end=" ")
        if self.right:
            self.right.inorder()

    """ Postorder """

    def postorder(self):
        if self.left:
            self.left.postorder()
        if self.right:
            self.right.postorder()
        print(self.value, end=" ")


b = BinarySearchTree(5)
print(b.value, b.left, b.right)

b.insert(3)
print(b.value, b.left.value, b.right)

b.insert(7)
print(b.value, b.left.value, b.right.value)

b.insert(10)
b.insert(9)

n, p = b.search(9)
print(n.value, p.value)

print(b.delete(9).value)
n, p = b.search(9)
print(n, p)

print(b.delete(5))
print(b.value, b.left.value, b.right.value)

b.inorder()
