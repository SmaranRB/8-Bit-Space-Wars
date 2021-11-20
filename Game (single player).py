import pygame
import random
import os

pygame.font.init()
pygame.mixer.init()
Width , Height = 900,500

# Loading BG
Bg = pygame.transform.scale(pygame.image.load(os.path.join('Assets','space-retro.png')),(900,500))

# Window name = display.set_mode((pixels width, pixels height))
root = pygame.display.set_mode((Width,Height))
pygame.display.set_caption ('8 Bit Space Wars') #Titlle bar name

# Loading surfaces (objects/elements):

#Yellow_Spaceship = image.load('Computer Science\\Project\\Pygame\\PygameForBeginners-main\\PygameForBeginners-main\\Assets\\spaceship_yellow.png')
Yellow_Spaceship = pygame.image.load(os.path.join('Assets','spaceship_yellow.png'))
Yellow_Spaceship = pygame.transform.rotate(pygame.transform.scale(Yellow_Spaceship, (55,40)),90)


#Red_Spaceship = image.load('Computer Science\\Project\\Pygame\\PygameForBeginners-main\\PygameForBeginners-main\\Assets\\spaceship_red.png')
Red_Spaceship = pygame.image.load(os.path.join('Assets','spaceship_red.png'))
Red_Spaceship = pygame.transform.rotate(pygame.transform.scale(Red_Spaceship, (55,40)),270)

# sounds:
Hit_Sound = pygame.mixer.Sound(os.path.join('Assets','Grenade+1.mp3'))
Shoot_Sound = pygame.mixer.Sound(os.path.join('Assets','Gun+Silencer.mp3'))
Shoot_Sound_2 = pygame.mixer.Sound(os.path.join('Assets','Gun+Silencer.mp3'))
Shoot_Sound_2.set_volume(0.2)
Bg_Music = pygame.mixer.music.load('Assets\\LHS-RLD-09.mp3')
Bg_Music_handler = pygame.mixer.music
Red_Wins = pygame.mixer.Sound(os.path.join('Assets','Red_Wins.mp3'))
Yellow_Wins = pygame.mixer.Sound(os.path.join('Assets','Yellow_Wins.mp3'))

Border = pygame.Rect(445,0,10,500)

Yellow_Hit = pygame.USEREVENT + 1
Red_Hit = pygame.USEREVENT + 2

Font = pygame.font.Font(os.path.join('arcade','ARCADE.TTF'),25)
Font2 = pygame.font.Font(os.path.join('arcade','ARCADE.TTF'),50)

#print(pygame.font.get_fonts())

def bg_color(Red,Yellow, Red_B, Yel_B,Red_Health,Yellow_Health):
    
    R = random.randint(0,255)
    G = random.randint(0,255)
    B = random.randint(0,255)

    root.blit(Bg,(0,0)) #Loading bg

    Txt1 = Font.render('Red Player Health:'+ str(Red_Health), 1, (255,255,255))
    Txt2 = Font.render('Yellow Player Health:'+ str(Yellow_Health), 1, (255,255,255))
    #root.blit(pygame.font.SysFont('monospace', 50).render('STR', 1, (255,255,255)), (450,450))
    root.blit(Txt1,(900- Txt1.get_width()-10,10))
    root.blit(Txt2,(10,10))

    root.blit(Yellow_Spaceship,(Yellow.x,Yellow.y)) # Loading spaceships
    root.blit(Red_Spaceship,(Red.x,Red.y))

    pygame.draw.rect(root, (0,0,0), Border)

    for bullet in Red_B:
        pygame.draw.rect(root, (255,0,0), bullet)

    for bullet in Yel_B:
        pygame.draw.rect(root, (255,255,0), bullet)

    pygame.display.update()   

def handle_bullets(Yel_B,Red_B,Yellow,Red):

    for bullet in Yel_B:
        bullet.x += 20
        if Red.colliderect(bullet):
            pygame.event.post(pygame.event.Event(Red_Hit))
            Yel_B.remove(bullet)

        elif bullet.x>900:
            Yel_B.remove(bullet)


    for bullet in Red_B:
        bullet.x -= 20
        if Yellow.colliderect(bullet):
            pygame.event.post(pygame.event.Event(Yellow_Hit))
            Red_B.remove(bullet)

        elif bullet.x<0:
            Red_B.remove(bullet)

