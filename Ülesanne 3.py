import pygame #Pygame import, mis võimaldab luua mänge ja funktsioone
import sys #Sys import, mis annab ligipääsu süsteemi funktsioonidele

 #Funktsiooni määramine, mis joonistab ruudustiku ekraanile
def joonista_ruudustik(ekraan, ruudu_kylg, ridade_arv, veergude_arv, ruudu_varv):
    for x in range(0, ekraani_laius, ruudu_kylg): #Tsükkel X-koordinaatide jaoks. Sellega kaetakse kõik veerud ekraanil
        for y in range(0, ekraani_korgus, ruudu_kylg): #Tsükkel Y-koordinaatide jaoks. Sellega kaetakse kõik veerud ekraanil
            pygame.draw.rect(ekraan, ruudu_varv, (x, y, ruudu_kylg, ruudu_kylg), 1) #Ruudu joonistamine

pygame.init() #Pygame alustamine, et saaks funktsioone kasutada

ekraani_laius, ekraani_korgus = 640, 480 #Ekraani kõrgus ja laiuse määramine
screen = pygame.display.set_mode([ekraani_laius, ekraani_korgus]) #Ekraani objekti loomine
pygame.display.set_caption("Harjutamine") #Akna pealkirja määramine

taustavärv = (102, 255, 102) #Taustavärvi määramine
screen.fill(taustavärv) #Ekraani taustaväriga täitmine

ruudu_kylg = 16 #ruudu külje määramine
ruudu_varv = (255, 0, 0) #ruudu värvi määramine

joonista_ruudustik(screen, ruudu_kylg, 40, 40, ruudu_varv) #Ruudustiku joonistamine vastavalt andmetele
pygame.display.flip() #Ekraani värskendus, et joonistused oleksid nähtavad

jookseb = True #True tsükli määramine
while jookseb: #Tsükkel kestab vastavalt järgmistele tingimustele
    for sündmus in pygame.event.get(): #Kõikide südmuste läbikäimine
        if sündmus.type == pygame.QUIT: #Akna sulgemine 
            jookseb = False #Tsükli lõpetamine

pygame.quit() #Pygame petamine
sys.exit() #Programmi töö lõpetamine
