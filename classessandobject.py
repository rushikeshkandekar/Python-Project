class MyClass:
    x = 5


p = MyClass()
print(p.x)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age


p1 = Person("John", 36)

print(p1.name)
print(p1.age)


class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __str__(self):
        return f"{self.name} {self.age}"


a = Person("John", 36)

print(a)


class Person:
    def __init__(my, name, age):
        my.name = name
        my.age = age

    def myfunc(self):
        print("Hello my name is " + self.name)


b = Person("John", 36)
b.myfunc()
