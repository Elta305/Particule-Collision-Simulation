import pygame
from class_Particle import Particle
from functions_geometric import euclidean_distance
from random import randint
from sys import exit

def main():
    pygame.init()
    WIDTH, HEIGHT = 1280, 780
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Particle Collider")
    clock = pygame.time.Clock()

    bg = pygame.Surface((WIDTH, HEIGHT))
    bg.fill((20, 20, 20))

    particles = []
    for i in range(50):
        pos = (randint(1, 1270), randint(10, 770))
        speed = randint(4, 8)
        radius = 5
        particles.append(Particle(pos, (1, 1), speed, radius, (randint(0, 255), randint(0, 255), randint(0, 255))))

    while True:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                pygame.quit()
                exit()
        
        screen.blit(bg, (0, 0))

        for particle in particles:
            for point in particles:
                distance = euclidean_distance(particle.pos, point.pos)
                if distance < 255:
                    color = [255 - distance, 255 - distance, 255 - distance]
                    if color[0] < 20:
                        color[0] = 20
                    if color[1] < 20:
                        color[1] = 20
                    if color[2] < 20:
                        color[2] = 20
                    pygame.draw.aaline(screen, color, particle.pos, point.pos, 3)

        for particle in particles:
            pygame.draw.circle(screen, particle.color, particle.pos, particle.radius)
            particle.guidance([0, WIDTH, 0, HEIGHT], particles)

        # for particle in particles:

        for particle in particles:
            particle.update_pos()

        pygame.display.update()
        clock.tick(30)

if __name__ == "__main__":
    main()