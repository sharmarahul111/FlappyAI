from game import Game
from bird import Bird, AgenticBird
from settings import *

init_window(WINDOW_WIDTH, WINDOW_HEIGHT, "FlappyAI")

set_target_fps(60)
game = Game()
game.birds += [AgenticBird() for _ in range(10)]

while not window_should_close():
	game.update()

	begin_drawing()
	clear_background((53, 35, 84))

	for bird in game.birds:
		bird.draw()

	game.pillars.draw()

	end_drawing()

close_window()