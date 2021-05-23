import pygame, random, help, credits, juego



def init ():

    pygame.init()
    screen_size = (1500, 1000)
    yellow         = [255, 255, 0]
    black       = (0, 0, 0)
    white          = (255, 255, 255)
    clock       = pygame.time.Clock()

    screen      = pygame.display.set_mode(screen_size)


    pygame.mixer.music.load("fondo_sound.wav")
    pygame.mixer.music.play(2)


    # estrellas
    coor_list = []
    for lo in range(50):
        x_e = random.randint(0, 2000)
        y_e = random.randint(0, 2000)
        coor_list.append([x_e, y_e])



    class button:
        def __init__(self, position, size, clr=[100, 100, 100], cngclr=None, func=None, text='', font='', font_size= 0, font_clr = ()): #atributos del botón
            self.clr    = clr
            self.size   = size
            self.func   = func
            self.surf   = pygame.Surface(size)
            self.rect   = self.surf.get_rect(center=position)

            if cngclr:
                self.cngclr = cngclr
            else:
                self.cngclr = clr

            if len(clr) == 4:
                self.surf.set_alpha(clr[3])

            #atributos texto
            self.font = pygame.font.SysFont(font, font_size)
            self.txt = text
            self.font_clr = font_clr
            self.txt_surf = self.font.render(self.txt, 1, self.font_clr)
            self.txt_rect = self.txt_surf.get_rect(center=[wh//2 for wh in self.size])

        def draw(self, screen):
            self.mouseover()

            self.surf.fill(self.curclr)
            self.surf.blit(self.txt_surf, self.txt_rect)
            screen.blit(self.surf, self.rect)

        def mouseover(self): #para saber la ubicación del mouse y así el botón pueda cambiar de color cuando el mouse esté ensima de el
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
        juego.init() #abre la ventana del juego
        pygame.quit()
    def fn2():
        help.init() #abre la ventana de ayuda
        pygame.quit()
    def fn3():
        pygame.quit() #hace que se cierre la ventana
    def fn4():
        credits.init()
        pygame.quit()


    #todos los botones necesarios

    button1 = button(position=(750, 800/2), size=(140, 45), clr=white, cngclr=yellow, func=fn1, text='Play', font = "segoeprint", font_size=35, font_clr = black)
    button2 = button((750, 1050/2), (140, 45), white, yellow, fn2, 'Help', font = "segoeprint", font_size=35, font_clr = black)
    button3 = button((750, 1300 / 2), (140, 45), white, yellow, fn4, 'Credits', font="segoeprint", font_size=35,font_clr=black)
    button4 = button((750, 1550/2), (140, 45), white, yellow, fn3, 'Exit', font = "segoeprint", font_size=35, font_clr = black)


    button_list = [button1, button2, button4, button3]

    Title = button((750, 160), (1500, 80), black, black, fn4, 'Going thought the shadow', font="sourcecodeproblack",font_size=72, font_clr=yellow)
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

        screen.blit (titulo, (250, 160))

        pygame.display.flip()
        clock.tick(60)

#BOE**********************************************************************************************************************

init()
