import pygame
import time
from card import Card
from pile import Pile
import random

# function for getting the suit color
def getColor(suit):
   if (suit == 'diamonds' or suit == 'hearts'):
      return 'red'
   else:
      return 'black'

#function for getting the opposite suit color
def oppositeColor(suit):
   if (suit == 'diamonds' or suit == 'hearts'):
      return 'black'
   else:
      return 'red'

#function for getting the rank in an integer
def getNumRank(rank):
   if(rank == 'ace'):
      return 1
   elif(rank == 'jack'):
      return 11
   elif(rank == 'queen'):
      return 12
   elif(rank == 'king'):
      return 13
   else:
      return int(rank)

if __name__ == "__main__":
   pygame.init()
   
   # display of 1400 by 800 pixels
   scene = pygame.display.set_mode((1120,800))
   pygame.display.set_caption("Solitaire")
   
   clock = pygame.time.Clock()
   
   # upper left pile of cards
   # contains every card in a deck
   deck = Pile(10,10)
   for suit in ['diamonds','clubs','hearts','spades']:
      for rank in ['ace','2','3','4','5','6','7','8','9','10','jack','queen','king']:
         card = Card(suit,rank)
         deck.push(card)
   deck.shuffle()
   
   # empty pile to put the next card in
   nextDeck = Pile(160,10)
   
   # solution wells
   well1 = Pile(460,10)
   well2 = Pile(610,10)
   well3 = Pile(760,10)
   well4 = Pile(910,10)
   
   
   # start of the lower piles of cards
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
  
   # initializes held card and last pile
   card = None
   previousPile = None
   
   scene.fill([0,153,0])
   deck.stage(scene,1,0,0)
   nextDeck.stage(scene,0,0,0)
      
   well1.stage(scene,0,0,0)
   well2.stage(scene,0,0,0)
   well3.stage(scene,0,0,0)
   well4.stage(scene,0,0,0)
      
   gamePile1.stage(scene,0,gamePile1.size(),1)
   gamePile2.stage(scene,0,gamePile2.size(),2)
   gamePile3.stage(scene,0,gamePile3.size(),3)
   gamePile4.stage(scene,0,gamePile4.size(),4)
   gamePile5.stage(scene,0,gamePile5.size(),5)
   gamePile6.stage(scene,0,gamePile6.size(),6)
   gamePile7.stage(scene,0,gamePile7.size(),7)
   
   running = True
   while running:
      # loop for events
      for event in pygame.event.get():
         if event.type == pygame.QUIT:
            running = False
         
         # if the mouse is pushed down
         # if you click on a pile, it grabs the top card
         elif event.type == pygame.MOUSEBUTTONDOWN:
            if deck.touched(event.pos):
               if(deck.isEmpty() == True):
                     for i in range(nextDeck.size()):
                        deck.push(nextDeck.pop())
                     nextDeck = Pile(160,10)
               else:
                  card = deck.pop()
                  previousPile = deck
               
            elif nextDeck.touched(event.pos):
               card = nextDeck.pop()
               previousPile = nextDeck
               
            elif well1.touched(event.pos):
               card = well1.pop()
               previousPile = well1
            elif well2.touched(event.pos):
               card = well2.pop()
               previousPile = well2
            elif well3.touched(event.pos):
               card = well3.pop()
               previousPile = well3
            elif well4.touched(event.pos):
               card = well4.pop()
               previousPile = well4
            
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
            elif gamePile7.touched(event.pos):
               card = gamePile7.pop()
               previousPile = gamePile7
         
         # if you lift up the mouse while holding a card      
         elif event.type == pygame.MOUSEBUTTONUP:
            # if you're clicking on a card, grab the rank and the suit
            if card:
               currentRank = card.rank
               currentSuit = card.suit
               
               # if you want to move the card to the next Deck
               if nextDeck.touched(event.pos):
                  nextDeck.push(card)

               # put any card into any well
               elif well1.touched(event.pos):
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
               
               # any card onto any game pile  
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
         # react event for cards
         if card:
            card.react(event,clock)
      
      #redo scene after every event
      scene.fill([0,153,0])
      deck.stage(scene,1,0,0)
      nextDeck.stage(scene,0,0,0)
      
      well1.stage(scene,0,0,0)
      well2.stage(scene,0,0,0)
      well3.stage(scene,0,0,0)
      well4.stage(scene,0,0,0)
      
      gamePile1.stage(scene,0,gamePile1.size(),1)
      gamePile2.stage(scene,0,gamePile2.size(),2)
      gamePile3.stage(scene,0,gamePile3.size(),3)
      gamePile4.stage(scene,0,gamePile4.size(),4)
      gamePile5.stage(scene,0,gamePile5.size(),5)
      gamePile6.stage(scene,0,gamePile6.size(),6)
      gamePile7.stage(scene,0,gamePile7.size(),7)
      if card:
         card.stage(scene,0,0,0)
         
      # update display
      pygame.display.update()