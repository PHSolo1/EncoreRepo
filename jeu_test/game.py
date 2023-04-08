import pygame
from player import Player
from monster import Monster, Mummy, Alien
from comet_event import CometFallEvent
from sounds import SoundManager


class Game:
    def __init__(self):
        #définir si jeu a commencé
        self.is_playing = False
        #génener notre joueur
        self.all_players = pygame.sprite.Group()
        self.player = Player(self)
        self.all_players.add(self.player)
        #génerer l'evenement
        self.comet_event = CometFallEvent(self)
        #groupe monstre
        self.all_monsters = pygame.sprite.Group()
        #gerer le son
        self.sound_manager = SoundManager()
        #mettre le score à 0
        self.font = pygame.font.Font("assets/assets/my_custom_font.ttf", 25)
        self.score = 0
        self.pressed = {}


    def start(self):
        self.is_playing = True
        self.spawn_monster(Mummy)
        self.spawn_monster(Mummy)
        self.spawn_monster(Alien)

    def add_score(self, points):
        self.score += points


    def game_over(self):
        #remettre jeu à neuf
        self.all_monsters = pygame.sprite.Group()
        self.comet_event.all_comets = pygame.sprite.Group()
        self.comet_event.reset_percent()
        self.player.health = self.player.max_health
        self.is_playing = False
        self.score = 0
        self.sound_manager.play('game_over')


    def update (self, screen):
        #afficher le score sur l'écran

        score_text = self.font.render(f"Score : {self.score}", 1 , (0, 0, 0))
        screen.blit(score_text, (20, 20))

        # appliquer image du joueur
        screen.blit(self.player.image, self.player.rect)


        # actualiser la barre de vie du joueur
        self.player.update_health_bar(screen)

        #actualiser la barre d'évenement du jeu
        self.comet_event.update_bar(screen)

        #actualiser l'animation du joueur
        self.player.update_animation()

        # récperer les projectile du joueur *

        for projectile in self.player.all_projectiles:
            projectile.move()
        # récuperer les monstre du jeu
        for monster in self.all_monsters:
            monster.forward()
            monster.update_health_bar(screen)
            monster.update_animation()

        #recuperer les cometes de notre jeu
        for comet in self.comet_event.all_comets :
            comet.fall()

        # appliquer l'ensemble des images de mon groupe de projectile
        self.player.all_projectiles.draw(screen)

        # appliquer ensemble des images de groupe de monstrr
        self.all_monsters.draw(screen)

        #appliquer l'ensemble des image du groupe de comètes
        self.comet_event.all_comets.draw(screen)

        # verifier si le joueur veut aller a gauche ou a droite
        if self.pressed.get(pygame.K_RIGHT) and self.player.rect.x + self.player.rect.width < 1080:
            self.player.mouv_right()
        elif self.pressed.get(pygame.K_LEFT) and self.player.rect.x > 0:
            self.player.mouv_left()


    def check_collision(self, sprite, group):
        return pygame.sprite.spritecollide(sprite, group, False, pygame.sprite.collide_mask)


    def spawn_monster(self, monster_classname):
        self.all_monsters.add(monster_classname.__call__(self))

