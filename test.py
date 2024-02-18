class supperMan:
    index = 0
    def __init__(self, name, weapon, color):
        self.name = name
        self.weapon = weapon
        self.color = color
        self.id = supperMan.index + 1
        supperMan.index += 1
    def show(self):
        print(self.name)
        print(self.weapon)
        print(self.color)
        print(self.id)

ManA = supperMan('Trung','Knight','Red')
ManB = supperMan('Tung','Bomb','Yellow')
ManC = supperMan('Phong','Bow','Green')

ManA.show()
ManB.show()
ManC.show()
print(supperMan.index)