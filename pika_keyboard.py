from pico2d import *

Bg_frame_width, Bg_frame_height = 1130, 700
open_canvas(Bg_frame_width, Bg_frame_height)
background = load_image('images//pikachu_bg.png')
character = load_image('images//sprite_sheet_1.png')

left, right, up, down = False, False, False, False

running = True
x, y = Bg_frame_width // 4 * 3 , 140
frame = 0

def handle_events():
    global running
    global left, right, up, down
    events = get_events()
    for event in events:
        if event.type == SDL_QUIT:
            running = False
        elif event.type == SDL_KEYDOWN:
            if event.key == SDLK_LEFT:
                left = True
            elif event.key == SDLK_RIGHT:
                right = True
            #elif event.key == SDLK_UP:
            #    up = True
            #elif event.key == SDLK_DOWN:
            #    down = True
        elif event.type == SDL_KEYUP:
            if event.key == SDLK_LEFT:
                left = False
            elif event.key == SDLK_RIGHT:
                right = False
            #elif event.key == SDLK_UP:
            #    up = False
            #elif event.key == SDLK_DOWN:
            #    down = False

# 메인 루프
while running:
    handle_events()  # 이벤트 처리
    clear_canvas()
    background.draw(Bg_frame_width // 2, Bg_frame_height // 2)  # 배경 그리기

    character.clip_composite_draw(frame * 67, 3 * 66, 67, 66, 0, 'h', x, y, 90, 90) #90,90 크기 조절
    #character.clip_draw(frame * 68, 3 * 66, 68, 66, x, y) #왼족보는 애니메이션
    # character.clip_draw(frame * 프레임의 x축 크기, 세로 갯수 -1 *프레임의 y축크기, 프레임의 x축 크기, 프레임의 y축크기, x, y)
    if left:
        x -= 10
       # character.clip_composite_draw(frame * 68, 3 * 66, 68, 66, 0,'h',x, y,90,90)  # 왼쪽 이동 애니메이션
    elif right:
        x += 10
        #character.clip_composite_draw(frame * 68, 3 * 63, 68, 63, 0,'h', x, y,100,100)  # 오른쪽 이동 애니메이션
    #else:
        #character.clip_composite_draw(frame * 68, 3 * 66, 68, 66, 0,'h',x, y,90,90)  # 입력이 없을 때 기본 애니메이션

    update_canvas()
    frame = (frame + 1) % 7  # 4개의 프레임 순환

    if x > Bg_frame_width -10:
        x = Bg_frame_width -10
    elif x < Bg_frame_width //2:
        x = Bg_frame_width //2

    delay(0.05)

close_canvas()
