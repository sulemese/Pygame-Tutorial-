import pygame
pygame.init()

#pencere oluşturduk
pencere = pygame.display.set_mode((640,480))

#görüntüyü yükleme
canavar = pygame.image.load("C:/Users/şule meşe/Downloads/monster.png")

#görüntünün koordinatlarını aldık bu bilgiyi görüntüyü pencereye yerleştirirken kullanacağız.
canavar_koordinat = canavar.get_rect()

#görüntünün pencerede konumunu belirledik. 
canavar_koordinat.topleft=(100,10)





#pencere olayları
durum = True
while durum:
     for etkinlik in pygame.event.get():
          if etkinlik.type == pygame.QUIT:
               durum = False
               
     #görüntüyü pencereye kopyaladık
     pencere.blit(canavar,canavar_koordinat)
     
     #pencere sürekli güncellensin
     pygame.display.update()
     
     
pygame.quit()