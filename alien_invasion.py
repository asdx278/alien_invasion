import sys
import pygame

class AlienInvasion:
    """Класс для управления ресурсами и поведением игры"""
    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы"""
        pygame.init()
        self.clock = pygame.time.Clock()
        # Фоновый цвет
        self.bg_color = (230, 230, 230)

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Запускает основной цикл игры"""
        while True:
            """Отслеживает события клваиатуры и мыши"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()
            # При каждом проходе цикла перерисовать экран
            self.screen.fill(self.bg_color)


            pygame.display.flip()
            # Частота кадров
            self.clock.tick(60)
            """Отображение последнего прорисованного экрана"""

if __name__ == '__main__':
    """Создание экземпляра и запуск игры"""
    ai = AlienInvasion()
    ai.run_game()