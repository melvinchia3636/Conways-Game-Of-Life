'''
Any live cell with two or three live neighbours survives.
Any dead cell with three live neighbours becomes a live cell.
All other live cells die in the next generation. Similarly, all other dead cells stay dead.
'''

import pygame
import copy
import math

class game_of_life():
	def __init__(self):
		pygame.init()
		self.screen = pygame.display.set_mode((1000, 1000))
		self.data = [[0 for j in range(100)] for i in range(100)]
		self.run = True
		self.clock = pygame.time.Clock()
		self.start = False
		self.initial = True

	def get_neighbour(self, i, j):
		neighbour = [[i+1, j], [i-1, j], [i, j+1], [i, j-1], [i+1, j+1], [i-1, j+1], [i+1, j-1], [i-1, j-1]]
		neighbour = [i for i in neighbour if 0<=i[0]<100 and 0<=i[1]<100]
		return neighbour

	def next_generation(self):
		self.last_generation = copy.deepcopy(self.data)
		for i in range(len(self.data)):
			for j in range(len(self.data[i])):
				self.count = [self.last_generation[k[0]][k[1]] for k in self.get_neighbour(i, j)].count(1)
				if self.last_generation[i][j] == 1:
					self.data[i][j] = 1 if self.count in range(2, 4) else 0
				elif self.last_generation[i][j] == 0:
					self.data[i][j] = 1 if self.count == 3 else 0

	def update(self):
		self.screen.fill((0, 0, 0))
		for i in range(len(self.data)):
			for j in range(len(self.data[i])):
				if self.data[i][j] == 1:
					pygame.draw.rect(self.screen, (255, 255, 255), (j*10, i*10, 10, 10))

	def user_initial(self):
		if self.initial:
			if pygame.mouse.get_pressed()[0]:
				x, y = pygame.mouse.get_pos()
				self.data[math.floor(y/10)][math.floor(x/10)] = 1
			if pygame.mouse.get_pressed()[2]:
				x, y = pygame.mouse.get_pos()
				self.data[math.floor(y/10)][math.floor(x/10)] = 0
			if pygame.mouse.get_pressed()[1]:
				self.initial = False
				self.start = True
			self.clock.tick(60)

	def start_game(self):
		while self.run:
			for event in pygame.event.get():  
				if event.type == pygame.QUIT:  
					self.run = False
			self.update()
			if self.start:
				self.next_generation()
				self.clock.tick(10)
			self.user_initial()
			pygame.display.update()

game = game_of_life()
game.start_game()
