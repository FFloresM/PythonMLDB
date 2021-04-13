class Punto2D():
	"""Punto en dos dimensiones"""
	def __init__(self, x=0, y=0):
		self.x = x
		self.y = y

	def getX(self):
		return self.x

	def getY(self):
		return self.y

	def setX(self, x):
		self.x = x

	def setY(self, y):
		self.y = y

	def __str__(self):
		return f"x = {self.getX()}, y = {self.getY()}"

	def __repr__(self):
		return f"x = {self.getX()}, y = {self.getY()}"

	def suma(self, x, y):
		return self.getX() + x, self.getY() + y

	def distancia(self, x, y):
		return ((self.getX()-x)**2 + (self.getY()-y)**2)**(1/2)

	def distancia(self, punto):
		return ((self.getX()-punto.getX())**2 + (self.getY()-punto.getY())**2)**(1/2)








        