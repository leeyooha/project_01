from pico2d import *
import game_framework
import pikachu_world
import play_mode

# 리소스 경로 상수
RESOURCE_PATH = "C:\\2DGP_proj\\project_01\\resource\\"

def right_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_d


def right_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_d


def left_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_a


def left_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_a


def up_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_w


def up_up(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYUP and e[1].key == SDLK_w


def y_150(e):
    return e[0] == 'y==150'


def g_down(e):
    return e[0] == 'INPUT' and e[1].type == SDL_KEYDOWN and e[1].key == SDLK_g


PIXEL_PER_METER = (1000 / 18)
RUN_SPEED_KMPH = 16.0
RUN_SPEED_MPM = (RUN_SPEED_KMPH * 1000.0 / 60.0)
RUN_SPEED_MPS = (RUN_SPEED_MPM / 60.0)
RUN_SPEED_PPS = (RUN_SPEED_MPS * PIXEL_PER_METER)

TIME_PER_ACTION = 0.5
ACTION_PER_TIME = 1.0 / TIME_PER_ACTION
FRAMES_PER_ACTION = 5


class Jump:
    @staticmethod
    def enter(pikachu, e):
        if up_down(e):
            pikachu.jump_sound.play()
            pikachu.speed_y = 6
        pikachu.action = 2

        pass

    @staticmethod
    def exit(pikachu, e):
        if g_down(e):
            pikachu.hit_ball()
        pass

    @staticmethod
    def do(pikachu):
        pikachu.frame = (pikachu.frame + FRAMES_PER_ACTION * (ACTION_PER_TIME * 2) * game_framework.frame_time) % 4
        pikachu.x += pikachu.speed_x * RUN_SPEED_PPS * game_framework.frame_time
        pikachu.x = clamp(50, pikachu.x, 500 - 50)

        if pikachu.speed_y != 0:
            pikachu.y += pikachu.speed_y * RUN_SPEED_PPS * game_framework.frame_time
            pikachu.speed_y = pikachu.speed_y - 0.03
        if pikachu.y < 150:
            pikachu.speed_y = 0
            pikachu.state_machine.handle_event(('y==150', 0))

        pass

    @staticmethod
    def draw(pikachu):
        pikachu.image.clip_draw(int(pikachu.frame) * 100, pikachu.action * 100, 100, 100, pikachu.x, pikachu.y)
        pass


class Jump_right:
    @staticmethod
    def enter(pikachu, e):
        if up_down(e):
            pikachu.jump_sound.play()
            pikachu.speed_y = 5
        pikachu.speed_x = 1
        pikachu.action = 2
        pass

    @staticmethod
    def exit(pikachu, e):
        if g_down(e):
            pikachu.hit_ball()
        pass

    @staticmethod
    def do(pikachu):
        pikachu.frame = (pikachu.frame + FRAMES_PER_ACTION * (ACTION_PER_TIME * 2) * game_framework.frame_time) % 4
        pikachu.x += pikachu.speed_x * RUN_SPEED_PPS * game_framework.frame_time
        pikachu.x = clamp(50, pikachu.x, 500 - 50)

        if pikachu.speed_y != 0:
            pikachu.y += pikachu.speed_y * RUN_SPEED_PPS * game_framework.frame_time
            pikachu.speed_y = pikachu.speed_y - 0.03
        if pikachu.y < 150:
            pikachu.speed_y = 0
            pikachu.state_machine.handle_event(('y==150', 0))

        pass

    @staticmethod
    def draw(pikachu):
        pikachu.image.clip_draw(int(pikachu.frame) * 100, pikachu.action * 100, 100, 100, pikachu.x, pikachu.y)
        pass


class Jump_left:
    @staticmethod
    def enter(pikachu, e):
        if up_down(e):
            pikachu.jump_sound.play()
            pikachu.speed_y = 7
        pikachu.speed_x = -1
        pikachu.action = 2
        pass

    @staticmethod
    def exit(pikachu, e):
        if g_down(e):
            pikachu.hit_ball()
        pass

    @staticmethod
    def do(pikachu):
        pikachu.frame = (pikachu.frame + FRAMES_PER_ACTION * (ACTION_PER_TIME * 2) * game_framework.frame_time) % 4
        pikachu.x += pikachu.speed_x * RUN_SPEED_PPS * game_framework.frame_time
        pikachu.x = clamp(50, pikachu.x, 500 - 50)

        if pikachu.speed_y != 0:
            pikachu.y += pikachu.speed_y * RUN_SPEED_PPS * game_framework.frame_time
            pikachu.speed_y = pikachu.speed_y - 0.03
        if pikachu.y < 150:
            pikachu.speed_y = 0
            pikachu.state_machine.handle_event(('y==150', 0))

        pass

    @staticmethod
    def draw(pikachu):
        pikachu.image.clip_draw(int(pikachu.frame) * 100, pikachu.action * 100, 100, 100, pikachu.x, pikachu.y)
        pass


class Run_right:
    @staticmethod
    def enter(pikachu, e):
        if y_150(e):
            pikachu.landing_sound.play()
        pikachu.speed_x, pikachu.action = 1, 3
        pass

    @staticmethod
    def exit(pikachu, e):
        if g_down(e):
            pikachu.hit_ball()
        pass

    @staticmethod
    def do(pikachu):
        pikachu.frame = (pikachu.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        pikachu.x += pikachu.speed_x * RUN_SPEED_PPS * game_framework.frame_time
        pikachu.x = clamp(25, pikachu.x, 500 - 25)

    @staticmethod
    def draw(pikachu):
        pikachu.image.clip_draw(int(pikachu.frame) * 100, pikachu.action * 100, 100, 100, pikachu.x, pikachu.y)
        pass


class Run_left:
    @staticmethod
    def enter(pikachu, e):
        if y_150(e):
            pikachu.landing_sound.play()
        pikachu.speed_x, pikachu.action = -1, 3
        pass

    @staticmethod
    def exit(pikachu, e):
        if g_down(e):
            pikachu.hit_ball()
        pass

    @staticmethod
    def do(pikachu):
        pikachu.frame = (pikachu.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8
        pikachu.x += pikachu.speed_x * RUN_SPEED_PPS * game_framework.frame_time
        pikachu.x = clamp(25, pikachu.x, 500 - 25)

    @staticmethod
    def draw(pikachu):
        pikachu.image.clip_draw(int(pikachu.frame) * 100, pikachu.action * 100, 100, 100, pikachu.x, pikachu.y)
        pass


class Idle:
    @staticmethod
    def enter(pikachu, e):
        if y_150(e):
            pikachu.landing_sound.play()
        pikachu.action = 3
        pikachu.speed_x = 0
        pikachu.frame = 0

    @staticmethod
    def exit(pikachu, e):
        if g_down(e):
            pikachu.hit_ball()
        pass

    @staticmethod
    def do(pikachu):
        pikachu.frame = (pikachu.frame + FRAMES_PER_ACTION * ACTION_PER_TIME * game_framework.frame_time) % 8

        pass

    @staticmethod
    def draw(pikachu):
        pikachu.image.clip_draw(int(pikachu.frame) * 100, pikachu.action * 100, 100, 100, pikachu.x, pikachu.y)
        pass


class StateMachine:
    def __init__(self, pikachu):
        self.pikachu = pikachu
        self.cur_state = Idle
        self.transitions = {
            Idle: {right_down: Run_right, left_down: Run_left, left_up: Run_right, right_up: Run_left, up_down: Jump,
                   g_down: Idle},
            Run_right: {right_down: Run_right, left_down: Idle, right_up: Idle, left_up: Run_right, up_down: Jump_right,
                        g_down: Run_right},
            Run_left: {right_down: Idle, left_down: Run_left, right_up: Run_left, left_up: Idle, up_down: Jump_left,
                       g_down: Run_right},
            Jump: {right_down: Jump_right, left_down: Jump_left, left_up: Jump_right, right_up: Jump_left, y_150: Idle,
                   g_down: Jump},
            Jump_right: {right_down: Jump_right, left_down: Jump, left_up: Jump_right, right_up: Jump, y_150: Run_right,
                         g_down: Jump_right},
            Jump_left: {right_down: Jump, left_down: Jump_left, left_up: Jump, right_up: Jump_left, y_150: Run_left,
                        g_down: Jump_left}
        }

    def start(self):
        self.cur_state.enter(self.pikachu, ('NONE', 0))

    def update(self):
        self.cur_state.do(self.pikachu)

    def handle_event(self, e):
        for check_event, next_state in self.transitions[self.cur_state].items():
            if check_event(e):
                self.cur_state.exit(self.pikachu, e)
                self.cur_state = next_state
                self.cur_state.enter(self.pikachu, e)
                return True

        return False

    def draw(self):
        self.cur_state.draw(self.pikachu)


class Pika1:
    def __init__(self):
        self.x, self.y = 200, 150
        self.image = load_image(RESOURCE_PATH + 'pikachu.png')
        self.frame = 0
        self.speed_y = 0
        self.speed_x = 0
        self.action = 0
        self.state_machine = StateMachine(self)
        self.state_machine.start()
        self.move = 0
        self.jump_sound = load_wav(RESOURCE_PATH + 'WAVE141_1.wav')
        self.jump_sound.set_volume(30)
        self.landing_sound = load_wav(RESOURCE_PATH + 'WAVE142_1.wav')
        self.landing_sound.set_volume(30)
        self.pikachu_sound = load_wav(RESOURCE_PATH + 'WAVE144_1.wav')
        self.pikachu_sound.set_volume(30)

    def update(self):
        self.state_machine.update()
        pass

    def handle_event(self, event):
        self.state_machine.handle_event(('INPUT', event))
        pass

    def draw(self):
        self.state_machine.draw()
        # draw_rectangle(*self.get_bb())

    def hit_ball(self):
        if self.x - play_mode.monster_ball.x < 10:
            self.pikachu_sound.play()
            pass
        pass

    def get_bb(self):
        return self.x - 40, self.y - 50, self.x + 50, self.y + 40

    def handle_collision(self, group, other):
        if group == 'pikachu:monster_ball':
            print('pikachu:ball')
            pass
