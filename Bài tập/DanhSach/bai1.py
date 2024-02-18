# class SoHoc:
#     def __init__(self):
#         self.number1 = 0
#         self.number2 = 0
#     def inputinfor(self):
#         self.number1 = int(input("enter for number 1 : "))
#         self.number2 = int(input("enter for number 2 : "))
#     def printinfor(self):
#         print("number 1 :",self.number1)
#         print("number 2 :",self.number2)
#     def add(self):
#         return self.number1 + self.number2
#     def subtract(self):
#         return self.number1 - self.number2
#     def multi(self):
#         return self.number1 * self.number2
#     def division(self):
#         return self.number1 / self.number2
    
# a = SoHoc()
# a.inputinfor()
# a.printinfor()
# print("add:",a.add())
# print("subtract:",a.subtract())
# print("multi:",a.multi())
# print("division:",a.division())

class SoHoc:
    def __init__(self):
        self._number1 = 0
        self._number2 = 0

    def get_number1(self):
        return self._number1

    def set_number1(self, value):
        self._number1 = value

    def get_number2(self):
        return self._number2

    def set_number2(self, value):
        self._number2 = value

    def inputInfo(self):
        self._number1 = float(input("Nhập số thứ nhất: "))
        self._number2 = float(input("Nhập số thứ hai: "))

    def printInfo(self):
        print("Số thứ nhất:", self._number1)
        print("Số thứ hai:", self._number2)

    def addition(self):
        return self._number1 + self._number2

    def subtract(self):
        return self._number1 - self._number2

    def multi(self):
        return self._number1 * self._number2

    def division(self):
        if self._number2 == 0:
            return "Không thể chia cho 0!"
        return self._number1 / self._number2


# Sử dụng lớp SoHoc
a = SoHoc()
a.inputInfo()

a._number1 = 10

print("Thông tin số học:")
a.printInfo()

print("Tổng:", a.addition())
print("Hiệu:", a.subtract())
print("Tích:", a.multi())
print("Thương:", a.division())
