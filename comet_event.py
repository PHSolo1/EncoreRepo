import pygame
from comet import Comet

#creer une classe pour gerer cette evenement a intervalle régulier

class CometFallEvent:

    #lors du chargement : creer un compteur
    def __init__(self, game):
        self.percent = 0
        self.percent_speed = 7
        self.game = game
        self.fall_mod = False

    #définir un groupe de sprite pour stocker nos cometes
        self.all_comets =pygame.sprite.Group()

    def add_percent(self):
        self.percent += self.percent_speed / 100

    def is_full_loaded(self):
        return self.percent >= 100

    def reset_percent(self):
        self.percent = 0

    def meteor_fall(self):
        #BOUCLE POUR LES VALEURS ENTRE 1 ET 10
        for i in range (1, 14):
        #apparaitre une premiere boule de feu
            self.all_comets.add(Comet(self))

    def attempt_fall(self):
        #la jauge d'évenement est totalement chargée
        if self.is_full_loaded() and len(self.game.all_monsters) == 0:
            self.meteor_fall()

            self.fall_mod = True #activer l'évenement

    def update_bar(self, surface):

        #ajouter du pourcentage a la barre
        self.add_percent()



        #barre noir (arriere plan)
        pygame.draw.rect(surface,   (0, 0, 0), [
            0,
            surface.get_height()-20,
            surface.get_width(),
            10
        ])
        #barre rouge (jauge d'évenement)
        pygame.draw.rect(surface, (187, 11, 11), [
            0,  # l'axe des x
            surface.get_height()-20,
            surface.get_width()/100*self.percent,
            10
        ])

