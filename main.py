def greet(name):
    if name is None:
        raise TypeError("Name cannot be None.")
    return f"Hello, {name}!"

def add(a, b):
    return a + b

def multiply(a, b):
    return a * b
