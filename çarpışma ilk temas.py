import pygame
import random
pygame.init()

window_width = 700
window_height = 800

window = pygame.display.set_mode((window_width,window_height))
speed = 5
fps = 60

clock = pygame.time.Clock()

monster = pygame.image.load("C:/Users/şule meşe/Downloads/monster.png")
monster_koordinat = monster.get_rect()
monster_koordinat.topleft=(150,150)

coin = pygame.image.load("C:/Users/şule meşe/Downloads/dollar.png")
coin_koordinat = coin.get_rect()
coin_koordinat.topleft=(500,500)

#pencere olayları
durum = True
while durum:
     for event in pygame.event.get():
          #çarpı tuşu
          if event.type == pygame.QUIT:
               durum = False
               
     tuş = pygame.key.get_pressed()   
     if tuş[pygame.K_LEFT] and monster_koordinat.left>0 : 
          monster_koordinat.x -= speed
     if tuş[pygame.K_RIGHT] and monster_koordinat.right<window_width:
          monster_koordinat.x += speed
     if tuş[pygame.K_UP] and monster_koordinat.top>0:
          monster_koordinat.y -= speed
     if tuş[pygame.K_DOWN] and monster_koordinat.bottom<window_height:
          monster_koordinat.y += speed
          
     window.fill((0,0,0))
     
     
     #objelerin etrafına dikdörtgen çizer
     pygame.draw.rect(window,(255,0,0),monster_koordinat,1)
     pygame.draw.rect(window,(255,0,0),coin_koordinat,1)
     
     #çarpışma olursa ödülü yeni konumda oluştursun 
     if monster_koordinat.colliderect(coin_koordinat):
          coin_koordinat.x = random.randint(0,window_width-32)
          coin_koordinat.y = random.randint(0,window_height-32)
          print("parayı kaptın")
               
     window.blit(monster,monster_koordinat)
     window.blit(coin,coin_koordinat)    
     pygame.display.update()
     clock.tick(fps)
          

