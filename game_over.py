import random
from pico2d import *
import game_framework
import pikachu_world
import server
import title_mode
from beach import Beach
from pikachu_map_obj import *  # 필요한 객체 임포트

class Game_over_pikachu:
    def __init__(self, x, winner_flag):
        self.x = x
        self.y = 220  # Pikachu의 중심 y 좌표 (조정)
        self.frame = 4  # 현재 프레임
        self.winner_flag = winner_flag  # 승자 여부 (1 = 승자, 0 = 패자)
        self.image = load_image('C:\\2DGP_proj\\project_01\\resource\\game_over_pikachu.png')
        self.frame_width = 100  # 프레임의 너비
        self.frame_height = 100  # 프레임의 높이
        self.frame_time = 0  # 프레임 전환 속도 조정용 시간 변수

    def update(self):
        #self.frame_time += 1
        #if self.frame_time >= 150:  # 프레임 전환 속도 (30 프레임마다 전환)
            #self.frame = (self.frame + 1) % 4  # 0~4 프레임 순환
            #self.frame_time = 0  # 초기화
        pass

    def draw(self):
        row_y = self.frame_height if self.winner_flag == 1 else 0  # 승자는 y=96, 패자는 y=0

        # 애니메이션 시트에서 적절한 프레임을 클립하여 그리기
        self.image.clip_draw(self.frame * self.frame_width, row_y, self.frame_width, self.frame_height, self.x, self.y)




# 이벤트 처리 함수
def handle_events():
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            game_framework.quit()
        elif event.type == SDL_KEYDOWN and event.key == SDLK_ESCAPE:
            game_framework.quit()
        elif (event.type, event.key) == (SDL_KEYDOWN, SDLK_SPACE):
            game_framework.stack.change_mode(title_mode)

# 초기화 함수
def init():
    global image, p_pikachu_sound

    # 승자와 패자 설정
    if server.winner == '1p':
        winner_pikachu = Game_over_pikachu(200, 1)  # 승자: 1
        loser_pikachu = Game_over_pikachu(800, 0)  # 패자: 0
    else:
        winner_pikachu = Game_over_pikachu(200, 0)  # 승자: 2
        loser_pikachu = Game_over_pikachu(800, 1)  # 패자: 1

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

    # 리소스 로드
    image = load_image('C:\\2DGP_proj\\project_01\\resource\\continue.png')
    p_pikachu_sound = load_wav('C:\\2DGP_proj\\project_01\\resource\\WAVE143_1.wav')
    p_pikachu_sound.set_volume(32)

# 종료 함수
def finish():
    p_pikachu_sound.play()
    server.score_1 = None
    server.score_2 = None
    server.winner = None
    pikachu_world.clear()

# 업데이트 함수
def update():
    pikachu_world.update()

# 화면 그리기 함수
def draw():
    clear_canvas()
    pikachu_world.render()
    image.draw(500, 400)  # "PRESS SPACE TO CONTINUE" 표시
    update_canvas()

# 일시 정지 함수
def pause():
    pass

# 재개 함수
def resume():
    pass
