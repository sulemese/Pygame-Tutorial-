import pygame

pygame.init()

#pencere oluşturuldu
pencere = pygame.display.set_mode((800,680))

#font listesi tanımlandı
font_listesi = pygame.font.get_fonts()

#tüm fontlar listelendi
for font in font_listesi:
     print(font)

#sistem fontu tanımlandı(font adı,font büyüklüğü)
font_ismi = pygame.font.SysFont('consolas',64)

#yazı oluşturuldu (yazılacak yazı,düzeltme yapılsın mı ? , renk)
yazı = font_ismi.render("Hello World",True,(255,0,0))

#yazının koordinatı alındı
yazı_koordinat = yazı.get_rect()

#yazının penceredeki konumu ayarlandı
yazı_koordinat.topleft=(150,150)

#pencere olayları
durum = True
while durum:
     for etkinlik in pygame.event.get():
          if etkinlik.type == pygame.QUIT:
               durum=False
     #yazı pencereye yerleştirildi
     pencere.blit(yazı,yazı_koordinat)
     #pencere sürekli güncellensin
     pygame.display.update()     
         
pygame.quit()
