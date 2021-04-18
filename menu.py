import pygame, random

# estrellas
coor_list = []
for lo in range(50):
    x_e = random.randint(0, 2000)
    y_e = random.randint(0, 2000)
    coor_list.append([x_e, y_e])



class button:
    def __init__(self, position, size, clr=[100, 100, 100], cngclr=None, func=None, text='', font='', font_size= 0, font_clr = ()):
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

    def mouseover(self):
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


# call back functions
def fn1():
    print('click')
def fn2():
    print('the player needs help')
def fn3():
    print ("Goodbye")
def fn4():
    print ("welcome to the game")



if __name__ == '__main__':
    pygame.init()
    screen_size = (1500, 1000)
    size        = 10
    clr         = [255, 255, 0]
    black       = (0, 0, 0)
    white          = (255, 255, 255)
    font_size   = 15
    font        = pygame.font.Font(None, font_size)
    clock       = pygame.time.Clock()

    screen    = pygame.display.set_mode(screen_size)




    button1 = button(position=(750, 800/2), size=(140, 45), clr=(255, 255, 255), cngclr=(255, 255, 0), func=fn1, text='Play', font = "segoeprint", font_size=35, font_clr = (0, 0, 0))
    button2 = button((750, 1050/2), (140, 45), (255, 255, 255), (255, 255, 0), fn2, 'Help', font = "segoeprint", font_size=35, font_clr = (0, 0, 0))
    button3 = button((750, 1300/2), (140, 45), (255, 255, 255), (255, 255, 0), fn3, 'Exit', font = "segoeprint", font_size=35, font_clr = (0, 0, 0))
    Title = button((750, 160), (1500, 80), (0, 0, 0), (0, 0, 0), fn4, 'Going thought the shadow', font = "sourcecodeproblack", font_size=72, font_clr = (255, 255, 0))

    button_list = [button1, button2, button3, Title]


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