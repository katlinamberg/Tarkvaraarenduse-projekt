import pygame
import sys

def joonista_ruudud(ekraan, ruudu_suurus, read, veerud, joone_varv):
    for rida in range(read):
        for veerg in range(veerud):
            x = veerg * ruudu_suurus
            y = rida * ruudu_suurus
            pygame.draw.rect(ekraan, joone_varv, (x, y, ruudu_suurus, ruudu_suurus), 1)

def main():
    pygame.init()

    # Ekraani seaded
    ekraani_laius, ekraani_korgus = 640, 480
    ekraan = pygame.display.set_mode([ekraani_laius, ekraani_korgus])
    pygame.display.set_caption("Ruudustik")

    # Parameetrid ruutude joonistamiseks
    ruudu_suurus = 20
    read = 24
    veerud = 32
    tausta_varv = (144, 238, 144)  # Heledam roheline taustavärv
    joone_varv = (255, 0, 0)       # Punane joonevärv

    # Mängutsükkel
    jookseb = True
    while jookseb:
        for sündmus in pygame.event.get():
            if sündmus.type == pygame.QUIT:
                jookseb = False

        # Tausta joonistamine
        ekraan.fill(tausta_varv)

        # Ruutude joonistamine
        joonista_ruudud(ekraan, ruudu_suurus, read, veerud, joone_varv)

        pygame.display.flip()

    # Lõpetamine
    pygame.quit()
    sys.exit()

if __name__ == "__main__":
    main()
