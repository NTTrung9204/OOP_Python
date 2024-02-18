class SV:
    def __init__(self, Name, Mssv, Gender, DTB):
        self.Name = Name
        self.Mssv = Mssv
        self.Gender = Gender
        self.DTB = DTB

    def GetMSSV(self):
        return self.Mssv
    
    def __eq__(self, other):
        return self.Name == other.Name and self.Mssv == other.Mssv and self.Gender == other.Gender and self.DTB == other.DTB
    
    def __str__(self):
        return f"Name: {self.Name}\nMssv: {self.Mssv}\nGender: {self.Gender}\nDTB: {self.DTB}\n"
    
class QLSV:
    def __init__(self):
        self.ListOfSV = []
        self.Quantity = 0

    def AddSV(self, SV):
        self.ListOfSV.append(SV)
        self.Quantity += 1
    
    def InsertSV(self, index, SV):
        self.ListOfSV.insert(index, SV)
        self.Quantity += 1

    def IndexOfSV(self, SV):
        for index in range(self.Quantity):
            if self.ListOfSV[index].Mssv == SV.Mssv:
                return index

    def RemoveSV(self, SV):
        self.ListOfSV = [Item for Item in self.ListOfSV if Item.Mssv != SV.Mssv]
        self.Quantity -= 1

    def RemoveAtSV(self, index):
        self.ListOfSV.pop(index)
        self.Quantity -= 1

    def UpdateSV(self, SV):
        index = self.IndexOfSV(SV)
        self.ListOfSV[index].Name = input("\nEnter for Name of SV : ")
        self.ListOfSV[index].Gender = bool(input("\nEnter for Gender of SV : "))
        self.ListOfSV[index].DTB = float(input("\nEnter for DTB of SV : "))
    
    def __str__(self):
        return "List Of SV : \n{}\nQuantity : {}".format("\n".join(SV.Name for SV in self.ListOfSV), self.Quantity)
    
    def __getitem__(self, index):
        return self.ListOfSV[index]
    
    def __setitem__(self, index, SV):
        self.ListOfSV[index] = SV

Trung = SV("Trung", 12213, True, 9.0)
Phong = SV("Phong", 12212, False, 3.0)
Vy = SV("Vy", 12211, False, 9.5)

Model_QLSV = QLSV()

Model_QLSV.AddSV(Trung)
Model_QLSV.AddSV(Phong)
Model_QLSV.AddSV(Vy)

Model_QLSV.RemoveSV(Phong)

Model_QLSV[1] = Phong

print(Model_QLSV)


