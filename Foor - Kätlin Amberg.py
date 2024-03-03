import pygame #Pygame import, mis võimaldab luua mänge ja graafikat
import sys #Sys import, mis annab ligipääsu süsteemi funktsioonidele

# Pygame initsialisitoon
pygame.init()

# Järgnevad funktsioonid seadistavad ekraani
ekraani_laius, ekraani_korgus = 300, 300 #Ekraani kõrguse ja laiuse määramine 
ekraan = pygame.display.set_mode((ekraani_laius, ekraani_korgus), pygame.RESIZABLE) #Ekraani objekti loomine
pygame.display.set_caption("Foor - Kätlin Amberg") #Akna pealkirja määramine

# Värvide määramine
MUST = (0, 0, 0)
HALL = (100, 100, 100)
PUNANE = (255, 0, 0)
KOLLANE = (255, 255, 0)
ROHELINE = (0, 255, 0)

# Ristküliku mõõtmed ja asukoht
ristkylik_laius, ristkylik_korgus = 100, 250 #Ristküliku laiuse ja kõrguse määramine
ristkylik_x = (ekraani_laius - ristkylik_laius) // 2 #Ristküliku X-koordinaadi arvutamine selleks, et see oleks ekraani keskel
ristkylik_y = (ekraani_korgus - ristkylik_korgus) // 2 #Ristküliku Y-koordinaadi arvutamine selleks, et see oleks ekraani keskel

# Joonistame ristküliku
ekraan.fill(MUST)  # Täidame ekraani musta värviga
pygame.draw.rect(ekraan, HALL, (ristkylik_x, ristkylik_y, ristkylik_laius, ristkylik_korgus), 2) #Piirjoone värvi määramine ja mõõtmete lisamine

# Ringide mõõtmed ja asukoht
ringi_raadius = 38 #ringi raadiuse määramine
ringi_x = ristkylik_x + ristkylik_laius // 2 #Ringi X-koordinaadi arvutamine selleks, et ringid oleksid ristküliku keskel

# Punase ring joonistamine
pygame.draw.circle(ekraan, PUNANE, (ringi_x, ristkylik_y + 43), ringi_raadius)
# Kollase ringi joonistamine
pygame.draw.circle(ekraan, KOLLANE, (ringi_x, ristkylik_y + ristkylik_korgus // 2), ringi_raadius)
# Rohelise ringi joonistamine
pygame.draw.circle(ekraan, ROHELINE, (ringi_x, ristkylik_y + ristkylik_korgus - 43), ringi_raadius)

pygame.display.flip()  # Ekraani värskendus selleks, et joonistused oleksid nähtavad

# Sündmuste tsükkel
jookseb = True
while jookseb: #Tsükkel kestab seni, kuni jookseb muutuja True
    for sündmus in pygame.event.get(): #Kõikide sündmuste järjestikkune läbi käimine
        if sündmus.type == pygame.QUIT: #QUIT puhul akna sulgemine
            jookseb = False #Muutuja ''jookseb'' väärtuse määramine

# Pygame'i ja programmi lõpetamine
pygame.quit()
sys.exit()

