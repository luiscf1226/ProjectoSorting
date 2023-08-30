import pygame
import time
import random
#initialize
pygame.init()
#width and height for screen
width,height=800,700
#window code to set display and caption
window=pygame.display.set_mode((width,height))
pygame.display.set_caption("Space dodge")
#image
background = pygame.image.load("background.jpg").convert()
background = pygame.transform.scale(background,(width,height)) 
#RGB colors
white = (255, 255, 255)
#bars1
bar_positions1 = []
#bars1
bar_positions2 = []
#array bars 1
bar_array1=[]
#array bars 2
bar_array2=[]
#area 1
bar_area1 = pygame.Rect(width // 4, 190, 540, 220)
#area 2
bar_area2 = pygame.Rect(width//4,440, 540, 220)
def quicksort(arr,bar_positions,bar_area):
    #check if its less than 2 dont need to order array
    if len(arr) < 2:
        return arr

    #pivot element at first elememt
    pivot = arr[0]
    
    #left and right arrays
    leftArray = []
    rightArray = []
    
    #assign resulting left if smaller right if bigger than pivot element
    for i in range(1, len(arr)):
        if arr[i] < pivot:
            leftArray.append(arr[i])
        else:
            rightArray.append(arr[i])

    #recursively order left and right, this creates more lefts and rights
    leftSort = quicksort(leftArray,bar_positions,bar_area)
    rightSort = quicksort(rightArray,bar_positions,bar_area)
    
    #add to array left middle pivot and right
    result = leftSort + [pivot] + rightSort
    
    # Update arr with the sorted result
    #this lets the array be updated each recursion iteration
    for i in range(len(result)):
        arr[i] = result[i]

    # Update bar_positions with new heights
    bar_positions = updateBarPositions(result,bar_area)       
   
    # Redraw the screen to see changes reflected in bar_positions
    drawBarsBox1(bar_positions, result)        
    
    pygame.time.wait(500)  # delay of 0.5 seconds
    pygame.display.update()
    return result
def bubblesort(random_numbers,bar_positions,bar_area):
    n = len(random_numbers)
    for i in range(n):
        for j in range(0, n-i-1):
            #swap if next element in array is greather 
            if random_numbers[j] > random_numbers[j+1]:
                random_numbers[j], random_numbers[j+1] = random_numbers[j+1], random_numbers[j]
                
                # Update bar_positions with new heights
                bar_positions = updateBarPositions(random_numbers,bar_area)
                
                # Redraw the screen to see changes reflected in bar_positions
                drawBarsBox2(bar_positions, random_numbers)
                  
                pygame.time.wait(500)  # delay of0.5 seconds
                
    pygame.display.update()
def drawBarsBox1(bar_positions,bar_heights):
    color_red = (170, 0, 0)
    bar_width = 10
    #gets x,y coordinates and height to be drawn from bars arrays
    for (bar_x, bar_y),bar_height in zip(bar_positions,bar_heights):
        pygame.draw.rect(window, color_red, [bar_x, bar_y, bar_width, bar_height])
    pygame.display.update()   
def insertBars1():
    #set bar area to the rectangle 
    bar_width = 10
   
    num_bars = 5

    # distance between bars
    distance_between_bars = 10

    # Generate bars
    
    for i in range(num_bars):
        #generate x coordinate
        bar_x = bar_area1.left + i * (bar_width + distance_between_bars)
        #random height
        bar_height = random.randint(50, 130)
        #generate y coordinate
        bar_y = bar_area1.bottom - bar_height
        bar_positions1.append((bar_x, bar_y))
        bar_array1.append(bar_height)

def drawBarsBox2(bar_positions2,bar_heights2):
    color_red = (170, 0, 0)
    bar_width = 10
    #gets x,y coordinates and height to be drawn from bars arrays
    for (bar_x, bar_y),bar_height in zip(bar_positions2,bar_heights2):
        pygame.draw.rect(window, color_red, [bar_x, bar_y, bar_width, bar_height])
    pygame.display.update()   
def insertBars2():
    #set bar area to the rectangle 
    bar_width = 10

    num_bars = 5

    # distance between bars
    distance_between_bars = 10

    # Generate bars
    
    for i in range(num_bars):
        #generate x coordinate
        bar_x = bar_area2.left + i * (bar_width + distance_between_bars)
        #random height
        bar_height = random.randint(50, 130)
        #generate y coordinate
        bar_y = bar_area2.bottom - bar_height
        bar_positions2.append((bar_x, bar_y))
        bar_array2.append(bar_height)
def updateBarPositions(bar_heights, reference_rect):

    bar_width = 10
    distance_between_bars = 10
    new_positions = []
    #since array changes with each iteration of sorting, it needs to update
    for i, height in enumerate(bar_heights):
        #get border of rectangle and add 10 to each bar
        bar_x = reference_rect.left + i * (bar_width + distance_between_bars)
        #subtract from bottom border height
        bar_y = reference_rect.bottom - height
        new_positions.append((bar_x, bar_y))
    return new_positions
def clearScreen():
    window.fill((255, 255, 255))  
def drawSetup(bar_positions1,bar_array1,bar_positions2,bar_array2):
    window.blit(background, (0, 0))  
    #Title object
    font = pygame.font.Font(None, 48)
    #create text 
    textTitle=font.render("Code Battle",True,white)
    # create surface title
    textTitleSurface = textTitle.get_rect()
    # set coordinates for text
    textTitleSurface.midtop=(width//2,20)
    window.blit(textTitle,textTitleSurface)

     #Settings Title object
    font2 = pygame.font.Font(None, 35)
    #create text 
    textTitle2=font2.render("Settings:",True,white)
    # create surface title
    textTitleSurface2 = textTitle2.get_rect()
    # set coordinates for text
    textTitleSurface2.midtop=(width//4,80)

    window.blit(textTitle2,textTitleSurface2)

    #Start game
    font3 = pygame.font.Font(None, 35)
    #create text 
    textTitle3=font3.render("Start Game:",True,white)
    # create surface title
    textTitleSurface3 = textTitle3.get_rect()
    # set coordinates for text
    textTitleSurface3.midtop=(width//3.7,140)
    window.blit(textTitle3,textTitleSurface3)

    #Sort1 
    font4 = pygame.font.Font(None, 35)
    #create text 
    textTitle4=font4.render("Sort #1:",True,white)
    # create surface title
    textTitleSurface4 = textTitle4.get_rect()
    # set coordinates for text
    textTitleSurface4.midtop=(width//6,300)
    window.blit(textTitle4,textTitleSurface4)

    #Sort2
    font5 = pygame.font.Font(None, 35)
    #create text 
    textTitle5=font5.render("Sort #2:",True,white)
    # create surface title
    textTitleSurface5 = textTitle5.get_rect()
    # set coordinates for text
    textTitleSurface5.midtop=(width//6,480)
    window.blit(textTitle5,textTitleSurface5)
    #button settings 
    # button colors
    color_button =(170, 0, 0)  

    # button fonts
    smallfont = pygame.font.SysFont(None, 35)

    # rendering text with different colors
    text_button = smallfont.render('Change', True, white)
    text = smallfont.render('Change' , True , white)
    pygame.draw.rect(window, color_button, [width//2.6,75, 110, 30])
    window.blit(text_button, (width//2.5,75))   
    #button game
    # button colors
    color_button =(170, 0, 0)

    # button fonts
    smallfont = pygame.font.SysFont(None, 35)

    # rendering text with different colors
    text_button = smallfont.render('Start', True, white)
    text = smallfont.render('start' , True , white)
    pygame.draw.rect(window, color_button, [width//2.6,135, 110, 30])
    window.blit(text_button, (width//2.5,135))     


    #Start game
    font3 = pygame.font.Font(None, 35)
    #create text 
    textTitle3=font3.render("Start Game:",True,white)
    # create surface title
    textTitleSurface3 = textTitle3.get_rect()
    # set coordinates for text
    textTitleSurface3.midtop=(width//3.7,140)
    window.blit(textTitle3,textTitleSurface3)

    #draws rectangle 1
    pygame.draw.rect(window, white, [width//4,190, 540, 220])

    pygame.draw.rect(window, white, [width//4,440, 540, 220])
      
    drawBarsBox1(bar_positions1,bar_array1)
    drawBarsBox2(bar_positions2,bar_array2)
def drawSettingScreen():
     #settings screen and button
    screenSettings=pygame.display.set_mode((600,400))
    pygame.display.set_caption('Settings')
    background = pygame.image.load("background.jpg").convert()
    background = pygame.transform.scale(background,(width,height)) 
    screenSettings.blit(background, (0, 0))
    pygame.display.update()
def redrawMain():
    #window code to set display and caption
    window=pygame.display.set_mode((width,height))
    pygame.display.set_caption("Space dodge")

    #image
    background = pygame.image.load("background.jpg").convert()

    # Transaparency
    alpha = 10  # 0 = fully transparent, 255 = fully opaque
    background.set_alpha(alpha)
    drawSetup(bar_positions1,bar_array1,bar_positions2,bar_array2)
    drawBarsBox1(bar_positions1,bar_array1)
    drawBarsBox2(bar_positions2,bar_array2)
    pygame.display.update()
def drawSettingSurface(window):
    set_surface=pygame.Surface((600,400))
    set_surface.fill((200,200,200))
    window.blit(set_surface,(200,150))
    
def main():
  
    #setting button
    settingButton=pygame.Rect(width//2.6,75, 110, 30) 
    #variable run to keep screen
    run=True
    sorted1 = False
    sorted2 = False
    drawSetup(bar_positions1,bar_array1,bar_positions2,bar_array1)
    #insert random bars to first array
    insertBars1()
     #insert random bars to second array
    insertBars2()
    show_settings=False
    while run:
        for event in pygame.event.get():
            #user closes window with x click on screen
            if (event.type==pygame.QUIT):
                run=False
                break
            #detect that setting button is clicked 
            if (event.type == pygame.MOUSEBUTTONDOWN):
                #get current mouse position
                mouse_position=pygame.mouse.get_pos()
                #check if user clicks settings button
                if(settingButton.collidepoint(mouse_position)):
                    print("mouse clicked on settings")
                    show_settings=True
                    '''drawSettingScreen()
                    run2 = True
                    while run2:
                        event = pygame.event.poll()
                        if event.type == pygame.QUIT:
                            redrawMain()'''
        if show_settings:
                drawSettingSurface(window)
                pygame.display.update()
        '''if not sorted1:
            bubblesort(bar_array1,bar_positions1,bar_area1)
            sorted1 = True  # array ordered so it can stop being sorted
        #order second array
        if not sorted2:
            quicksort(bar_array2,bar_positions2,bar_area2)
            sorted2 = True  # array ordered so it can stop being sorted'''

       

    pygame.quit()

#run file if its main
if __name__=="__main__":
    main()
