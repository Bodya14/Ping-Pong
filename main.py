import pygame

pygame.init()

fon = pygame.image.load('fon5.png')
mw = pygame.display.set_mode((500, 500))
mw.blit(fon, (0, 0))
clock = pygame.time.Clock()
game_over = False
dx = 10
dy = 3

platform_x = 460
platform_y = 220
platformis_x = 15
platformis_y = 220
move_UP = False
move_DOWN = False
kop_UP = False
kop_DOWN = False


class Area():
    def __init__(self, x=0, y=0, width=10, height=10, color=None):
        self.rect = pygame.Rect(x, y, width, height)
        self.fill_color = 0, 0, 0
        if color:
            self.fill_color = color

    def color(self, new_color):
        self.fill_color = new_color

    def fill(self):
        pygame.draw.rect(mw, self.fill_color, self.rect)

    def collidepoint(self, x, y):
        return self.rect.collidepoint(x, y)

    def colliderect(self, rect):
        return self.rect.colliderect(rect)


class Label(Area):
    def set_text(self, text, fsize=12, text_color=(0, 0, 0)):
        self.image = pygame.font.SysFont('verdana', fsize).render(text, True, text_color)

    def draw(self, shift_x=0, shift_y=0):
        self.fill()
        mw.blit(self.image, (self.rect.x + shift_x, self.rect.y + shift_y))


class Picture(Area):
    def __init__(self, filename, x=0, y=0, width=10, height=10):
        Area.__init__(self, x=x, y=y, width=width, height=height, color=None)
        self.image = pygame.image.load(filename)

    def draw(self):
        mw.blit(self.image, (self.rect.x, self.rect.y))


ball = Picture('Ball23.png', 160, 200, 50, 50)
platform = Picture('platform24.png', platform_x, platform_y, 30, 100)
platformis = Picture('platform25.png', platformis_x, platformis_y, 30, 100)

while not game_over:
    mw.blit(fon, (0, 0))

    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            game_over = True
        if event.type == pygame.KEYDOWN:
            if event.key == pygame.K_UP:
                move_UP = True
            if event.key == pygame.K_w:
                kop_UP = True
            if event.key == pygame.K_DOWN:
                move_DOWN = True
            if event.key == pygame.K_s:
                kop_DOWN = True
        elif event.type == pygame.KEYUP:
            if event.key == pygame.K_UP:
                move_UP = False
            if event.key == pygame.K_w:
                kop_UP = False
            if event.key == pygame.K_DOWN:
                move_DOWN = False
            if event.key == pygame.K_s:
                kop_DOWN = False

    if move_UP:
        platform.rect.y -= 5
    if move_DOWN:
        platform.rect.y += 5
    if kop_UP:
        platformis.rect.y -= 5
    if kop_DOWN:
        platformis.rect.y += 5

    ball.rect.x += dx
    ball.rect.y += dy
    if ball.rect.y > 400 or ball.rect.y < 0:
        dy *= -1

    if ball.rect.colliderect(platform.rect):
        dx *= -1

    if ball.rect.colliderect(platformis.rect):
        dx *= -1

    if ball.rect.x > 490:
        time_text = Label(150, 150, 0, 0, )
        time_text.set_text('Лівий переміг!', 60, (255, 0, 0))
        time_text.draw(10, 10)
        game_over = True

    if ball.rect.x < -40:
        time_text = Label(150, 150, 0, 0, )
        time_text.set_text('Правий переміг!', 60, (255, 0, 0))
        time_text.draw(10, 10)
        game_over = True

    platform.draw()
    platformis.draw()
    ball.draw()
    pygame.display.update()
    clock.tick(40)
