class Employee():
    company = "ITC"
    def show(self):
        print(f"The name of the employee is {self.name} and the salary is {self.salary}")
class Programmer(Employee):
    company = "ITC infotech"
    def showLanguage(self):
        print(f"The programmer {self.name} can code in {self.language}")

a = Employee()
b = Programmer()
print(a.company,b.company)