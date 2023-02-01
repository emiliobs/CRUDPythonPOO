from Product import Product
from ProductDB import ProductDB


productDB = ProductDB()
productDB.AddProduct(Product('Smartphone', 555))
productDB.AddProduct(Product('Laptop Envy', 1500))
productDB.AddProduct(Product('Delete', 000000000))
productDB.AddProduct(Product('Bike', 345))
productDB.AddProduct(Product('Phone x', 545454))
productDB.AddProduct(Product('Delete 1', 4353545))
print("List of Products:")
productDB.showProducts()

print("=============================")
print()

#print("Select a Product by Name:")
productByName = productDB.getProduct("Laptop Envy")
print(f"Select a Product by Name: {productByName.Name}")
print(productByName)

print("=============================")
print()

print("Updated Price of Product by Name!")
productDB.updateProductPrice("Smartphone", "3456788")
productDB.updateProductPrice("Bike", "2500")

productDB.showProducts()


print("=============================")
print()

print("Deleted a Product by Name doesn't Exist!")
productDB.deleteProduct('Deletes')
print()
productDB.showProducts()


print("=============================")
print()

print("Deleted Product by Name!")
productDB.deleteProduct('Delete')
productDB.deleteProduct("Delete 1")
print()
productDB.showProducts()


