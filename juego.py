import pygame, random,final

#Definir colores
def init():
	GRAY         = (100, 100, 100)
	NAVYBLUE     = ( 60,  60, 100)
	WHITE        = (255, 255, 255)
	RED          = (255,   0,   0)
	GREEN        = (  0, 255,   0)
	FOREST_GREEN = ( 31, 162,  35)
	BLUE         = (  0,   0, 255)
	SKY_BLUE     = ( 39, 145, 251)
	YELLOW       = (255, 255,   0)
	ORANGE       = (255, 128,   0)
	PURPLE       = (255,   0, 255)
	CYAN         = (  0, 255, 255)
	BLACK        = (  0,   0,   0)
	NEAR_BLACK    = ( 19,  15,  48)
	COMBLUE      = (233, 232, 255)
	GOLD         = (255, 215,   0)

	class Shadow(pygame.sprite.Sprite): #Subclase de la clase Sprite
		def __init__(self): #Se inicializa la clase
			super().__init__() #Se inicializa la superclase
			self.image = pygame.image.load("nube_negra.png").convert() #Se carga la imagen
			self.image.set_colorkey(WHITE) #Le quita el fondo blanco
			self.rect = self.image.get_rect() #Se obtienen las coordenadas de la clase(imagen), es decir posicionar el sprite

	class Six(pygame.sprite.Sprite): #llamar el sprite
		def __init__(self): #inicializar la clase
			super().__init__() # inicializar la superclase para sprite
			self.image = pygame.image.load("Six.png").convert() #Se carga la imagen
			self.image.set_colorkey(WHITE) #Le quita el fondo blanco
			self.rect = self.image.get_rect() #Se obtienen las cooredenadas de la imagen
			self.speed_x = 0 #Se define la velocidad de x
			self.speed_y = 0 #Se define la velocidad en y

		def changespeed(self, x): #Metodo para cambiar la velocidad
			self.speed_x += x #Se va aumentando la x

		def update(self):
			self.rect.x += self.speed_x #Se va a ir aumentando la velocidad en x
			six.rect.y = 900 #Se define en que coordenada esta

	class Rayo(pygame.sprite.Sprite):
		def __init__(self):
			super().__init__()
			self.image = pygame.image.load("rayo_oscuro.png").convert()
			self.rect = self.image.get_rect()

		def update(self):
			self.rect.y -= 4


	pygame.init() #Inicializar la libreria de pygame

	#Crear ventana
	SCREEN_WIDTH = 1500
	SCREEN_HEIGHT = 1000
	screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
	clock = pygame.time.Clock() #Controlar los frames por second
	done = False
	score = 0 #marcador

	shadow_list = pygame.sprite.Group() #la lista almacena las instancias del for
	all_sprite_list = pygame.sprite.Group() #La lista contiene los sprites
	rayo_list = pygame.sprite.Group()

	for i in range(50): #Se crean 50 meteoros
		shadow = Shadow()
		shadow.rect.x = random.randrange(SCREEN_WIDTH - 40)  #Se posicionan aleatoriamente en el ancho -40
		shadow.rect.y = random.randrange(450) #Se posicionan aleatoriamente el alto de 450

		# Se agregan elementos a la lista
		shadow_list.add(shadow)
		all_sprite_list.add(shadow)

	six = Six()
	all_sprite_list.add(six) #agregamos al personaje a la lista para que luego se dibuje en pantalla

	pygame.mixer.music.load('fondo_sound.wav')
	pygame.mixer.music.play(5)

	sound = pygame.mixer.Sound("rayo.wav")

	#Crear bucle principal
	while not done:
		for event in pygame.event.get(): #Se rastrean los eventos, se registra lo que sucede en la ventana
			if event.type == pygame.QUIT: #Es para cerrar la ventana
				done = True

			#Eventos teclado
			if event.type == pygame.KEYDOWN: #Detectar si una tecla fue oprimida
				if event.key == pygame.K_LEFT: #Si la tecla es:
					six.changespeed(-3) #Se va hacia la izquierda
				if event.key == pygame.K_RIGHT: #Si se oprime la tecla se:
					six.changespeed(3) #Se va a la derecha
				if event.key == pygame.K_SPACE: #Si se oprime la tecla espacio
					rayo = Rayo()
					rayo.rect.x = six.rect.x + 45
					rayo.rect.y = six.rect.y - 20

					rayo_list.add(rayo)
					all_sprite_list.add(rayo)
					sound.play()

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					six.changespeed(3)
				if event.key == pygame.K_RIGHT:
					six.changespeed(-3)

		all_sprite_list.update()

		for rayo in rayo_list:
			shadow_hit_list = pygame.sprite.spritecollide(rayo, shadow_list, True) #La lista almacena los elementos que hayan tocado el rayo
			for shadow in shadow_hit_list:
				all_sprite_list.remove(rayo)
				rayo_list.remove(rayo)
				score += 1 #Se incrementa el marcador, cada vez que la nube toca con el rayo
				print(score)
				if score == 50: #Si el marcador llega a 50
					final.init() #Se abre final.py
					pygame.quit()

			if rayo.rect.y < -10:
				all_sprite_list.remove(rayo)
				rayo_list.remove(rayo)

		screen.fill([255, 255, 255])

		all_sprite_list.draw(screen) #Parametro para dibujar las imagenes en la ventana

		pygame.display.flip() #Actualizar la pantalla
		clock.tick(60) #velocidad del objeto

	pygame.quit()
