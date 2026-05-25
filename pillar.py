from settings import *
import random

class Pillar:
	def __init__(self, x):
		self.x = x

		self.width = 80
		self.gap_height = 150

		self.speed = 3

		# random gap position
		self.gap_y = random.randint(100, WINDOW_HEIGHT - 100)

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

