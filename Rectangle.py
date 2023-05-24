#Thomas Carney
#CIS261
#Rectangle

from dataclasses import dataclass

@dataclass
class Rectangle():
    height: int
    width: int
#    def __init__(self, height, width):
#        self.height = height
#        self.width = width

    def getPerimeter(self):
        return self.height * 2 + self.width * 2

    @property
    def area(self):
        return self.height * self.width

#    def show(self):
#        print(f'Perimeter:  {self.perimeter}')
#        print(f'Area:  {self.area}')

    def getStr(self):
            s = ""
            w = "* " * self.width + "\n"
            s += w
            for i in range(self.height-2):
                s += "* "
                s += "  " * (self.width-2)
                s += "* \n"
            s += w
            return s


def main():
    print('Rectangle Calculator\n')

    again = "y"
    while again.lower() == "y":
        height = int(input('Height:     '))
        width = int(input('Width:      '))
        rectangle = Rectangle(height,width)

        #rec.show()
        print("Perimeter:", rectangle.getPerimeter())
        print("Area:     ", rectangle.area)
        print(rectangle.getStr())
        again = input("Continue? (y/n): ").lower()
        print()

    print("Bye!")
if __name__ == "__main__":
    main()