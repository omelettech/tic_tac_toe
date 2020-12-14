import pygame
import sys
import random

pygame.init()

def tflipflop(turn):
	if turn==0:
		return 1
	elif turn==1:
		return 0
def checkstuff(box,counter):

	#verticals
	if box[0]==box[1]==box[2]:
		if turn==0:
			return 'O JITSE'
		else:
			return 'TOMAR X JITSE'

	if box[3]==box[4]==box[5]:
		if turn==0:
			return 'O JITSE'
		else:
			return 'TOMAR X JITSE'

	if box[6]==box[7]==box[8]:
		if turn==0:
			return 'O JITSE'
		else:
			return 'TOMAR X JITSE'

	#horizontals
	if box[0]==box[3]==box[6]:
		if turn==0:
			return 'O JITSE'
		else:
			return 'TOMAR X JITSE'

	if box[1]==box[4]==box[7]:
		if turn==0:
			return 'O JITSE'
		else:
			return 'TOMAR X JITSE'

	if box[2]==box[5]==box[8]:
		if turn==0:
			return 'O JITSE'
		else:
			return 'TOMAR X JITSE'

	#diagonals
	if box[0]==box[4]==box[8]:
		if turn==0:
			return 'O JITSE'
		else:
			return 'TOMAR X JITSE'

	if box[2]==box[4]==box[6]:
		if turn==0:
			return 'O JITSE'
		else:
			return 'TOMAR X JITSE'

	if box[4]=='enabledx' or box[4]=='enabledo':
		for i in range(8):
			if draw[i]==draw[i+1]:
				counter+=1
			else:
				counter=0

	if counter==8:
		return 'DRAW'

def drawstuff():

	if box[0] == 'enabledx':
		if blink[0]!=5:
			screen.blit(move_1[0],(f_line/2,f_line/2))
		if blink[0]==5:
			screen.blit(move_1[1],(f_line/2,f_line/2))
	if box[1] == 'enabledx':
		if blink[1]!=5:
			screen.blit(move_1[0],(f_line/2,f_line+f_line/2))
		if blink[1]==5:
			screen.blit(move_1[1],(f_line/2,f_line+f_line/2))
	if box[2] == 'enabledx':
		if blink[2]!=5:
			screen.blit(move_1[0],(f_line/2,s_line+f_line/2))
		if blink[2]==5:
			screen.blit(move_1[1],(f_line/2,s_line+f_line/2))
	if box[3] == 'enabledx':
		if blink[3]!=5:
			screen.blit(move_1[0],(f_line+f_line/2,f_line/2))
		if blink[3]==5:
			screen.blit(move_1[1],(f_line+f_line/2,f_line/2))
	if box[4] == 'enabledx':
		if blink[4]!=5:
			screen.blit(move_1[0],(f_line+f_line/2,f_line+f_line/2))
		if blink[4]==5:
			screen.blit(move_1[1],(f_line+f_line/2,f_line+f_line/2))
	if box[5] == 'enabledx':
		if blink[5]!=5:
			screen.blit(move_1[0],(f_line+f_line/2,s_line+f_line/2))
		if blink[5]==5:
			screen.blit(move_1[1],(f_line+f_line/2,s_line+f_line/2))
	if box[6] == 'enabledx':
		if blink[6]!=5:
			screen.blit(move_1[0],(s_line+f_line/2,f_line/2))
		if blink[6]==5:
			screen.blit(move_1[1],(s_line+f_line/2,f_line/2))
	if box[7] == 'enabledx':
		if blink[7]!=5:
			screen.blit(move_1[0],(s_line+f_line/2,f_line+f_line/2))
		if blink[7]==5:
			screen.blit(move_1[1],(s_line+f_line/2,f_line+f_line/2))
	if box[8] == 'enabledx':
		if blink[8]!=5:
			screen.blit(move_1[0],(s_line+f_line/2,s_line+f_line/2))
		if blink[8]==5:
			screen.blit(move_1[1],(s_line+f_line/2,s_line+f_line/2))




	if box[0] == 'enabledo':
		if blink[0]!=5:
			screen.blit(move_1[2],(f_line/2,f_line/2))
		if blink[0]==5:
			screen.blit(move_1[3],(f_line/2,f_line/2))
	if box[1] == 'enabledo':
		if blink[1]!=5:
			screen.blit(move_1[2],(f_line/2,f_line+f_line/2))
		if blink[1]==5:
			screen.blit(move_1[3],(f_line/2,f_line+f_line/2))
	if box[2] == 'enabledo':
		if blink[2]!=5:
			screen.blit(move_1[2],(f_line/2,s_line+f_line/2))
		if blink[2]==5:
			screen.blit(move_1[3],(f_line/2,s_line+f_line/2))
	if box[3] == 'enabledo':
		if blink[3]!=5:
			screen.blit(move_1[2],(f_line+f_line/2,f_line/2))
		if blink[3]==5:
			screen.blit(move_1[3],(f_line+f_line/2,f_line/2))
	if box[4] == 'enabledo':
		if blink[4]!=5:
			screen.blit(move_1[2],(f_line+f_line/2,f_line+f_line/2))
		if blink[4]==5:
			screen.blit(move_1[3],(f_line+f_line/2,f_line+f_line/2))
	if box[5] == 'enabledo':
		if blink[5]!=5:
			screen.blit(move_1[2],(f_line+f_line/2,s_line+f_line/2))
		if blink[5]==5:
			screen.blit(move_1[3],(f_line+f_line/2,s_line+f_line/2))
	if box[6] == 'enabledo':
		if blink[6]!=5:
			screen.blit(move_1[2],(s_line+f_line/2,f_line/2))
		if blink[6]==5:
			screen.blit(move_1[3],(s_line+f_line/2,f_line/2))
	if box[7] == 'enabledo':
		if blink[7]!=5:
			screen.blit(move_1[2],(s_line+f_line/2,f_line+f_line/2))
		if blink[7]==5:
			screen.blit(move_1[3],(s_line+f_line/2,f_line+f_line/2))
	if box[8] == 'enabledo':
		if blink[8]!=5:
			screen.blit(move_1[2],(s_line+f_line/2,s_line+f_line/2))
		if blink[8]==5:
			screen.blit(move_1[3],(s_line+f_line/2,s_line+f_line/2))




