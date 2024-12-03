from pico2d import *
import game_framework

# 리소스 경로 상수
RESOURCE_PATH = "C:\\2DGP_proj\\project_01\\resource\\"

# 이벤트 처리 함수들
def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_RIGHT


def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_RIGHT


def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_LEFT


def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_LEFT


def up_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_UP


def up_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_UP


def y_150(e):
    return e[0] == 'y==150'


def l_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_SPACE


# 피카츄의 이동과 동작에 필요한 값들
PIXEL_PER_METER = (1000 / 18)
RUN_SPEED_KMPH = 12.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5


class Jump:
    @staticmethod
    def enter(pikachu_2, e):
        if up_down(e):
            pikachu_2.speed_y = 4
            pikachu_2.jump_sound.play()
        pikachu_2.action = 2

    @staticmethod
    def exit(pikachu_2, e):
        if l_down(e):
            pikachu_2.hit_ball()
        pass

    @staticmethod
    def do(pikachu_2):
        pikachu_2.frame = (pikachu_2.frame + FRAMES_PER_ACTION * 2 * ACTION_PER_TIME * game_framework.frame_time) % 4
        pikachu_2.x += pikachu_2.speed_x * RUN_SPEED_PPS * game_framework.frame_time
        pikachu_2.x = clamp(500 + 25, pikachu_2.x, 1000 - 25)

        if pikachu_2.speed_y != 0:
            pikachu_2.y += pikachu_2.speed_y * RUN_SPEED_PPS * game_framework.frame_time
            pikachu_2.speed_y = pikachu_2.speed_y - 0.03
        if pikachu_2.y < 150:
            pikachu_2.speed_y = 0
            pikachu_2.state_machine.handle_event(('y==150', 0))

        pass

    @staticmethod
    def draw(pikachu_2):
        pikachu_2.image.clip_composite_draw(int(pikachu_2.frame) * 100, int(pikachu_2.action) * 100, 100, 100, 0, 'h',
                                            pikachu_2.x, pikachu_2.y, 100, 100)


class Jump_right:
    @staticmethod
    def enter(pikachu_2, e):
        if up_down(e):
            pikachu_2.speed_y = 7
            pikachu_2.jump_sound.play()
        pikachu_2.speed_x = 1
        pikachu_2.action = 2
        pass

    @staticmethod
    def exit(pikachu_2, e):
        if l_down(e):
            pikachu_2.hit_ball()
        pass

    @staticmethod
    def do(pikachu_2):
        pikachu_2.frame = (pikachu_2.frame + FRAMES_PER_ACTION * 2 * ACTION_PER_TIME * game_framework.frame_time) % 4
        pikachu_2.x += pikachu_2.speed_x * RUN_SPEED_PPS * game_framework.frame_time
        pikachu_2.x = clamp(500 + 25, pikachu_2.x, 1000 - 25)

        if pikachu_2.speed_y != 0:
            pikachu_2.y += pikachu_2.speed_y * RUN_SPEED_PPS * game_framework.frame_time
            pikachu_2.speed_y = pikachu_2.speed_y - 0.03
        if pikachu_2.y < 150:
            pikachu_2.speed_y = 0
            pikachu_2.state_machine.handle_event(('y==150', 0))

        pass

    @staticmethod
    def draw(pikachu_2):
        pikachu_2.image.clip_composite_draw(int(pikachu_2.frame) * 100, int(pikachu_2.action) * 100, 100, 100, 0, 'h',
                                            pikachu_2.x, pikachu_2.y, 100, 100)


class Jump_left:
    @staticmethod
    def enter(pikachu_2, e):
        if up_down(e):
            pikachu_2.speed_y = 5
            pikachu_2.jump_sound.play()
        pikachu_2.speed_x = -1
        pikachu_2.action = 2
        pass

    @staticmethod
    def exit(pikachu_2, e):
        if l_down(e):
            pikachu_2.hit_ball()
        pass

    @staticmethod
    def do(pikachu_2):
        pikachu_2.frame = (pikachu_2.frame + FRAMES_PER_ACTION * 2 * ACTION_PER_TIME * game_framework.frame_time) % 4
        pikachu_2.x += pikachu_2.speed_x * RUN_SPEED_PPS * game_framework.frame_time
        pikachu_2.x = clamp(500 + 25, pikachu_2.x, 1000 - 25)

        if pikachu_2.speed_y != 0:
            pikachu_2.y += pikachu_2.speed_y * RUN_SPEED_PPS * game_framework.frame_time
            pikachu_2.speed_y = pikachu_2.speed_y - 0.03
        if pikachu_2.y < 150:
            pikachu_2.speed_y = 0
            pikachu_2.state_machine.handle_event(('y==150', 0))

        pass

    @staticmethod
    def draw(pikachu_2):
        pikachu_2.image.clip_composite_draw(int(pikachu_2.frame) * 100, int(pikachu_2.action) * 100, 100, 100, 0, 'h',
                                            pikachu_2.x, pikachu_2.y, 100, 100)


