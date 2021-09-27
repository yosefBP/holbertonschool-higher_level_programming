#!/usr/bin/python3
""" 1-main """
from models.rectangle import Rectangle

if __name__ == "__main__":

    rect_1 = Rectangle(10, 2)
    print(rect_1.id)

    rect_2 = Rectangle(2, 10)
    print(rect_2.id)

    rect_3 = Rectangle(10, 2, 0, 0, 12)
    print(rect_3.id)

    print("x", rect_2.x)
    print("y", rect_2.y)
    print("width", rect_2.width)
    print("height", rect_2.height)
