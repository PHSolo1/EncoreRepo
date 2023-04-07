import pygame
import random
#creer une classe pour gérer la comète
from monster import Alien, Mummy


class Comet(pygame.sprite.Sprite):

    def __init__(self, comet_event):
        super().__init__()
        #définir l'image associée de la comète
        self.image = pygame.image.load('assets/assets/comet.png')
        self.rect = self.image.get_rect()
        self.velocity = random.randint(1, 3)
        self.rect.x = random.randint(20, 800)
        self.rect.y = - random.randint(0, 800)
        self.comet_event = comet_event



    def remove(self):
        self.comet_event.all_comets.remove(self)
        #jouer le son
        self.comet_event.game.sound_manager.play('meteorite')
        #verifier si le nombre de comte est 0
        if len(self.comet_event.all_comets) == 0:
            #remettre la barre a 0
            self.comet_event.reset_percent()
            #apparaitre a nouveau les 2 premiers monstres
            self.comet_event.game.start()
    def fall(self):
        self.rect.y += self.velocity
        if self.rect.y >= 550:
        #retirer la boule de feu
            self.remove()

        #si ya plus de bdf sur le jeu

        if len(self.comet_event.all_comets) == 0:
            #evenement fini
            self.comet_event.reset_percent()
            self.comet_event.fall_mod = False

        #verifier si la comet touche le joueur
        if self.comet_event.game.check_collision(self, self.comet_event.game.all_players):
            print("joueur touché")
            self.remove()
            #subir 20 points de degats
            self.comet_event.game.player.damage(20)


