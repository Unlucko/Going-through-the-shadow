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
    msg = mifuente.render("Ganaste!!!", 0, (255, 255, 0))



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

        screen.blit(msg, (550, 450))

        pygame.display.flip()
        clock.tick(60)