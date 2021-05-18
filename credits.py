import pygame, random


def init():
    pygame.init()
    sz = (1500, 1000)
    black = (0, 0, 0)
    white = (255, 255, 255)
    screen = pygame.display.set_mode(sz)
    clock = pygame.time.Clock()

    coor_list = []
    for lo in range(50):
        x_e = random.randint(0, 2000)
        y_e = random.randint(0, 2000)
        coor_list.append([x_e, y_e])

    mifuente = pygame.font.SysFont("sourcecodeproblack", 72)
    mifuente2 = pygame.font.SysFont("segoeprint", 30)
    titulo = mifuente.render("Creadores", 0, (255, 255, 0))
    l1 = mifuente2.render ("Este juego, fue creado por César Segura, Valentina Herrera y Lucía Ardila ya que", 0, (255, 255, 255))
    l2 = mifuente2.render("Como estudiantes de primer semestre de Matemátixcas aplicadas y ciencias de", 0, (255, 255, 255))
    l3 = mifuente2.render("la computación de la escuela de ingeniería, ciencia y tecnología de la universidad del rosario,", 0, (255, 255, 255))
    l4 = mifuente2.render("decidimos hacer este juego como proyecto para el curso de programación de computadores.", 0, (255, 255, 255))

    game_over = False
    while not game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = True

        screen.fill(black)

        # animación estrallas
        for coord in coor_list:
            x_e = coord[0]
            y_e = coord[1]
            pygame.draw.circle(screen, white, (x_e, y_e), 2)
            coord[1] += 1
            if coord[1] > 1000:
                coord[1] = 0
        screen.blit(titulo, (560, 85))
        screen.blit(l1, (130, 300))
        screen.blit(l2, (140, 400))
        screen.blit(l3, (50, 500))
        screen.blit(l4, (60, 600))
        pygame.display.flip()
        clock.tick(60)
