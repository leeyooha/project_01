from pico2d import *

class MonsterBall:
    def __init__(self, x, y):
        # 이미지 로드
        self.image = load_image(r'C:\2DGP_proj\project_01\images\ball_sprite_sheet.png')
        self.x, self.y = x, y
        self.speed_x, self.speed_y = 3, -2  # 초기 이동 속도
        self.frame = 0  # 애니메이션 프레임 초기화

    def update(self):
        # 몬스터볼 이동
        self.x += self.speed_x
        self.y += self.speed_y
        self.speed_y -= 0.1  # 중력 효과

        # 경계 충돌 처리
        if self.x <= 50 or self.x >= 1080:
            self.speed_x = -self.speed_x
        if self.y <= 140:
            self.speed_y = -self.speed_y * 0.8  # 바운스 효과

        # 애니메이션 프레임 업데이트
        self.frame = (self.frame + 1) % 8  # 총 8 프레임

    def draw(self):
        # 스프라이트에서 애니메이션 프레임 선택
        self.image.clip_draw(self.frame * 64, 0, 64, 64, self.x, self.y)

    def get_bb(self):
        # 충돌 박스 정의
        return self.x - 32, self.y - 32, self.x + 32, self.y + 32

    def handle_collision(self, group, other):
        if group == 'pikachu:monster_ball':
            self.speed_x = -self.speed_x
            self.speed_y += 5  # 충돌 시 위로 튀기기
