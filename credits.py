import pygame, random, help, juego


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
    l2 = mifuente2.render("Como estudiantes de primer semestre de Matemáticas aplicadas y ciencias de", 0, (255, 255, 255))
    l3 = mifuente2.render("la computación de la escuela de ingeniería, ciencia y tecnología de la universidad del rosario,", 0, (255, 255, 255))
    l4 = mifuente2.render("decidimos hacer este juego como proyecto para el curso de programación de computadores.", 0, (255, 255, 255))

    class button:
        def __init__(self, position, size, clr=[100, 100, 100], cngclr=None, func=None, text='', font='', font_size=0,
                     font_clr=()):
            self.clr = clr
            self.size = size
            self.func = func
            self.surf = pygame.Surface(size)
            self.rect = self.surf.get_rect(center=position)

            if cngclr:
                self.cngclr = cngclr
            else:
                self.cngclr = clr

            if len(clr) == 4:
                self.surf.set_alpha(clr[3])

            self.font = pygame.font.SysFont(font, font_size)
            self.txt = text
            self.font_clr = font_clr
            self.txt_surf = self.font.render(self.txt, 1, self.font_clr)
            self.txt_rect = self.txt_surf.get_rect(center=[wh // 2 for wh in self.size])

        def draw(self, screen):
            self.mouseover()

            self.surf.fill(self.curclr)
            self.surf.blit(self.txt_surf, self.txt_rect)
            screen.blit(self.surf, self.rect)

        def mouseover(self):
            self.curclr = self.clr
            pos = pygame.mouse.get_pos()
            if self.rect.collidepoint(pos):
                self.curclr = self.cngclr

        def call_back(self, *args):
            if self.func:
                return self.func(*args)


    def fnmb():


        # estrellas
        coor_list = []
        for lo in range(50):
            x_e = random.randint(0, 2000)
            y_e = random.randint(0, 2000)
            coor_list.append([x_e, y_e])

        class button:
            def __init__(self, position, size, clr=[100, 100, 100], cngclr=None, func=None, text='', font='',font_size=0, font_clr=()):  # atributos del botón
                self.clr = clr
                self.size = size
                self.func = func
                self.surf = pygame.Surface(size)
                self.rect = self.surf.get_rect(center=position)

                if cngclr:
                    self.cngclr = cngclr
                else:
                    self.cngclr = clr

                if len(clr) == 4:
                    self.surf.set_alpha(clr[3])

                self.font = pygame.font.SysFont(font, font_size)
                self.txt = text
                self.font_clr = font_clr
                self.txt_surf = self.font.render(self.txt, 1, self.font_clr)
                self.txt_rect = self.txt_surf.get_rect(center=[wh // 2 for wh in self.size])

            def draw(self, screen):
                self.mouseover()

                self.surf.fill(self.curclr)
                self.surf.blit(self.txt_surf, self.txt_rect)
                screen.blit(self.surf, self.rect)

            def mouseover(
                self):  # para saber la ubicación del mouse y así el botón pueda cambiar de color cuando el mouse esté ensima de el
                self.curclr = self.clr
                pos = pygame.mouse.get_pos()
                if self.rect.collidepoint(pos):
                    self.curclr = self.cngclr

            def call_back(self, *args):
                if self.func:
                    return self.func(*args)

        class text:
            def __init__(self, msg, position, clr=[100, 100, 100], font="Segoe Print", font_size=15, mid=False):
                self.position = position
                self.font = pygame.font.SysFont(font, font_size)
                self.txt_surf = self.font.render(msg, 1, clr)

                if len(clr) == 4:
                    self.txt_surf.set_alpha(clr[3])

                if mid:
                    self.position = self.txt_surf.get_rect(center=position)

            def draw(self, screen):
                screen.blit(self.txt_surf, self.position)

        # call back funciones
        def fn1():
            juego.init()  # abre la ventana del juego
            pygame.quit()

        def fn2():
            help.init()  # abre la ventana de ayuda
            pygame.quit()

        def fn3():
            pygame.quit()  # hace que se cierre la ventana

        def fn4():
            print("welcome to the game")

        def fn5():
            credits.init()
            pygame.quit()

        pygame.init()
        screen_size = (1500, 1000)
        size = 10
        clr = [255, 255, 0]
        black = (0, 0, 0)
        white = (255, 255, 255)
        font_size = 15
        font = pygame.font.Font(None, font_size)
        clock = pygame.time.Clock()

        screen = pygame.display.set_mode(screen_size)

        pygame.mixer.music.load("hylt.wav")
        pygame.mixer.music.play(2)

        button1 = button(position=(750, 800 / 2), size=(140, 45), clr=(255, 255, 255), cngclr=(255, 255, 0),
                             func=fn1, text='Play', font="segoeprint", font_size=35, font_clr=(0, 0, 0))
        button2 = button((750, 1050 / 2), (140, 45), (255, 255, 255), (255, 255, 0), fn2, 'Help', font="segoeprint",
                             font_size=35, font_clr=(0, 0, 0))
        button3 = button((750, 1300 / 2), (140, 45), (255, 255, 255), (255, 255, 0), fn5, 'Credits',
                             font="segoeprint", font_size=35, font_clr=(0, 0, 0))
        button4 = button((750, 1550 / 2), (140, 45), (255, 255, 255), (255, 255, 0), fn3, 'Exit', font="segoeprint",
                             font_size=35, font_clr=(0, 0, 0))
        Title = button((750, 160), (1500, 80), (0, 0, 0), (0, 0, 0), fn4, 'Going thought the shadow',
                           font="sourcecodeproblack", font_size=72, font_clr=(255, 255, 0))

        button_list = [button1, button2, button4, button3, Title]

        crash = True
        while crash:
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    crash = False
                elif event.type == pygame.KEYDOWN:
                    if event.key == pygame.K_ESCAPE:
                        crash = False

                elif event.type == pygame.MOUSEBUTTONDOWN:
                    if event.button == 1:
                        pos = pygame.mouse.get_pos()
                        for b in button_list:
                            if b.rect.collidepoint(pos):
                                b.call_back()

            screen.fill(black)

            for b in button_list:
                b.draw(screen)

            # animación estrallas
            for coord in coor_list:
                x_e = coord[0]
                y_e = coord[1]
                pygame.draw.circle(screen, white, (x_e, y_e), 2)
                coord[1] += 1
                if coord[1] > 1000:
                    coord[1] = 0

            pygame.display.flip()
            clock.tick(60)





    backbutton = button(position=(750, 880), size=(140, 45), clr=(255, 255, 255), cngclr=(255, 255, 0), func=fnmb, text='Back', font = "segoeprint", font_size=35, font_clr = (0, 0, 0))
    list = [backbutton]



    game_over = True
    while game_over:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                game_over = False
            elif event.type == pygame.KEYDOWN:
                if event.key == pygame.K_ESCAPE:
                    game_over = False
            elif event.type == pygame.MOUSEBUTTONDOWN:
                if event.button == 1:
                    pos = pygame.mouse.get_pos()
                    for b in list:
                        if b.rect.collidepoint(pos):
                            b.call_back()



        screen.fill(black)


        for b in list:
            b.draw(screen)


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
