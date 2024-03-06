import pygame
from settings import *


class Overlay:
  def __init__(self, player):
    
    # Configuración general
    self.superficie_pantalla = pygame.display.get_surface()
    self.player = player

    ruta_ovealy = './graphics/overlay/'

    self.herramientas_superficies = {herramienta:pygame.image.load(f'{ruta_ovealy}{herramienta}.png').convert_alpha() for herramienta in player.herramientas}    
    self.semillas_superficies = {semilla:pygame.image.load(f'{ruta_ovealy}{semilla}.png').convert_alpha() for semilla in player.semillas}    
    #print(self.herramientas_superficies)
    #print(self.semillas_superficies)

  def display(self):
    # Mostrar overlay herramientas
    herramienta_superficie = self.herramientas_superficies[self.player.herramienta_seleccionada]
    herramienta_rect = herramienta_superficie.get_rect(midbottom = POSICION_OVERLAY['herramientas'])  
    
    self.superficie_pantalla.blit(herramienta_superficie, herramienta_rect)

    
    
    # Mostrar overlay semillas
    semilla_superficie = self.semillas_superficies[self.player.semilla_seleccionada]
    semilla_rect = semilla_superficie.get_rect(midbottom = POSICION_OVERLAY['semillas'])  
    
    self.superficie_pantalla.blit(semilla_superficie, semilla_rect)
