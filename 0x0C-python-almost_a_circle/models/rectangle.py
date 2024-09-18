#!/usr/bin/python3

# Assuming Base class is in the same directory as Rectangle
from base import Base

class Rectangle(Base):
    def __init__(self, width, height, x=0, y=0, id=None):
        # Call the super class with id
        super().__init__(id)
        
        # Assign the attributes
        self.__width = width
        self.__height = height
        self.__x = x
        self.__y = y
    
    # Getter and Setter for width
    @property
    def width(self):
        return self.__width
    
    @width.setter
    def width(self, value):
        # Validating width attribute
        if not isinstance(value,int):
            raise TypeError("Width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.__width = value
    
    # Getter and Setter for height
    @property
    def height(self):
        return self.__height
    
    @height.setter
    def height(self, value):
        # Validating height attribute
        if not isinstance(value,int):
            raise TypeError("height must be an integer")
        if value <= 0:
            raise ValueError("height must be > 0")
        self.__height = value
    
    # Getter and Setter for x
    @property
    def x(self):
        return self.__x
    
    @x.setter
    def x(self, value):
        # Validating x attribute
        if value <= 0:
            raise ValueError("x must be > 0")
        self.__x = value
    
    # Getter and Setter for y
    @property
    def y(self):
        return self.__y
    
    @y.setter
    def y(self, value):
        # Validating y attribute
        if value <= 0:
            raise ValueError("y must be > 0")
        self.__y = value

    # Updating class rectangle by adding public method area
    def area(self):
        return self.__height * self.__width
    
    # updating rectangle with a public method to display rectangle instance with # character
    def display(self):
        for  _ in range(self.y):
            print()
        for _ in range(self.height):
            print(""*self.x + "#"* self.width)
    
    # update by overriding __str__method
    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}/{self.height}"
    
    # updating Rectangle by adding a public method that assigns an argument to each attribute
    def update(self,*args,**kwargs):
        if args:
            if len(args)> 0:
                self.id = args[0]
            if len(args)> 1:
                self.__width = args[1]
            if len(args)> 2:
                self.__height = args[2]
            if len(args)> 3:
                self.__x= args[3]
            if len(args)> 4:
                self.__y = args[4]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'width' in kwargs:
                self.width = kwargs['width']
            if 'height' in kwargs:
                self.height = kwargs['height']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']


r1 =Rectangle(10, 10, 10, 10)
print(r1)

r1.update(89)
print(r1)

r1.update(89, 2)
print(r1)

r1.update(89, 2, 3)
print(r1)

r1.update(89, 2, 3, 4)
print(r1)

r1.update(89, 2, 3, 4, 5)
print(r1)