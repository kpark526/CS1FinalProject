import pygame
from card import Card
import random

class Pile:
   def __init__(self,x,y):
      self.stack = []
      self.top_visible = False
      
      self.location = pygame.Rect(x,y,140,200)
      
   def stage(self, scene, deck, size, gp):
      if len(self.stack) > 0:
         self.stack[-1].stage(scene,deck,size,gp)
      else:
         pygame.draw.rect(scene, [0,53,0], self.location)
         
   def touched(self,pos):
      return self.location.collidepoint(pos)
   
   def push(self,card):
      self.stack.append(card)
      card.location = self.location
      card.held = False
   
   def pop(self):
      if len(self.stack) > 0:
         card = self.stack.pop()
         card.location = self.location.copy()
         card.held = True
         return card
   
   def isEmpty(self):
      return len(self.stack) == 0
   
   def size(self):
      return len(self.stack)
         
   def peek(self):
      card = self.stack[-1]
      return card
   
   def shuffle(self):
      random.shuffle(self.stack)