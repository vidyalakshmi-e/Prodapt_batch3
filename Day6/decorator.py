def logging_decorator(func):
    def wrapper():
        print("Before calling the function.")
        func()
        print("After calling the function")
    return wrapper

@logging_decorator
def say_hello():
    print("Hello!")

@logging_decorator
def say_goodbaye():
    print("Goodbye!")

@logging_decorator
def say_welcome():
    print("Welcome!")