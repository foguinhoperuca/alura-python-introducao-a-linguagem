class Owner:
    def __init__(self, name, age):
        self._name = name
        self._age = age

    def say_hello(self):
        print(f"Hello! My name is {self._name}! I am {self._age} years old.")

