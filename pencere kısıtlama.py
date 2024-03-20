import pygame
pygame.init()

#sabitler 
window_width=800
window_height=800
speed = 5 
fps = 60



#hareketlerin daha akıcı olması için fps ayarlayacağız. bu nedenle clock tanımladık. 
clock = pygame.time.Clock()

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
     
     #and bağlaçları objenin pencere sınırları içinden çıkmaması için tanımlanmıştır.     
     tuş = pygame.key.get_pressed()
     if tuş[pygame.K_LEFT] and monster_koordinat.left>0 : 
          monster_koordinat.x -= speed
     if tuş[pygame.K_RIGHT] and monster_koordinat.right<window_width:
          monster_koordinat.x += speed
     if tuş[pygame.K_UP] and monster_koordinat.top>0:
          monster_koordinat.y -= speed
     if tuş[pygame.K_DOWN] and monster_koordinat.bottom<window_height:
          monster_koordinat.y += speed
               
     #objenin hareketi esnasında  yenisi oluşturulurken  eski obje silinsin. tekrarı engeller.               
     window.fill((0,0,0))              
     #obje belirtilen kordinata yerleştirildi 
     window.blit(monster,monster_koordinat)
     #pencere sürekli güncellensin
     pygame.display.update()
     
     #fps ayarı için (frame per second)
     clock.tick(fps)
               
               
pygame.quit()