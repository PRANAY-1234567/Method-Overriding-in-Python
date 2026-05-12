# Method Overriding

class A:
    def first(self):
        print("Inside method first")

    def second(self):
        print("Inside method second")


class B(A):   # Inheriting class A
    def first(self):
        super().first()   # Calling parent class method
        print("Inside new method first")


class Inh4:
    @staticmethod
    def main():
        obj = B()
        obj.first()
        obj.second()


# Calling main method
Inh4.main()