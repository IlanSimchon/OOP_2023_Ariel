# Author: OMKAR PATHAK
# Editor: Ofri Tavor

# This program illustrates an example of Binary Search Tree using Python
# Binary Search Tree, is a node-based binary tree data structure which has the following properties:
#
# The left subtree of a node contains only nodes with keys less than the node’s key.
# The right subtree of a node contains only nodes with keys greater than the node’s key.
# The left and right subtree each must also be a binary search tree.
# There must be no duplicate nodes.

class Node(object):
    def __init__(self, data):
        self.data = data
        self.leftChild = None
        self.rightChild = None

    def insert(self, data):
        ''' For inserting the data in the Tree '''
        if self.data == data:
            return False        # As BST cannot contain duplicate data

        elif data < self.data:
            ''' Data less than the root data is placed to the left of the root '''
            if self.leftChild:
                return self.leftChild.insert(data)
            else:
                self.leftChild = Node(data)
                return True

        else:
            ''' Data greater than the root data is placed to the right of the root '''
            if self.rightChild:
                return self.rightChild.insert(data)
            else:
                self.rightChild = Node(data)
                return True

    def minValueNode(self, node):
        current = node

        # loop down to find the leftmost leaf
        while(current.leftChild is not None):
            current = current.leftChild

        return current

    def maxValueNode(self, node):
        current = node

        # loop down to find the leftmost leaf
        while(current.rightChild is not None):
            current = current.rightChild

        return current


    def delete(self, data,root):
        ''' For deleting the node '''
        if self is None:
            return None

        # if current node's data is less than that of root node, then only search in left subtree else right subtree
        if data < self.data:
            self.leftChild = self.leftChild.delete(data,root)
        elif data > self.data:
            self.rightChild = self.rightChild.delete(data,root)
        else:
            # deleting node with one child
            if self.leftChild is None:

                if self == root:
                    temp = self.minValueNode(self.rightChild)
                    self.data = temp.data
                    self.rightChild = self.rightChild.delete(temp.data,root)

                temp = self.rightChild
                self = None
                return temp
            elif self.rightChild is None:

                if self == root:
                    temp = self.maxValueNode(self.leftChild)
                    self.data = temp.data
                    self.leftChild = self.leftChild.delete(temp.data,root)

                temp = self.leftChild
                self = None
                return temp

            # deleting node with two children
            # first get the inorder successor
            temp = self.minValueNode(self.rightChild)
            self.data = temp.data
            self.rightChild = self.rightChild.delete(temp.data, root)

        return self

    def find(self, data):
        ''' This function checks whether the specified data is in tree or not '''
        if(data == self.data):
            return True
        elif(data < self.data):
            if self.leftChild:
                return self.leftChild.find(data)
            else:
                return False
        else:
            if self.rightChild:
                return self.rightChild.find(data)
            else:
                return False

    def preorder(self, keep):
        '''For preorder traversal of the BST '''
        if self:
            print(str(self.data), end = ' ')
            keep.append(self.data)
            if self.leftChild:
                self.leftChild.preorder(keep)
            if self.rightChild:
                self.rightChild.preorder(keep)

    def inorder(self, keep):
        ''' For Inorder traversal of the BST '''
        if self:
            if self.leftChild:
                self.leftChild.inorder(keep)
            keep.append(self.data)
            print(str(self.data), end = ' ')
            if self.rightChild:
                self.rightChild.inorder(keep)

    def postorder(self, keep):
        ''' For postorder traversal of the BST '''
        if self:
            if self.leftChild:
                self.leftChild.postorder(keep)
            if self.rightChild:
                self.rightChild.postorder(keep)
            keep.append(self.data)
            print(str(self.data), end = ' ')

class Tree(object):
    def __init__(self):
        self.root = None

    def insert(self, data):
        if self.root:
            return self.root.insert(data)
        else:
            self.root = Node(data)
            return True

    def delete(self, data):
        if self.root is not None:
            return self.root.delete(data,self.root)

    def find(self, data):
        if self.root:
            return self.root.find(data)
        else:
            return False

    def preorder(self, keep=[]):
        if self.root is not None:
            print()
            print('Preorder: ')
            self.root.preorder(keep)

    def inorder(self, keep=[]):
        print()
        if self.root is not None:
            print('Inorder: ')
            self.root.inorder(keep)

    def postorder(self, keep=[]):
        print()
        if self.root is not None:
            print('Postorder: ')
            self.root.postorder(keep)

    def level_order(self, keep):
        if self.root is not None:
            print('LevelOrder: ')
            q = []
            q.insert(0, self.root)
            while len(q) > 0:
                node = q.pop(0)
                keep.append(node.data)
                if node.leftChild is not None:
                    q.append(node.leftChild)
                if node.rightChild is not None:
                    q.append(node.rightChild)

    """Default iterator: inOrder Traversal iterator"""

    def __iter__(self):
        keep = []
        self.inorder(keep)
        return keep.__iter__()

    def create_custom_iterator(self, iterator_type: int):
        keep = []
        if iterator_type==0:
            self.inorder(keep)
        elif iterator_type==1:
            self.preorder(keep)
        elif iterator_type==2:
            self.postorder(keep)
        elif iterator_type==3:
            self.level_order(keep)
        else:
            self.level_order(keep)
            keep.reverse()
        return keep.__iter__()

if __name__ == '__main__':
    tree = Tree()
    tree.insert(10)
    tree.insert(12)
    tree.insert(5)
    tree.insert(4)
    tree.insert(20)
    tree.insert(8)
    tree.insert(7)
    tree.insert(15)
    tree.insert(13)
    print(tree.find(1))
    print(tree.find(12))
    keep = []
    # tree.inorder(keep)
    tree.level_order(keep)
    it = tree.create_custom_iterator(5)

    ''' Following tree is getting created:
                    10
                 /      \
               5         12
              / \           \
            4     8          20
                 /          /
                7         15
                         /
                       13
    '''

    tree.preorder()
    tree.inorder()
    tree.postorder()
    print('\n\nAfter deleting 20')
    tree.delete(20)
    tree.inorder()
    tree.preorder()
    print('\n\nAfter deleting 10')
    tree.delete(10)
    tree.inorder()
    tree.preorder()
    it = tree.create_custom_iterator(5)
