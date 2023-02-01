from Product import Product
from ProductDB import ProductDB


productDB = ProductDB()
productDB.AddProduct(Product('Smartphone', 555))
productDB.AddProduct(Product('Laptop Envy', 1500))
print("List of Products:")
productDB.showProducts()

