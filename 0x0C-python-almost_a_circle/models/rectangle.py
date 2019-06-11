#!/usr/bin/python3
"""class Rectangle"""


from models.base import Base


class Rectangle(Base):
    """ class Rectangle"""
    def __init__(self, width, height, x=0, y=0, id=None):
        """inicializa class Rectangle"""
        super().__init__(id)
        self.width = width
        self.height = height
        self.x = x
        self.y = y

    def __str__(self):
        """change str""""
        return ("[Rectangle] ({}) {}/{} - {}/{}".format
                (self.id, self.__x, self.__y, self.__width, self.__height))

    @property
    def width(self):
        """define width"""
        return self.__width

    @width.setter
    def width(self, value):
        """update width"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format("width"))
        if value <= 0:
            raise ValueError("{} must be > 0".format("width"))
        self.__width = value

    @property
    def height(self):
        """define height"""
        return self.__height

    @height.setter
    def height(self, value):
        """update height"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format("height"))
        if value <= 0:
            raise ValueError("{} must be > 0".format("height"))
        self.__height = value

    @property
    def x(self):
        """define x"""
        return self.__x

    @x.setter
    def x(self, value):
        """update x"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format("x"))
        if value < 0:
            raise ValueError("{} must be >= 0".format("x"))
        self.__x = value

    @property
    def y(self):
        """define y"""
        return self.__y

    @y.setter
    def y(self, value):
        """update y"""
        if type(value) is not int:
            raise TypeError("{} must be an integer".format("y"))
        if value < 0:
            raise ValueError("{} must be >= 0".format("y"))
        self.__y = value

    def area(self):
        """define area"""
        return self.__width * self.__height

    def display(self):
        """print rectangle with #"""
        alto = self.__height
        ancho = self.__width
        for y in range(self.__y):
            print()
        for i in range(alto):
            for x in range(self.__x):
                print(" ", end='')
            for j in range(ancho):
                print("#", end='')
                if j == (ancho - 1):
                    print("")
