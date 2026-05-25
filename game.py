from settings import *
from bird import Bird
from pillar import Pillars

class Game:
	def __init__(self):
		self.birds = []
		self.pillars = Pillars()
		self.generation = 1

	def check_collision(self, bird, pillar):
		# simple AABB collision
		bird_left = bird.x - bird.radius
		bird_right = bird.x + bird.radius
		bird_top = bird.y - bird.radius
		bird_bottom = bird.y + bird.radius

		# top pipe
		top_pipe_bottom = pillar.gap_y - pillar.gap_height // 2

		# bottom pipe
		bottom_pipe_top = pillar.gap_y + pillar.gap_height // 2

		pillar_left = pillar.x
		pillar_right = pillar.x + pillar.width

		# collision with pillar horizontally
		if bird_right > pillar_left and bird_left < pillar_right:
			# collision with top pipe
			if bird_top < top_pipe_bottom:
				return True

			# collision with bottom pipe
			if bird_bottom > bottom_pipe_top:
				return True

		return False

	def update(self):
		# update pillars
		self.pillars.update()

		# get next pillar to project on
		next_pillar = None
		if self.pillars.pillars:
			next_pillar = self.pillars.pillars[0]
			for pillar in self.pillars.pillars:
				if pillar.x+pillar.width > Bird.x - Bird.radius:
					next_pillar = pillar
					# pillar.color = RED
					break
		# update birds
		for bird in self.birds:
			bird.set_target(next_pillar)
			bird.update()

		# collision check
		for bird in self.birds[:]:
			for pillar in self.pillars.pillars:
				if self.check_collision(bird, pillar):
					if len(self.birds) == 1:
						self.reset(self.birds[0])
					else:
						self.birds.remove(bird)
					break
	
	def reset(self, best_bird: AgenticBird):
		self.birds = [best_bird] + best_bird.mutate(500, .1) 
		self.pillars = Pillars()
		self.generation += 1