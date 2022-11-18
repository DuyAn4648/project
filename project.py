import pygame
import time
pygame.init()
pygame.font.init()
pygame.mixer.init()
pygame.mixer.pre_init(frequency=44100,size=-16,channels=2,buffer=512)
#Nền
a=(800,600)
screen=pygame.display.set_mode(a)
pygame.display.set_caption('Quê Lúa Yên Thành')
WHITE=(255,255,255)
BLACK=(0,0,0)
font = pygame.font.Font('freesansbold.ttf', 32)
dialogue_font = pygame.font.SysFont('utf8', 32)
running=True
language=0
bg=pygame.image.load(('bg1.jpg'))
bando=pygame.image.load(('map.png'))
menu=pygame.image.load(('menu.png'))
home=pygame.image.load(('home.png'))
home=pygame.transform.scale(home,(50,50))
dichvu1=pygame.image.load(('amthuc.png'))
dichvu1=pygame.transform.scale(dichvu1,a)
dichvu2=pygame.image.load(('nghiduong.png'))
dichvu2=pygame.transform.scale(dichvu2,a)
dichvu3=pygame.image.load(('giaothong.png'))
dichvu3=pygame.transform.scale(dichvu3,a)
back1=pygame.image.load(('Back1.png'))
back1=pygame.transform.scale(back1,(100,50))
muiten1=pygame.image.load(('arrowleft.png'))
muiten1=pygame.transform.scale(muiten1,(200,200))
muiten2=pygame.image.load(('arrowright.png'))
muiten2=pygame.transform.scale(muiten2,(200,200))
x='bg'
dichvu=0
# các biến trong map
location=0
dencuong=0
truongbon=0
#Đền Cuông
dencuong1=pygame.image.load(('dencuong/ĐC1.jpeg'))
dencuong1=pygame.transform.scale(dencuong1,a)
dencuong2=pygame.image.load(('dencuong/ĐC2.jpeg'))
dencuong2=pygame.transform.scale(dencuong2,a)
dencuong3=pygame.image.load(('dencuong/ĐC3.jpeg'))
dencuong3=pygame.transform.scale(dencuong3,a)
dencuong4=pygame.image.load(('dencuong/ĐC4.jpeg'))
dencuong4=pygame.transform.scale(dencuong4,a)
dencuong5=pygame.image.load(('dencuong/ĐC6.jpeg'))
dencuong5=pygame.transform.scale(dencuong5,a)
dencuong6=pygame.image.load(('dencuong/ĐC7.jpeg'))
dencuong6=pygame.transform.scale(dencuong6,a)
dencuong7=pygame.image.load(('dencuong/ĐC8.jpeg'))
dencuong7=pygame.transform.scale(dencuong7,a)
dencuong8=pygame.image.load(('dencuong/ĐC9.jpeg'))
dencuong8=pygame.transform.scale(dencuong8,a)
dencuong9=pygame.image.load(('dencuong/ĐC10.jpeg'))
dencuong9=pygame.transform.scale(dencuong9,a)
#Truông Bồn
truongbonbg_sound=pygame.mixer.Sound('truongbon/bg.mp3')
truongbonbg=pygame.image.load(('truongbon/bg.png'))
truongbonbg=pygame.transform.scale(truongbonbg,a)
#Main
while running:
	mouse_x,mouse_y=pygame.mouse.get_pos()
	print(mouse_x,mouse_y,x,location)
	screen.blit(bg,(0,0))
	#Tương tác
	for event in pygame.event.get():
		if event.type==pygame.QUIT:
			running=False
		if event.type==pygame.MOUSEBUTTONDOWN:
			if event.button==1:
			#Menu
				if (mouse_x>260 and mouse_x<522) and (mouse_y>320 and mouse_y<400) and x=='bg':
					x='menu'
					break
			#Nút Home
				if (mouse_x>0 and mouse_x<45) and (mouse_y>0 and mouse_y<50):
					x='bg'
			#Dịch vụ
				if (mouse_x>259 and mouse_x<525) and (mouse_y>345 and mouse_x<435) and x=='menu':
					x='dichvu'
				if x=='dichvu':
					if  (mouse_x>50 and mouse_x<255) and (mouse_y>10 and mouse_y<100):
						dichvu-=1
						if dichvu<0:
							dichvu=0
					elif (mouse_x>550 and mouse_x<755) and (mouse_y>10 and mouse_y<100):
						dichvu+=1
						if dichvu>2:
							dichvu=2
					elif (mouse_x>700 and mouse_x<800) and (mouse_y>555 and mouse_y<600):
						x='menu'
			#Bản đồ 
				if (mouse_x>250 and mouse_x<525) and (mouse_y>168 and mouse_y<262) and x=='menu':
					x='bando'
				#Chọn địa điểm
				if x=='bando':
					if(mouse_x>617 and mouse_x<660) and (mouse_y>368 and mouse_y<408):
						location='dencuong'
						x=0
						dencuong=0
					if(545<mouse_x<585) and (400<mouse_y<440):
						location='truongbon'
						x=0
						truongbon=0

				#Các địa điểm
				if(mouse_x>20 and mouse_x<140) and (11<mouse_y<111):
					if location=='dencuong':
						dencuong-=1
						if dencuong<0:
							dencuong=0
				if(658<mouse_x<778) and(11<mouse_y<111):
					if location=='dencuong':
						dencuong+=1
						if dencuong>8:
							dencuong=8
				if (mouse_x>0 and mouse_x<100) and (mouse_y>555 and mouse_y<600) and location !=0:
					location=0
					x='bando'
#Chuyển Phông Nền
	if x=='bg':
		screen.blit(bg,(0,0))
	elif x=='menu':
		screen.blit(menu,(0,0))
	elif x=='bando':
		screen.blit(bando,(0,0))
		truongbonbg_sound.stop()
	elif x=='dichvu':
		if dichvu==0:
			screen.blit(dichvu1,(0,0))
		if dichvu==1:
			screen.blit(dichvu2,(0,0))
		if dichvu==2:
			screen.blit(dichvu3,(0,0))
		screen.blit(back1,(700,555))
	if x!='bg':
		screen.blit(home,(0,0))
#Bản đồ
	#Đền Cuông
	if location=='dencuong':
		if dencuong==0:
			screen.blit(dencuong1,(0,0))
		if dencuong==1:
			screen.blit(dencuong2,(0,0))
		if dencuong==2:
			screen.blit(dencuong3,(0,0))
		if dencuong==3:
			screen.blit(dencuong4,(0,0))
		if dencuong==4:
			screen.blit(dencuong5,(0,0))
		if dencuong==5:
			screen.blit(dencuong6,(0,0))
		if dencuong==6:
			screen.blit(dencuong7,(0,0))
		if dencuong==7:
			screen.blit(dencuong8,(0,0))
		if dencuong==8:
			screen.blit(dencuong9,(0,0))
		screen.blit(muiten1,(-20,-40))
		screen.blit(muiten2,(620,-40))
		screen.blit(back1,(0,555))
	if location=='truongbon':
		screen.blit(truongbonbg,(0,0))
		truongbonbg_sound.play()
		screen.blit(back1,(0,555))
	pygame.display.flip()
pygame.quit()