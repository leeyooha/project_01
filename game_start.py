from pico2d import *

import game_framework
import play_mode
import title_mode

# 리소스 경로 상수
#RESOURCE_PATH = "C:\\2DGP_proj\\project_01\\resource\\"


def init_game_logic():
    global game_monster_ball, pika1, pika2

    # 공 초기화
    game_monster_ball.x = 750  # 중앙
    game_monster_ball.y = 580
    game_monster_ball.speed_x = 0
    game_monster_ball.speed_y = -1

    # 플레이어 초기화
    pika1.x, pika1.y = 200, 150  # 왼쪽 플레이어
    pika1.speed_x = 0
    pika1.speed_y = 0
    pika1.state_machine.start()  # Idle 상태로 초기화

    pika2.x, pika2.y = 1000, 150  # 오른쪽 플레이어
    pika2.speed_x = 0
    pika2.speed_y = 0
    pika2.state_machine.start()  # Idle 상태로 초기화

def handle_events():
    """이벤트 처리"""
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.stack.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.stack.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            game_framework.stack.change_mode(play_mode)


def init():
    """초기화 함수"""
    global logo_start_time, scale_factor
    global background_image, game_start_image, ready_image

    # 리소스 로드
    background_image = load_image('resource\\game_start_map.png')
    game_start_image = load_image('resource\\start.png')
    ready_image = load_image('resource\\ready.png')

    logo_start_time = get_time()
    scale_factor = 1
    pass

def finish():
    """정리 함수"""
    pass


def update():
    """업데이트 함수"""
    global scale_factor
    scale_factor += 0.005
    # 1.5초 후 플레이 모드로 전환
    if get_time() - logo_start_time >= 1.5:
        game_framework.stack.change_mode(play_mode)


def draw():
    """화면 렌더링"""
    global scale_factor
    clear_canvas()

    # 배경 그리기
    background_image.draw(500, 350)

    # 준비 이미지와 시작 이미지 그리기
    if get_time() - logo_start_time <= 0.5:
        ready_image.draw(500, 500)
    else:
        game_start_image.clip_draw(
            0, 0, 100, 50, 500, 500, 100 * scale_factor, 50 * scale_factor
        )

    update_canvas()


def pause():
    """일시 정지"""
    pass


def resume():
    """재개"""
    pass

