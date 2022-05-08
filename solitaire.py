import pygame
import time
from card import Card
from pile import Pile
import random


if __name__ == "__main__":
   pygame.init()
   
   # display of 1400 by 800 pixels
   scene = pygame.display.set_mode((1120,800))
   pygame.display.set_caption("Solitaire")
   
   clock = pygame.time.Clock()
   
   
   deck = Pile(10,10)
   for suit in ['diamonds','clubs','hearts','spades']:
      for rank in ['ace','2','3','4','5','6','7','8','9','10','jack','queen','king']:
         card = Card(suit,rank)
         deck.push(card)
   deck.shuffle()
   
   well1 = Pile(460,10)
   well2 = Pile(610,10)
   well3 = Pile(760,10)
   well4 = Pile(910,10)
   
   gamePile1 = Pile(10,250)
   gamePile1.push(deck.pop())
   
   gamePile2 = Pile(160,250)
   for i in range(2):
      gamePile2.push(deck.pop())
   
   gamePile3 = Pile(310,250)
   for i in range(3):
      gamePile3.push(deck.pop())
      
   
   gamePile4 = Pile(460,250)
   for i in range(4):
      gamePile4.push(deck.pop())
      
   gamePile5 = Pile(610,250)
   for i in range(5):
      gamePile5.push(deck.pop())
   
   gamePile6 = Pile(760,250)
   for i in range(6):
      gamePile6.push(deck.pop())
      
   gamePile7 = Pile(910,250)
   for i in range(7):
      gamePile7.push(deck.pop())
  
   card = None
   previousPile = None
   
   running = True
   while running:
      # loop for events
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            running = False
         elif event.type == pygame.MOUSEBUTTONDOWN:
            if deck.touched(event.pos):
               card = deck.pop()
               previousPile = deck
            elif gamePile1.touched(event.pos):
               card = gamePile1.pop()
               previousPile = gamePile1
            elif gamePile2.touched(event.pos):
               card = gamePile2.pop()
               previousPile = gamePile2
            elif gamePile3.touched(event.pos):
               card = gamePile3.pop()
               previousPile = gamePile3
            elif gamePile4.touched(event.pos):
               card = gamePile4.pop()
               previousPile = gamePile4
            elif gamePile5.touched(event.pos):
               card = gamePile5.pop()
               previousPile = gamePile5
            elif gamePile6.touched(event.pos):
               card = gamePile6.pop()
               previousPile = gamePile6
            elif gamePile6.touched(event.pos):
               card = gamePile6.pop()
               previousPile = gamePile6
         elif event.type == pygame.MOUSEBUTTONUP:
            if card:
               currentRank = card.rank
               currentSuit = card.suit
               if well1.touched(event.pos):
                  well1.push(card)
                  card = None
               elif well2.touched(event.pos):
                  well2.push(card)
                  card = None
               elif well3.touched(event.pos):
                  well3.push(card)
                  card = None
               elif well4.touched(event.pos):
                  well4.push(card)
                  card = None
                  
               elif gamePile1.touched(event.pos):
                  gamePile1.push(card)
                  card = None
               elif gamePile2.touched(event.pos):
                  gamePile2.push(card)
                  card = None
               elif gamePile3.touched(event.pos):
                  gamePile3.push(card)
                  card = None
               elif gamePile4.touched(event.pos):
                  gamePile4.push(card)
                  card = None
               elif gamePile5.touched(event.pos):
                  gamePile5.push(card)
                  card = None
               elif gamePile6.touched(event.pos):
                  gamePile6.push(card)
                  card = None
               elif gamePile7.touched(event.pos):
                  gamePile7.push(card)
                  card = None
               else:
                  previousPile.push(card)
                  card = None
         if card:
            card.react(event,clock)
      
      #redo scene after every event
      scene.fill([0,153,0])
      deck.stage(scene)
      well1.stage(scene)
      well2.stage(scene)
      well3.stage(scene)
      well4.stage(scene)
      
      gamePile1.stage(scene)
      gamePile2.stage(scene)
      gamePile3.stage(scene)
      gamePile4.stage(scene)
      gamePile5.stage(scene)
      gamePile6.stage(scene)
      gamePile7.stage(scene)
      if card:
         card.stage(scene)
         
      # update display
      pygame.display.update()

