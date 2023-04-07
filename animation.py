import pygame
import random

#classe qui va s'occuper des animations
class  AnimateSprite(pygame.sprite.Sprite):
    #d&finir les choses a faire a la creaton de l'entité
    def __init__(self, sprite_name, size=(200, 200)):
        super().__init__()
        self.size = size
        self.image = pygame.image.load(f'assets/assets/{sprite_name}.png')
        self.image = pygame.transform.scale(self.image, size)
        self.current_image = 0  #commencer l'anim a l'image 0
        self.images = animations.get(sprite_name)
        self.animation = False

    #définir une methode pour démarrrer l'animation
    def start_animation(self):
        self.animation = True

    # définir une methode pour animer le sprite
    def animate(self, loop=False):
        #verifier si l'annim est active
        if self.animation:


            #passer à l'image sivante
            self.current_image += random.randint(0, 1)

            #vérifier si on a atteint la fin de l'animation
            if self.current_image >= len(self.images):
                #remettre l'animation au depart
                self.current_image = 0
                #desactivation de l'animation
                self.animation = False
                #verifier si l'animation n'est pas en mode boucle
                if loop is True:
                    self.animation = True

        #mmodifier l'image précedeente par la suivante
        self.image = self.images[self.current_image]
        self.image = pygame.transform.scale(self.image, self.size)


    #définir une focntion pour charger les images d'un sprite
def load_animation_images(sprite_name):
    #charger les 24 images
    images =[]
    #récuprer le chemin du dossier pour ce sprite
    path =f'assets/assets/{sprite_name}/{sprite_name}'

        #charger de boucler sur chaque fichier et image dans ce dossier
    for num in range(1, 24):
        image_path = path + str(num) + '.png'
        images.append(pygame.image.load(image_path))

        #renvoyer le contenu de la liste d'image

    return images




#définir un dictionnaire qui va contenir les images chargées de chaque sprite
animations = {
    'mummy' : load_animation_images('mummy'),
    'player': load_animation_images('player'),
    'alien' : load_animation_images('alien')
}


