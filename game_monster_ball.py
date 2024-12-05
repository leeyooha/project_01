import random
from pico2d import *
import game_framework
import play_mode

# 리소스 경로 수정
RESOURCE_PATH = "C:\\2DGP_proj\\project_01\\resource\\"

PIXEL_PER_METER = (1000 / 18)
RUN_SPEED_KMPH = 8.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 7


class MonsterBall:
    def __init__(self, start_x):
        # 리소스 경로에 맞춰 수정
        self.image = load_image(RESOURCE_PATH + 'monster_ball.png')
        self.x, self.y = start_x, 580
        self.frame = 0
        self.speed_x, self.speed_y = 0, -1
        self.hit_x = None
        self.game = 0
        # 리소스 경로에 맞춰 수정
        self.crashing_sound = load_wav(RESOURCE_PATH + 'WAVE146_1.wav')
        self.crashing_sound.set_volume(20)

    def reset_position(self, winner_x):
        """승리한 플레이어 위치에 따라 몬스터볼 초기화"""
        self.x = winner_x
        self.y = 580
        self.speed_x = 0
        self.speed_y = -1
        self.hit_x = None
        self.game = 0

    def update(self):
        # 애니메이션 처리
        self.frame = (self.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 5

        # 공의 위치 업데이트
        self.y += self.speed_y * RUN_SPEED_PPS * game_framework.frame_time
        self.x += self.speed_x * RUN_SPEED_PPS * game_framework.frame_time
        self.x = clamp(25 - 1, self.x, 975 + 1)  # 화면 범위 안에서 이동
        self.y = clamp(150 - 1, self.y, 675 + 1)

        # 중력 적용 (속도 감소)
        self.speed_y -= 0.03

        # 벽에 부딪히면 반대 방향으로 튕기기
        if self.x <= 25 or self.x >= 975:
            self.speed_x = -self.speed_x
        if self.y >= 675:  # 바닥에 닿으면 속도 반대로
            self.speed_y = -self.speed_y

        # 바닥에 가까워지면 튕기는 효과 (공이 피카츄의 머리 위로 닿을 때)
        if self.y <= 150:
            self.crashing_sound.play()
            self.speed_y = -self.speed_y / 2  # 속도를 반으로 줄이면서 튕기기

        # 속도 제한 (최대, 최소값 설정)
        self.speed_x = clamp(-10, self.speed_x, 10)
        self.speed_y = clamp(-10, self.speed_y, 10)

    def draw(self):
        self.image.clip_draw(int(self.frame) * 100, 0, 100, 100, self.x, self.y)

        # 게임 시작 후 첫 번째 위치에 공이 가면 'hit_x' 값 설정
        if self.game == 0 and self.y <= 151:
            self.game = 1
        if self.game == 1:
            if self.hit_x is None:
                self.hit_x = self.x
            else:
                # 공이 떨어진 후 공의 위치를 다시 그리기
                self.image.clip_draw(6 * 100, 0, 100, 100, self.hit_x, 100)

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 50, self.y + 50  # 공의 충돌 영역

    def handle_collision(self, group, a):
        if group == 'pika1:monster_ball':  # 피카츄1과 충돌 시
            self.speed_x += (self.x - play_mode.pika1.x) / 50  # 속도 조정
            self.speed_y += (self.y - (play_mode.pika1.y - 10)) / 50  # 속도 조정
            self.y += self.speed_y * RUN_SPEED_PPS * game_framework.frame_time  # 위치 이동
            self.x += self.speed_x * RUN_SPEED_PPS * game_framework.frame_time

        if group == 'pika2:monster_ball':  # 피카츄2와 충돌 시
            self.speed_x += (self.x - play_mode.pika2.x) / 50  # 속도 조정
            self.speed_y += (self.y - (play_mode.pika2.y - 10)) / 50  # 속도 조정

        if group == 'monster_ball:net':  # 네트와 충돌 시
            if self.y - 50 >= 220 + 140:  # 네트에 공이 닿으면 튕김 처리
                self.speed_y = -self.speed_y
            else:  # 네트 상단에 부딪히면 수평 반사 처리
                self.speed_x = -self.speed_x




