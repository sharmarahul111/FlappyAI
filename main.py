from game import Game
from bird import Bird, AgenticBird
from settings import *

init_window(WINDOW_WIDTH, WINDOW_HEIGHT, "FlappyAI")

set_target_fps(60)
game = Game()
game.birds += [AgenticBird() for _ in range(500)]

while not window_should_close():
	game.update()

	begin_drawing()
	clear_background((53, 35, 84))

	for bird in game.birds:
		bird.draw()
	game.pillars.draw()
	draw_text(f"GENERATION: {game.generation}", 200, 20, 35, WHITE)
	draw_text(f"BIRDS: {len(game.birds)}", 200, 60, 25, WHITE)


	end_drawing()

close_window()