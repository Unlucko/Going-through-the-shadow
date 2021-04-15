import pygame, sys
pygame.init()

# Definir colores
BLACK  = (   0,   0,   0)
WHITE  = ( 255, 255, 255)
GREEN  = (   0, 255,   0)
RED    = ( 255,   0,   0)
BLUE   = (   0,   0, 255)

size = (800, 500)

# Crear ventana
screen = pygame.display.set_mode(size)


while True:
	for event in pygame.event.get():
		if event.type == pygame.QUIT:
			sys.exit()

	# Camviar color del fondo
	screen.fill(WHITE)
	###----- ZONA DE DIBUJO
	pygame.draw.line(screen, GREEN, [0, 100], [200, 300], 5)
	pygame.draw.rect(screen, BLACK, (100,100, 80, 80))


	###----- ZONA DE DIBUJO
	# Actualizar pantalle
	pygame.display.flip()