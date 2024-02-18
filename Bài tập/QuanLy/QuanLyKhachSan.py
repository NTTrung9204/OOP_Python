import random
import time

class BinaryTree:
    def __init__(self):
        self.Root = None

    def Insert(self, Node):
        if self.Root == None : 
            self.Root = Node
        else:
            self._InsertRecursive(self.Root, Node)

    def _InsertRecursive(self, CurrentNode, Node):
        if CurrentNode.Values < Node.Values:
            if CurrentNode.Right == None : CurrentNode.Right = Node
            else : self._InsertRecursive(CurrentNode.Right, Node)
        if CurrentNode.Values > Node.Values:
            if CurrentNode.Left == None : CurrentNode.Left = Node
            else : self._InsertRecursive(CurrentNode.Left, Node)

    def DisplayLNR(self):
        if self.Root is None : print("Tree don't have any elements!")
        else :
            self._DisplayLNRRecursive(self.Root)
    
    def _DisplayLNRRecursive(self, CurrentNode):
        if CurrentNode is not None:
            self._DisplayLNRRecursive(CurrentNode.Left)
            print(CurrentNode)
            self._DisplayLNRRecursive(CurrentNode.Right)

    def NumberOfLeaveNode(self):
        return self._NumberOfLeaveNodeRecursive(self.Root)
    
    def _NumberOfLeaveNodeRecursive(self, CurrentNode):
        if CurrentNode is None : 
            return 0
        if CurrentNode.Left is None and CurrentNode.Right is None : 
            return 1
        
        LeftLeaveNode = self._NumberOfLeaveNodeRecursive(CurrentNode.Left)
        RightLeaveNode = self._NumberOfLeaveNodeRecursive(CurrentNode.Right)

        return LeftLeaveNode + RightLeaveNode
    
    def NumberOfNode(self):
        return self._NumberOfNodeRecursive(self.Root)
    
    def _NumberOfNodeRecursive(self, CurrentNode):
        if CurrentNode is None : 
            return 0
        
        LeftNode = self._NumberOfNodeRecursive(CurrentNode.Left)
        RightNode = self._NumberOfNodeRecursive(CurrentNode.Right)

        return LeftNode + RightNode + 1
    
    def DepthOfTree(self):
        return self._DepthOfTreeRecursive(self.Root)
    
    def _DepthOfTreeRecursive(self, CurrentNode):
        if CurrentNode is None:
            return 0
        
        LeftDepth = self._DepthOfTreeRecursive(CurrentNode.Left)
        RightDepth = self._DepthOfTreeRecursive(CurrentNode.Right)

        return max(LeftDepth, RightDepth) + 1
    
    def Delete(self, Node):
        self.Root = self._Delete(self.Root, Node)

    def _Delete(self, Root, Node):
        if Root is None:
            return Root
        if Node.Values < Root.Values:
            Root.Left = self._Delete(Root.Left, Node)
        elif Node.Values > Root.Values:
            Root.Right = self._Delete(Root.Right, Node)
        else:
            if Root.Left is None:
                return Root.Right
            elif Root.Right is None:
                return Root.Left
            Root.Values = self._FindMinValue(Root.Right)
            Root.Right = self._Delete(Root.Right, Root)
        return Root

    def _FindMinValue(self, Node):
        current = Node
        while current.Left is not None:
            current = current.Left
        return current.Values

class Person:
    def __init__(self, Name, PhoneNumber, BirthDay, Schedule):
        self.Name = Name
        self.ID = self.CreateID()
        self.PhoneNumber = PhoneNumber
        self.BirthDay = BirthDay
        self.Schedule = Schedule

    def SetSchedule(self, Schedule):
        self.Schedule = Schedule

    def GetSchedule(self):
        return self.Schedule
    
    def ShowInfor(self):
        return f"{self.Name} | {self.PhoneNumber} | {self.Schedule}"

    def UpdateInfor(self):
        self.Name = input(f"Enter for Name of Person {self.ID}/{self.PhoneNumber} : ")

    def CreateID(self):
        return int(''.join([str(random.randint(0, 9)) for _ in range(10)]))
    
    def __str__(self):
        return f"{self.Name:7}{self.PhoneNumber:8}   {self.BirthDay:12}{self.ID:17}"

