import pygame
pygame.init()
boyut = (400,400)
pencere1 = pygame.display.set_mode(boyut)

durum = True
while durum:
     for etkinlik in pygame.event.get():
          #pencerede yapılan tüm mouse eventlerini veya olayları loglar. 
          print(etkinlik)
          #eğer çarpıya basılırsa fordan çıkar ve pencere kapanır
          if etkinlik.type == pygame.QUIT: 
               durum = False

pygame.quit()