from pico2d import *

import game_framework
import game_over
import game_start
import pikachu_world
import pause_mode
import play_mode

import server
from beach import Beach
from game_monster_ball import MonsterBall
from pika_1 import Pika1
from pika_2 import Pika2
from pikachu_map_obj import *

RESOURCE_PATH = "C:\\2DGP_proj\\project_01\\resource\\"

# 전역 변수
pika1 = None
pika2 = None
game_monster_ball = None

def init():
    global pika1, pika2, game_monster_ball

    # 스코어 초기화
    if server.score_1 is None:
        server.score_1 = Score(100, 600, 0)
    pikachu_world.add_object(server.score_1, 2)

    if server.score_2 is None:
        server.score_2 = Score(900, 600, 0)
    pikachu_world.add_object(server.score_2, 2)

    # 배경 및 오브젝트 추가
    pikachu_world.add_object(Beach(), 0)
    pikachu_world.add_object(Net(), 2)
    pikachu_world.add_object(Wave(), 1)

    clouds = [Cloud(random.randint(0, 1000), random.randint(400, 700)) for _ in range(10)]
    pikachu_world.add_objects(clouds, 1)

    # 캐릭터 추가
    pika1 = Pika1()
    pikachu_world.add_object(pika1, 2)

    pika2 = Pika2()
    pikachu_world.add_object(pika2, 2)

    # 몬스터 볼 추가
    start_ball = pika1.x if server.winner in ['1p', None] else pika2.x
    game_monster_ball = MonsterBall(start_ball)
    pikachu_world.add_object(game_monster_ball, 2)

    # 충돌 설정
    pikachu_world.add_collision_pair('pika1:monster_ball', pika1, None)
    pikachu_world.add_collision_pair('pika1:monster_ball', None, game_monster_ball)

    pikachu_world.add_collision_pair('pika2:monster_ball', pika2, None)
    pikachu_world.add_collision_pair('pika2:monster_ball', None, game_monster_ball)

    pikachu_world.add_collision_pair('monster_ball:net', game_monster_ball, None)
    pikachu_world.add_collision_pair('monster_ball:net', None, Net())


def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        #elif event.type == SDL_KEYDOWN and event.key == SDLK_SPACE:
            #game_framework.push_mode(pause_mode)
        else:
            pika1.handle_event(event)
            pika2.handle_event(event)


def update():
    global game_monster_ball

    pikachu_world.update()
    pikachu_world.handle_collisions()

    if game_monster_ball.y <= 150:
        handle_score_update()


def handle_score_update():
    global game_monster_ball, pika1, pika2

    # 공의 위치를 기반으로 득점 판별
    if game_monster_ball.x <= 500:  # 공이 왼쪽 영역(1P) 바닥에 닿았을 때
        server.score_2.count += 1  # 2P가 득점
        server.winner = '2p'  # 승자는 2P
        loser = pika1  # 패자는 1P
    else:  # 공이 오른쪽 영역(2P) 바닥에 닿았을 때
        server.score_1.count += 1  # 1P가 득점
        server.winner = '1p'  # 승자는 1P
        loser = pika2  # 패자는 2P

    # 패배자의 머리 위로 공 배치
    game_monster_ball.x = loser.x  # 패배자의 x 위치
    game_monster_ball.y = loser.y + 50  # 패배자의 머리 위로 배치
    game_monster_ball.speed_x = 0  # 수평 이동 속도 제거
    game_monster_ball.speed_y = -10  # 아래로 떨어지는 속도 설정

    print(f"Ball repositioned above loser ({'1P' if loser == pika1 else '2P'}) at ({game_monster_ball.x}, {game_monster_ball.y})")

    # 점수 조건 확인
    if server.score_1.count >= 10 or server.score_2.count >= 10:
        print("Game Over Triggered")
        game_framework.stack.change_mode(game_over)  # 게임 종료 화면으로 전환
    else:
        print("Resetting Game Start")
        game_framework.stack.change_mode(game_start)  # 다음 라운드 시작


def draw():
    clear_canvas()
    pikachu_world.render()
    update_canvas()


def pause():
    pass


def resume():
    pass


def finish():
    #global pika1, pika2, game_monster_ball
    #del pika1, pika2, game_monster_ball
    pikachu_world.clear()

