from pico2d import *

# 화면 크기 설정
Bg_frame_width, Bg_frame_height = 1130, 700
open_canvas(Bg_frame_width, Bg_frame_height)

# 이미지 로드
background = load_image('images//pikachu_bg.png')  # 배경 이미지
character = load_image('images//sprite_sheet_1.png')  # 피카츄 이미지
monster_ball_image = load_image('images//ball_sprite_sheet.png')  # 몬스터볼 이미지

# 전역 변수 초기화
left, right, up, down, shift = False, False, False, False, False
running = True

# 오른쪽 피카츄 초기 위치
x, y = Bg_frame_width // 4 * 3, 140
frame = 0

# 몬스터볼 초기 위치 및 속도
ball_x, ball_y = 500, 350
ball_speed_x, ball_speed_y = 3, -2
ball_frame = 0

# 몬스터볼 프레임 크기와 간격
BALL_FRAME_WIDTH = 62  # 공 프레임 너비
BALL_FRAME_HEIGHT = 62  # 공 프레임 높이
BALL_FRAME_SPACING = 2  # 프레임 간 간격

# 피카츄 움직임 속도
fall_speed = 5
boosted_fall_speed = 20
up_speed = 10
boosted_up_speed = 20

# 왼쪽 피카츄 고정 위치
left_pikachu_x, left_pikachu_y = Bg_frame_width // 4, 140

# 이벤트 처리 함수
def handle_events():
    global running
    global left, right, up, down, shift
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                left = True
            elif event.key == SDLK_RIGHT:
                right = True
            elif event.key == SDLK_UP:
                up = True
            elif event.key == SDLK_DOWN:
                down = True
            elif event.key == SDLK_LSHIFT:
                shift = True
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                left = False
            elif event.key == SDLK_RIGHT:
                right = False
            elif event.key == SDLK_UP:
                up = False
            elif event.key == SDLK_DOWN:
                down = False
            elif event.key == SDLK_LSHIFT:
                shift = False

# 메인 루프
while running:
    handle_events()

    # 몬스터볼 업데이트
    ball_x += ball_speed_x
    ball_y += ball_speed_y
    ball_speed_y -= 0.1  # 중력 효과
    if ball_x <= 50 or ball_x >= Bg_frame_width - 50:  # 좌우 경계 충돌
        ball_speed_x = -ball_speed_x
    if ball_y <= 140:  # 바닥 충돌
        ball_speed_y = -ball_speed_y * 0.8
    ball_frame = (ball_frame + 1) % 8  # 애니메이션 프레임 업데이트

    # 오른쪽 피카츄 이동
    if shift and left:
        x -= 10
    elif shift and right:
        x += 10
    elif shift and up:
        y += boosted_up_speed
    elif up:
        y += up_speed
    elif down:
        y -= boosted_fall_speed
    elif left:
        x -= 10
    elif right:
        x += 10
    else:
        y -= fall_speed  # 기본 하강

    # 화면 경계 처리
    if x > Bg_frame_width - 10:
        x = Bg_frame_width - 10
    elif x < Bg_frame_width // 2:
        x = Bg_frame_width // 2
    if y > Bg_frame_height - 10:
        y = Bg_frame_height - 10
    elif y < 140:
        y = 140

    # 화면 그리기
    clear_canvas()
    background.draw(Bg_frame_width // 2, Bg_frame_height // 2)  # 배경 그리기

    # 왼쪽 피카츄 그리기
    character.clip_composite_draw(frame * 67, 3 * 66, 67, 66, 0, '', left_pikachu_x, left_pikachu_y, 90, 90)

    # 오른쪽 피카츄 그리기
    character.clip_composite_draw(frame * 67, 3 * 66, 67, 66, 0, 'h', x, y, 90, 90)

    # 몬스터볼 그리기
    monster_ball_image.clip_draw(
        ball_frame * (BALL_FRAME_WIDTH + BALL_FRAME_SPACING),
        0,
        BALL_FRAME_WIDTH,
        BALL_FRAME_HEIGHT,
        ball_x,
        ball_y
    )

    update_canvas()

    # 애니메이션 프레임 업데이트
    if shift and (left or right):
        frame = (frame + 1) % 4
    else:
        frame = (frame + 1) % 7

    delay(0.05)

close_canvas()
