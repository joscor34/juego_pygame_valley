import pygame
from settings import *
from support import *
from mytimer import Timer

class Player(pygame.sprite.Sprite):
  def __init__(self, pos, group):
    super().__init__(group)

    self.import_assets()

    self.status = 'down_idle'
    self.frame_index = 0
    # Se configuran las propiedades de nuestro personaje
    self.image = self.animations[self.status][self.frame_index]
    #self.image.fill('black')
    self.rect = self.image.get_rect(center = pos)

    # Configuración para el movimiento
    self.direction = pygame.math.Vector2()
    self.pos = pygame.math.Vector2(self.rect.center)
    self.speed = 350

    # Configuración temporizadores
    self.timers = {
      'uso herramienta': Timer(600, self.usar_herramienta),
      'cambio herramienta': Timer(500),
      'uso semilla': Timer(600, self.usar_semilla),
      'cambio semilla': Timer(500)
    }

    # Variables para uso de herramienta
    self.herramientas = ['axe', 'hoe', 'water']
    self.index_herramienta = 0
    self.herramienta_seleccionada = self.herramientas[self.index_herramienta]
    
    # Variables para el uso de semillas
    self.semillas = ['corn', 'tomato']
    self.index_semillas = 0
    self.semilla_seleccionada = self.semillas[self.index_semillas]


  def usar_herramienta(self):
    print(self.herramienta_seleccionada)

  def usar_semilla(self):
    pass
   
  def import_assets(self):
    self.animations = {'up':[], 'down': [], 'left':[], 'right':[],
                       'up_idle': [], 'down_idle': [], 'left_idle':[], 'right_idle':[],
                       'up_axe': [], 'down_axe': [], 'left_axe':[], 'right_axe':[],
                       'up_hoe': [], 'down_hoe': [], 'left_hoe':[], 'right_hoe':[],
                       'up_water': [], 'down_water': [], 'left_water':[], 'right_water':[],
                      }

    for animation in self.animations.keys():
      ruta_completa = './graphics/character/' + animation

      self.animations[animation] = import_folder(ruta_completa)
    

  def animate(self, dt):
    self.frame_index += 4 * dt
    if self.frame_index >= len(self.animations[self.status]):
      self.frame_index = 0

    self.image = self.animations[self.status][int(self.frame_index)]


  def input(self):

    keys = pygame.key.get_pressed()

    #if not self.timers['uso herramienta'].activate:
      # Movimiento vertical
      # --------------------------------------
    
    if not self.timers['uso herramienta'].activo:

      if keys[pygame.K_w]:
        self.direction.y = -1
        self.status = 'up'

      elif keys[pygame.K_s]:
        self.direction.y = 1
        self.status = 'down'

      else:
        self.direction.y = 0
      # Movimiento Horizontal
      # --------------------------------------
      if keys[pygame.K_a]:
        self.direction.x = -1
        self.status = 'left'

      elif keys[pygame.K_d]:
        self.direction.x = 1
        self.status = 'right'

      else:
        self.direction.x = 0
      # --------------------------------------

      #Uso de la herramienta
      # --------------------------------------
      if keys[pygame.K_f]:
        self.timers['uso herramienta'].activate()
        self.direction = pygame.math.Vector2()
        self.frame_index = 1

      if keys[pygame.K_e] and not self.timers['cambio herramienta'].activo:
        self.timers['cambio herramienta'].activate()
        self.index_herramienta += 1

        # Comparador que se encargar de reasignar el valor del index a 0 cuando llega a su límite.
        if self.index_herramienta >= len(self.herramientas):
          self.index_herramienta = 0

        self.herramienta_seleccionada = self.herramientas[self.index_herramienta]

      # Uso de las semillas
      #---------------------------------------
      # Planta semillas
      if keys[pygame.K_h]:
        self.timers['uso semilla'].activate()
        self.direction = pygame.math.Vector2()
        self.frame_index = 0
        print(f'Se planto una semilla de: {self.semilla_seleccionada}')

      # Cambiar semillas
      if keys[pygame.K_1] and not self.timers['cambio semilla'].activo:
        self.timers['cambio semilla'].activate()
        self.index_semillas = 0
        self.semilla_seleccionada = self.semillas[self.index_semillas]


      if keys[pygame.K_2] and not self.timers['cambio semilla'].activo:
        self.timers['cambio semilla'].activate()
        self.index_semillas = 1
        self.semilla_seleccionada = self.semillas[self.index_semillas]

  def actualizar_timers(self):
    for timer in self.timers.values():
      timer.update()


  def get_status(self):

    # Si mi personaje no se está desplazando
    if  self.direction.magnitude() == 0:
      self.status = self.status.split('_')[0] + '_idle'

    if self.timers['uso herramienta'].activo:
      self.status = self.status.split('_')[0] + '_' + self.herramienta_seleccionada



    #if self.timers['uso herramienta'].activate:
    #  self.status = self.status.split('_')[0] + '_' + self.herramienta_seleccionada

  
  def move(self, dt):

    # Se hace la normalización de nuestros vectores de movimiento
    if self.direction.magnitude() > 0:
      self.direction = self.direction.normalize()

    # Movimiento horizontal
    self.pos.x += self.direction.x * self.speed * dt
    self.rect.centerx = self.pos.x

    # Movimiento vertical
    self.pos.y += self.direction.y * self.speed * dt
    self.rect.centery = self.pos.y

  def update(self, dt):
    self.input()
    self.get_status()
    self.actualizar_timers()
    self.move(dt)
    self.animate(dt) 
