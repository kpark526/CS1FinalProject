import pygame
from card import Card
import random

class Pile:
   def __init__(self,x,y):
      self.stack = []
      self.top_visible = False
      
      self.location = pygame.Rect(x,y,140,200)
      
   def stage(self, scene):
      if len(self.stack) > 0:
         self.stack[-1].stage(scene)
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
         
   def peek(self):
      return self.stack[-1]
   
   def shuffle(self):
      random.shuffle(self.stack)