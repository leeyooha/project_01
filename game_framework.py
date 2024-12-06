import time

frame_time = 0.0  # 전역 frame_time 정의

class ModeStack:
    def __init__(self):
        self.stack = []
        self.running = False

    def change_mode(self, mode):
        if self.stack:
            self.stack[-1].finish()
            self.stack.pop()
        self.stack.append(mode)
        mode.init()

    def push_mode(self, mode):
        if self.stack:
            self.stack[-1].pause()
        self.stack.append(mode)
        mode.init()

    def pop_mode(self):
        if self.stack:
            self.stack[-1].finish()
            self.stack.pop()
        if self.stack:
            self.stack[-1].resume()

    def quit(self):
        self.running = False

    def run(self, start_mode):
        global frame_time
        self.running = True
        self.stack = [start_mode]
        start_mode.init()

        current_time = time.time()

        while self.running:
            if self.stack:
                current_mode = self.stack[-1]
                current_mode.handle_events()
                current_mode.update()
                current_mode.draw()

            frame_time = time.time() - current_time
            current_time += frame_time

        while self.stack:
            self.stack[-1].finish()
            self.stack.pop()


# 전역 스택 인스턴스
stack = ModeStack()

# 전역 함수
def run(start_mode):
    stack.run(start_mode)

# game_framework.py
def change_mode(self, mode):
    if self.stack:  # 현재 모드가 존재하면
        self.stack[-1].finish()  # 현재 모드 종료
        self.stack.pop()  # 스택에서 제거
    self.stack.append(mode)  # 새 모드 추가
    mode.init()  # 새 모드 초기화

