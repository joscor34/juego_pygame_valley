import pygame
from player import Player
from overlay import Overlay
from generic import Generic
from settings import *

class Level():
  def __init__(self):

    # Se crea la superficie de nuestra pantalla
    self.display_surface = pygame.display.get_surface()

    # Creamos un grupo con todos los sprites del nivel
    self.all_sprites = CameraGroup()

    # Configuramos el jugador
    self.setup()
    
    # Creamos un overlay específico para cada jugador
    self.overlay = Overlay(self.player)
  

  def setup(self):

    terreno = pygame.image.load('./graphics/world/ground.png').convert_alpha()

    Generic(pos=(0,0), surf=terreno, groups = self.all_sprites)

    self.player = Player((250, 250), self.all_sprites)


    
    


  def run(self, dt):

    self.display_surface.fill('black')

    # Se dibujan nuestros sprites en toda la superficie de la pantalla
    self.all_sprites.customize_draw(self.player)

    # Actualizamos esos sprites
    self.all_sprites.update(dt)

    # Mostrar el overlay
    self.overlay.display()

class CameraGroup(pygame.sprite.Group):
  def __init__(self):
    super().__init__()
    self.display_surface = pygame.display.get_surface()
    self.offset = pygame.math.Vector2()
  
  def customize_draw(self, player):
    self.offset.x = player.rect.centerx - VENTANA_LARGO / 2
    self.offset.y = player.rect.centery - VENTANA_ANCHO / 2

    for sprite in self.sprites():
      offset_rect = sprite.rect.copy()
      offset_rect.center -= self.offset

      self.display_surface.blit(sprite.image, offset_rect)

