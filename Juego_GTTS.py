import pygame, random,final

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

	class Shadow(pygame.sprite.Sprite):
		def __init__(self):
			super().__init__()
			self.image = pygame.image.load("nube1.png").convert()
			self.image.set_colorkey(WHITE)
			self.rect = self.image.get_rect()

	class Six(pygame.sprite.Sprite): #llamar el sprite
		def __init__(self): #inicializar la clase
			super().__init__() # inicializar la superclase para sprite
			self.image = pygame.image.load("Six.png").convert()
			self.image.set_colorkey(WHITE)
			self.rect = self.image.get_rect()
			self.speed_x = 0
			self.speed_y = 0

		def changespeed(self, x):
			self.speed_x += x

		def update(self):
			self.rect.x += self.speed_x
			six.rect.y = 900

	class Rayo(pygame.sprite.Sprite):
		def __init__(self):
			super().__init__()
			self.image = pygame.image.load("rayo.png").convert()
			self.rect = self.image.get_rect()

		def update(self):
			self.rect.y -= 4


	pygame.init()

	SCREEN_WIDTH = 1500
	SCREEN_HEIGHT = 1000
	screen = pygame.display.set_mode([SCREEN_WIDTH, SCREEN_HEIGHT])
	clock = pygame.time.Clock()
	done = False
	score = 0

	shadow_list = pygame.sprite.Group()
	all_sprite_list = pygame.sprite.Group()
	rayo_list = pygame.sprite.Group()

	for i in range(50):
		shadow = Shadow()
		shadow.rect.x = random.randrange(SCREEN_WIDTH - 40)
		shadow.rect.y = random.randrange(450)


		shadow_list.add(shadow)
		all_sprite_list.add(shadow)

	six = Six()
	all_sprite_list.add(six)

	while not done:
		for event in pygame.event.get():
			if event.type == pygame.QUIT:
				done = True

			if event.type == pygame.KEYDOWN:
				if event.key == pygame.K_LEFT:
					six.changespeed(-3)
				if event.key == pygame.K_RIGHT:
					six.changespeed(3)
				if event.key == pygame.K_SPACE:
					rayo = Rayo()
					rayo.rect.x = six.rect.x + 45
					rayo.rect.y = six.rect.y - 20

					rayo_list.add(rayo)
					all_sprite_list.add(rayo)

			if event.type == pygame.KEYUP:
				if event.key == pygame.K_LEFT:
					six.changespeed(3)
				if event.key == pygame.K_RIGHT:
					six.changespeed(-3)

		all_sprite_list.update()

		for rayo in rayo_list:
			shadow_hit_list = pygame.sprite.spritecollide(rayo, shadow_list, True)
			for shadow in shadow_hit_list:
				all_sprite_list.remove(rayo)
				rayo_list.remove(rayo)
				score += 1
				print(score)
				if score == 50:
					final.init()
					pygame.quit()

			if rayo.rect.y < -10:
				all_sprite_list.remove(rayo)
				rayo_list.remove(rayo)

		screen.fill([255, 255, 255])

		all_sprite_list.draw(screen)

		pygame.display.flip()
		clock.tick(60)

	pygame.quit()

