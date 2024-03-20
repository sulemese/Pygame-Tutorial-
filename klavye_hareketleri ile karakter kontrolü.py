import pygame
pygame.init()

#sabitler 
window_width=800
window_height=800
speed = 20 

#pencere oluşturuldu
window_size  = (window_width,window_height)
window = pygame.display.set_mode(window_size)

#obje tanımlandı 
monster = pygame.image.load("C:/Users/şule meşe/Downloads/monster.png")

#objenin boyutu rect şeklinde alındı
monster_koordinat = monster.get_rect()

#objenin pencerede yerleşeceği kordinat tanımlandı 
monster_koordinat.topleft=(window_width/2,window_height/2)

#pencere olayları
durum = True
while durum:
     for event in pygame.event.get():
          #çarpı tuşu
          if event.type == pygame.QUIT:
               durum = False
          #klavye tuşları
          if event.type == pygame.KEYDOWN:
               #sol yön tuşu
               if event.key == pygame.K_LEFT:
                    monster_koordinat.x -= speed
               if event.key == pygame.K_RIGHT:
                    monster_koordinat.x += speed
               if event.key ==  pygame.K_UP:
                    monster_koordinat.y -= speed
               if event.key == pygame.K_DOWN:
                    monster_koordinat.y += speed
     #objenin hareketi esnasında  yenisi oluşturulurken  eski obje silinsin. tekrarı engeller.               
     window.fill((0,0,0))              
     #obje belirtilen kordinata yerleştirildi 
     window.blit(monster,monster_koordinat)
     #pencere sürekli güncellensin
     pygame.display.update()
     
               
               
pygame.quit()