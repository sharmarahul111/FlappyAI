from settings import *
import random

class Pillar:
	def __init__(self, x):
		self.x = x

		self.width = 80
		self.gap_height = 150

		self.speed = 3

		# random gap position
		self.gap_y = random.randint(200, WINDOW_HEIGHT - 200)

	def update(self):
		self.x -= self.speed

	def draw(self):
		# top pipe
		top_height = self.gap_y - self.gap_height // 2
		draw_rectangle(
			int(self.x),
			0,
			self.width,
			top_height,
			GREEN
		)

		# bottom pipe
		bottom_y = self.gap_y + self.gap_height // 2
		bottom_height = WINDOW_HEIGHT - bottom_y

		draw_rectangle(
			int(self.x),
			int(bottom_y),
			self.width,
			bottom_height,
			GREEN
		)

class Pillars:
	def __init__(self):
		self.pillars = []

		self.spawn_timer = 0
		self.spawn_interval = 120

	def create(self):
		# spawn at right edge
		new_x = WINDOW_WIDTH + 50
		self.pillars.append(Pillar(new_x))

	def update(self):
		# spawn logic
		self.spawn_timer += 1
		if self.spawn_timer >= self.spawn_interval:
			self.create()
			self.spawn_timer = 0

		# update pillars
		for pillar in self.pillars:
			pillar.update()

		# remove off-screen pillars
		self.pillars = [p for p in self.pillars if p.x + p.width > 0]

	def draw(self):
		for pillar in self.pillars:
			pillar.draw()