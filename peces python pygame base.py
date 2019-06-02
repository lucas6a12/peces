import random
import math

def generarCardumen(n, w, h, speed=10):
	boids = []
	for i in range(n):
		x, y		= random.randint(1, w), random.randint(1, h)
		course		= random.uniform(-1, 1)
		vx, vy		= random.randint(1, speed)/speed, random.randint(1, speed)/speed
		boids.append(
			[
				[x, y],		# 0 [0, 1]
				[vx, vy],	# 1 [0, 1]
			])
	return boids

def distancia(i, j):
	return i*j


def corregir(boid, width, height, border=25):
	return boid

def moveCloser(fish, boids): # COHESION
	return fish

def moveWith(fish, boids): # ALINEAMIENTO
	return fish

def moveAway(fish, boids, min_dist=20): # SEPARATION
	return fish

def move(fish, max_speed):
	return fish

def vecindad(pez_i, boids, max_distance):
	return boids

import random, math
import pygame, sys
from pygame.locals import *


SIZE 				= WIDTH, HEIGHT	= 800, 600
MAX_SPEED			= 10
GOLDFISH, OCEANBLUE	= Color(243, 134, 48), Color(28, 107, 160)
MAX_DISTANCE		= 100
N					= 100

pygame.init()
screen = pygame.display.set_mode(SIZE)
boids = generarCardumen(N, WIDTH, HEIGHT, 10)
while True:
	screen.fill(OCEANBLUE)
	for i in range(len(boids)):
		close		= vecindad(i, boids, MAX_DISTANCE)
		boids[i]	= moveCloser(boids[i], close) # COHESION
		boids[i]	= moveWith(boids[i], close) # ALINEAMIENTO
		boids[i]	= moveAway(boids[i], close, 20) # SEPARATION

		boids[i] = corregir(boids[i], WIDTH, HEIGHT)
		boids[i] = move(boids[i], MAX_SPEED) # MOVER
		try:
			pygame.draw.circle(screen, GOLDFISH, [int(boids[i][0][0]), int(boids[i][0][1])], 3, 0)
		except:
			print(boids[i])
	pygame.display.flip()
	pygame.time.delay(29)

	for event in pygame.event.get():
		if event.type == QUIT or (event.type == KEYDOWN and event.key == K_ESCAPE): # Se cierra el programa
			pygame.quit()
			sys.exit()
    
