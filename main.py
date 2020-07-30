#----------------------------------------------------------DOG RUN-------------------------------------------------------------------
import pygame
from pygame.locals import*
import sys
import random
import math
#------------------------------------------------------------------------------------------------------------------------------------
def main():
	pygame.init()
	pygame.display.set_caption('Dog Run By Garg_Aryan')
	SCREENWIDHT=590
	SCREENHEIGHT=332
	Screen = pygame.display.set_mode((SCREENWIDHT,SCREENHEIGHT))
#-----------------------------------------------------------------------------------------------------------------------------------

#----------------------------------------------Inserting all the images-------------------------------------------------------------
	PLAYER=pygame.image.load('picture/dog.png')
	CAR=pygame.image.load('picture/taxi.png')
	BUSHES=pygame.image.load('picture/bush.png')
	BACKGROUND=pygame.image.load('picture/background.png')
	BARREL=pygame.image.load('picture/oil.png')
	LION=pygame.image.load('picture/lion.png')
	MESSAGE=pygame.image.load('picture/message.png')
#-----------------------------------------------------------------------------------------------------------------------------------

#------------------------------------------------------Game sounds------------------------------------------------------------------

	hit = pygame.mixer.Sound('audio/hit.wav')
	background = pygame.mixer.Sound('audio/background.wav')
	wing = pygame.mixer.Sound('audio/wing.wav')
	point = pygame.mixer.Sound('audio/point.wav')
#--------------------------------------------------Setting the volume---------------------------------------------------------------
	background.set_volume(0.30)
	hit.set_volume(0.45)
	wing.set_volume(0.65)
#-----------------------------------------------------------------------------------------------------------------------------------
#---------------------------------------------------Creating objects-----------------------------------------------------------
	objects=[CAR,BUSHES,BARREL,LION]
#-----------------------------------------------------------------------------------------------------------------------------------
		
#----------------------------------------------Defining coordinates of Player------------------------------------------------------
	playerx=PLAYER.get_width()-35
	playery=210
#-----------------------------------------------------------------------------------------------------------------------------------
	var=True	
#--------------------------------------------------welcomeScreen function-----------------------------------------------------------------
	def welcomeScreen():	
		background.play(-1)
		while True:
			for event in pygame.event.get():	
				if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
					pygame.quit()
					sys.exit()
  	
			
				elif event.type == KEYDOWN and event.key == K_SPACE:
					mainGame()
					break		
				else:
					Screen.fill((255,255,255))
					Screen.blit(MESSAGE,(0,0))
				
					pygame.display.update()
#-----------------------------------------------------------------------------------------------------------------------------------					
#----------------------------------------------mainGame function--------------------------------------------------------------------	
	def mainGame():
	
		global var
	#---------------------------------------Score function----------------------------------------------------------------------
		scoreValue=0
		font = pygame.font.Font('freesansbold.ttf', 28)


		def showScore():
			score=font.render("Score:"+ str(scoreValue),True,(255,255,255))
			Screen.blit(score,(10,10))
	#--------------------------------------------------------------------------------------------------------------------------
	#-------------------------------------gameOver function--------------------------------------------------------------------
		def gameOver():
		
			while True:	
				for event in pygame.event.get():	
					if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
						pygame.quit()
						sys.exit()
					if event.type == KEYDOWN and (event.key == K_SPACE or event.key==K_RETURN):
						main()
					
					
					
			
				font = pygame.font.Font('freesansbold.ttf', 40)


				Screen.fill((255,255,255))
				text=font.render(f"Game Over\nScore: {scoreValue}",True,(0,0,50))
				Screen.blit(text,(92,140))
				background.set_volume(0)			
				pygame.display.update()
				#welcomeScreen()
	#---------------------------------------------------------------------------------------------------------------------------


		i=0
		obj1x=526		
		obj2x=200
		obj1=random.choice(objects)	
		obj2=random.choice(objects)	
		playery=210
		while True:
			for event in pygame.event.get():		
				if event.type==QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE):
					pygame.quit()
				
					
				if event.type == KEYDOWN and event.key == K_BACKSPACE:
					welcomeScreen()
				if var:
					if event.type == KEYDOWN and event.key == K_SPACE:
						playery-=90
						var=False
						wing.play()
						i+=0.05
						
			Screen.blit(BACKGROUND,(0,0))
			Screen.blit(PLAYER,(playerx,playery))
			Screen.blit(obj1,(obj1x,210))
			Screen.blit(obj2,(obj2x,210))
			playery+=0.27                                          #Down speed of the dog
			if obj1x<=-obj1.get_width():
				obj1x=random.randint(526,1200)
				obj1=random.choice(objects)				
				scoreValue+=1
				point.play()
			if obj2x<=-obj2.get_width():
				obj2x=random.randint(1700,2000)
				obj2=random.choice(objects)
				scoreValue+=1
				point.play()
			dist=math.sqrt((playerx-obj1x)**2 + (playery-210)**2)
			
				
			showScore()

			if dist<50:
				hit.play()
				gameOver()				
			if playery>=200:
				playery=210	
				var=True
			if i>1.4:
				i=1.4						#To set the max speed limit
			obj1x=obj1x-0.85-i					     #Speed of the objects						
			obj2x=obj2x-0.85-i
			pygame.display.update()                		
#-----------------------------------------------------------------------------------------------------------------------------------
	welcomeScreen()
#-----------------------------------------------------------------------------------------------------------------------------------
if __name__=="__main__":
	main()
#-----------------------------------------------------------------------------------------------------------------------------------














	

