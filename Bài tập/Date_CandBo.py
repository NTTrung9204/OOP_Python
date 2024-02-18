class Date:
    def __init__(self, Day, Month, Year):
        self.Day = Day
        self.Month = Month
        self.Year = Year

    def __str__(self):
        return f"{self.Day} | {self.Month} | {self.Year}"
    
class CanBo(Date):
    def __init__(self, Id, Name, BirthDay, Salary):
        super().__init__(BirthDay.Day, BirthDay.Month, BirthDay.Year)
        self.Id = Id
        self.Name = Name
        self.Salary = Salary
        self.Grand = 500

    def CalSalary(self):
        return self.Salary + self.Grand
    
    
    
