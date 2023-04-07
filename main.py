import pygame
import math
from game import Game
from player import Player
pygame.init()

#définir unr clock
clock = pygame.time.Clock()
FPS = 60


# génerer la fenêtre du jeu
pygame.display.set_caption("comet fall game")
screen = pygame.display.set_mode((1080, 720))


background = pygame.image.load('assets/assets/bg.jpg')

#charger notre banniere

banner = pygame.image.load("assets/assets/banner.png")
banner = pygame.transform.scale(banner, (500, 500))
banner_rect = banner.get_rect()
banner_rect.x = math.ceil( screen.get_width()/4)


#charger notre bouton play
play_button = pygame.image.load("assets/assets/button.png")
play_button = pygame.transform.scale(play_button,(400, 150))
play_button_rect =play_button.get_rect()
play_button_rect.x = math.ceil( screen.get_width()/3.33)
play_button_rect.y =  math.ceil( screen.get_height()/2)

game = Game()
#charfger nnotre joueur

player = Player(game)
running = True


# boucle tant que condition est vrai
while running:
    # appliquer arrière plan
    screen.blit(background, (0, -200))

    #vérifier si notre jeu a commencé ou non
    if game.is_playing :
            #déclencher les éléments de la maprtie
        game.update(screen)
    #si notre jeu n'a pas commencé
    else:
        #ajouter mon écran de bienvenu

        screen.blit(play_button, play_button_rect)
        screen.blit(banner, (banner_rect))

    # mettre à jour
    pygame.display.flip()
    for event in pygame.event.get():

        # que l'évenement est fermeture de fenêtre
        if event.type == pygame.QUIT:
            running = False
            pygame.quit()
        #detecter si un joueur lache la touche du clvier

        elif event.type == pygame.KEYDOWN:
            game.pressed[event.key] = True

            #détecter si espace est enclenchée pour lancer le projectile
            if event.key == pygame.K_SPACE:
                if game.is_playing:
                    game.player.launch_projectile()
                else:
                    # mettre le jeu en mode lancé en changeant
                    game.start()
                    game.sound_manager.play('click')

        elif event.type == pygame.KEYUP:
            game.pressed[event.key] = False

        elif event.type == pygame.MOUSEBUTTONDOWN:
            #verifer si souris en collision avec le bouton play
            if  play_button_rect.collidepoint(event.pos):
                #mettre le jeu en mode lancé en changeant
                game.start()
                game.sound_manager.play('click')
    #fixer le nombre de fps sur ma clock
        clock.tick(FPS)


