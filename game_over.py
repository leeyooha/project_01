import random

from pico2d import *

import game_framework
import pikachu_world
import server
import title_mode
from beach import Beach
from pikachu_map_obj import *

# 리소스 경로 상수
RESOURCE_PATH = "C:\\2DGP_proj\\project_01\\resource\\"

def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            game_framework.change_mode(title_mode)


def init():
    global image, p_pikachu_sound
    if server.winner == '1p':
        winner_pikachu = Game_over_pikachu(200, 1)
        loser_pikachu = Game_over_pikachu(800, 0)
    else:
        winner_pikachu = Game_over_pikachu(200, 0)
        loser_pikachu = Game_over_pikachu(800, 1)

    pikachu_world.add_object(loser_pikachu, 2)
    pikachu_world.add_object(winner_pikachu, 2)

    beach = Beach()
    pikachu_world.add_object(beach, 0)

    net = Net()
    pikachu_world.add_object(net, 2)

    wave = Wave()
    pikachu_world.add_object(wave, 1)

    clouds = [Cloud(random.randint(0, 1000), random.randint(400, 700)) for _ in range(10)]
    pikachu_world.add_objects(clouds, 1)

    image = load_image(RESOURCE_PATH + 'continue.png')

    p_pikachu_sound = load_wav(RESOURCE_PATH + 'WAVE143_1.wav')
    p_pikachu_sound.set_volume(32)


def finish():
    p_pikachu_sound.play()
    server.score_1 = None
    server.score_2 = None
    server.winner = None
    pikachu_world.clear()


def update():
    pikachu_world.update()


def draw():
    clear_canvas()
    pikachu_world.render()
    image.draw(500, 400)
    update_canvas()


def pause():
    pass


def resume():
    pass