def Win(Red_Health,Yellow_Health):

    Winner = ''

    if Yellow_Health <= 0:
        Bg_Music_handler.set_volume(0.1)
        Red_Wins.play()
        Win_color = (255,0,5)
        Winner = 'Red Wins!'

    elif Red_Health <= 0:
        Bg_Music_handler.set_volume(0.1)
        Yellow_Wins.play()
        Win_color = (255,255,0)
        Winner = 'Yellow Wins!'

    if Winner != '':
        Win_Text = Font2.render(Winner,1, Win_color)
        root.blit(Win_Text, (450 - Win_Text.get_width()/2 ,250 - Win_Text.get_height()))
        pygame.display.update()
        
        pygame.time.delay(5000)
        Bg_Music_handler.set_volume(1)
        return('Game over')


def main():

    #pygame.time.delay(5000)

    Red =  pygame.Rect(700, 300, 55, 40)
    Yellow = pygame.Rect(100, 300, 55, 40)

    Red_B = []
    Yel_B = []
    
    Red_Health = 10
    Yellow_Health = 10

    #Bg_Music.set_volume(0)
    Bg_Music_handler.play()
    run = True
    
    i = 0
    
    while run: # Prevent pygame from instantly quitting
        
        pygame.time.Clock().tick(1000) # FPS, No of times the display rereashes itself
        i+=1

        if i % 20 == 0 :
            bullet = pygame.Rect(Yellow.x+Yellow.width, Yellow.y + (40/2)+4 , 10 , 5)
            Shoot_Sound_2.play()
            Yel_B.append(bullet)

        for Event in pygame.event.get(): #Making sure the game quits when asked to (when we click the 'X' icon)
            if Event.type == pygame.QUIT:
                run = False
                
            if Event.type == pygame.KEYDOWN:
                
                if Event.key == pygame.K_RCTRL and len(Red_B)<3:
                    bullet = pygame.Rect(Red.x, Red.y + (40/2)+4 , 10 , 5)
                    Shoot_Sound.play()
                    Red_B.append(bullet)
                
            if Event.type == Red_Hit:
                    Hit_Sound.play()
                    Red_Health -= 1

            if Event.type == Yellow_Hit:
                    Hit_Sound.play()
                    Yellow_Health -=1

       

        Keys_Pressed = pygame.key.get_pressed()

################################################################################

        #L = [10,20,30,40,50,60]
        L = [1,2,3,4,56,7,8,9,10,11,12,13,14,15]
        Random1 = random.sample(L, 1)*2
        Random2 = random.sample(L, 1)*2
        Random3 = random.sample(L, 1)*2
        Random4 = random.sample(L, 1)*2

# DIRECTIon
################################################################################      '
        if i%2 == 0:
            if Random1 and Yellow.x - Random1[0] >= 0:
                Yellow.x-=Random1[0]

            if Random2 and Yellow.x + Random2[0] <= Border.right-55:
                Yellow.x+=Random2[0]

            if Random3 and Yellow.y - Random3[0] >= 0:
                Yellow.y-=Random3[0]

            if Random4 and Yellow.y + Random4[0] <= 500-40:
                Yellow.y+=Random4[0]
################################################################################
        if Keys_Pressed[pygame.K_LEFT] and Red.x - 5 >= Border.left+10:
            Red.x-=5

        if Keys_Pressed[pygame.K_RIGHT] and Red.x + 5 <= 900-40:
            Red.x+=5

        if Keys_Pressed[pygame.K_UP] and Red.y - 5 >= 0:
            Red.y-=5

        if Keys_Pressed[pygame.K_DOWN] and Red.y - 5 <= 500-40:
            Red.y+=5

        handle_bullets(Yel_B, Red_B, Yellow, Red)
        bg_color(Red, Yellow, Red_B, Yel_B, Red_Health, Yellow_Health)
        if Win(Red_Health, Yellow_Health) == 'Game over':
            break

    if run == True:
        Bg_Music_handler.stop()
        main()

if __name__ == '__main__':
    main()