class Product:
    def __init__(self, Price, Name, QRCode, Quantity):
        self.Price = Price
        self.Name = Name
        self.QRCode = QRCode
        self.Quantity = Quantity

class Person:
    def __init__(self, Name, Age, ID, Gender, Height, Weight, Phone, Material):
        self.Name = Name
        self.Age = Age
        self.ID = ID
        self.Gender = Gender
        self.Height = Height
        self.Weight = Weight
        self.Phone = Phone
        self.Material = Material


class Student(Person):
    def __init__(self, Name, Age, ID, Gender, Height, Weight, Phone, Material, Grade, Class, Score):
        super().__init__(Name, Age, ID, Gender, Height, Weight, Phone, Material)
        self.Grade = Grade
        self.Class = Class
        self.Score = Score

    def ShowInfor(self):
        print(f"{self.Grade} | {self.Class} | {self.Score}")

    def Earn():
        print("Get 10$ from father")

class Staff(Person):
    def __init__(self, Name, Age, ID, Gender, Height, Weight, Phone, Material, Sale, Role):
        super().__init__(Name, Age, ID, Gender, Height, Weight, Phone, Material)
        self.Sale = Sale
        self.Role = Role

    def Saler():
        print("Saleeeeee")

class Iphone(Product):
    def __init__(self, Price, Name, QRCode, Quantity, Generation, Color):
        super().__init__(Price, Name, QRCode, Quantity)
        self.Generation = Generation
        self.Color = Color

    def TakeAPicture():
        print("Smile~~~, Chup Chup")

    def ShowInfor(self):
        print(f"{self.Generation} | {self.Color}")

class Book(Product):
    def __init__(self, Price, Name, QRCode, Quantity, Type, Color, Author):
        super().__init__(Price, Name, QRCode, Quantity)
        self.Type = Type
        self.Color = Color
        self.Author = Author

    def Learn():
        print("Learn Something!")

    def ShowInfor(self):
        print(f"{self.Type} | {self.Color} | {self.Author}")

class QLCH:
    def __init__(self, Phone, Book, Staff):
        self.Phone = Phone
        self.Book = Book
        self.Staff = Staff