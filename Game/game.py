import pygame
import random
import os
import sys
import threading
import time

global start_time1
global start_time2

global end_time1
global end_time2

thread1_time = 0
thread2_time = 0

# initialize
pygame.init()
# width and height for screen
width, height = 800, 700
# window code to set display and caption
window = pygame.display.set_mode((width, height))
pygame.display.set_caption("Sort Royale")
# image
background = pygame.image.load(os.path.join("assets", "background.jpg")).convert()
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
bar_area2 = pygame.Rect(width // 4, 440, 540, 220)


def selectionSort(lista, bar_positions, bar_area):
    if bar_area2 == bar_area:
        global start_time2
        start_time2 = time.time()
    elif bar_area1 == bar_area:
        global start_time1
        start_time1 = time.time()
    for i in range(0, len(lista) - 1):
        minimum = lista[i]
        swap = -1
        for j in range(i + 1, len(lista)):
            if minimum > lista[j]:
                minimum = lista[j]
                swap = j
        if swap != -1:
            lista[swap] = lista[i]
            lista[i] = minimum
            bar_positions = updateBarPositions(lista, bar_area)
            # Redraw the screen to see changes reflected in bar_positions
            if bar_area2 == bar_area:
                drawBarsBox2(bar_positions, lista)
            elif bar_area1 == bar_area:
                drawBarsBox1(bar_positions, lista)
            pygame.time.wait(400)  # delay of0.4 seconds
            pygame.display.update()
    if bar_area2 == bar_area:
        global end_time2
        end_time2 = time.time()
        global thread2_time
        thread2_time = end_time2 - start_time2
        print(f"Time taken by the algorithm: {thread2_time} seconds")

    elif bar_area1 == bar_area:
        global end_time1
        end_time1 = time.time()
        global thread1_time
        thread1_time = end_time1 - start_time1
        print(f"Time taken by the algorithm: {thread1_time} seconds")


def mergeSort(lista, bar_positions, bar_area):
    if bar_area2 == bar_area:
        global start_time2
        start_time2 = time.time()
    elif bar_area1 == bar_area:
        global start_time1
        start_time1 = time.time()
    if len(lista) == 1:
        return lista

    middle = len(lista) // 2
    left = lista[:middle]
    right = lista[middle:]
    l1 = mergeSort(left, bar_positions, bar_area)
    l2 = mergeSort(right, bar_positions, bar_area)
    if bar_area2 == bar_area:
        global end_time2
        end_time2 = time.time()
        global thread2_time
        thread2_time = end_time2 - start_time2
        print(f"Time taken by the algorithm: {thread2_time} seconds")

    elif bar_area1 == bar_area:
        global end_time1
        end_time1 = time.time()
        global thread1_time
        thread1_time = end_time1 - start_time1
        print(f"Time taken by the algorithm: {thread1_time} seconds")
    return merge(l1, l2, bar_area, bar_positions)


def merge(listaA, listaB, bar_area, bar_positions):
    listaNueva = []
    while len(listaA) > 0 and len(listaB) > 0:
        if listaA[0] > listaB[0]:
            listaNueva.append(listaB.pop(0))
        else:
            listaNueva.append(listaA.pop(0))
    # Update bar_positions with new heights

    if len(listaA) > 0:
        listaNueva.extend(listaA)
    elif len(listaB) > 0:
        listaNueva.extend(listaB)
    bar_positions = updateBarPositions(listaNueva, bar_area)
    # Redraw the screen to see changes reflected in bar_positions
    if bar_area2 == bar_area:
        drawBarsBox2(bar_positions, listaNueva)
    elif bar_area1 == bar_area:
        drawBarsBox1(bar_positions, listaNueva)

    pygame.time.wait(400)  # delay of0.4 seconds
    pygame.display.update()
    return listaNueva


class Node:
    def __init__(self, data):
        # define left to none and right to none when initialize
        # set data to value received by object
        self.left = None
        self.right = None
        self.data = data


# insert in nodes


def insertNodes(array, bar_positions, bar_area):
    if bar_area2 == bar_area:
        global start_time2
        start_time2 = time.time()
    elif bar_area1 == bar_area:
        global start_time1
        start_time1 = time.time()
    for i in range(len(array)):
        insertCall(array[i])

    final_array = []  # Initialize an empty final_array here
    printTreeinOrder(rootNode, final_array, bar_positions, bar_area)
    if bar_area2 == bar_area:
        global end_time2
        end_time2 = time.time()
        global thread2_time
        thread2_time = end_time2 - start_time2
        print(f"Time taken by the algorithm: {thread2_time} seconds")

    elif bar_area1 == bar_area:
        global end_time1
        end_time1 = time.time()
        global thread1_time
        thread1_time = end_time1 - start_time1
        print(f"Time taken by the algorithm: {thread1_time} seconds")


# printTree in Order, will print left farthest child will then go right recursively


def printTreeinOrder(node, final_array, bar_positions, bar_area):
    if node != None:
        # visit left child
        printTreeinOrder(node.left, final_array, bar_positions, bar_area)
        # go back and print node value
        final_array.append(node.data)

        # Update bar_positions with new heights
        bar_positions = updateBarPositions(final_array, bar_area)
        # Redraw the screen to see changes reflected in bar_positions
        if bar_area2 == bar_area:
            drawBarsBox2(bar_positions, final_array)
        elif bar_area1 == bar_area:
            drawBarsBox1(bar_positions, final_array)
        pygame.time.wait(400)  # delay of0.4 seconds
        pygame.display.update()

        # visit right child
        printTreeinOrder(node.right, final_array, bar_positions, bar_area)


# insertNode function recursively if smaller or greater will decide to go left child or right
def insertNode(node, data):
    # check if theres a root if not make it the current Node
    if node == None:
        node = Node(data)
        return node

    # if value is smaller than current in node it will be assigned to left node recursively
    if data <= node.data:
        node.left = insertNode(node.left, data)

    # if value is greater than current in node it will be assigned to left node recursively
    elif data >= node.data:
        node.right = insertNode(node.right, data)

    # recursion ends and node is inserted with data checked if smaller or greater than current
    return node


def insertCall(data):
    global rootNode

    rootNode = insertNode(rootNode, data)


#


def insertionSort(lista, bar_positions, bar_area):
    if bar_area2 == bar_area:
        global start_time2
        start_time2 = time.time()
    elif bar_area1 == bar_area:
        global start_time1
        start_time1 = time.time()
    for i in range(1, len(lista)):
        key = lista[i]
        for j in range(i - 1, -1, -1):
            if key < lista[j]:
                lista[j + 1] = lista[j]
                lista[j] = key
                # Update bar_positions with new heights
                bar_positions = updateBarPositions(lista, bar_area)
                # Redraw the screen to see changes reflected in bar_positions
                if bar_area2 == bar_area:
                    drawBarsBox2(bar_positions, lista)
                elif bar_area1 == bar_area:
                    drawBarsBox1(bar_positions, lista)
            pygame.time.wait(400)  # delay of0.4 seconds
    if bar_area2 == bar_area:
        global end_time2
        end_time2 = time.time()
        global thread2_time
        thread2_time = end_time2 - start_time2
        print(f"Time taken by the algorithm: {thread2_time} seconds")

    elif bar_area1 == bar_area:
        global end_time1
        end_time1 = time.time()
        global thread1_time
        thread1_time = end_time1 - start_time1
        print(f"Time taken by the algorithm: {thread1_time} seconds")


def heapify(random_numbers, n, i):
    # position of the greatest number
    greatest = i
    # position of left child
    left = 2 * i + 1
    # position of right child
    right = 2 * i + 2
    # if left child is greatest than number alocated on greatest position
    if left < n and random_numbers[i] < random_numbers[left]:
        # then the greatest number is alocated in left child
        greatest = left

    # if right child is greatest than number alocated on greatest position
    if right < n and random_numbers[greatest] < random_numbers[right]:
        # then the greatest number is alocated in right child
        greatest = right

    # if greatest position has changed
    if greatest != i:
        # then we change the original greatest with the child that has the greatest number
        random_numbers[i], random_numbers[greatest] = (
            random_numbers[greatest],
            random_numbers[i],
        )
        # recall the function to continue evaluating
        heapify(random_numbers, n, greatest)


def heapsort(random_numbers, bar_positions, bar_area):
    if bar_area2 == bar_area:
        global start_time2
        start_time2 = time.time()
    elif bar_area1 == bar_area:
        global start_time1
        start_time1 = time.time()
    n = len(random_numbers)
    # iterates the array from the end to the begining
    for i in range(n, -1, -1):
        # calls heapify to generates the max heap
        heapify(random_numbers, n, i)

    # iterates the array from the end to the second element
    for i in range(n - 1, 0, -1):
        # changes the max with the last position
        random_numbers[i], random_numbers[0] = random_numbers[0], random_numbers[i]
        # calls the heapify function with a reduced len of the array
        heapify(random_numbers, i, 0)
        # Update bar_positions with new heights
        bar_positions = updateBarPositions(random_numbers, bar_area)
        # Redraw the screen to see changes reflected in bar_positions
        if bar_area2 == bar_area:
            drawBarsBox2(bar_positions, random_numbers)
        elif bar_area1 == bar_area:
            drawBarsBox1(bar_positions, random_numbers)
        pygame.time.wait(400)  # delay of0.4 seconds
    if bar_area2 == bar_area:
        global end_time2
        end_time2 = time.time()
        global thread2_time
        thread2_time = end_time2 - start_time2
        print(f"Time taken by the algorithm: {thread2_time} seconds")

    elif bar_area1 == bar_area:
        global end_time1
        end_time1 = time.time()
        global thread1_time
        thread1_time = end_time1 - start_time1
        print(f"Time taken by the algorithm: {thread1_time} seconds")
    return random_numbers


# method to check if its sorted


def is_sorted(arr):
    for i in range(len(arr) - 1):
        if arr[i] > arr[i + 1]:
            return False
    return True


# run bogo sort while its not sorted


def bogosort(random_numbers, bar_positions, bar_area):
    if bar_area2 == bar_area:
        global start_time2
        start_time2 = time.time()
    elif bar_area1 == bar_area:
        global start_time1
        start_time1 = time.time()
    while not is_sorted(random_numbers):
        if killThread:
            return
        else:
            random.shuffle(random_numbers)
            # Update bar_positions with new heights
            bar_positions = updateBarPositions(random_numbers, bar_area)
            # Redraw the screen to see changes reflected in bar_positions
            if bar_area2 == bar_area:
                drawBarsBox2(bar_positions, random_numbers)
            elif bar_area1 == bar_area:
                drawBarsBox1(bar_positions, random_numbers)
            pygame.time.wait(400)  # delay of0.4 seconds
    if bar_area2 == bar_area:
        global end_time2
        end_time2 = time.time()
        global thread2_time
        thread2_time = end_time2 - start_time2
        print(f"Time taken by the algorithm: {thread2_time} seconds")

    elif bar_area1 == bar_area:
        global end_time1
        end_time1 = time.time()
        global thread1_time
        thread1_time = end_time1 - start_time1
        print(f"Time taken by the algorithm: {thread1_time} seconds")
    return random_numbers


def quicksort(arr, bar_positions, bar_area):
    if bar_area2 == bar_area:
        global start_time2
        start_time2 = time.time()
    elif bar_area1 == bar_area:
        global start_time1
        start_time1 = time.time()
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
            if bar_area2 == bar_area:
                drawBarsBox2(bar_positions, result)
            elif bar_area1 == bar_area:
                drawBarsBox1(bar_positions, result)
            pygame.time.wait(400)  # delay of 0.5 seconds
    if bar_area2 == bar_area:
        global end_time2
        end_time2 = time.time()
        global thread2_time
        thread2_time = end_time2 - start_time2
        print(f"Time taken by the algorithm: {thread2_time} seconds")

    elif bar_area1 == bar_area:
        global end_time1
        end_time1 = time.time()
        global thread1_time
        thread1_time = end_time1 - start_time1
        print(f"Time taken by the algorithm: {thread1_time} seconds")
    return result


def bubblesort(random_numbers, bar_positions, bar_area):
    if bar_area2 == bar_area:
        global start_time2
        start_time2 = time.time()
    elif bar_area1 == bar_area:
        global start_time1
        start_time1 = time.time()
    n = len(random_numbers)
    for i in range(n):
        for j in range(0, n - i - 1):
            # swap if next element in array is greather
            if killThread:
                return
            if random_numbers[j] > random_numbers[j + 1]:
                random_numbers[j], random_numbers[(j + 1)] = (
                    random_numbers[j + 1],
                    random_numbers[j],
                )

                # Update bar_positions with new heights
                bar_positions = updateBarPositions(random_numbers, bar_area)

                # Redraw the screen to see changes reflected in bar_positions
                if bar_area2 == bar_area:
                    drawBarsBox2(bar_positions, random_numbers)
                elif bar_area1 == bar_area:
                    drawBarsBox1(bar_positions, random_numbers)

                pygame.time.wait(400)  # delay of0.4 seconds
    if bar_area2 == bar_area:
        global end_time2
        end_time2 = time.time()
        global thread2_time
        thread2_time = end_time2 - start_time2
        print(f"Time taken by the algorithm: {thread2_time} seconds")

    elif bar_area1 == bar_area:
        global end_time1
        end_time1 = time.time()
        global thread1_time
        thread1_time = end_time1 - start_time1
        print(f"Time taken by the algorithm: {thread1_time} seconds")


def drawBarsBox1(bar_positions, bar_heights):
    pygame.draw.rect(window, white, bar_area1)
    color_red = (170, 0, 0)
    bar_width = 10
    # gets x,y coordinates and height to be drawn from bars arrays
    for (bar_x, bar_y), bar_height in zip(bar_positions, bar_heights):
        pygame.draw.rect(window, color_red, [bar_x, bar_y, bar_width, bar_height])
    pygame.display.update()


def drawBarsBox2(bar_positions2, bar_heights2):
    pygame.draw.rect(window, white, bar_area2)
    color_red = (170, 0, 0)
    bar_width = 10
    # gets x,y coordinates and height to be drawn from bars arrays
    for (bar_x, bar_y), bar_height in zip(bar_positions2, bar_heights2):
        pygame.draw.rect(window, color_red, [bar_x, bar_y, bar_width, bar_height])
    pygame.display.update()


def insertBars(num_bars):
    # set bar area to the rectangle
    bar_width = 10

    # distance between bars
    distance_between_bars = 5

    # Generate bars
    for i in range(num_bars):
        # generate x coordinate
        bar_x2 = bar_area2.left + i * (bar_width + distance_between_bars)
        bar_x1 = bar_area1.left + i * (bar_width + distance_between_bars)
        # random height
        bar_height = random.randint(50, 130)
        # generate y coordinate
        bar_y1 = bar_area1.bottom - bar_height
        bar_y2 = bar_area2.bottom - bar_height
        bar_positions1.append((bar_x1, bar_y1))
        bar_positions2.append((bar_x2, bar_y2))
        bar_array1.append(bar_height)
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


def drawSetup(alg1Txt, alg2Txt):
    window.blit(background, (0, 0))
    # Title object
    font = pygame.font.Font(None, 48)
    # create text
    textTitle = font.render("Code Battle", True, white)
    # create surface title
    textTitleSurface = textTitle.get_rect()
    # set coordinates for text
    textTitleSurface.midtop = (width // 2, 20)
    window.blit(textTitle, textTitleSurface)

    # Settings Title object
    font2 = pygame.font.Font(None, 35)
    # create text
    textTitle2 = font2.render("Settings:", True, white)
    # create surface title
    textTitleSurface2 = textTitle2.get_rect()
    # set coordinates for text
    textTitleSurface2.midtop = (width // 4, 80)
    window.blit(textTitle2, textTitleSurface2)

    # Start game
    # create text
    textTitle3 = font2.render("Start Game:", True, white)
    # create surface title3
    textTitleSurface3 = textTitle3.get_rect()
    # set coordinates for text
    textTitleSurface3.midtop = (width // 3.7, 140)
    window.blit(textTitle3, textTitleSurface3)

    # Sort1
    # create text
    textSort = font2.render("Sort:", True, white)
    window.blit(textSort, (width // 3 - 150, 310))
    # txt algoritmo 1
    txtoAlg1 = font2.render(alg1Txt, True, white)
    window.blit(txtoAlg1, (65, 310 - 40))

    # Sort2
    # create text
    textTitle5 = font2.render("Sort:", True, white)
    window.blit(textTitle5, (width // 3 - 150, 560))
    # txt Algoritmo 2
    txtoAlg2 = font2.render(alg2Txt, True, white)
    window.blit(txtoAlg2, (65, 560 - 40))

    # rendering text with different colors
    text_button = font2.render("Change", True, white)
    # pygame.draw.rect(window, color_button, [width//2.6, 75, 110, 30])
    window.blit(text_button, (width // 2.5, 75))

    # draws rectangle 1
    pygame.draw.rect(window, white, [width // 4, 190, 540, 220])
    pygame.draw.rect(window, white, [width // 4, 440, 540, 220])

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


def main_menu(algo1, algo2):
    alg1 = algo1
    alg2 = algo2
    global killThread
    showedWinner = False
    # insert random bars to arrays
    num_bars = 10
    insertBars(num_bars)
    # draw all main_menu components
    alg1Txt = "Quick"
    alg2Txt = "Insertion"
    drawSetup(alg1Txt, alg2Txt)
    global rootNode
    rootNode = None
    waiting = False
    # create threads for sorting methods
    thread1 = None
    thread2 = None
    click = False
    startThread = True
    showed_winner = False
    while True:
        text_button_settings = pygame.font.SysFont(None, 35).render(
            "Change", True, white
        )
        text_button_start = pygame.font.SysFont(None, 35).render("Start", True, white)
        # text = smallfont.render('start', True, white)
        mx, my = pygame.mouse.get_pos()
        settingButton = pygame.Rect(width // 2.6, 75, 110, 30)
        startButton = pygame.Rect(width // 2.6, 135, 110, 30)
        if settingButton.collidepoint((mx, my)):
            if click:
                showed_winner = False
                killThread = True
                alg1, alg2, num_bars = settings(num_bars, alg1, alg2)
                thread1 = None
                thread2 = None
                # insert random bars to arrays
                clearArrays()
                # insertBars1()
                insertBars(num_bars)
                # draw all main_menu components
                alg1Txt, alg2Txt = textoDeAlgoritmos(alg1, alg2)
                drawSetup(alg1Txt, alg2Txt)
                startThread = True

        if startButton.collidepoint((mx, my)):
            if click and startThread:
                thread1 = threading.Thread(
                    target=alg1,
                    args=(bar_array1, bar_positions1, bar_area1),
                    daemon=True,
                )
                thread2 = threading.Thread(
                    target=alg2,
                    args=(bar_array2, bar_positions2, bar_area2),
                    daemon=True,
                )
                startThread = False
                thread1.start()
                pygame.display.update()
                thread2.start()
                pygame.display.update()

                if thread1.is_alive() == False and thread2.is_alive() == False:
                    startThread = True

        pygame.draw.rect(window, (170, 0, 0), settingButton)
        window.blit(text_button_settings, (width // 2.5, 75))
        pygame.draw.rect(window, (170, 0, 0), startButton)
        window.blit(text_button_start, (width // 2.5, 135))

        click = False
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    click = True
        global thread1_time
        global thread2_time
        thread1_time_final = thread1_time
        thread3_time_final = thread2_time
        if (
            thread1 is not None
            and thread2 is not None
            and thread1_time_final is not None
            and thread3_time_final is not None
        ):
            if (
                thread1_time_final < thread3_time_final
                and not thread1.is_alive()
                and not thread2.is_alive()
                and not showedWinner
            ):
                loser_name = textoDeAlgoritmos(alg1, alg2)[1]
                winner_name = textoDeAlgoritmos(alg1, alg2)[0]
                clearArrays()
                pygame.display.update()
                winnerWindow(
                    winner_name,
                    loser_name,
                    thread2_time,
                    thread1_time,
                    alg1,
                    alg2,
                    num_bars,
                )
                showedWinner = True

                pygame.display.update()

            elif (
                thread3_time_final < thread1_time_final
                and not thread1.is_alive()
                and not thread2.is_alive()
                and not showedWinner
            ):
                winner_name = textoDeAlgoritmos(alg1, alg2)[0]
                loser_name = textoDeAlgoritmos(alg1, alg2)[
                    1
                ]  # Fixing an apparent mistake where you fetched the winner_name twice
                clearArrays()
                
                pygame.display.update()
                winnerWindow(
                    winner_name,
                    loser_name,
                    thread2_time,
                    thread1_time,
                    alg1,
                    alg2,
                    num_bars,
                )
                showedWinner = True

                pygame.display.update()

        pygame.display.update()
        clock.tick(60)


def winnerWindow(winner, loser, timeW, timeL, alg1, alg2, num_bars):
    # Cargar assets

    click = False
    showed_winner = False
    img_winner = pygame.image.load(os.path.join("assets", "winner.png"))
    font = pygame.font.SysFont(None, 48)

    waiting = True  # Set waiting to True only here

    while waiting:
        # Limpiar pantalla
        window.blit(background, (0, 0))

        # Preparar textos
        title = font.render("GAME OVER", True, white)
        winner_text = font.render(f"Winner: {winner}", True, white)
        tw = round(timeW, 2)
        winner_time_text = font.render(f"Time Winner: {tw}", True, white)
        loser_text = font.render(f"Loser: {loser}", True, white)
        tl = round(timeL, 2)
        loser_time_text = font.render(f"Time Loser: {tl}", True, white)
        diff = timeL - timeW
        td = round(diff, 2)
        diff_text = font.render(f"Time Difference: {td}", True, white)

        # Mostrar en pantalla
        window.blit(title, (width / 2 - title.get_width() / 2, 20))
        window.blit(img_winner, (width / 2 - img_winner.get_width() / 2, 200))
        window.blit(winner_text, (100, 300))
        window.blit(winner_time_text, (100, 350))
        window.blit(loser_text, (100, 400))
        window.blit(loser_time_text, (100, 450))
        window.blit(diff_text, (100, 500))

        pygame.display.update()

        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    waiting = False
                    main_menu(quicksort, insertNodes)
                    pygame.display.update()
                    clearArrays()
                    break  # Exit the while loop


def textoDeAlgoritmos(alg1, alg2):
    img1, img2, texto1, texto2 = selectAlgLastSettings(alg1, alg2)
    txtAlg1 = texto1.split()
    txtAlg2 = texto2.split()
    return txtAlg1[0], txtAlg2[0]


def loopSettings(sizeArray, inputRect, enter, img1, img2, alg1, alg2):
    # fondo, texto de retorno al menu
    window.blit(background, (0, 0))
    escapeToGoBack = pygame.font.SysFont(None, 45).render(
        "Press ESC to save and return to the main menu", True, white
    )
    window.blit(escapeToGoBack, (width // 12.5, 75))
    # texto de tamaño de arreglo
    # tamaño normal de letra e indicaciones
    base_font = pygame.font.SysFont(None, 40)
    textoSizeArreglo = base_font.render("Tamaño de arreglo: ", True, white)
    window.blit(textoSizeArreglo, (70, 200))
    textoIndicaciones = base_font.render("(Entre 5 y 35) ", True, white)
    window.blit(textoIndicaciones, (width // 2 + 140, 200))
    # dibuja el input del texto dentro de la cajita
    textoTamanio = base_font.render(sizeArray, True, white)
    # si la cajita de input se selecciona, dibujarla y asignar el nuevo número
    if enter == False:
        pygame.draw.rect(window, white, inputRect, 2)
    window.blit(textoTamanio, (inputRect.x + 5, inputRect.y + 5))

    # dibuja las imágenes de los algoritmos
    pygame.draw.rect(window, white, pygame.Rect(width // 2 - 360 - 2, 290, 344, 220))
    pygame.draw.rect(window, white, pygame.Rect(width // 2 + 20 - 2, 290, 344, 220))
    window.blit(img1, (width // 2 - 360, 300))
    window.blit(img2, (width // 2 + 20, 300))

    # dibuja el texto de los algoritmos
    window.blit(base_font.render(alg1, True, white), (width // 2 - 290, 540))
    window.blit(base_font.render(alg2, True, white), (width // 2 + 90, 540))

    # triángulos
    triangle_vertices1 = [(40, 555), (70, 540), (70, 570)]
    pygame.draw.polygon(window, white, triangle_vertices1)
    triangle_vertices2 = [(380, 555), (350, 540), (350, 570)]
    pygame.draw.polygon(window, white, triangle_vertices2)
    triangle_vertices3 = [(420, 555), (450, 540), (450, 570)]
    pygame.draw.polygon(window, white, triangle_vertices3)
    triangle_vertices4 = [(760, 555), (730, 540), (730, 570)]
    pygame.draw.polygon(window, white, triangle_vertices4)


def settings(size, algo1, algo2):
    images = loadImages()
    global killThread
    run = True
    alg1 = algo1
    alg2 = algo2
    textInput = str(size)
    temp = str(size)
    # dibuja rectángunlo de input de size del arreglo
    inputRect = pygame.Rect(width // 2.2, 195, 100, 32)
    enter = False
    # cargar imagenes de algoritmos y crear variables del texto a mostrar
    images = loadImages()
    # obtiene los nombres e imagenes de la última configuración
    img1, img2, algTxt1, algTxt2 = selectAlgLastSettings(alg1, alg2)

    loopSettings(
        textInput, inputRect, enter, images[img1], images[img2], algTxt1, algTxt2
    )
    active = False
    changeButtons = []
    changeButtons.append(pygame.Rect(40, 540, 30, 30))
    changeButtons.append(pygame.Rect(350, 540, 30, 30))
    changeButtons.append(pygame.Rect(420, 540, 30, 30))
    changeButtons.append(pygame.Rect(730, 540, 30, 30))
    while run:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                sys.exit()
            if event.type == pygame.MOUSEBUTTONDOWN:
                mx, my = pygame.mouse.get_pos()
                changeAlg(mx, my, changeButtons, img1, img2, algTxt1, algTxt2)
                if (
                    changeButtons[0].collidepoint((mx, my))
                    or changeButtons[1].collidepoint((mx, my))
                    or changeButtons[2].collidepoint((mx, my))
                    or changeButtons[3].collidepoint((mx, my))
                ):
                    img1, img2, algTxt1, algTxt2 = changeAlg(
                        mx, my, changeButtons, img1, img2, algTxt1, algTxt2
                    )
                if inputRect.collidepoint((mx, my)):
                    active = True
                    enter = False
                else:
                    try:
                        sizeArray = int(textInput)
                        if sizeArray < 5 or sizeArray > 35:
                            textInput = temp
                    except ValueError:
                        textInput = temp
                        print("Ingrese un número válido")
                    active = False
                    enter = True
            if event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    run = False
                    killThread = False
                    alg1, alg2 = nuevosAlgoritmos(img1, img2)
                    try:
                        sizeArray = int(textInput)
                        if sizeArray < 5 or sizeArray > 40:
                            textInput = temp
                    except ValueError:
                        textInput = temp
                    active = False
                if active:
                    if event.key == pygame.K_RETURN:
                        try:
                            sizeArray = int(textInput)
                            if sizeArray < 5 or sizeArray > 40:
                                textInput = temp
                            else:
                                enter = True
                                active = False
                        except ValueError:
                            textInput = temp
                            print("Ingrese un número válido")
                            enter = True
                    elif event.key == pygame.K_BACKSPACE:
                        textInput = textInput[:-1]
                    else:
                        textInput += event.unicode
        loopSettings(
            textInput, inputRect, enter, images[img1], images[img2], algTxt1, algTxt2
        )
        pygame.display.update()
        clock.tick(60)
    return alg1, alg2, int(textInput)


# retorna los nuevos algoritmos de las configuraciones
def nuevosAlgoritmos(img1, img2):
    images = [img1, img2]
    algoritmos = []
    for img in images:
        if img == 0:
            algoritmos.append(insertionSort)
        elif img == 1:
            algoritmos.append(selectionSort)
        elif img == 2:
            algoritmos.append(quicksort)
        elif img == 3:
            algoritmos.append(bubblesort)
        elif img == 4:
            algoritmos.append(bogosort)
        elif img == 5:
            algoritmos.append(heapsort)
        elif img == 6:
            algoritmos.append(insertNodes)
        elif img == 7:
            algoritmos.append(mergeSort)
    return algoritmos[0], algoritmos[1]


# selecciona los algoritmos de la configuración actual
def selectAlgLastSettings(alg1, alg2):
    algorithms = [alg1, alg2]
    images = []
    algTxts = []
    for alg in algorithms:
        if alg == insertionSort:
            images.append(0)
            algTxts.append("Insertion Sort")
        elif alg == selectionSort:
            images.append(1)
            algTxts.append("Selection Sort")
        elif alg == quicksort:
            images.append(2)
            algTxts.append("Quick Sort")
        elif alg == bubblesort:
            images.append(3)
            algTxts.append("Bubble Sort")
        elif alg == bogosort:
            images.append(4)
            algTxts.append("Bogo Sort")
        elif alg == heapsort:
            images.append(5)
            algTxts.append("Heap Sort")
        elif alg == insertNodes:
            images.append(6)
            algTxts.append("Tree Sort")
        elif alg == mergeSort:
            images.append(7)
            algTxts.append("Merge Sort")
    return images[0], images[1], algTxts[0], algTxts[1]


def changeAlg(mx, my, changeButtons, img1, img2, algTxt1, algTxt2):
    nombres = [
        "Insertion Sort",
        "Selection Sort",
        "Quick Sort",
        "Bubble Sort",
        "Bogo Sort",
        "Heap Sort",
        "Tree Sort",
        "Merge Sort",
    ]
    nNombres = len(nombres)
    change = 0
    if changeButtons[0].collidepoint((mx, my)):
        if (img1 - 1) % nNombres != img2:
            img1 = (img1 - 1) % nNombres
        else:
            img1 = (img1 - 2) % nNombres
        change = 1
    elif changeButtons[1].collidepoint((mx, my)):
        if (img1 + 1) % nNombres != img2:
            img1 = (img1 + 1) % nNombres
        else:
            img1 = (img1 + 2) % nNombres
        change = 1
    elif changeButtons[2].collidepoint((mx, my)):
        if (img2 - 1) % nNombres != img1:
            img2 = (img2 - 1) % nNombres
        else:
            img2 = (img2 - 2) % nNombres
        change = 2
    elif changeButtons[3].collidepoint((mx, my)):
        if (img2 + 1) % nNombres != img1:
            img2 = (img2 + 1) % nNombres
        else:
            img2 = (img2 + 2) % nNombres
        change = 2

    if change == 1:
        algTxt1 = nombres[img1]
    if change == 2:
        algTxt2 = nombres[img2]
    return img1, img2, algTxt1, algTxt2


def loadImages():
    width = 340
    height = 200
    images = []
    images.append(
        pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "insertion.png")), (width, height)
        )
    )
    images.append(
        pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "selection.png")), (width, height)
        )
    )
    images.append(
        pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "quick.png")), (width, height)
        )
    )
    images.append(
        pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "bubble.png")), (width, height)
        )
    )
    images.append(
        pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "bogo.png")), (width, height)
        )
    )
    images.append(
        pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "heap.png")), (width, height)
        )
    )
    images.append(
        pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "tree.png")), (width, height)
        )
    )
    images.append(
        pygame.transform.scale(
            pygame.image.load(os.path.join("assets", "merge.png")), (width, height)
        )
    )
    return images


def main():
    main_menu(quicksort, insertNodes)


# run file if its main
if __name__ == "__main__":
    main()
