from pyray import *
from bird import Bird
from pillar import Pillars
from settings import *

init_window(WINDOW_WIDTH, WINDOW_HEIGHT, "FlappyAI")

set_target_fps(60)
bird = Bird(100, 100)
pillars = Pillars()

while not window_should_close():
	bird.update()
	pillars.update()

	begin_drawing()
	clear_background((53, 35, 84))

	bird.draw()
	pillars.draw()

	end_drawing()

close_window()