import pygame

class Card:
   def __init__(self, suit, rank):
      self.suit = suit
      self.rank = rank
      self.faceup = True
      self.held = False
      
      front = pygame.image.load('./cards/' + rank + '_of_' + suit + '.png')
      front = pygame.transform.smoothscale(front, (140, 200))
      self.front = front
      
      back = pygame.image.load('./cards/card_back.png')
      back = pygame.transform.smoothscale(back, (140, 200))

      self.back = back
      
      self.location = self.front.get_rect()
      
   def stage(self, scene):
      if self.faceup:
         scene.blit(self.front, self.location)
      
      else:
         scene.blit(self.back, self.location)
   
   def touched(self,pos):
      return self.location.collidepoint(pos)
      
   def react(self,event,clock):
      if event.type == pygame.MOUSEBUTTONDOWN:
         if self.touched(event.pos):
            if clock.tick() < 500:
               self.faceup = not self.faceup
            else:
               self.held = True
      elif event.type == pygame.MOUSEBUTTONUP:
         if self.touched(event.pos):
            self.held = False
      elif event.type == pygame.MOUSEMOTION:
         if self.held:
            self.location.move_ip(event.rel)