import sys


def preorder(v):
    if v == '.':
        return
    print(v, end='')
    preorder(l_child[v])
    preorder(r_child[v])


def inorder(v):
    if v == '.':
        return
    inorder(l_child[v])
    print(v, end='')
    inorder(r_child[v])


def postorder(v):
    if v == '.':
        return
    postorder(l_child[v])
    postorder(r_child[v])
    print(v, end='')


N = int(sys.stdin.readline().rstrip())
l_child = {}
r_child = {}
for _ in range(N):
    v, l, r = sys.stdin.readline().rstrip().split()
    l_child[v] = l
    r_child[v] = r

preorder('A')
print()
inorder('A')
print()
postorder('A')
print()
