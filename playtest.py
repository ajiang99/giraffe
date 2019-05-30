import unittest

class Bird:
    def __init__(self, age, weight, color):
        self.age = age
        self.weight = weight
        self.color = color

    def fly(self):
        print("I can fly")

    def eat(self):
        print("I can eat")

    def print_info(self):
        print(self.age)
        print(self.weight)
        print(self.color)


class Penguin(Bird):
    def __init__(self):
        Bird.__init__(self,99,99,99)

    def fly(self):
        print("I can't fly")


def main():
    generic = Bird(11, 44, "black")
    penguin = Penguin(])

    generic.print_info()
    penguin.print_info()


if __name__ == "__main__":
    main()