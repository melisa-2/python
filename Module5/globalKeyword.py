greeting = "Hello"

def greet(name):
    '''declaring 'message' as a global variable'''
    global message
    message = f"{greeting}, {name}"
    print(message)

greet("Melisa")
print(message)

message= f"{greeting}, student"
print(message)