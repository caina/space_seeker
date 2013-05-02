from random import randrange
import pyglet
from pyglet.image import Animation, AnimationFrame
from cocos.sprite import *


class SpaceShip():
	
	global spriteSheet
	global spritesInSheet

	spriteSheet = pyglet.image.ImageGrid(pyglet.image.load("resources/space_ship2.gif"), 3, 3)
	spritesInSheet = spriteSheet.get_texture_sequence()
	
	def changeSpaceState(self, state):

		if state == "standart":
			return Sprite(spritesInSheet[7])
		elif state=="left":
			print "oi"
			return Sprite(spritesInSheet[0])
		elif state == "right":
			return Sprite(spritesInSheet[2])
		elif state == "up":
			return Sprite(spritesInSheet[1])
	
	def CreateSpaceShip(self):
		# spaceShip = Sprite("resources/space_ship.gif")
		return SpaceShip().changeSpaceState("standart")
