
class Vehiculo():
	""" Clase para crear vehículos"""
	def __init__(self, color, ruedas):
		self.color = color
		self.ruedas = ruedas

	#getters
	def getColor(self):
		return self.color

	def getRuedas(self):
		return self.ruedas

	#setters
	def setColor(self, color):
		self.color = color

	def setRuedas(self, ruedas):
		self.ruedas = ruedas

	def mostrar(self):
		print("color", self.color)
		print("numero de ruedas", self.ruedas)


class Moto(Vehiculo):
	"""MOTO"""
	def __init__(self, color, cilindrada):
		Vehiculo.__init__(self,color, 2)
		self.cilindrada = cilindrada




class Audiencia():
	"""clase para crear audiencias"""
	def __init__(self, rit, tipo_audiencia, materia):
		self.rit = rit
		self.tipo_audiencia = tipo_audiencia
		self.materia = materia
		#self.bloques = 0

	def asignarBloques(self, n):
		self.bloques = n

	def mostrar(self):
		print(self.rit, self.tipo_audiencia, self.materia, self.bloques)

	def setAbogado(self, nombre, insti):
		self.abogado = nombre
		self.insti = insti

	def plazo(self):
		if self.materia == "vulneración de derechos":
			self.plazo_max = 10

	def duracion(self):
		if self.materia == "" and self.tipo_audiencia == "":
			self.bloques = 2