class Employee(Person):
    def __init__(self, Name, PhoneNumber, BirthDay, Position, Schedule):
        super().__init__(Name, PhoneNumber, BirthDay, Schedule)
        self.Position = Position
        self.IdEmployee = self.__IdEmployee()

    def SetPosition(self, Position):
        self.Position = Position

    def GetPosition(self):
        return self.Position
    
    def __IdEmployee(self):
        return str(self.ID) + str(self.PhoneNumber) + str(self.ID * self.PhoneNumber)[-1:-5] + str(len(self.Position))
    
    def ShowInfor(self):
        return super().ShowInfor() + f" | {self.Position}"
    
class Customer(Person):
    def __init__(self, Name, PhoneNumber, BirthDay, Schedule, Room):
        super().__init__(Name, PhoneNumber, BirthDay, Schedule)
        self.Room = Room
        self.IdCustomer = self.__IdCustomer()

    def __IdCustomer(self):
        return str(self.ID) + str(self.PhoneNumber) + str(self.ID * self.PhoneNumber)[-1:-5] + str(len(self.Room))

    def GetRoom(self):
        return self.Room
    
    def SetRoom(self, Room):
        self.Room = Room

class Node(Customer):
    def __init__(self, Name, PhoneNumber, BirthDay, Schedule, Room):
        super().__init__(Name, PhoneNumber, BirthDay, Schedule, Room)
        self.Values = self.CreateID()
        self.Left = None
        self.Right = None

class Room:
    def __init__(self, Price, Color, Area, TypeRoom, IdRoom, MaxAmount = 5, CurrentAmount = 0):
        self.Price = Price
        self.MaxAmount = MaxAmount
        self.CurrentAmount = CurrentAmount
        self.Color = Color
        self.Area = Area
        self.TypeRoom = TypeRoom
        self.IdRoom = IdRoom

    def GetMaxAmount(self):
        return self.MaxAmount
    
    def SetCurrentAmount(self, Amount):
        self.CurrentAmount = Amount

    def GetIdRoom(self):
        return self.IdRoom
    
    def UpdateRoom(self):
        self.Price = int(input(f"Enter for Price of Room {self.TypeRoom}/{self.IdRoom} : "))

    def ShowRoom(self):
        return f"{self.TypeRoom} | {self.IdRoom} | {self.Price} | {self.MaxAmount} | {self.CurrentAmount} | {self.Color} | {self.Area}"
    
class VipRoom(Room):
    def __init__(self, Price, Color, Area, TypeRoom, IdRoom, Services, MaxAmount = 5, CurrentAmount = 0):
        super().__init__(Price, Color, Area, TypeRoom, IdRoom, MaxAmount, CurrentAmount)
        self.Services = Services

    def ShowRoom(self):
        return super().ShowRoom() + f" | {self.Services}"

class ManageRoom:
    def __init__(self, RoomSize):
        self.ListRoomSize = RoomSize
        self.ListOfRoom = {}
        self.ListCurrentRoom = 0

    def AddRoom(self, Room):
        if self.ListCurrentRoom < self.ListRoomSize:
            if Room.TypeRoom not in self.ListOfRoom:
                self.ListOfRoom[Room.TypeRoom] = [Room]
            else : self.ListOfRoom[Room.TypeRoom].append(Room)
            self.ListCurrentRoom += 1
            print("=======| Add Room Successfully! |=======")
        else : print("=======| Add Room Failure! |=======")

    def ShowListRoom(self):
        print("\nList of Room\n")
        for TypeRoom in self.ListOfRoom:
            for Room in self.ListOfRoom[TypeRoom]:
                print(Room.ShowRoom())

    def UpdateRoom(self, IdRoom):
        for TypeRoom in self.ListOfRoom:
            for Room in self.ListOfRoom[TypeRoom]:
                if Room.IdRoom == IdRoom:
                    Room.UpdateRoom()
                    print("=======| Update Room Successfully! |=======")
                    return

    def DeleteRoom(self, IdRoom):
        for TypeRoom in self.ListOfRoom:
            for Room in self.ListOfRoom[TypeRoom]:
                if Room.IdRoom == IdRoom:
                    self.ListOfRoom[TypeRoom].remove(Room)
                    print("=======| Update Room Successfully! |=======")
                    return

