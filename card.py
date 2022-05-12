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
   
   # changed so that if the card is on the deck pile it starts face down
   # otherwise it starts face up   
   def stage(self, scene, deck, size, gp):
      if deck == 1:
         scene.blit(self.back, self.location)
      else:
         if self.faceup:
            if(size != 0):
               if(gp == 1):
                  scene.blit(self.front, (10, 250))
               elif(gp == 2):
                  scene.blit(self.front, (160, 250))
               elif(gp == 2):
                  scene.blit(self.front, (310, 250))
               elif(gp == 2):
                  scene.blit(self.front, (460, 250))
               elif(gp == 2):
                  scene.blit(self.front, (610, 250))
               elif(gp == 2):
                  scene.blit(self.front, (760, 250))
               elif(gp == 2):
                  scene.blit(self.front, (910, 250))
               else:
                  scene.blit(self.front,self.location)
            else:
               scene.blit(self.front,self.location)
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