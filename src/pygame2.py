# -*- coding: UTF-8 -*-
import pygame
import random
#默认情况下，图片需要跟代码在同一路径下
background = 'sky.jpg'
pic1 = 'pic1.jpg'

# 初始化pygame组件
pygame.init()	#必带初始化语句
screen_y_max = 800
screen = pygame.display.set_mode((600, screen_y_max), 0, 32)	#创建窗体
pygame.display.set_caption("sky")	#设置窗体名

bg = pygame.image.load(background).convert()	#载入背景图片

# 用死循环来确保窗体不会自动关闭
rate = 1
y = 0
count = 0
while True:
	count += 1
	# 检测退出事件pygame.QUIT
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			pygame.quit()

	screen.blit(bg, (10,y))	#通过"位块传送"的方式画图，位置为0到y
	print(y,count)

	
	ex1 = random.randrange(20, 600)
	ey1 = random.randrange(10, 50)

	pg = pygame.image.load(pic1).convert_alpha()
	# screen.blit(pg, (40, 350))
	screen.blit(pg, (ex1, ey1))

	pygame.display.update()	#显示，若没有显示语句，则无法在窗体上显示任何图片
	screen.fill([0,0,0])
	pygame.time.wait(100)