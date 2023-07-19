import sys

sys.setrecursionlimit(50000)

class Node:
    data = None
    l_child = None
    r_child = None

    def __init__(self, data):
        self.data = data


class BinaryTree:
    root = None

    def preorder(self, v):
        if v == None:
            return
        print(v.data)
        self.preorder(v.l_child)
        self.preorder(v.r_child)

    def inorder(self, v):
        if v == None:
            return
        self.inorder(v.l_child)
        print(v.data)
        self.inorder(v.r_child)

    def postorder(self, v):
        if v == None:
            return
        self.postorder(v.l_child)
        self.postorder(v.r_child)
        print(v.data)

    def insert(self, num):
        newNode = Node(num)
        if self.root == None:
            self.root = newNode
            return

        cur = self.root
        parent = None
        while cur != None:
            parent = cur
            if cur.data > num:
                cur = cur.l_child
            else:
                cur = cur.r_child
        if parent.data > num:
            parent.l_child = newNode
        else:
            parent.r_child = newNode


tree = BinaryTree()
while True:
    input = sys.stdin.readline().rstrip()
    if input == '':
        break
    tree.insert(int(input))

tree.postorder(tree.root)
