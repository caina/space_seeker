from random import randrange
import pyglet
from pyglet.image import Animation, AnimationFrame
from cocos.sprite import *


class SpaceShip():
	
	global spriteSheet
	global spritesInSheet

	power = 0
	acceleration = 0
	maxAcceleration = 5
	minAcceleration = -5
	accelerationRate = 0.7
	gravityAction = -0.9
	spaceShipWeight = 5


	spriteSheet = pyglet.image.ImageGrid(pyglet.image.load("resources/space_ship2.gif"), 3, 3)
	spritesInSheet = spriteSheet.get_texture_sequence()
	
	def changeSpaceState(self, state):

		if state == "standart":
			return Sprite(spritesInSheet[7])
		elif state=="left":
			
			return Sprite(spritesInSheet[0])
		elif state == "right":
			return Sprite(spritesInSheet[2])
		elif state == "up":
			return Sprite(spritesInSheet[1])
	
	def CreateSpaceShip(self):
		# spaceShip = Sprite("resources/space_ship.gif")
		return SpaceShip().changeSpaceState("standart")

	def getAcceleration(self):
		if self.acceleration > self.minAcceleration:
			print "speeed doooown"
			self.acceleration -= 0.5

		return (self.spaceShipWeight * self.gravityAction) + self.acceleration		
	def boostUp(self):
		print self.acceleration 
		if self.acceleration < self.maxAcceleration:
			self.acceleration += self.accelerationRate

