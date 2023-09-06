#imports necessary
import random
import threading
import time
#function to determine if array is sorted
class Node:

    def __init__(self,data=0):
        #define left to none and right to none when initialize
        #set data to value received by object
        self.left=None
        self.right=None
        self.data=data
#insert in nodes
def insertNodes(array):
    for i in range(len(array)):
       insertCall(array[i])
#printTree in Order, will print left farthest child will then go right recursively
def printTreeinOrder(node):
 
    if(node != None):
        #visit left child
        printTreeinOrder(node.left)
        #go back and print node value
       
        final_array.append(node.data)
        print("Treesort: "+str(final_array))
        #visit right child
        printTreeinOrder(node.right)

        
#insertNode function recursively if smaller or greater will decide to go left child or right
def insertNode(node,data):

    #check if theres a root if not make it the current Node
    if (node==None):
        node=Node(data)
        return node
    
    #if value is smaller than current in node it will be assigned to left node recursively
    if(data<node.data):
        node.left=insertNode(node.left,data)
       
    #if value is greater than current in node it will be assigned to left node recursively    
    elif (data>node.data):
        node.right=insertNode(node.right,data)    
        
   
    #recursion ends and node is inserted with data checked if smaller or greater than current
    return node
def insertCall(data):

    global rootNode
    rootNode=insertNode(rootNode,data)
#
def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True
#function for bogosort algorithm
def bogosort(arr):
    while not is_sorted(arr):
        random.shuffle(arr)
    
        print("Bogosort:", arr)
#function for quick sort
def quicksort(arr):
    #check if its less than 2 dont need to order array
    if len(arr) < 2:
        return arr
    #pivot element at first elememt
    #left and right arrays
    pivot = arr[0]
    leftArray = []
    rightArray = []
    #assign left if smaller right if bigger than pivot element
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            leftArray.append(arr[i])
        else:
            rightArray.append(arr[i])

    #recursively order left and right, this creates more lefts and rights
    leftSort = quicksort(leftArray)
    rightSort = quicksort(rightArray)
    #add to array left middle pivot and right
    result = leftSort + [pivot] + rightSort
    #print before returning
    print("Quicksort :", result)
    return result
#rootNode started

rootNode = Node()
#set to none to have no children
rootNode = None
#array with numbers
random_numbers = [23, 56, 12,3,6, 89, 45, 67, 34, 90, 10, 78,100]
print("Before sort:")
print(random_numbers)
final_array=[]
#create threads with target and argumments to the function called
thread1 = threading.Thread(target=quicksort, args=(random_numbers,))
#thread2 = threading.Thread(target=bogosort, args=(random_numbers.copy(),))
thread3 = threading.Thread(target=insertNodes, args=(random_numbers.copy(),))
#starts threads
thread1.start()
#thread2.start()
thread3.start()
printTreeinOrder(rootNode)
#join means thread finished
thread1.join()
#join means thread finished
#thread2.join()
#join means thread finished
thread3.join()
