import pygame
from random import randint
from time import sleep

pygame.mixer.init()
pygame.mixer.music.load('ratsasan.mp3')
pygame.mixer.music.play(10, 0.1, 1)

pygame.init()
clock = pygame.time.Clock()

display_size = [550, 500]
display = pygame.display.set_mode(display_size)
bg = pygame.image.load('bg.jpg')

text = pygame.font.Font(None, 30)
textt = pygame.font.SysFont('arialblack', 15)
name = "Neyaz"
texte = pygame.font.Font(None, 65)
over = 'Game Over . You lose ! !'

pole_width = 55
pole_gap = 100
pole_x = 550
top_pole_height = randint(25, 450)
pole_color = (110, 40, 110)

polea_width = 70
polea_gap = 125
polea_x = 550
top_polea_height = randint(20, 450)
polea_color = (60, 0, 50)

bird = pygame.image.load('bird.png')
bird_x = 200
bird_y = 200
score = 0

keep_alive = True
while keep_alive:

    # event adding code........................................
    pygame.event.get()
    keys = pygame.key.get_pressed()
    if keys[pygame.K_UP]:
        bird_y = bird_y - 5
    if keys[pygame.K_DOWN]:
        bird_y = bird_y + 6.5
    if keys[pygame.K_RIGHT]:
        bird_x = bird_x + 4
    if keys[pygame.K_LEFT]:
        bird_x = bird_x - 4

    display.blit(bg, [0, 0])
    display.blit(bird, [bird_x, bird_y])
    # first pole code -----------------------------------
    pole_x = pole_x - 2.7
    if pole_x <= -pole_width:
        pole_x = 550
        top_pole_height = randint(50, 400)
        score = score + 5
    pygame.draw.rect(display, pole_color, (pole_x, 0, pole_width, top_pole_height))
    pygame.draw.rect(display, pole_color, (pole_x, top_pole_height + pole_gap, pole_width, 500))
    if pole_x <= bird_x + 50 and bird_x <= pole_x + pole_width:
        if bird_y <= top_pole_height or bird_y + 50 >= top_pole_height + pole_gap:
            score = score - score - 5

            over_texte = texte.render(f'{over}', True, (250, 240, 240), sleep(.02))
            print(display.blit(over_texte, (10, 220)))

    # 2nd pole code---------------------------------------
    polea_x = polea_x - .8
    if polea_x + 200 <= -polea_width + 200:
        polea_x = 550 + 500
        top_polea_height = randint(20, 450)

    pygame.draw.rect(display, polea_color, (polea_x, 0, polea_width, top_polea_height))
    pygame.draw.rect(display, polea_color, (polea_x, top_polea_height + polea_gap, polea_width, 500))
    if polea_x <= bird_x + 50 and bird_x <= polea_x + polea_width:
        if bird_y <= top_polea_height or bird_y + 50 >= top_polea_height + polea_gap:
            score = score - score - 5

            over_texte = texte.render(f'{over}', True, (250, 240, 230), sleep(.021))
            print(display.blit(over_texte, (10, 220)))
            keep_alive = False
        keep_alive = True

    score_text = text.render(f'Score:{score}', True, (0, 255, 255))
    display.blit(score_text, (0, 0))
    # name setting code
    name_textt = textt.render(f'Made By:{name}', True, (225, 255, 255))
    display.blit(name_textt, (0, 475))
    pygame.display.update()
    clock.tick(60)
