# Імпортуємо pygame
import pygame

# Імпортуємо клас логіки гри
from cube_game.app import GameApp

# Імпортуємо клас рендеру
from cube_game.view import GameView


def main():
    # Ініціалізуємо всі модулі pygame
    pygame.init()

    # Створюємо обʼєкт візуалізації гри
    view = GameView(width=400, height=400)

    # Створюємо обʼєкт логіки гри
    app = GameApp()

    # Повідомлення для консолі
    print("Гра стартувала! Закрийте вікно, щоб завершити.")

    # Прапорець роботи головного циклу
    running = True

    # ГОЛОВНИЙ ЦИКЛ ГРИ
    while running:

        # Обробка подій pygame
        for event in pygame.event.get():
            # Якщо користувач закрив вікно
            if event.type == pygame.QUIT:
                # Завершуємо цикл гри
                running = False

        # =========================
        # ОНОВЛЕННЯ ЛОГІКИ ГРИ
        # =========================

        # Оновлюємо стан гравця (рух з клавіатури)
        app.update()

        # =========================
        # РЕНДЕР ГРИ
        # =========================

        # Очищаємо екран
        view.clear()

        # Малюємо кубик гравця (піксельні координати)
        view.draw_cube(app.player, color=(0, 255, 0))

        # Малюємо кубик ворога (піксельні координати)
        view.draw_cube(app.enemy, color=(255, 0, 0))

        # Оновлюємо екран і обмежуємо FPS
        view.update()

    # Коректно завершуємо pygame
    pygame.quit()

    # Викликаємо stop(), якщо він існує
    if hasattr(app, "stop"):
        app.stop()

    # Повідомлення про завершення
    print("Гра завершена.")


# Точка входу в програму
if __name__ == "__main__":
    main()
