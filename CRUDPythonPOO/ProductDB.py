 
class ProductDB():
    def __init__(self):
        self.Products = []

    def AddProduct(self, product):
        self.Products.append(product)

    def getProduct(self, name):
        for product in self.Products:
            if product.Name == name:
                return product
        return None

    def updateProductPrice(self, name, price):
        product = self.getProduct(name)
        if product:             
            product.updatePrice(price)

           

    def deleteProduct(self, name):
        product = self.getProduct(name)
        if product:
            self.Products.remove(product)
        else:
            print("Sorry! The product does not Exist!")



    def showProducts(self):
        for product in self.Products:
            print(product)

