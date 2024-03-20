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
monster_koordinat.topleft=(150,150)

#pencere olayları
durum = True
while durum:
     for event in pygame.event.get():
          #çarpı tuşu
          if event.type == pygame.QUIT:
               durum = False
          #mouse tuşları
          if event.type == pygame.MOUSEBUTTONDOWN:
               mouse_x_değeri = event.pos[0]
               mouse_y_değeri = event.pos[1]
               monster_koordinat.x = mouse_x_değeri
               monster_koordinat.y = mouse_y_değeri
               
     #objenin hareketi esnasında  yenisi oluşturulurken  eski obje silinsin. tekrarı engeller.               
     window.fill((0,0,0))              
     #obje belirtilen kordinata yerleştirildi 
     window.blit(monster,monster_koordinat)
     #pencere sürekli güncellensin
     pygame.display.update()
     
               
               
pygame.quit()