class ProbHash:
    hastable = list()
    n = 0

    def __init__(self, cap):
        self.hastable = cap*[None]
        self.n = cap
    
    def hashFunction(self, mykey):
        return mykey%self.n
    
    def rehashFunction(self, hkey):
        return hkey+1
    
    def insertData(self, student_obj):
        indeg = self.hashFunction(student_obj.getId())
        while self.hastable[indeg] != None:
            if indeg == self.n-1:
                print("Not Do it!")
                return None
            indeg = self.rehashFunction(indeg)
        print("Yes", indeg)
        self.hastable[indeg] = student_obj
    
    def searchData(self, key):
        indeg = self.hashFunction(key)
        if self.hastable[indeg] == None:
            print("No has.")
            return None
        while self.hastable[indeg].getId() != key:
            if indeg == self.n-1:
                print("No.")
                return None
            indeg = self.rehashFunction(indeg)
        print("Found", key, "at index", indeg)
        return self.hastable[indeg]
        

class Student:
    id = ""
    name = ""
    gpa = 0.0

    def __init__(self, id, name, gpa):
        self.id = id
        self.name = name
        self.gpa = gpa
    
    def getId(self):
        return self.id
    def getName(self):
        return self.name
    def getGpa(self):
        return self.gpa
    def printDetail(self):
        return "ID:", self.name, "\nName:", self.name, "\nGPA:", self.gpa

s1 = Student(65070001, "Sandee Boonmak", 3.05)
s2 = Student(65070077, "Somsak Jaidee", 2.78)
s3 = Student(65070021, "Somsri Jaiyai", 3.44)
s4 = Student(65070042, "Sommai Meeboon", 2.89)
myHash = ProbHash(20)
myHash.insertData(s1)
myHash.insertData(s2)
myHash.insertData(s3)
myHash.insertData(s4)

std = myHash.searchData(65070077)
std.printDetail()
print("-------------------------")
std = myHash.searchData(65070021)
std.printDetail()
print("-------------------------")
std = myHash.searchData(65070042)
std.printDetail()
print("-------------------------")
std = myHash.searchData(65070032)