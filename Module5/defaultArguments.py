def greet_person(name, greeting="Hello"):
    message= f"{greeting}, {name}"
    return message

default_greeting = greet_person("alice")

print(default_greeting)

custum_greeting = greet_person("bob", "hi")
print(custum_greeting)