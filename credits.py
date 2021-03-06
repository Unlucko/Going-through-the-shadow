import pygame, random, help, juego, credits


def init():


    pygame.init()
    sz      = (1500, 1000)
    yellow = (255, 255, 0)
    black   = (0, 0, 0)
    white   = (255, 255, 255)
    screen  = pygame.display.set_mode(sz)
    clock   = pygame.time.Clock()




    coor_list = []
    for lo in range(50):
        x_e = random.randint(0, 2000)
        y_e = random.randint(0, 2000)
        coor_list.append([x_e, y_e])


    #texto que aparece en pantalla
    mifuente = pygame.font.SysFont("sourcecodeproblack", 72)
    mifuente2 = pygame.font.SysFont("segoeprint", 30)
    titulo = mifuente.render("Creadores", 0, yellow)
    l1 = mifuente2.render ("Este juego, fue creado por César Segura, Valentina Herrera y Lucía Ardila ya que", 0, white)
    l2 = mifuente2.render("Como estudiantes de primer semestre de Matemáticas aplicadas y ciencias de", 0, white)
    l3 = mifuente2.render("la computación de la escuela de ingeniería, ciencia y tecnología de la universidad del rosario,", 0, white)
    l4 = mifuente2.render("decidimos hacer este juego como proyecto para el curso de programación de computadores.", 0, white)


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


    def fnmb(): #abrir la ventana de menú

        pygame.init()
        screen_size = (1500, 1000)
        yellow = [255, 255, 0]
        black = (0, 0, 0)
        white = (255, 255, 255)
        clock = pygame.time.Clock()

        screen = pygame.display.set_mode(screen_size)

        pygame.mixer.music.load("fondo_sound.wav")
        pygame.mixer.music.play(2)

        # estrellas
        coor_list = []
        for lo in range(50):
            x_e = random.randint(0, 2000)
            y_e = random.randint(0, 2000)
            coor_list.append([x_e, y_e])

        class button:
            def __init__(self, position, size, clr=[100, 100, 100], cngclr=None, func=None, text='', font='',
                         font_size=0, font_clr=()):  # atributos del botón
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

                # atributos texto
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

        # call back funciones
        def fn1():
            pygame.mixer.music.load("click.wav")
            pygame.mixer.music.play()
            juego.init()  # abre la ventana del juego
            pygame.quit()

        def fn2():
            help.init()  # abre la ventana de ayuda
            pygame.quit()

        def fn3():
            pygame.quit()  # hace que se cierre la ventana

        def fn4():
            credits.init()
            pygame.quit()

        # todos los botones necesarios

        button1 = button(position=(750, 800 / 2), size=(140, 45), clr=white, cngclr=yellow, func=fn1, text='Play',
                         font="segoeprint", font_size=35, font_clr=black)
        button2 = button((750, 1050 / 2), (140, 45), white, yellow, fn2, 'Help', font="segoeprint", font_size=35,
                         font_clr=black)
        button3 = button((750, 1300 / 2), (140, 45), white, yellow, fn4, 'Credits', font="segoeprint", font_size=35,
                         font_clr=black)
        button4 = button((750, 1550 / 2), (140, 45), white, yellow, fn3, 'Exit', font="segoeprint", font_size=35,
                         font_clr=black)

        button_list = [button1, button2, button4, button3]

        Title = button((750, 160), (1500, 80), black, black, fn4, 'Going thought the shadow', font="sourcecodeproblack",
                       font_size=72, font_clr=yellow)
        mifuente = pygame.font.SysFont("sourcecodeproblack", 72)
        titulo = mifuente.render("Going thought the shadow", 0, yellow)

        sound = pygame.mixer.Sound("click.wav")

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
                        for b in button_list:
                            if b.rect.collidepoint(pos):
                                sound.play()
                                b.call_back()
                                pygame.quit()

            screen.fill(black)

            for b in button_list:
                b.draw(screen)

            # animación estrellas
            for coord in coor_list:
                x_e = coord[0]
                y_e = coord[1]
                pygame.draw.circle(screen, white, (x_e, y_e), 2)
                coord[1] += 1
                if coord[1] > 1000:
                    coord[1] = 0

            screen.blit(titulo, (250, 160))

            pygame.display.flip()
            clock.tick(60)



    #botón de regreso al menú
    backbutton = button(position=(750, 880), size=(140, 45), clr=white, cngclr=yellow, func=fnmb, text='Back', font = "segoeprint", font_size=35, font_clr = black)
    list = [backbutton]

    sound = pygame.mixer.Sound("click.wav")

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
                            sound.play()
                            b.call_back()
                            pygame.quit()



        screen.fill(black)


        for b in list:
            b.draw(screen)


        # animación estrellas
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

