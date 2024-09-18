#!/usr/bin/python3
# importing Rectangle from rectangle file

from rectangle import Rectangle

class Square(Rectangle):
    def __init__(self, size, x=0, y=0, id=None):
        super().__init__(size,size,x,y,id)
        self.size =size

    # Getter and setter for size
    @property
    def get_size(self):
        return self.size
    
    @size.setter
    def size(self,value):
        if not isinstance(value,int):
            raise TypeError("width must be an integer")
        if value <= 0:
            raise ValueError("width must be > 0")
        self.width = value
        self.height = value

    def update(self ,*args,**kwargs):
        if args:
            if len(args) > 0:
                self.id = args[0]
            if len(args) > 1:
                self.size = args[1]
            if len(args) >2:
                self.x = args[2]
            if len(args) > 3:
                self.y = args[3]
        else:
            if 'id' in kwargs:
                self.id = kwargs['id']
            if 'size' in kwargs:
                self.size = kwargs['size']
            if 'x' in kwargs:
                self.x = kwargs['x']
            if 'y' in kwargs:
                self.y = kwargs['y']



    def __str__(self):
        return f"[Rectangle] ({self.id}) {self.x}/{self.y} - {self.width}"
    # updating the class rectangle to return a dictionary representation of a Rectangle

    def to_dictionary(self):
        return {
            "id":self.id,
            "width": self.width,
            "height":self.height,
            "x":self.x,
            "y":self.y            
            }
    # updating the class square to return a dictionary representation of Square

    def to_dictionary(self):
        return{
            "id": self.id,
            "size": self.size,
            "x":self.x,
            "y":self.y
             }
