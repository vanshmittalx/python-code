class Employee:
    a = 1
    @classmethod
    def show(cls):
        print(f"The class attribute is {cls.a}")
o = Employee()
o.a = 45
o.show()