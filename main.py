from pyray import *
from bird import Bird
from settings import *
init_window(WINDOW_WIDTH, WINDOW_HEIGHT, "FlappyAI")

set_target_fps(60)
bird = Bird(100,100)
while not window_should_close():
	begin_drawing()
	clear_background((53, 35, 84))
	bird.draw()
	bird.update()
	end_drawing()
close_window()