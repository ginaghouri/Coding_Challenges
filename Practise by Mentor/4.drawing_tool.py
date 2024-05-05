import pygame

def main():
    pygame.init()
    pygame.display.set_caption("Drawing Tool v0.1 by Mouiz Ghouri (King_ftw)")

    running = True
    lmb_state = False
    last_pixel = {'x': -1, 'y': -1}

    screen = pygame.display.set_mode((500, 500))
    screen.fill((255, 255, 255))

    def drawPixel(mouse_position, last_x, last_y):
        if last_x != -1:
            x1, y1 = last_x, last_y
            pygame.draw.line(screen, (50, 50, 50), (x1, y1), mouse_position, 5)
        else:
            pygame.draw.rect(screen, (50, 50, 50), (*mouse_position, 1, 1))

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

            if event.type == pygame.MOUSEBUTTONDOWN:
                lmb_state = True

            elif event.type == pygame.MOUSEBUTTONUP:
                lmb_state = False
                last_pixel['x'] = -1
                last_pixel['y'] = -1

            elif event.type == pygame.MOUSEMOTION:
                if lmb_state:
                    drawPixel(pygame.mouse.get_pos(), last_pixel['x'], last_pixel['y'])
                    last_pixel['x'], last_pixel['y'] = pygame.mouse.get_pos()

        pygame.display.update()

if __name__ == "__main__":
    main()
