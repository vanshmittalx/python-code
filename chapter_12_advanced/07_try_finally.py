def main():
    try:
        number = int(input("Enter number: "))
        print(number)
        return
    
    except Exception as e:
        print("Wrong input type")
        return

    finally: #run always even when value is returned
        print("I am inside finally")

main()