class ManageEmployee:
    def __init__(self, EmployeeSize):
        self.EmployeeSize = EmployeeSize
        self.ListEmployee = {}
        self.CurrentEmployee = 0

    def AddEmployee(self, Employee):
        if self.CurrentEmployee < self.EmployeeSize:
            if Employee.Position not in self.ListEmployee:
                self.ListEmployee[Employee.Position] = [Employee]
            else : self.ListEmployee[Employee.Position].append(Employee)
            self.CurrentEmployee += 1
            print("=======| Add Employee Successfully! |=======")
        else : print("=======| Add Employee Failure! |=======")

    def ShowListEmployee(self):
        print("\nAll Employee\n")
        for Position in self.ListEmployee:
            for Employee in self.ListEmployee[Position]:
                print(Employee.ShowInfor())

    def UpdateEmployee(self, IdEmployee):
        for Position in self.ListEmployee:
            for Employee in self.ListEmployee[Position]:
                if Employee.IdEmployee == IdEmployee:
                    Employee.UpdateInfor()
                    print("=======| Update Employee Successfully! |=======")
                    return

    def DeleteEmployee(self, IdEmployee):
        for Position in self.ListEmployee:
            for Employee in self.ListEmployee[Position]:
                if Employee.IdEmployee == IdEmployee:
                    self.ListEmployee[Position].remove(Employee)
                    print("=======| Delete Employee Successfully! |=======")
                    return

class ManageCustomer:
    def __init__(self):
        self.CurrentCustomer = []
        self.OldCustomer = BinaryTree()
        self.AmountCurrentCustomer = 0
        self.AmountOldCustomer = 0
        self.LoadCurrentCustomer()
        self.LoadOldCustomer()

    def LoadCurrentCustomer(self):
        with open("CurrentCustomer.txt", "r") as file:
            if file is not None:
                for Line in file:
                    Item = Line.strip().split()
                    print(Line)
                    print(Item)

    def LoadOldCustomer(self):
        with open("OldCustomer.txt", "r") as file:
            if file is not None:
                for Line in file:
                    Item = Line.strip().split()
                    print(Line)
                    print(Item)

    def AddCustomer(self, Customer):
        self.OldCustomer.Insert(Customer)

class QLKS():
    def __init__(self, RoomSize, EmployeeSize):
        self.ManageRoom = ManageRoom(RoomSize)
        self.ManageEmployee = ManageEmployee(EmployeeSize)
        self.Revenue = 0

    def AddRoom(self, Room):
        self.ManageRoom.AddRoom(Room)

    def ShowRoom(self):
        self.ManageRoom.ShowListRoom()

    def UpdateRoom(self, IdRoom):
        self.ManageRoom.UpdateRoom(IdRoom)

    def DeleteRoom(self, IdRoom):
        self.ManageRoom.DeleteRoom(IdRoom)
        
    def AddEmployee(self, Employee):
        self.ManageEmployee.AddEmployee(Employee)

    def ShowEmployee(self):
        self.ManageEmployee.ShowListEmployee()

    def UpdateEmployee(self, IdEmployee):
        self.ManageEmployee.UpdateEmployee(IdEmployee)

    def DeleteEmployee(self, IdEmployee):
        self.ManageEmployee.DeleteEmployee(IdEmployee)

Trung = Employee("Trung", 8486888, "20/02/2004", "Executive", "9->17")
Phong = Employee("Phong", 2231132, "12/07/2005", "Protector", "7->18")
Tran  = Employee("Trân" , 1212132, "10/06/2005", "Staff"    , "9->18")
Phuc  = Employee("Phúc" , 3331442, "08/03/2005", "Staff"    , "9->18")
Vy    = Employee("Vy"   , 1221322, "28/11/2002", "Director" , "8->18")

RoomA = Room(120, "Red"   , 50, "Vip"   , 102, 3)
RoomB = Room(100, "Green" , 40, "Vip"   , 112, 4)
RoomC = Room(70 , "Yellow", 30, "Normal", 201)
RoomD = Room(50 , "Grey"  , 20, "Normal", 202)
RoomE = Room(20 , "Black" , 15, "Normal", 203)

TrungPerson = Node("Trung", 8486888, "20/02/2004", "Executive", "9->17")
PhongPerson = Node("Phong", 2231132, "12/07/2005", "Protector", "7->18")
TranPerson  = Node("Trân" , 1212132, "10/06/2005", "Staff"    , "9->18")
PhucPerson  = Node("Phúc" , 3331442, "08/03/2005", "Staff"    , "9->18")
VyPerson    = Node("Vy"   , 1221322, "28/11/2002", "Director" , "8->18")

# Model = BinaryTree()

# test = ManageCustomer()

Model = QLKS(5, 10)
Model.AddRoom()
Model.AddEmployee()