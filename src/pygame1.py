# -*- coding: UTF-8 -*-


import pygame
pygame.init()
caption=pygame.display.set_caption('My Python App')
# screen=pygame.display.set_mode([1024,1024]) #窗口大小为320*200
screen=pygame.display.set_mode((640, 480), pygame.DOUBLEBUF, 32) #窗口大小为320*200
# screen.fill([198,226,255]) #用白色填充窗体
# '''
while True:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
    pygame.display.update()
    screen.fill([198,226,255]) #用白色填充窗体
    obj = pygame.image.load("_20170929100047.jpg").convert_alpha()
    screen.blit(obj, (20,10))
    # pygame.draw.rect(screen,[255,0,0],[150,150,150,140],0)
    # pygame.draw.circle(screen,[0,0,0],[150,100],20,1)
sys.exit()
# '''