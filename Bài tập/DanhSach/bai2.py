class NhanVien:
    def __init__(self) -> None:
        self.name = None
        self.age = None
        self.address = None
        self.wage = None
        self.timeWork = None
    
    def inputInfor(self) -> None:
        self.name = input("Enter for name: ")
        self.age = int(input("Enter for age: "))
        self.address = input("Enter for address: ")
        self.wage = int(input("Enter for wage: "))
        self.timeWork = int(input("Enter for timeWork: "))

    def printInfor(self) -> None:
        print("Name:",self.name)
        print("Age:",self.age)
        print("Address:",self.address)
        print("Wage:",self.wage)
        print("TimeWork:",self.timeWork)

    def tinhThuong(self) -> int:
        if self.timeWork >= 200:
            return self.wage * 0.2
        if self.timeWork >= 100:
            return self.wage * 0.1
        return 0

Trung = NhanVien()
Trung.inputInfor()
Trung.printInfor()
print("Trung'wage:",Trung.tinhThuong())