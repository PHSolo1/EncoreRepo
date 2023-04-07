import pygame
from projectile import Projectile
import animation

class Player(animation.AnimateSprite) :
    def __init__(self, game):
        super().__init__('player')
        self.game = game
        self.health = 100
        self.max_health =100
        self.attack = 20
        self.velocity = 2
        self.all_projectiles = pygame.sprite.Group()
        self.rect =self.image.get_rect()
        self.rect.x = 400                          
        self.rect.y = 500

    def damage(self, amount):
        if self.health - amount > amount:
            self.health -= amount
        else :
            #si le joueur n'a plus de pv
            self.game.game_over()


    def update_animation(self):
        self.animate()

    def update_health_bar(self, surface):

        # déssiner arriere plan
            pygame.draw.rect(surface, (60, 63, 60), [self.rect.x + 50, self.rect.y + 20, self.max_health, 5])

        # déssiner la barre de vie
            pygame.draw.rect(surface, (111, 210, 46), [self.rect.x + 50, self.rect.y + 20, self.health, 5])

    def launch_projectile(self):
        #créer une nvelle instance de la classe projectile
        projectile = Projectile(self)
        self.all_projectiles.add(Projectile(self))
        #jouer le son
        self.game.sound_manager.play('tir')
        #demarrer l'animation du lancé
        self.start_animation()
    def mouv_right(self):
        #si le joueur ne collisionne pas un monstre

        self.rect.x += self.velocity

    def mouv_left(self):
        if not self.game.check_collision(self, self.game.all_monsters):
            self.rect.x -= self.velocity


