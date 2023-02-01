class Product:
	def __init__(self, name, price):
		self.Name = name
		self.Price = price

		
	def updatePrice(self, price):
		self.Price = price
		 
	


	def __str__(self): return f"{self.Name}: {self.Price}"


		 
     