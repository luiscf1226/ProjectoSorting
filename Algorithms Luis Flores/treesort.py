final_array = []

class Node:
    def __init__(self, data=0):
        self.left = None
        self.right = None
        self.data = data

def printTreeinOrder(node):
    global final_array

    if node is not None:
        printTreeinOrder(node.left)
        final_array.append(node.data)
        print(f"Array after adding {node.data}: {final_array}")
        printTreeinOrder(node.right)

def insertNode(node, data):
    if node is None:
        node = Node(data)
        return node

    if data < node.data:
        node.left = insertNode(node.left, data)
    elif data > node.data:
        node.right = insertNode(node.right, data)

    return node

def insertCall(data):
    global rootNode
    rootNode = insertNode(rootNode, data)

rootNode = None
random_numbers = [23, 56, 12, 3, 6, 89, 45, 67, 34, 90, 10, 78, 100]
print("Before sort:")
print(random_numbers)

for num in random_numbers:
    insertCall(num)

print("After sort:")
final_array = []
printTreeinOrder(rootNode)
print(f"Final sorted array: {final_array}")
