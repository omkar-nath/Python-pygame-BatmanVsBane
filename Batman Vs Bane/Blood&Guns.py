import pygame
import time
import random
pygame.init()
dark_yellow=(255,215,0)
dark_golden=(184,134,11)
olive=(128,128,0)
dark_olive=(85,107,47)
dark_green=(0,100,0)
forest_green=(34,139,34)
aqua=(0,255,255)
cyan=(224,255,255)
magents=(139,0,139)
orchid=(153,50,204)
saddle_brown=(139,69,19)
slate_gray=(119,136,153)
black2=(0,0,0,0.5)
marron=(128,0,0)
black=(0,0,0)
firebrick=(139,0,0)
white=(255,255,255)
grey=(128,128,128)
teal=(0,128,128)
display_width=1000
display_height=563

gameDisplay=pygame.display.set_mode((display_width,display_height))
clock=pygame.time.Clock()
intro_image=pygame.image.load("game_intro2.jpg")
batman_health=pygame.image.load("health_bat2.png")
bane_health=pygame.image.load("bane_health.png")
smallfont=pygame.font.Font("batmfa__.ttf",22);
mediumfont=pygame.font.Font("style.otf",30)
largefont=pygame.font.Font("batmfo__.ttf",60)
extralarge=pygame.font.SysFont("style.otf",120)



def text_objects(text,color,size):
    if size=="small":
       textSurface=smallfont.render(text,True,color)
    elif size=="medium":
       textSurface=mediumfont.render(text,True,color)
    elif size=="large":
       textSurface=largefont.render(text,True,color)
    elif size=="extralarge":
       textSurface=largefont.render(text,True,color)
    return textSurface,textSurface.get_rect()
def text_to_button(msg,color,buttonx,buttony,buttonwidth,buttonheight,size="small"):
     textSurf,textRect=text_objects(msg,color,size)
     textRect.center=((buttonx+(buttonwidth/2)),buttony+(buttonheight/2))
     gameDisplay.blit(textSurf,textRect)
def message_to_screen(msg,color,y_displace=0,size="small"):
     textSurface,textRect=text_objects(msg,color,size)
     textRect.center=(display_width/2),(display_height/2)+y_displace
     gameDisplay.blit(textSurface,textRect)
def game_controls():
       gcont=True

       while gcont:
              for event in pygame.event.get():
                if event.type==pygame.QUIT:
                       pygame.quit()
                       quit()
                       
                
              gameDisplay.fill(marron)
 
             
              message_to_screen("Controls",orchid,-100,"large")
              message_to_screen("For firing :Spacebar",dark_yellow,20,"medium" )
              message_to_screen("Move turret:Up and Down arrows",dark_yellow,90,"medium" )
              message_to_screen("Move tank:Left and right arrows",dark_yellow,140,"medium" )
              message_to_screen("Increase Power:Press D",dark_yellow,180,"medium")
              
             
              
              button("Play",150,560,100,50,dark_green,forest_green,action="play")
              button_back("Back",350,560,100,50,dark_yellow,cyan,action="back")
              button("Quit",550,560,100,50,aqua,orchid,action="quit")
              pygame.display.update()
              
              clock.tick(15)
def button_back(text,x,y,width,height,inactive_color,active_color,action=None):
    cur=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    if x+width>cur[0]>x and y+height>cur[1]>y:
        pygame.draw.rect(gameDisplay,active_color,(x,y,width,height))
        if click[0]==1 and action!=None:
            if action=="back":
                game_intro()
    else:
       pygame.draw.rect(gameDisplay,inactive_color,(x,y,width,height))
    text_to_button(text,black,x,y,width,height)
def button(text,x,y,width,height,inactive_color,active_color,action=None):
    cur=pygame.mouse.get_pos()
    click=pygame.mouse.get_pressed()
    
    if x+width>cur[0]>x and y+height>cur[1]>y:
        pygame.draw.rect(gameDisplay,active_color,(x,y,width,height))
        if click[0]==1 and action!=None:
            if action=="quit":
             pygame.quit()
             quit()
            if action=="controls":
               game_controls()
            if action=="play":
               gameLoop()
            
    else:
        pygame.draw.rect(gameDisplay,inactive_color,(x,y,width,height))
    text_to_button(text,black,x,y,width,height)
    
def pause():
       paused=True
       message_to_screen("Paused",teal,-100,size="large")
       message_to_screen("Press C to continue and Q to quit",25)
       pygame.display.update()
       while paused:
              for event in pygame.event.get():
                 if event.type==pygame.QUIT:
                        pygame.quit()
                        quit()
                 if event.type==pygame.KEYDOWN:
                     if event.key==pygame.K_c:
                            paused=False
                     elif event.key==pygame.K_q:
                            pygame.quit()
                            quit()
              #gameDisplay.fill(white)
              
              clock.tick(5)
def health_bars(player_health,enemy_health):
    
    if player_health>75:
        player_health_color=dark_green
    elif player_health>50:
        player_health_color=light_yellow
    else:
        player_health_color=red
        
    if enemy_health>75:
        enemy_health_color=dark_green
    elif enemy_health>50:
        enemy_health_color=light_yellow
    else:
        enemy_health_color=red
    
    gameDisplay.blit(batman_health,[820,2])
    pygame.draw.rect(gameDisplay,player_health_color,(880,58,player_health,25))
    gameDisplay.blit(bane_health,[101,-3])
    pygame.draw.rect(gameDisplay,enemy_health_color,(20,58,enemy_health,25))
    
    
def game_intro():
       pygame.mixer.music.load("music1.mp3")
       pygame.mixer.music.play(-1)       
       intro=True

       while intro:
              for event in pygame.event.get():
                if event.type==pygame.QUIT:
                       pygame.quit()
                       quit()
                       
                if event.type==pygame.KEYDOWN:
                    if event.key==pygame.K_q:
                        pygame.quit()
                        quit()
                    if event.key==pygame.K_c:
                        intro=False
              gameDisplay.fill(teal)
              gameDisplay.blit(intro_image,[0,0])
              pygame.display.update()
             
 
             
              message_to_screen("BATMAN VS BANE",white,-240,"large")
              #message_to_screen("Lets Fight,and see who got balls :)",forest_green,-50,"medium" )
              
             
              
              button("Play",460,170,150,50,white,grey,action="play")
              button("Controls",460,230,150,50,white,grey,action="controls")
              button("Quit",460,300,150,50,white,grey,action="quit")
              
              


              








              pygame.display.update()
              
              clock.tick(15)
def gameLoop():
            pygame.mixer.music.stop()
            player_health=100
            enemy_health=100
            gameExit=False
            gameOver=False
            #while not gameExit:
            while not gameExit:
                               for event in pygame.event.get():
                                  if event.type==pygame.QUIT:
                                           gameOver=False
                                           gameExit=True
                                  if event.type==pygame.KEYDOWN:
                                       if event.key==pygame.K_q:
                                            gameExit=True
                                            gameOver=False
                                       if event.key==pygame.K_c:
                                            gameLoop()
                               for event in pygame.event.get():
                                  if event.type==pygame.QUIT:
                                            gameExit=True


                           
                               gameDisplay.fill(grey)
                               
                               health_bars(player_health,enemy_health)
                               pygame.display.update()
            pygame.quit()
            quit()
game_intro()
gameLoop()
                               
