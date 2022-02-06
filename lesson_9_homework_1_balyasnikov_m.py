# пока не разобрался с приватными и защищенными переменными
import time
import pygame


class TrafficLight:
    __color = 'red'
    previous_color = ''
    width, height, fps= 100, 100, 20
    RED = (255, 0, 0)
    GREEN = (0, 255, 0)
    YELLOW = (255, 255, 0)
    colors_list = ['red', 'yellow', 'green']

    def __color_checker(callback):
        def wrapper(*args):
            if args[1] not in TrafficLight.colors_list:
                raise ValueError('Wrong color name!')
            initialize = callback(*args)
            return initialize

        return wrapper

    @__color_checker
    def __init__(self, color):
        TrafficLight.__color = color
        self.color = color
        if TrafficLight.previous_color == '':
            TrafficLight.previous_color = TrafficLight.colors_list[TrafficLight.colors_list.index(self.color) - 1]
        if self.color == 'red' and TrafficLight.previous_color == 'green':
            self.color_rgb = TrafficLight.RED
            self.timeout = 7
        elif self.color == 'yellow' and TrafficLight.previous_color == 'red':
            self.color_rgb = TrafficLight.YELLOW
            self.timeout = 2
        elif self.color == 'green' and TrafficLight.previous_color == 'yellow':
            self.color_rgb = TrafficLight.GREEN
            self.timeout = 5
        else:
            raise ValueError('Wrong sequence!')

    def running(self, running=True):
        pygame.init()
        screen = pygame.display.set_mode((TrafficLight.width, TrafficLight.height))
        pygame.display.set_caption('Traffic Light')
        clock = pygame.time.Clock()
        while running:
            clock.tick(TrafficLight.fps)
            screen.fill(self.color_rgb)
            pygame.display.flip()
            time.sleep(self.timeout)
            running = False
        pygame.display.flip()
        pygame.quit()


svet_1 = TrafficLight('green')
svet_1.running()