randbg=random.randint(0,1)
magenta=194, 50, 199
green=88, 196, 45
if randbg==0:
	line_colour=magenta
else:
	line_colour=green	
counter=0
blink=[1]*9
draw=[False]*9
l=600
d=0.04*l
box = ['d','i','s','a','b','l','e','d',':P']
directory = 'C:/Users/Butt_crack/Desktop/python/Tic_Tac_Toe/'
move = [pygame.image.load(directory+'cross.png'),pygame.image.load(directory+'Gol.png')]
move_1 = [pygame.image.load(directory+'cross_1.png'),pygame.image.load(directory+'cross_2.png'),pygame.image.load(directory+'Gol_1.png'),pygame.image.load(directory+'Gol_2.png')]
winnerscreen=[pygame.image.load(directory+'winner.png'),pygame.image.load(directory+'winner_1.png'),pygame.image.load(directory+'winner_3.png')]
bg=[pygame.image.load(directory+'bg_M.png'),pygame.image.load(directory+'bg_G.png')]
x=0
y=0
l_game=l-(2*d)
clicks=0
f_line=l_game/3
s_line=(l_game*2)/3
clock = pygame.time.Clock()
winner=''
myfont = pygame.font.SysFont('arial', 72)



box_list = []

turn = 0



pygame.display.set_caption('Tic Tac Toe')
screen=pygame.display.set_mode((l,l))



game_over=False

