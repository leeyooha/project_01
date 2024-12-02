import time

class ModeStack:
    def __init__(self):
        self.stack = []
        self.running = False
        self.frame_time = 0.0

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

            self.frame_time = time.time() - current_time
            frame_rate = 1.0 / self.frame_time if self.frame_time > 0 else float('inf')
            current_time += self.frame_time
            # print(f'Frame Time: {self.frame_time:.6f}, Frame Rate: {frame_rate:.2f}')

        while self.stack:
            self.stack[-1].finish()
            self.stack.pop()
