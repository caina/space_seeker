from cocos.director import *
from cocos.scene import *
from cocos.layer import *
from cocos.sprite import *
from cocos.euclid import Point2
from game.SpaceShip import SpaceShip

class TutorialLayer(ColorLayer):
	is_event_handler = True

	global LEFT  
	global UP
	global RIGHT
	global DOWN
	# global LAST_KEY
	global spaceShip

	spaceShip = SpaceShip()

	LEFT = 65361  
	UP = 65362  
	RIGHT = 65363  
	DOWN = 65364  
	LAST_KEY = DOWN

	width = 0
	height = 0

	def __init__(self):
		super(TutorialLayer, self).__init__(0,0,100,255)

		width,height = director.get_window_size()
		self.ship = spaceShip.CreateSpaceShip()
		self.ship.position = self.width/2, self.height/2
		self.add(self.ship)

		self.chars_pressed = set()
		self.schedule(self.update)
		print self.ship

	def on_key_press(self, key, modifiers):
		self.chars_pressed.add(key)

	def on_key_release(self, key, modifiers):
		self.chars_pressed.remove(key)

	def update(self, dt):
		x,y = self.ship.position

		if LEFT in self.chars_pressed:
			if self.LAST_KEY != LEFT:
				self.remove(self.ship)
				self.ship = spaceShip.changeSpaceState("left")
				self.add(self.ship)
			x -= 2
			self.LAST_KEY = LEFT

		if UP in self.chars_pressed:
			if self.LAST_KEY != UP:
				self.remove(self.ship)
				self.ship = spaceShip.changeSpaceState("up")
				self.add(self.ship)
			
			y += 2
			self.LAST_KEY = UP
			spaceShip.boostUp()
		if RIGHT in self.chars_pressed:
			if self.LAST_KEY != RIGHT:
				self.remove(self.ship)
				self.ship = spaceShip.changeSpaceState("right")
				self.add(self.ship)
			self.LAST_KEY = RIGHT
			x += 2
		if DOWN in self.chars_pressed:
			if self.LAST_KEY != DOWN:
				self.remove(self.ship)
				self.ship = spaceShip.changeSpaceState("standart")
				self.add(self.ship)
			self.LAST_KEY = DOWN
				
		#print y, self.height
		
		y += spaceShip.getAcceleration()
		#print y
		if y < 0:
			y= self.height-25

		self.ship.position = (x,y)


director.init()
director.run(Scene(TutorialLayer()))