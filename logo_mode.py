from pico2d import *

import game_framework
import title_mode

# 리소스 경로 상수
#RESOURCE_PATH = "C:\\2DGP_proj\\project_01\\resource\\"

def handle_events():
    """이벤트 처리"""
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.stack.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.stack.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            game_framework.stack.change_mode(title_mode)


def init():
    """초기화 함수"""
    global logo_start_time, logo_image
    logo_image = load_image('resource\\tuk_credit.png')
    logo_start_time = get_time()


def finish():
    """정리 함수"""
    pass


def update():
    """업데이트 함수"""
    # 2초 후 타이틀 모드로 전환
    if get_time() - logo_start_time >= 2.0:
        game_framework.stack.change_mode(title_mode)


def draw():
    """화면 렌더링"""
    clear_canvas()
    logo_image.draw(500, 350)
    update_canvas()


def pause():
    """일시 정지"""
    pass


def resume():
    """재개"""
    pass
