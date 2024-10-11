def farheneit_to_celsius(temperature):
    return 5*(temperature-32)/9
temp = int(input("Enter temperature in farheneit: "))
celsius=farheneit_to_celsius(temp)
print(f"{round(celsius,2)} C")