from pico2d import *
import random
from pikachu_world import remove_object

# 리소스 경로 상수
#RESOURCE_PATH = "C:\\2DGP_proj\\project_01\\resource\\"

class Net:
    def __init__(self):
        self.image = load_image('resource\\net.png')

    def update(self):
        pass

    def draw(self):
        self.image.draw(500, 220)
        # draw_rectangle(*self.get_bb())

    def get_bb(self):
        return 500 - 3, 220 - 140, 500 + 3, 220 + 140

    def handle_collision(self, group, a):
        pass


class Wave:
    def __init__(self):
        self.image = load_image('resource\\wave.png')
        self.y = 0
        self.dir = 1

    def update(self):
        if self.y > 25:
            self.dir = -0.1
        elif self.y < -25:
            self.dir = 0.1
        self.y += self.dir

    def draw(self):
        self.image.draw(500, self.y)


class Cloud:
    def __init__(self, x, y):
        self.image = load_image('resource\\cloud.png')
        self.x = x
        self.y = y
        self.speed = random.randint(1, 5)

    def update(self):
        self.x += self.speed / 5
        if self.x >= 1000:
            self.x = -100
            self.y = random.randint(400, 700)
            self.speed = random.randint(1, 5)

    def draw(self):
        self.image.draw(self.x, self.y)


class Score:
    def __init__(self, x, y, count):
        self.image = load_image('resource\\score.png')
        self.x = x
        self.y = y
        self.count = count

    def update(self):
        pass

    def draw(self):
        self.image.clip_draw((self.count % 10) * 30, 0, 30, 30, self.x, self.y, 50, 50)


class GameOverPikachu:
    def __init__(self, x, action):
        self.image = load_image('resource\\game_over_pikachu.png')
        self.x = x
        self.y = 150
        self.frame = 0
        self.action = action

    def update(self):
        if self.frame < 4:
            self.frame += 1
            delay(0.1)

    def draw(self):
        self.image.clip_draw((self.frame % 5) * 100, self.action * 100, 100, 100, self.x, self.y, 100, 100)
