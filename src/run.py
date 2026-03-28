import pygame
from cube_game.entities.cube import Cube
from cube_game.entities.enemy import Enemy
import pygame.display
import pygame.event
import pygame.key

# Глобальні змінні стану гри
WIDTH = 400
HEIGHT = 400
screen = None
player = None
enemy = None


def init_game():
    """Ініціалізація гри."""
    global screen, player, enemy
    pygame.init()
    screen = pygame.display.set_mode((WIDTH, HEIGHT))
    pygame.display.set_caption("Cube Game")
    player = Cube(start_x_px=200, start_y_px=200, size_px=200)
    enemy = Enemy(start_x_px=200, start_y_px=200, size_px=50)
    print("Гра стартувала! Закрийте вікно, щоб завершити.")


def handle_input():
    """Обробка вхідних даних."""
    global player
    keys = pygame.key.get_pressed()
    dx = dy = 0
    speed = 4.0

    if keys[pygame.K_LEFT]:
        dx -= speed
    elif keys[pygame.K_RIGHT]:
        dx += speed


    if keys[pygame.K_UP]:
        dy -= speed
    elif keys[pygame.K_DOWN]:
        dy += speed

    if dx != 0 or dy != 0:
        player.move(dx, dy, 0.0)


def check_collision() -> bool:
    """Перевіряє зіткнення гравця та ворога через collidepoint."""
    return player.collidepoint(enemy.center) or enemy.collidepoint(player.center)


def render():
    """Рендеринг гри."""
    global screen, player, enemy
    screen.fill((144, 0, 255))
    
    # Малюємо гравця (зелений куб)
    player_x = int(player.position[0])
    # print(player_x)
    # exit()

    player_y = int(player.position[1])
    player_size = int(player.size)
    pygame.draw.rect(screen, (0, 255, 0), (player_x, player_y, player_size, player_size))
    
    # Малюємо ворога (червоний куб)
    enemy_x = int(enemy.position[0])
    enemy_y = int(enemy.position[1])
    enemy_size = int(enemy.size)
    pygame.draw.rect(screen, (255, 0, 0), (enemy_x, enemy_y, enemy_size, enemy_size))
    
    pygame.display.flip()


def main_loop():
    """Головний цикл гри."""
    running = True
    clock = pygame.time.Clock()
    
    collision_detected = False

    while running:
        for event in pygame.event.get():
            if event.type == pygame.QUIT:
                running = False

        handle_input()
        current_collision = check_collision()
        if current_collision and not collision_detected:
            print("Гравець і ворог зіштовхнулися через collidepoint!")
        collision_detected = current_collision

        render()
        clock.tick(60)  # 60 FPS

    pygame.quit()
    print("Гра завершена.")


# Точка входу
if __name__ == "__main__":
    init_game()
    main_loop()