while not game_over:
	i=0
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()
		

			#display stuff
		elif event.type ==pygame.MOUSEMOTION:
			mouse_pos=pygame.mouse.get_pos()
			if mouse_pos[0]>0 and mouse_pos[0]<f_line:
				if mouse_pos[1]>0 and mouse_pos[1]<f_line:
					x=0
					y=0
					
				elif mouse_pos[1]>f_line and mouse_pos[1]<s_line:
					x=0
					y=f_line
					

				elif mouse_pos[1]>s_line and mouse_pos[1]<l_game:
					x=0
					y=s_line
					

			elif mouse_pos[0]>f_line and mouse_pos[0]<s_line:
				if mouse_pos[1]>0 and mouse_pos[1]<f_line:
					x=f_line
					y=0
					

				elif mouse_pos[1]>f_line and mouse_pos[1]<s_line:
					x=f_line
					y=f_line		
					
				elif mouse_pos[1]>s_line and mouse_pos[1]<l_game:
					x=f_line
					y=s_line
				

			elif mouse_pos[0]>s_line and mouse_pos[0]<l_game:
				if mouse_pos[1]>0 and mouse_pos[1]<f_line:
					x=s_line
					y=0
				


				elif mouse_pos[1]>f_line and mouse_pos[1]<s_line:
					x=s_line
					y=f_line
					
					
				elif mouse_pos[1]>s_line and mouse_pos[1]<l_game:
					x=s_line
					y=s_line



		if event.type == pygame.MOUSEBUTTONDOWN:
			click_pos=pygame.mouse.get_pos()
			if click_pos[0]>0 and click_pos[0]<f_line:
				if click_pos[1]>0 and click_pos[1]<f_line:
					if box[0]!='enabledx' and turn==0:
						turn=1
						box[0]='enabledx'
						draw[0]=True
					elif box[0]!='enabledo' and turn==1 and box[0]!='enabledx':
						turn=0
						box[0]='enabledo' 
						draw[0]=True


					
				elif click_pos[1]>f_line and click_pos[1]<s_line:
					if box[1]!='enabledx' and turn==0:
						turn=1
						box[1]='enabledx'
						draw[1]=True
					elif box[1]!='enabledo' and turn==1 and box[1]!='enabledx':
						turn=0
						box[1]='enabledo' 
						draw[1]=True




				elif click_pos[1]>s_line and click_pos[1]<l_game:
					if box[2]!='enabledx' and turn==0:
						turn=1
						box[2]='enabledx'
						draw[2]=True
					elif box[2]!='enabledo' and turn==1 and box[2]!='enabledx':
						turn=0
						box[2]='enabledo'
						draw[2]=True 



			elif click_pos[0]>f_line and click_pos[0]<s_line:
				if click_pos[1]>0 and click_pos[1]<f_line:
					if box[3]!='enabledx' and turn==0:
						turn=1
						box[3]='enabledx'
						draw[3]=True
					elif box[3]!='enabledo' and turn==1 and box[3]!='enabledx':
						turn=0
						box[3]='enabledo'
						draw[3]=True 




				elif click_pos[1]>f_line and click_pos[1]<s_line:
					if box[4]!='enabledx' and turn==0:
						turn=1
						box[4]='enabledx'
						draw[4]=True
					elif box[4]!='enabledo' and turn==1 and box[4]!='enabledx':
						turn=0
						box[4]='enabledo' 
						draw[4]=True


					
				elif click_pos[1]>s_line and click_pos[1]<l_game:
					if box[5]!='enabledx' and turn==0:
						turn=1
						box[5]='enabledx'
						draw[5]=True
					elif box[5]!='enabledo' and turn==1 and box[5]!='enabledx':
						turn=0
						box[5]='enabledo' 
						draw[5]=True




			elif click_pos[0]>s_line and click_pos[0]<l_game:
				if click_pos[1]>0 and click_pos[1]<f_line:
					if box[6]!='enabledx' and turn==0:
						turn=1
						box[6]='enabledx'
						draw[6]=True
					elif box[6]!='enabledo' and turn==1 and box[6]!='enabledx':
						turn=0
						box[6]='enabledo' 
						draw[6]=True





				elif click_pos[1]>f_line and click_pos[1]<s_line:
					if box[7]!='enabledx' and turn==0:
						turn=1
						box[7]='enabledx'
						draw[7]=True
					elif box[7]!='enabledo' and turn==1 and box[7]!='enabledx':
						turn=0
						box[7]='enabledo' 
						draw[7]=True



					
				elif click_pos[1]>s_line and click_pos[1]<l_game:
					if box[8]!='enabledx' and turn==0:
						turn=1
						box[8]='enabledx'
						draw[8]=True
					elif box[8]!='enabledo' and turn==1 and box[8]!='enabledx':
						turn=0
						box[8]='enabledo' 
						draw[8]=True



	for i in range(9):
		blink[i]=random.randint(1,30)


					

	

	
	#drawing
	screen.blit(bg[randbg],(0,0))

	pygame.draw.rect(screen,(line_colour),(d+l_game/3,d,5,l_game))
	pygame.draw.rect(screen,(line_colour),(d+((l_game*2)/3),d,5,l_game))
	pygame.draw.rect(screen,(line_colour),(d,d+l_game/3,l_game,5))
	pygame.draw.rect(screen,(line_colour),(d,d+((l_game*2)/3),l_game,5))
	screen.blit(move[turn],(x+f_line/2,y+f_line/2))
	drawstuff()
	winner=checkstuff(box,counter)
	if winner=='TOMAR X JITSE':
		screen.blit(winnerscreen[0],(0,0))
	if winner=='O JITSE':
		screen.blit(winnerscreen[1],(0,0))
	if winner=='DRAW':
		screen.blit(winnerscreen[2],(0,0))
		
		

	clock.tick(30)




	pygame.display.update()

	