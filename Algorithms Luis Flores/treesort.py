class Node:

    def __init__(self,data=0):
        #define left to none and right to none when initialize
        #set data to value received by object
        self.left=None
        self.right=None
        self.data=data
#printTree in Order, will print left farthest child will then go right recursively
def printTreeinOrder(node):

    if(node != None):
        #visit left child
        printTreeinOrder(node.left)
        #go back and print node value
        final_array.append(node.data)
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
#rootNode started
rootNode = Node()
#set to none to have no children
rootNode = None
random_numbers= [23, 56, 12,3,6, 89, 45, 67, 34, 90, 10, 78,100]
print("Before sort: "+"\n")
print(random_numbers)


for i in range(len(random_numbers)):
    insertCall(random_numbers[i])

print("After sort: "+"\n")
final_array=[]
printTreeinOrder(rootNode)
print(final_array)