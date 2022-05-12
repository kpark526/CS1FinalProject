import pygame
import time
from card import Card
from pile import Pile
import random
import os

if __name__ == "__main__":
   pygame.init()
   
   # display of 1400 by 800 pixels
   scene = pygame.display.set_mode((1120,800))
   pygame.display.set_caption("Solitaire Menu")
   
   pygame.mixer.init()
   pygame.mixer.music.load('theme.mp3')
   pygame.mixer.music.play(loops = -1)
   
   color = (255,255,255)
   boxColor = (255,234,236)
   boxColor2 = (243,154,157)
   width = scene.get_width()
   height = scene.get_height()
   fonty = pygame.font.SysFont('Arial',35)
   welcomeFont = pygame.font.SysFont('Arial',50)
   easyText = fonty.render('Freestyle Solitaire',True,(0,0,0))
   hardText = fonty.render('"Classic" Solitaire',True,color)
   welcomeText = welcomeFont.render('Pick a Mode',True,color)
   
   running = True
   while running:
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            running = False
         elif event.type == pygame.MOUSEBUTTONDOWN:
            if width/2 < mouse[0] < width/2+325 and height/2 <= mouse[1] < height/2+40:
               pygame.quit()
               os.system("python solitaire_easy.py")
            elif width/2 - 400 < mouse[0] < width/2+325-400and height/2 <= mouse[1] < height/2+40:
               pygame.quit()
               os.system("python solitaire_hard.py")
      
      scene.fill([63,108,81])
      mouse = pygame.mouse.get_pos()
      pygame.draw.rect(scene,boxColor,[width/2,height/2,325,40])
      scene.blit(easyText, (width/2+50,height/2))
      pygame.draw.rect(scene,boxColor2,[width/2-400,height/2,325,40])
      scene.blit(hardText,(width/2+50-400,height/2))
      scene.blit(welcomeText,(width/2+50-200,height/2-200))
      pygame.display.update()