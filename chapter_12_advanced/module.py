def func():
    print("Hello world!")
if __name__ == "__main__":
    #if this code is run by its own file
    print("We are directly running this code")
    func()
    print(__name__)