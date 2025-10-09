import sys, pygame
import random
import ball

pygame.init()
random.seed()

windowsize = windowwidth, windowheight = 640, 480
black = 0, 0, 0
screen = pygame.display.set_mode(windowsize)


balls = [ball.Ball() for i in range(4)]

while 1:
    for event in pygame.event.get():
        if event.type == pygame.QUIT: 
            sys.exit()
        elif event.type == pygame.KEYDOWN:
            if event.key == pygame.K_DOWN:
                for b in balls:
                    b.speeddown()
            elif event.key == pygame.K_UP:
                for b in balls:
                    b.speedup()
 
    screen.fill(black)   
    for b in balls:
        b.move()
        b.draw(screen)
    pygame.display.flip()

    ball.Ball.Clock.tick()