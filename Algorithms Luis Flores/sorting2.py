import random
import threading

class Node:
    def __init__(self, data=0):
        self.left = None
        self.right = None
        self.data = data

def insertNodes(array):
    for i in range(len(array)):
        insertCall(array[i])

def printTreeinOrder(node):
    if node is not None:
        printTreeinOrder(node.left)
        print("Treesort:", node.data)
        print(final_array)
        final_array.append(node.data)
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
    printTreeinOrder(rootNode)

def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True

def bogosort(arr):
    while not is_sorted(arr):
        random.shuffle(arr)

def quicksort(arr):
    if len(arr) < 2:
        return arr
    pivot = arr[0]
    leftArray = []
    rightArray = []
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            leftArray.append(arr[i])
        else:
            rightArray.append(arr[i])
    leftSort = quicksort(leftArray)
    rightSort = quicksort(rightArray)
    result = leftSort + [pivot] + rightSort
    return result

final_array = []
rootNode = None
random_numbers = [92, 3, 13, 100, 4]

print("Before sort:")
print(random_numbers)

thread1 = threading.Thread(target=quicksort, args=(random_numbers,))
thread2 = threading.Thread(target=bogosort, args=(random_numbers.copy(),))
thread3 = threading.Thread(target=insertNodes, args=(random_numbers.copy(),))

thread1.start()
thread2.start()
thread3.start()

thread1.join()
thread2.join()
thread3.join()
