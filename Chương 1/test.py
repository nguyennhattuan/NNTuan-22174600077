class Polygon: #đa giác
    def __init__(self, sides):
        self.sides = sides

    def perimeter(self):
        return sum(self.sides)

class Parallelogram(Polygon):#hình bình hành
    def __init__(self, base, height, side):
        super().__init__([base, side, base, side])
        self.height = height
        self.base = base

    def area(self):
        return self.base * self.height

class Rectangle(Parallelogram):# hình chữ nhật
    def __init__(self, length, width):
        super().__init__(length, width, length)
        self.length = length
        self.width = width

    def area(self):
        return self.length * self.width

class Square(Rectangle): #hình vuông
    def __init__(self, side):
        super().__init__(side, side)
        self.side = side

# Nhập thông tin và tính toán chu vi và diện tích của các hình
if __name__ == "__main__":
    base = float(input("Nhập chiều dài cơ sở của hình bình hành: "))
    height = float(input("Nhập chiều cao của hình bình hành: "))
    length = float(input("Nhập chiều dài của hình chữ nhật: "))
    width = float(input("Nhập chiều rộng của hình chữ nhật: "))
    side = float(input("Nhập độ dài cạnh của hình vuông: "))

    parallelogram = Parallelogram(base, height, side)
    rectangle = Rectangle(length, width)
    square = Square(side)

    print("Chu vi và diện tích của các hình:")
    print(f"Hình bình hành - Chu vi: {parallelogram.perimeter()}, Diện tích: {parallelogram.area()}")
    print(f"Hình chữ nhật - Chu vi: {rectangle.perimeter()}, Diện tích: {rectangle.area()}")
    print(f"Hình vuông - Chu vi: {square.perimeter()}, Diện tích: {square.area()}")
