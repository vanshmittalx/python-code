class Employee():
    company = "ITC"
    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")

class Coder():
    language = "Python"
    def printLanguages(self):
        print(f"Your language is {self.language}")

class Programmer(Employee, Coder):
    company = "ITC infotech"
    def showLanguage(self):
        print(f"The programmer {self.name} can code in {self.language}")

a = Employee()
b = Programmer()
b.name = "Vansh"
b.salary = 120000
b.show()
b.printLanguages()
b.showLanguage()
