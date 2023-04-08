import pygame
import sys
import random

pygame.init()
screen = pygame.display.set_mode((1280, 720))
clock = pygame.time.Clock()
pygame.display.set_caption("Dino Game")
ground = pygame.image.load("assets/assets/ground.png")
ground = pygame.transform.scale(ground, (1280, 20))
ground1 = pygame.image.load("assets/assets/ground.png")
ground1 = pygame.transform.scale(ground, (1280, 20))
ground_rect = ground.get_rect(center=(640, 480))
ground_rect1 = ground.get_rect(center=(640, 480))
Dinosaur = pygame.image.load("assets/assets/Dino1.png")
Dinosaur1 = pygame.image.load("assets/assets/Dino2.png")
cactus = pygame.image.load("assets/assets/cacti/cactus1.png")
cactus1 = pygame.image.load("assets/assets/cacti/cactus2.png")
Dinosaur = pygame.transform.scale(Dinosaur, (60, 75))
Dinosaur1 = pygame.transform.scale(Dinosaur1, (60, 75))
game_font = pygame.font.Font("assets/assets/PressStart2P-Regular.ttf", 15)
speed = 1
groundx = 0
groundy = 480
dinosaurx = 50
dinosaury = groundy - 20
counter = 1
dinovelocity = 0
dinogravity = 4
score = 0
cactusx = random.random() * 1000 + 1000
cactusx1 = random.random() * 1000 + 1200
screen.blit(cactus, (cactusx, groundy - 30))
screen.blit(cactus1, (cactusx1, groundy - 30))
game_state = 'playing'
while True:
    groundx -= speed
    cactusx -= speed
    cactusy = groundy - 30
    cactusx1 -= speed

    if cactusx < -20:
        cactusx = random.random() * 1000 + 1000
    if cactusx1 < -20:
        cactusx1 = random.random() * 1000 + 1000

    speed += 0.001
    if groundx < -1280:
        groundx = 0
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            pygame.quit()
            sys.exit()
    screen.fill('white')
    screen.blit(ground, (groundx, groundy))
    screen.blit(ground1, (groundx+1280, groundy))
    screen.blit(cactus, (cactusx, cactusy))
    screen.blit(cactus1, (cactusx1, cactusy))

    counter = counter + 1
    score = score+0.1
    display_score = int(score)

    if counter >= 10:
        screen.blit(Dinosaur1, (dinosaurx, dinosaury))
        if counter == 20:
            counter = 0
    else:
        screen.blit(Dinosaur, (dinosaurx, dinosaury))
    font = pygame.font.Font(None, 36)
    score_text = game_font.render(str(display_score), True, (0, 0, 0))
    screen.blit(score_text, (1180, 10))

    keys = pygame.key.get_pressed()
    if keys[pygame.K_SPACE]:
        dinovelocity = 15
        dinovelocity -= dinogravity
        dinosaury -= dinovelocity
    if dinosaury < groundy - 150:
        dinosaury = groundy - 150

    elif dinosaury < 470:
        dinosaury += dinogravity
        if dinosaury > groundy - 50:
            dinosaury = groundy-50

    if dinosaury > cactusy - 3 and dinosaurx > cactusx or (dinosaury > cactusy - 3 and dinosaurx > cactusx) or (dinosaury > cactusy - 3 and dinosaurx > cactusx):
        score = 0
        speed = 1
        screen.fill(255,255,255)
        GameOverText = game_font.render('Game Over', True, (0, 0, 0))
        screen.blit(GameOverText, (600, 270))
    pygame.display.update()
    clock.tick(120)
