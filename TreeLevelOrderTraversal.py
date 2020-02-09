class Node:
    def __init__(self, info):
        self.info = info
        self.left = None
        self.right = None
        self.level = None

    def __str__(self):
        return str(self.info)


class BinarySearchTree:
    def __init__(self):
        self.root = None

    def create(self, val):
        if self.root == None:
            self.root = Node(val)
        else:
            current = self.root

            while True:
                if val < current.info:
                    if current.left:
                        current = current.left
                    else:
                        current.left = Node(val)
                        break
                elif val > current.info:
                    if current.right:
                        current = current.right
                    else:
                        current.right = Node(val)
                        break
                else:
                    break


"""
Node is defined as
self.left (the left child of the node)
self.right (the right child of the node)
self.info (the value of the node)
"""


def levelOrder(root):
    nodesToProcess = []
    result = []

    if root:
        nodesToProcess.append(root)

    while nodesToProcess:
        node = nodesToProcess.pop(0)
        result.append(node.info)
        if node.left:
            nodesToProcess.append(node.left)
        if node.right:
            nodesToProcess.append(node.right)

    return result

def levelOrderNodesOf(aNodesNumberString, aStringNodesList):

    tree = BinarySearchTree()
    t = int(aNodesNumberString)

    arr = list(map(int, aStringNodesList.split()))

    for i in range(t):
        tree.create(arr[i])

    return levelOrder(tree.root)