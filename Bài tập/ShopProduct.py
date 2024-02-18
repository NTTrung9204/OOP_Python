class Product:
    def __init__(self, name, description, price, listRate):
        self.name = name
        self.description = description
        self.price = price
        self.listRate = listRate

    def viewInfor(self):
        print(f"INFORMATION OF {self.name}")
        print(f"Description : {self.description}")
        print(f"Price : {self.price}")
        print(f"List rate : {self.listRate}")

class Shop:
    def __init__(self):
        self.listProduct = []

    def productList(self):
        return self.listProduct
    
    def addProduct(self):
        print("Enter for infor of product")
        name = input("Name : ")
        description = input("Description : ")
        price = int(input("Price : "))
        listRate = list(map(int,input("List rate : ").split()))
        self.listProduct.append(Product(name, description, price, listRate))
    
    def removeProduct(self):
        print("Enter for name of product need to remove!")
        nameOfProduct = input("Enter for name :")
        for product in self.productList():
            listProductNew = []
            if product.name != nameOfProduct:
                listProductNew.append(product)
        self.listProduct = listProductNew
    
    def iterateProductList(self):
        print("ALL PRODUCT : ")
        for product in self.productList():
            print(f"Name : {product.name}, rate : {sum(product.listRate)/len(product.listRate)}")

    def searchProduct(self):
        print("Search for product!")
        priceA, priceB = map(int,input("Enter for price. Ex : 24-40 : ").split("-"))
        for product in self.productList():
            if product.price >= priceA and product.price <= priceB:
                product.viewInfor()

class ProductManagementSystem:
    def main():
        shop = Shop()
        while(True):
            print("1. Add new product")
            print("2. remove product")
            print("3. Iterate product list")
            print("4. Search product")
            print("5. Exit")
            option = int(input("Enter for your choose : "))
            match option:
                case 1:
                    shop.addProduct()
                case 2:
                    shop.removeProduct()
                case 3:
                    shop.iterateProductList()
                case 4:
                    shop.searchProduct()
                case _:
                    break

if __name__ == "__main__":
    ProductManagementSystem.main()
