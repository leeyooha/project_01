from pico2d import *

import game_framework
import pikachu_world

def handle_events():
    """이벤트 처리"""
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.pop_mode()


def init():
    """초기화 함수"""
    pass


def finish():
    """정리 함수"""
    pass


def update():
    """업데이트 함수"""
    pass


def draw():
    """화면 렌더링"""
    clear_canvas()
    pikachu_world.render()
    update_canvas()


def pause():
    """일시 정지"""
    pass


def resume():
    """재개"""
    pass
