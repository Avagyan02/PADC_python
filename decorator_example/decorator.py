def myDecorator(func):
    def wrapper():
        print("Hello World")
        func()
        print("Hello World Twice")
    return wrapper

@myDecorator
def sayHello():
    print("hello!")

sayHello()