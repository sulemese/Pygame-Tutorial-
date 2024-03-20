import pygame
pygame.init()

#pencere oluşturur
window  = pygame.display.set_mode((800,800))

#ses efektlerini tanımlama
jump = pygame.mixer.Sound("C:/Users/şule meşe/Downloads/cartoon-jump-6462.mp3")
loss = pygame.mixer.Sound("C:/Users/şule meşe/Downloads/080205_life-lost-game-over-89697.mp3")

#ses efektini çalıştırma
jump.play()
pygame.time.delay(1000) #time ayarlanarak sesler arasında zaman aralığı oluşturur.
loss.play()

#arka plan müziği tanımlandı 
pygame.mixer.music.load("C:/Users/şule meşe/Downloads/game-music-7408.mp3")

#arka plan müziğini çalıştırma (-1 değeri oyun bitene kadar müziği çaldırır.)
pygame.mixer.music.play(-1)


#pencere olayları
durum = True
while durum:
     for event in pygame.event.get():
          if event.type == pygame.QUIT:
               durum=False
               
pygame.quit()