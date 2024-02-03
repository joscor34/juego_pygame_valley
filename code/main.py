import pygame, sys # Importamos pygame y sys
from level import Level
# Comentario de prueba

# Creamos una clase la cual contendrá nuestro juego
class Game:

  # Creamos un método mágico para inicializar nuestros atributos
  def __init__(self):
    pygame.init() # Iniciamos pygame
    self.screen = pygame.display.set_mode((500,500)) # Le decimos a pygame que tendrá una ventana de 128x128
    self.clock = pygame.time.Clock() # Creamos un reloj interno

    self.level = Level()

  def ejecutar(self):
    while True:
      # Es ciclo recorre cada pulsación que haga el usuario
      for evento in pygame.event.get():
        # Si la pulsación coincide con el evento QUIT
        if evento.type == pygame.QUIT:
          # Le decimos a pygame que finalice
          pygame.quit()
          # Cerramos la ventaja que nos genere
          sys.exit()
      
      dt = self.clock.tick() / 1000
      pygame.display.update()

      self.level.run(dt)

# Se crea una instancia de Game
game = Game()

# Ejecutamos el método "ejecutar"
game.ejecutar()

