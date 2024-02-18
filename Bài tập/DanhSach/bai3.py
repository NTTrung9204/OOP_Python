class soNguyenTo:
    def __init__(self, number) -> None:
        if self.isPrime(number):
            self._store = number
        else : self._store = None

    def isPrime(number):
        if number < 2 : return False
        for i in range(2,int(number**0.5)+1):
            if number%i==0 : return False
        return True
    
    def nextPrime(self):
        if self._store == None : return None
        number = self._store + 1
        while(True):
            if self.isPrime(number) : 
                return number
            number += 1
    
    def get_store(self):
        return self._store
    
    def set_store(self, number):
        if self.isPrime(number) : self._store = number
        print("Not set!!!")
num = int(input("Enter for input: "))
n = soNguyenTo(num)

if n.get_store is not None:
    print("Store Prime is :",n.get_store())
    print("Next Prime is :",n.nextPrime())

