class Employee:
    name = "Vansh"
    age = 21
    language = "Py"
    salary = 120000

    def __init__(self, name, salary, language):
        self.name = name
        self.salary = salary
        self.language = language

    def getInfo(self):
        print(f"The salary is {self.salary}, the language is {self.language}")

    @staticmethod
    def greet():
        print("Hello")

vansh = Employee("Vansh", 2000000, "Python")
vansh.greet()
vansh.getInfo()