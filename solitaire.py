import pygame
import time
from card import Card
from pile import Pile


if __name__ == "__main__":
   pygame.init()
   
   # display of 1400 by 800 pixels
   scene = pygame.display.set_mode((1400,800))
   pygame.display.set_caption("Solitaire")
   
   pile1 = Pile(100,100)
   
   for suit in ['diamonds','clubs','hearts']:
      for rank in ['2','4','8']:
         card = Card(suit,rank)
         pile1.push(card)
   pile2 = Pile(400,100)
   
   card = None
   
   running = True
   while running:
      # loop for events
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            running = False
         elif event.type == pygame.MOUSEBUTTONDOWN:
            if pile1.touched(event.pos):
               card = pile1.pop()
      
      #fill with green pixels
      scene.fill([0,153,0])
      pile1.stage(scene)
      pile2.stage(scene)
      # update display
      pygame.display.update()

