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
background = pygame.image.load("background.jpg").convert_alpha() 

# Transaparency
alpha = 30  # 0 = fully transparent, 255 = fully opaque
background.set_alpha(alpha)

#RGB colors
white = (255, 255, 255)

def drawMainTitle():
    #Title object
    font = pygame.font.Font(None, 48)
    #create text 
    textTitle=font.render("Code Battle",True,white)
    # create surface title
    textTitleSurface = textTitle.get_rect()
    # set coordinates for text
    textTitleSurface.midtop=(width//2,20)
    window.blit(textTitle,textTitleSurface)
def drawButtonSettings():
    #button settings 
    # button colors
    color_button =(0, 170, 170)  

    # button fonts
    smallfont = pygame.font.SysFont(None, 35)

    # rendering text with different colors
    text_button = smallfont.render('Change', True, white)
    text = smallfont.render('Change' , True , white)
    pygame.draw.rect(window, color_button, [width//2.6,75, 110, 30])
    window.blit(text_button, (width//2.5,75))   
def drawButtonGame():
    #button game
    # button colors
    color_button =(0, 170, 170)  

    # button fonts
    smallfont = pygame.font.SysFont(None, 35)

    # rendering text with different colors
    text_button = smallfont.render('Start', True, white)
    text = smallfont.render('start' , True , white)
    pygame.draw.rect(window, color_button, [width//2.6,135, 110, 30])
    window.blit(text_button, (width//2.5,135))     
def drawSettingsTitle():
    #Settings Title object
    font2 = pygame.font.Font(None, 35)
    #create text 
    textTitle2=font2.render("Settings:",True,white)
    # create surface title
    textTitleSurface2 = textTitle2.get_rect()
    # set coordinates for text
    textTitleSurface2.midtop=(width//4,80)

    window.blit(textTitle2,textTitleSurface2)
def drawstartGametitle():
    #Start game
    font3 = pygame.font.Font(None, 35)
    #create text 
    textTitle3=font3.render("Start Game:",True,white)
    # create surface title
    textTitleSurface3 = textTitle3.get_rect()
    # set coordinates for text
    textTitleSurface3.midtop=(width//3.7,140)
    window.blit(textTitle3,textTitleSurface3)
def drawSort1Title():
   #Sort1 
    font4 = pygame.font.Font(None, 35)
    #create text 
    textTitle4=font4.render("Sort #1:",True,white)
    # create surface title
    textTitleSurface4 = textTitle4.get_rect()
    # set coordinates for text
    textTitleSurface4.midtop=(width//6,300)
    window.blit(textTitle4,textTitleSurface4)
def drawSort2Title():
   #Sort2
    font5 = pygame.font.Font(None, 35)
    #create text 
    textTitle5=font5.render("Sort #2:",True,white)
    # create surface title
    textTitleSurface5 = textTitle5.get_rect()
    # set coordinates for text
    textTitleSurface5.midtop=(width//6,480)
    window.blit(textTitle5,textTitleSurface5)
def drawSort1Box():
    pygame.draw.rect(window, white, [width//4,190, 540, 220])
def drawSort2Box():
    pygame.draw.rect(window, white, [width//4,440, 540, 220])
def drawSetup():
    window.blit(background,(0,0))
    pygame.display.update()
def main():
    #variable run to keep screen
    run=True
    while run:
        for event in pygame.event.get():
            #user closes window with x click on screen
            if (event.type==pygame.QUIT):
                run=False
                break
        drawMainTitle()
        drawSettingsTitle()
        drawstartGametitle()
        drawSort1Title()
        drawSort2Title()
        drawButtonSettings()
        drawButtonGame()
        drawSort1Box()
        drawSort2Box()
        drawSetup()
      

    pygame.quit()

#run file if its main
if __name__=="__main__":
    main()