class Run_right:
    @staticmethod
    def enter(pikachu_2, e):
        if y_150(e):
            pikachu_2.landing_sound.play()
        pikachu_2.speed_x, pikachu_2.action = 1, 3
        pass

    @staticmethod
    def exit(pikachu_2, e):
        if l_down(e):
            pikachu_2.hit_ball()
        pass

    @staticmethod
    def do(pikachu_2):
        pikachu_2.frame = (pikachu_2.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        pikachu_2.x += pikachu_2.speed_x * RUN_SPEED_PPS * game_framework.frame_time
        pikachu_2.x = clamp(525, pikachu_2.x, 975)

    @staticmethod
    def draw(pikachu_2):
        pikachu_2.image.clip_composite_draw(int(pikachu_2.frame) * 100, int(pikachu_2.action) * 100, 100, 100, 0, 'h',
                                            pikachu_2.x, pikachu_2.y, 100, 100)


class Run_left:
    @staticmethod
    def enter(pikachu_2, e):
        if y_150(e):
            pikachu_2.landing_sound.play()
        pikachu_2.speed_x, pikachu_2.action = -1, 3
        pass

    @staticmethod
    def exit(pikachu_2, e):
        if l_down(e):
            pikachu_2.hit_ball()
        pass

    @staticmethod
    def do(pikachu_2):
        pikachu_2.frame = (pikachu_2.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        pikachu_2.x += pikachu_2.speed_x * RUN_SPEED_PPS * game_framework.frame_time
        pikachu_2.x = clamp(525, pikachu_2.x, 975)

    @staticmethod
    def draw(pikachu_2):
        pikachu_2.image.clip_composite_draw(int(pikachu_2.frame) * 100, int(pikachu_2.action) * 100, 100, 100, 0, 'h',
                                            pikachu_2.x, pikachu_2.y, 100, 100)


class Idle:
    @staticmethod
    def enter(pikachu_2, e):
        if y_150(e):
            pikachu_2.landing_sound.play()
        pikachu_2.action = 3
        pikachu_2.speed_x = 0
        pikachu_2.frame = 0

    @staticmethod
    def exit(pikachu_2, e):
        if l_down(e):
            pikachu_2.hit_ball()
        pass

    @staticmethod
    def do(pikachu_2):
        pikachu_2.frame = (pikachu_2.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

        pass

    @staticmethod
    def draw(pikachu_2):
        pikachu_2.image.clip_composite_draw(int(pikachu_2.frame) * 100, int(pikachu_2.action) * 100, 100, 100, 0, 'h',
                                            pikachu_2.x, pikachu_2.y, 100, 100)


class StateMachine:
    def __init__(self, pikachu_2):
        self.pikachu_2 = pikachu_2
        self.cur_state = Idle
        self.transitions = {
            Idle: {right_down: Run_right, left_down: Run_left, left_up: Run_right, right_up: Run_left, up_down: Jump,
                   l_down: Idle},
            Run_right: {right_down: Run_right, left_down: Idle, right_up: Idle, left_up: Run_right, up_down: Jump_right,
                        l_down: Run_right},
            Run_left: {right_down: Idle, left_down: Run_left, right_up: Run_left, left_up: Idle, up_down: Jump_left,
                       l_down: Run_right},
            Jump: {right_down: Jump_right, left_down: Jump_left, left_up: Jump_right, right_up: Jump_left, y_150: Idle,
                   l_down: Jump},
            Jump_right: {right_down: Jump_right, left_down: Jump, left_up: Jump_right, right_up: Jump, y_150: Run_right,
                         l_down: Jump_right},
            Jump_left: {right_down: Jump, left_down: Jump_left, left_up: Jump, right_up: Jump_left, y_150: Run_left,
                        l_down: Jump_left}
        }

    def start(self):
        self.cur_state.enter(self.pikachu_2, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.pikachu_2)

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.pikachu_2, e)
                self.cur_state = next_state
                self.cur_state.enter(self.pikachu_2, e)
                return True

        return False

    def draw(self):
        self.cur_state.draw(self.pikachu_2)


class Pika2:
    def __init__(self):
        self.x, self.y = 1000 - 200, 150
        self.image = load_image(RESOURCE_PATH + 'pikachu.png')
        self.frame = 0
        self.speed_y = 0
        self.speed = 0
        self.action = 0
        self.state_machine = StateMachine(self)
        self.state_machine.start()
        self.move = 0
        self.jump_sound = load_wav(RESOURCE_PATH + 'WAVE141_1.wav')
        self.jump_sound.set_volume(32)
        self.landing_sound = load_wav(RESOURCE_PATH + 'WAVE142_1.wav')
        self.landing_sound.set_volume(32)
        self.pikachu_sound = load_wav(RESOURCE_PATH + 'WAVE144_1.wav')
        self.pikachu_sound.set_volume(32)

    def update(self):
        self.state_machine.update()
        pass

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))
        pass

    def draw(self):
        self.state_machine.draw()
        #draw_rectangle(*self.get_bb())

    def hit_ball(self):
        self.pikachu_sound.play()
        pass

    def get_bb(self):
        return self.x - 50, self.y - 50, self.x + 40, self.y + 40

    def handle_collision(self, group, other):
        if group == 'pika2:monster_ball':
            print('pika2:ball')
        pass
