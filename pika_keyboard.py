from pico2d import *

Bg_frame_width, Bg_frame_height = 1130, 700
open_canvas(Bg_frame_width, Bg_frame_height)
background = load_image('images//pikachu_bg.png')
character = load_image('images//sprite_sheet_1.png')

# 전역 변수 초기화
left, right, up, down, shift = False, False, False, False, False

running = True
x, y = Bg_frame_width // 4 * 3, 140  # 오른쪽 피카츄 초기 위치
frame = 0
fall_speed = 5  # 기본 하강 속도
boosted_fall_speed = 20  # DOWN 키를 눌렀을 때 하강 속도
up_speed = 10  # 기본 상승 속도
boosted_up_speed = 20  # Shift + UP 키를 눌렀을 때 상승 속도

# 왼쪽 피카츄 고정 위치
left_pikachu_x, left_pikachu_y = Bg_frame_width // 4, 140

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
            elif event.key == SDLK_LSHIFT:  # Shift 키 입력 처리
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
            elif event.key == SDLK_LSHIFT:  # Shift 키 해제 처리
                shift = False

# 메인 루프
while running:
    handle_events()  # 이벤트 처리
    clear_canvas()
    background.draw(Bg_frame_width // 2, Bg_frame_height // 2)  # 배경 그리기

    # 왼쪽 피카츄 고정된 위치에서 오른쪽을 향하도록 출력
    character.clip_composite_draw(frame * 67, 3 * 66, 67, 66, 0, '', left_pikachu_x, left_pikachu_y, 90, 90)

    # 오른쪽 피카츄 이동 및 애니메이션 출력
    if shift and left:  # Shift + LEFT 키 입력 처리
        x -= 10
        character.clip_composite_draw(frame * 67, 1 * 66, 67, 66, 0, 'h', x, y, 90, 90)
    elif shift and right:  # Shift + RIGHT 키 입력 처리
        x += 10
        character.clip_composite_draw(frame * 67, 1 * 66, 67, 66, 0, '', x, y, 90, 90)
    elif shift and up:  # Shift + UP 키 입력 처리
        y += boosted_up_speed  # 빠르게 상승
        character.clip_composite_draw(frame * 67, 2 * 66, 67, 66, 0, 'h', x, y, 90, 90)
    elif up:  # UP 키 입력 처리 (위로 이동)
        y += up_speed
        character.clip_composite_draw(frame * 67, 3 * 66, 67, 66, 0, 'h', x, y, 90, 90)
    elif down:  # DOWN 키 입력 처리 (빠르게 아래로 이동)
        y -= boosted_fall_speed  # 빠르게 하강
        character.clip_composite_draw(frame * 67, 3 * 66, 67, 66, 0, 'h', x, y, 90, 90)
    elif left:  # LEFT 키 입력 처리
        x -= 10
        character.clip_composite_draw(frame * 67, 3 * 66, 67, 66, 0, 'h', x, y, 90, 90)
    elif right:  # RIGHT 키 입력 처리
        x += 10
        character.clip_composite_draw(frame * 67, 3 * 66, 67, 66, 0, '', x, y, 90, 90)
    else:  # 입력이 없을 때 기본 애니메이션
        y -= fall_speed  # 기본 하강 속도
        character.clip_composite_draw(frame * 67, 3 * 66, 67, 66, 0, 'h', x, y, 90, 90)

    # 화면 경계 조건 처리 (오른쪽 피카츄만 경계 처리)
    if x > Bg_frame_width - 10:
        x = Bg_frame_width - 10
    elif x < Bg_frame_width // 2:
        x = Bg_frame_width // 2

    if y > Bg_frame_height - 10:  # 위쪽 경계 처리
        y = Bg_frame_height - 10
    elif y < 140:  # 아래쪽 경계 처리
        y = 140

    update_canvas()
    if shift and (left or right):  # Shift + 방향키를 누를 때 0~3 프레임 순환
        frame = (frame + 1) % 4
    else:  # 나머지 상태에서는 7개의 프레임 순환
        frame = (frame + 1) % 7
    delay(0.05)

close_canvas()
