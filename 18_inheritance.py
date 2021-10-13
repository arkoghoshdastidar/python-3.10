class Person:
    def __init__(self, fname, lname):
        self.firstname = fname
        self.lastname = lname

    def printPerson(self):
        print(self.firstname, self.lastname)


class Student(Person):
    def __init__(self, fname, lname, year):
         super().__init__(fname, lname)
         self.year = year

    def welcome(self):
         print("Welcome", self.firstname, self.lastname, "to the class of", self.year)


x = Student("aron", "blaze", 2020)
x.welcome()
