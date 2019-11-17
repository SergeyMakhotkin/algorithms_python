from binarytree import tree, bst, Node, build


class MyNode:

    def __init__(self, data, left=None, right=None):
        self.data = data
        self.left = left
        self.right = right


# 1 способ формирования дерева. использование функции tree из модуля binarytree
a = tree(height=4, is_perfect=False)
# print(a)

b = bst(height=5, is_perfect=True)
# print(b)

# 2 способ формирования дерева. использование класса Node из модуля binarytree
c = Node(7)
c.left = Node(3)
c.right = Node(11)
c.left.left = Node(1)
c.left.right = Node(5)
c.right.left = Node(9)
c.right.right = Node(13)
print(c)

# 3 способ. использование списка и функции build
d = build([7, 3, 11, 1, 5, 9, 3, None, 2, None, 6])
print(d)
