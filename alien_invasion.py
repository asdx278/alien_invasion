import sys
import pygame

class AlienInvasion:
    """Класс для управления ресурсами и поведением игры"""
    def __init__(self):
        """Инициализирует игру и создает игровые ресурсы"""
        pygame.init()

        self.screen = pygame.display.set_mode((1200, 800))
        pygame.display.set_caption("Alien Invasion")

    def run_game(self):
        """Запускает основной цикл игры"""
        while True:
            """Отслеживает события клваиатуры и мыши"""
            for event in pygame.event.get():
                if event.type == pygame.QUIT:
                    sys.exit()


            pygame.display.flip()
            """Отображение последнего прорисованного экрана"""

if __name__ == '__main__':
    """Создание экземпляра и запуск игры"""
    ai = AlienInvasion()
    ai.run_game()