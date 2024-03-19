import pygame

#pygame içinde bulunan paketler başlatılır
pygame.init()


#pencere boyutu ayarlanır
genişlik = 750
yükseklik = 600
#pencere oluşturulur 
pencere = pygame.display.set_mode((genişlik,yükseklik))


#renkler tanımlanır
BEYAZ = (255,255,255)
KIRMIZI = (255,0,0)
YEŞİL = (0,255,0)
MAVİ = (0,0,255)
SARI = (255,255,0)


#çizgi çizdirilir(pencere,renk,başlangıç kordinatı,bitiş kordinatı,kalınlık)
pygame.draw.line(pencere,KIRMIZI,(0,0),(150,250),5)
pygame.draw.line(pencere,BEYAZ,(150,250),(260,350),2)

#daire çizdirilir (pencere,renk,merkez nokta kordinatı,yarıçap,kalınlık)
pygame.draw.circle(pencere,MAVİ,(300,300),155,3)

#içi dolu daire çizdirilir (içi boş ile farkı kalınlık=0 olmasıdır)
pygame.draw.circle(pencere,SARI,(460,25),155,0)

#dikdörtgen çizdirilir (pencere,renk,(başlangıç x noktası , başlangıç y noktası,x genişliği, y genişliği),kalınlık)
pygame.draw.rect(pencere,KIRMIZI,(195,255,100,65),2)

#pencerenin olayları
durum = True
while durum:
     for etkinlik in pygame.event.get():
          if etkinlik.type == pygame.QUIT:
               durum = False
     #pencereyi sürekli günceller
     pygame.display.update()
     
     
               
#Tüm paketler kapatılır              
pygame.quit()
