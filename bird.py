from settings import *
from network import Network
import numpy as np
from random import choice
colors = [
    Color(255, 0, 0, 255),      # red
    Color(0, 255, 0, 255),      # green
    Color(0, 0, 255, 255),      # blue
    Color(0, 255, 255, 255),    # aqua
    Color(255, 192, 203, 255),  # pink
    Color(0, 0, 128, 255),      # navy
    Color(128, 0, 128, 255),    # purple
    Color(255, 255, 0, 255),    # yellow
    Color(255, 165, 0, 255),    # orange
    Color(0, 128, 128, 255),    # teal
    Color(50, 205, 50, 255),    # lime
    Color(255, 0, 255, 255),    # magenta
]

class Bird:
	def __init__(self, x, y):
		self.x = x
		self.y = y

		self.radius = 20
		self.color = choice(colors)
		

		self.velocity_y = 0

		# gravity settings
		self.gravity = 0.5
		self.max_fall_speed = 12

	def control(self):
		if is_key_pressed(KEY_SPACE):
			return True
		return False

	def update(self):
		# flap
		if self.control():
			self.velocity_y = -8
			

		# gravity
		self.velocity_y += self.gravity

		if self.velocity_y > self.max_fall_speed:
			self.velocity_y = self.max_fall_speed

		# move
		self.y += self.velocity_y

		# top collision
		ceiling_y = self.radius

		if self.y < ceiling_y:
			self.y = ceiling_y
			self.velocity_y = 0

		# bottom collision
		floor_y = WINDOW_HEIGHT - self.radius

		if self.y > floor_y:
			self.y = floor_y
			self.velocity_y = 0

	def draw(self):
		draw_circle(
			int(self.x),
			int(self.y),
			self.radius,
			self.color
		)

class AgenticBird(Bird):
	def __init__(self, x, y):
		super().__init__(x, y)
		self.network = Network(2,4,1)
		self.thrashold = .5

	def control(self):
		data = np.array([self.x, self.y])
		decision = self.network.forward(data)
		if decision >= self.thrashold:
			return True
		else:
			return False
	