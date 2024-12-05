from pico2d import *

import game_framework
import game_start

# 리소스 경로 상수
RESOURCE_PATH = "C:\\2DGP_proj\\project_01\\resource\\"


def handle_events():
    """이벤트 처리"""
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.stack.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.stack.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            wav.play()
            game_framework.stack.change_mode(game_start)


def init():
    """초기화 함수"""
    global title_image, continue_image, wav

    # 리소스 로드
    title_image = load_image(RESOURCE_PATH + 'title.png')
    continue_image = load_image(RESOURCE_PATH + 'continue.png')
    wav = load_wav(RESOURCE_PATH + 'WAVE144_1.wav')
    wav.set_volume(32)


def finish():
    """정리 함수"""
    pass


def update():
    """업데이트 함수"""
    pass


def draw():
    """화면 렌더링"""
    clear_canvas()
    title_image.draw(500, 350)
    continue_image.draw(500, 400)
    update_canvas()


def pause():
    """일시 정지"""
    pass


def resume():
    """재개"""
    pass
