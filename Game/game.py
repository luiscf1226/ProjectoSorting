import pygame
import random
import os
import sys
import time
import threading

# initialize
pygame.init()
# width and height for screen
width, height = 800, 700
# window code to set display and caption
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Space dodge")
# image
background = pygame.image.load("background.jpg").convert()
background = pygame.transform.scale(background, (width, height))
# RGB colors
white = (255, 255, 255)
# bars1
bar_positions1 = []
# bars1
bar_positions2 = []
# array bars 1
bar_array1 = []
# array bars 2
bar_array2 = []
# area 1
bar_area1 = pygame.Rect(width // 4, 190, 540, 220)
# area 2
bar_area2 = pygame.Rect(width//4, 440, 540, 220)

def selectionSort(lista,bar_positions,bar_area):
    for i in range(0, len(lista) -1):
        #set mininum for current number
        minimum = lista[i]
        swap = -1
        for j in range(i + 1, len(lista)):
            #find if theres another number smaller than current minimum
            if minimum > lista[j]:
                minimum = lista[j]
                #swap to be the current minimum
                swap = j
        if swap != -1:
            lista[swap] = lista[i]
            lista[i] = minimum
             #Update bar_positions with new heights
            bar_positions = updateBarPositions(lista, bar_area)
            # Redraw the screen to see changes reflected in bar_positions
         
            drawBarsBox1(bar_positions, lista)
            pygame.time.wait(400)  # delay of0.4 seconds


class Node:

    def __init__(self,data=0):
        #define left to none and right to none when initialize
        #set data to value received by object
        self.left=None
        self.right=None
        self.data=data
#insert in nodes
def insertNodes(array,rootNode,bar_positions,bar_area):
    for i in range(len(array)):
       insertCall(array[i],rootNode)
    
#printTree in Order, will print left farthest child will then go right recursively
def printTreeinOrder(node,final_array,bar_positions,bar_area):
 
    if(node != None):
        #visit left child
        printTreeinOrder(node.left,final_array,bar_positions,bar_area)
        #go back and print node value
        final_array.append(node.data)
        print("Treesort: "+str(final_array))
        # Update bar_positions with new heights
        bar_positions = updateBarPositions(final_array, bar_area)
        # Redraw the screen to see changes reflected in bar_positions
       
        drawBarsBox2(bar_positions, final_array)
        pygame.time.wait(400)  # delay of0.4 seconds
        pygame.display.update();

        #visit right child
        printTreeinOrder(node.right,final_array,bar_positions,bar_area)
        
       
        
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
def insertCall(data,rootNode):


    rootNode=insertNode(rootNode,data)
#
def insertionSort(lista,bar_positions,bar_area):
    for i in range(1, len(lista)):
        #set key to look for numbers smaller than in array
        key = lista[i]
        for j in range(i - 1, -1, -1):
            #if key is smaller than current number move to left 
            if key < lista[j]:
                lista[j + 1] = lista[j]
                lista[j] = key
                #Update bar_positions with new heights
                bar_positions = updateBarPositions(lista, bar_area)
                # Redraw the screen to see changes reflected in bar_positions

                drawBarsBox1(bar_positions, lista)
                pygame.time.wait(400)  # delay of0.4 seconds
def heapify(random_numbers, n, i):
    #position of the greatest number
    greatest = i
    #position of left child
    left = 2*i+1
    #position of right child
    right = 2*i+2
    #if left child is greatest than number alocated on greatest position
    if left < n and random_numbers[i] < random_numbers[left]:
        #then the greatest number is alocated in left child
        greatest = left

    #if right child is greatest than number alocated on greatest position
    if right < n and random_numbers[greatest] < random_numbers[right]:
        #then the greatest number is alocated in right child
        greatest = right

    #if greatest position has changed
    if greatest != i:
        #then we change the original greatest with the child that has the greatest number
        random_numbers[i], random_numbers[greatest] = random_numbers[greatest], random_numbers[i]
        #recall the function to continue evaluating
        heapify(random_numbers,n,greatest)

def heapsort(random_numbers,bar_positions,bar_area):
    n=len(random_numbers)
    #iterates the array from the end to the begining
    for i in range(n,-1,-1):
        #calls heapify to generates the max heap
        heapify(random_numbers,n,i)

    #iterates the array from the end to the second element
    for i in range(n-1,0,-1):
        #changes the max with the last position
        random_numbers[i], random_numbers[0] = random_numbers[0], random_numbers[i]
        #calls the heapify function with a reduced len of the array
        heapify(random_numbers, i, 0)
         # Update bar_positions with new heights
        bar_positions = updateBarPositions(random_numbers, bar_area)
        # Redraw the screen to see changes reflected in bar_positions
        drawBarsBox2(bar_positions, random_numbers)
        pygame.time.wait(400)  # delay of0.4 seconds
    return random_numbers

#method to check if its sorted
def is_sorted(arr):
    for i in range(len(arr) - 1):
        
        if arr[i] > arr[i + 1]:
            return False
    return True
#run bogo sort while its not sorted
def bogosort(random_numbers,bar_positions,bar_area):
    while not is_sorted(random_numbers):
        if killThread:
                return
        else:
            random.shuffle(random_numbers)
            # Update bar_positions with new heights
            bar_positions = updateBarPositions(random_numbers, bar_area)
            # Redraw the screen to see changes reflected in bar_positions
            drawBarsBox1(bar_positions, random_numbers)
            pygame.time.wait(400)  # delay of0.4 seconds
    return random_numbers

def quicksort(arr, bar_positions, bar_area):
    if killThread:
        return []  # raise Exception("Terminar función recursiva")
    else:
        # check if its less than 2 dont need to order array
        if len(arr) < 2:
            return arr
        # pivot element at first elememt
        pivot = arr[0]

        # left and right arrays
        leftArray = []
        rightArray = []

        # assign resulting left if smaller right if bigger than pivot element
        for i in range(1, len(arr)):
            if arr[i] < pivot:
                leftArray.append(arr[i])
            else:
                rightArray.append(arr[i])

        # recursively order left and right, this creates more lefts and rights
        leftSort = quicksort(leftArray, bar_positions, bar_area)
        rightSort = quicksort(rightArray, bar_positions, bar_area)

        # add to array left middle pivot and right
        result = leftSort + [pivot] + rightSort

        # Update arr with the sorted result
        # this lets the array be updated each recursion iteration
        for i in range(len(result)):
            arr[i] = result[i]

        # Update bar_positions with new heights
        bar_positions = updateBarPositions(result, bar_area)

        # Redraw the screen to see changes reflected in bar_positions
       
        if killThread == False:
            drawBarsBox2(bar_positions, result)
            pygame.time.wait(400)  # delay of 0.5 seconds
    return result


def bubblesort(random_numbers, bar_positions, bar_area):
    n = len(random_numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            # swap if next element in array is greather
            if killThread:
                return
            if random_numbers[j] > random_numbers[j+1]:
                random_numbers[j], random_numbers[(
                    j+1)] = random_numbers[j+1], random_numbers[j]

                # Update bar_positions with new heights
                bar_positions = updateBarPositions(random_numbers, bar_area)

                # Redraw the screen to see changes reflected in bar_positions
               
                drawBarsBox2(bar_positions, random_numbers)
                pygame.time.wait(400)  # delay of0.4 seconds


def drawBarsBox1(bar_positions, bar_heights):
    # area 2
    #bar_area2 = pygame.Rect(width//4, 440, 540, 220)
    pygame.draw.rect(window, white, [width//4, 190, 540, 220])
    color_red = (170, 0, 0)
    bar_width = 10
    # gets x,y coordinates and height to be drawn from bars arrays
    for (bar_x, bar_y), bar_height in zip(bar_positions, bar_heights):
        pygame.draw.rect(window, color_red, [
            bar_x, bar_y, bar_width, bar_height])
    pygame.display.update()


def drawBarsBox2(bar_positions2, bar_heights2):
    pygame.draw.rect(window, white, [width//4, 440, 540, 220])
    color_red = (170, 0, 0)
    bar_width = 10
    # gets x,y coordinates and height to be drawn from bars arrays
    for (bar_x, bar_y), bar_height in zip(bar_positions2, bar_heights2):
        pygame.draw.rect(window, color_red, [
            bar_x, bar_y, bar_width, bar_height])
    pygame.display.update()


def insertBars1():
    # set bar area to the rectangle
    bar_width = 10
    num_bars = 10

    # distance between bars
    distance_between_bars = 5

    # Generate bars

    for i in range(num_bars):
        # generate x coordinate
        bar_x = bar_area1.left + i * (bar_width + distance_between_bars)
        # random height
        bar_height = random.randint(50, 130)
        # generate y coordinate
        bar_y = bar_area1.bottom - bar_height
        bar_positions1.append((bar_x, bar_y))
        bar_array1.append(bar_height)


def insertBars2():
    # set bar area to the rectangle
    bar_width = 10
    num_bars = 10

    # distance between bars
    distance_between_bars = 5

    # Generate bars
    for i in range(num_bars):
        # generate x coordinate
        bar_x = bar_area2.left + i * (bar_width + distance_between_bars)
        # random height
        bar_height = random.randint(50, 130)
        # generate y coordinate
        bar_y = bar_area2.bottom - bar_height
        bar_positions2.append((bar_x, bar_y))
        bar_array2.append(bar_height)


def updateBarPositions(bar_heights, reference_rect):

    bar_width = 10
    distance_between_bars = 5
    new_positions = []
    # since array changes with each iteration of sorting, it needs to update
    for i, height in enumerate(bar_heights):
        # get border of rectangle and add 10 to each bar
        bar_x = reference_rect.left + i * (bar_width + distance_between_bars)
        # subtract from bottom border height
        bar_y = reference_rect.bottom - height
        new_positions.append((bar_x, bar_y))
    return new_positions


def clearScreen():
    window.fill((255, 255, 255))


def drawSetup(bar_positions1, bar_array1, bar_positions2, bar_array2):
    window.blit(background, (0, 0))
    # Title object
    font = pygame.font.Font(None, 48)
    # create text
    textTitle = font.render("Code Battle", True, white)
    # create surface title
    textTitleSurface = textTitle.get_rect()
    # set coordinates for text
    textTitleSurface.midtop = (width//2, 20)
    window.blit(textTitle, textTitleSurface)

    # Settings Title object
    font2 = pygame.font.Font(None, 35)
    # create text
    textTitle2 = font2.render("Settings:", True, white)
    # create surface title
    textTitleSurface2 = textTitle2.get_rect()
    # set coordinates for text
    textTitleSurface2.midtop = (width//4, 80)

    window.blit(textTitle2, textTitleSurface2)

    # Start game
    font3 = pygame.font.Font(None, 35)
    # create text
    textTitle3 = font3.render("Start Game:", True, white)
    # create surface title
    textTitleSurface3 = textTitle3.get_rect()
    # set coordinates for text
    textTitleSurface3.midtop = (width//3.7, 140)
    window.blit(textTitle3, textTitleSurface3)

    # Sort1
    font4 = pygame.font.Font(None, 35)
    # create text
    textTitle4 = font4.render("Sort #1:", True, white)
    # create surface title
    textTitleSurface4 = textTitle4.get_rect()
    # set coordinates for text
    textTitleSurface4.midtop = (width//6, 300)
    window.blit(textTitle4, textTitleSurface4)

    # Sort2
    font5 = pygame.font.Font(None, 35)
    # create text
    textTitle5 = font5.render("Sort #2:", True, white)
    # create surface title
    textTitleSurface5 = textTitle5.get_rect()
    # set coordinates for text
    textTitleSurface5.midtop = (width//6, 480)
    window.blit(textTitle5, textTitleSurface5)
    # button settings
    # button colors
    color_button = (170, 0, 0)

    # button fonts
    smallfont = pygame.font.SysFont(None, 35)

    # rendering text with different colors
    text_button = smallfont.render('Change', True, white)
    # text = smallfont.render('Change', True, white)
    # pygame.draw.rect(window, color_button, [width//2.6, 75, 110, 30])
    window.blit(text_button, (width//2.5, 75))
    # button game
    # button colors
    # color_button = (170, 0, 0)

    # button fonts
    smallfont = pygame.font.SysFont(None, 35)

    # rendering text with different colors
    # text_button = smallfont.render('Start', True, white)
    # text = smallfont.render('start', True, white)
    # pygame.draw.rect(window, color_button, [width//2.6, 135, 110, 30])
    # window.blit(text_button, (width//2.5, 135))

    # draws rectangle 1
    pygame.draw.rect(window, white, [width//4, 190, 540, 220])
    pygame.draw.rect(window, white, [width//4, 440, 540, 220])

    drawBarsBox1(bar_positions1, bar_array1)
    drawBarsBox2(bar_positions2, bar_array2)


click = False
clock = pygame.time.Clock()
killThread = False


def clearArrays():
    bar_positions1.clear()
    bar_positions2.clear()
    bar_array1.clear()
    bar_array2.clear()


def main_menu():


    global killThread
    startThread = False
    # insert random bars to arrays
    insertBars1()
    insertBars2()
    # draw all main_menu components
    drawSetup(bar_positions1, bar_array1, bar_positions2, bar_array2)

    # create threads for sorting methods
    bubblesort_thread = None
    quicksort_thread = None
    bogosort_thread=None
    heapsort_thread=None
    insertionSort_thread=None
    selectionSort_thread=None
    thread3=None
    startThread = True

    #rootNode started

    rootNode = Node()
    #set to none to have no children
 

    while True:
        text_button_settings = pygame.font.SysFont(
            None, 35).render('Change', True, white)
        text_button_start = pygame.font.SysFont(
            None, 35).render('Start', True, white)
        # text = smallfont.render('start', True, white)
        mx, my = pygame.mouse.get_pos()
        settingButton = pygame.Rect(width//2.6, 75, 110, 30)
        startButton = pygame.Rect(width//2.6, 135, 110, 30)
        if settingButton.collidepoint((mx, my)):
            if click:
                killThread = True
                settings()
                # insert random bars to arrays
                clearArrays()
                insertBars1()
                insertBars2()
                # draw all main_menu components
                drawSetup(bar_positions1, bar_array1,
                          bar_positions2, bar_array2)
                startThread = True

        bubblesort_thread = threading.Thread(
            target=bubblesort, args=(bar_array2, bar_positions2, bar_area2), daemon=True)
        
        bogosort_thread = threading.Thread(
            target=bogosort, args=(bar_array1, bar_positions1, bar_area1), daemon=True)
        
        heapsort_thread = threading.Thread(
            target=heapsort, args=(bar_array2, bar_positions2, bar_area2), daemon=True)
        
        quicksort_thread = threading.Thread(
            target=quicksort, args=(bar_array2, bar_positions2, bar_area2), daemon=True)
        
        thread3 = threading.Thread(target=insertNodes, args=(bar_array1,rootNode,bar_positions1,bar_area1), daemon=True)

        insertionSort_thread= threading.Thread(target=insertionSort,args=(bar_array1,bar_positions1,bar_area1), daemon=True)

        selectionSort_thread= threading.Thread(target=insertionSort,args=(bar_array1,bar_positions1,bar_area1), daemon=True)
        if startButton.collidepoint((mx, my)):
            if click and startThread:
                startThread = False
                #bubblesort_thread.start()
              
                #thread3.start()
                #bogosort_thread.start()
                #heapsort_thread.start()
                bubblesort_thread.start()
                pygame.display.update()
                # startThread1 = False
                insertionSort_thread.start()
                pygame.display.update()
                #selectionSort_thread.start()
               
                #quicksort_thread.start()
               
             
                #printTreeinOrder(rootNode,bar_array1,bar_positions1,bar_area1)
                
                if bubblesort_thread.is_alive() == False and insertionSort_thread.is_alive() == False:
                    startThread = True
                '''if bogosort_thread.is_alive() == False and quicksort_thread.is_alive() == False:
                    startThread = True'''
                '''if heapsort_thread.is_alive() == False and quicksort_thread.is_alive() == False:
                    startThread = True'''
                '''if insertionSort_thread.is_alive() == False and quicksort_thread.is_alive() == False:
                    startThread = True'''
                '''if selectionSort_thread.is_alive() == False and quicksort_thread.is_alive() == False:
                    startThread = True'''
                
        pygame.draw.rect(window, (170, 0, 0), settingButton)
        window.blit(text_button_settings, (width//2.5, 75))
        pygame.draw.rect(window, (170, 0, 0), startButton)
        window.blit(text_button_start, (width//2.5, 135))

        click = False
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True

        if bubblesort_thread is not None and not bubblesort_thread.is_alive():
            bubblesort_thread = None
        if bogosort_thread is not None and not bogosort_thread.is_alive():
            bogosort_thread = None
        if heapsort_thread is not None and not heapsort_thread.is_alive():
            heapsort_thread = None
        if quicksort_thread is not None and not quicksort_thread.is_alive():
            quicksort_thread = None
        if insertionSort_thread is not None and not insertionSort_thread.is_alive():
            insertionSort_thread = None
        if selectionSort_thread is not None and not selectionSort_thread.is_alive():
            selectionSort_thread = None

        pygame.display.update()
        clock.tick(60)


def settings():
    global killThread
    run = True
    window.blit(background, (0, 0))
    escapeToGoBack = pygame.font.SysFont(
        None, 45).render('Press ESC to return to the main menu', True, white)
    window.blit(escapeToGoBack, (width//7, 120))
    while run:
        for event in pygame.event.get():
            if (event.type == pygame.QUIT):
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    killThread = False

        pygame.display.update()
        clock.tick(60)


def main():
    main_menu()


# run file if its main
if __name__ == "__main__":
    main()
