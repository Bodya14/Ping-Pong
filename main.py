import pygame
pygame.init()

pygame.display.set_caption("Ping_pong")
 
wind_width = 500
wind_height = 500

back_win_color = (128, 0, 128)

fon = pygame.image.load('fon5.png')
mw = pygame.display.set_mode((wind_width, wind_height))
clock = pygame.time.Clock()
game_over= False
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
      self.fill_color = 0,0,0
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
      
ball_width = 50
ball_height = 50
ball = Picture('Ball23.png', 160, 200, ball_width, ball_height)
platform = Picture('platform24.png', platform_x, platform_y, 30, 100)
platformis = Picture('platform25.png', platformis_x, platformis_y, 30, 100)
 
show_platforms = True

def show_winner_screen(winner_text):
    global show_platforms
    if winner_text == 'Лівий переміг!' or winner_text == 'Правий переміг!':
        mw.fill(back_win_color if winner_text == 'Лівий переміг!' else back_win_color)
        show_platforms = False
    else:
        mw.blit(fon, (0, 0))
        show_platforms = True
    
    time_text = Label(0, 0, 0, 0)
    time_text.set_text(winner_text, 60, (255, 255, 255)) 
    text_width, text_height = time_text.image.get_size()
    x = (wind_width - text_width) / 2
    y = (wind_height - text_height) / 2
    time_text.draw(x, y) 
    restart_label = Label(0, 0, 0, 0)
    restart_label.set_text('Натисніть пробіл, щоб почати гру знову', 20, (0, 0, 0))
    restart_width, restart_height = restart_label.image.get_size()
    restart_x = (wind_width - restart_width) / 2
    restart_y = y + text_height + 20
    restart_label.draw(restart_x, restart_y)
    pygame.display.update()
    
show_winner = False
 
while not game_over:
    mw.blit(fon,(0, 0))
    
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
            if event.key == pygame.K_SPACE:
                if show_winner:
                    ball.rect.x = 160
                    ball.rect.y = 200
                    dx = 10
                    dy = 3
                    platform.rect.y = 220
                    platformis.rect.y = 220
                    show_winner = False
                    show_platforms = True
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
      platform.rect.y -=5
    if move_DOWN:
        platform.rect.y +=5
    if kop_UP:
        platformis.rect.y -=5
    if kop_DOWN:
        platformis.rect.y +=5
    
        
    ball.rect.x += dx
    ball.rect.y += dy
    
    if  ball.rect.y > wind_height - ball_height or ball.rect.y < 0:
        dy *= -1
    
    if ball.rect.colliderect(platform.rect):
        dx *= -1

    if ball.rect.colliderect(platformis.rect):
        dx *= -1

    if ball.rect.x > wind_width:
        show_winner_screen('Лівий переміг!')
        show_winner = True

    if ball.rect.x < -ball_width:
        show_winner_screen('Правий переміг!')
        show_winner = True
    
    if show_platforms:
        platform.draw()
        platformis.draw()

    ball.draw()   
    pygame.display.update()
    clock.tick(40)
