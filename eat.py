def func():
    return 1

example = func()
print(example)

def hello():
    return "Hi Shawn!"

def other(some_def_func):
    print("Other code here")
    print(some_def_func())

other(hello)

def new_dec(orginal_func):
    def wrap_func():

        print("Some extra code")

        orginal_func()

        print("Some more code")
    
    return wrap_func

def fuc_needs_dec():
    print("Lets get decorated here")

decorated_func = new_dec(fuc_needs_dec)
decorated_func()

@new_dec
def fuc_needs_dec():
    print("This decorator works!")

fuc_needs_dec()