import pygame
pygame.init()
width, height = 1356 , 700
screen = pygame.display.set_mode((width, height))
pygame.display.set_caption("algo")

black = (0, 0, 0)
blanc = (255, 255, 255)
green= (0,255,0)
running = True
my_font = pygame.font.SysFont('Comic Sans MS', height//8)
menu=True
jeu=None
jeumap=[]
turnp1=True
def option():
    global width,height,my_font
    pygame.draw.rect(screen, blanc, (0, height/2,width , 10))
    pygame.draw.rect(screen, blanc, (width/2, 0,10 , height))
    pygame.font.init()  
    text="morpion"
    text_surface = my_font.render(text, False, blanc)
    screen.blit(text_surface, (width*2/16,height/8))
    text="super morpion"
    text_surface = my_font.render(text, False, blanc)
    screen.blit(text_surface, (width*9/16,height/8))
    text="anti morpion"
    text_surface = my_font.render(text, False, blanc)
    screen.blit(text_surface, (width*2/16,height*5/8))
    text="puissance 4"
    text_surface = my_font.render(text, False, blanc)
    screen.blit(text_surface, (width*9/16,height*5/8))

def morpion():
    pygame.draw.rect(screen, blanc, (0, height/3,width , 10))
    pygame.draw.rect(screen, blanc, (width/3, 0,10 , height))
    pygame.draw.rect(screen, blanc, (width*2/3, 0,10 , height))
    pygame.draw.rect(screen, blanc, (0, height*2/3,width , 10))
def morpionclickcheck(x,y,jeumap):
    global turnp1
    if x<width/3:#toute a gauche
        jeumap,turnp1=morpionpositionement(jeumap,0,turnp1,y)
    elif x>width*2/3:
        jeumap,turnp1=morpionpositionement(jeumap,2,turnp1,y)
    else:
        jeumap,turnp1=morpionpositionement(jeumap,1,turnp1,y)
    return jeumap   
def morpionpositionement(jeumap,hauteur,turnp1,y):
    if y<height/3:#toute en haut
            if jeumap[0][hauteur]==0:
                if turnp1:
                    jeumap[0][hauteur]=1
                    turnp1=False
                else:
                    jeumap[0][hauteur]=2
                    turnp1=True
    elif y>height*2/3:
            if jeumap[2][hauteur]==0:
                if turnp1:
                    jeumap[2][hauteur]=1
                    turnp1=False
                else:
                    jeumap[2][hauteur]=2
                    turnp1=True
    else:
            if jeumap[1][hauteur]==0:
                if turnp1:
                    jeumap[1][hauteur]=1
                    turnp1=False
                else:
                    jeumap[1][hauteur]=2
                    turnp1=True
    return jeumap,turnp1    
def checkoption(x,y,jeu,menu,jeumap):
    if x<width/2:
        if y<height/2:#si morpion
            jeu=morpion
            menu=False
            jeumap=[[0,0,0],[0,0,0],[0,0,0]]
        elif y>height/2+10:#si anti morpion
            jeu=3
            menu=False
            jeumap=[[0,0,0],[0,0,0],[0,0,0]]
    elif x>width/2+10:#si super morpion
        if y<height/2:
            jeu=2
            menu=False
        elif y>height/2+10:#si puissance 4
            jeu=4
            menu=False
    return jeu,menu,jeumap

def dessinmorpion(map):
    for i in range(3):
        for m in range(3):
            if map[i][m]==1:
                pygame.draw.line(screen, blanc,((m+1)*width/3,(i)*height/3),((m)*width/3,(i+1)*height/3))
                pygame.draw.line(screen, blanc,((m)*width/3,(i)*height/3),((m+1)*width/3,(i+1)*height/3))
            elif map[i][m]==2:
                pygame.draw.circle(screen,blanc,((m+0.5)*width/3,(i+0.5)*height/3),height/8,width=10)
while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
        elif event.type== pygame.KEYDOWN:
            if event.key ==pygame.K_ESCAPE:
                pygame.quit()
        elif event.type==pygame.MOUSEBUTTONDOWN:
            mousex,mousey=pygame.mouse.get_pos()
            if menu:
                jeu,menu,jeumap=checkoption(mousex,mousey,jeu,menu,jeumap)
            else:
                if jeu==morpion:
                    jeumap=morpionclickcheck(mousex,mousey,jeumap)
                    print(jeumap)  
    if jeumap!=[]:
        dessinmorpion(jeumap)
    if menu:
        option()
    else:
        jeu()
    pygame.display.flip()
    screen.fill(black)
pygame.quit()