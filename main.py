from pico2d import *
import game_framework
import logo_mode as start_mode
import title_mode

open_canvas(1000, 700)
game_framework.run(start_mode)
close_canvas()