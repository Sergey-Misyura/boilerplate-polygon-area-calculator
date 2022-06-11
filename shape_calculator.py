class Rectangle:
    def __init__(self, width, height):
        self.width = width
        self.height = height

    def __repr__(self):
        return f'Rectangle(width={self.width}, height={self.height})'

    def set_width(self, width):
        self.width = width

    def set_height(self, height):
        self.height = height

    def get_area(self):
        return self.width * self.height

    def get_perimeter(self):
        return 2 * self.width + 2 * self.height

    def get_diagonal(self):
        return (self.width ** 2 + self.height ** 2) ** .5

    def get_picture(self):
        if (self.width < 50) and (self.height < 50):
            return ('*' * self.width + '\n') * self.height
        else:
            return "Too big for picture."

    def get_amount_inside(self, shape):
        nums = (self.width // shape.width) * (self.height // shape.height)
        return nums


class Square(Rectangle):
    def __init__(self, side):
        self.width = side
        self.height = side

    def __repr__(self):
        return f'Square(side={self.width})'

    def set_width(self, width):
        self.width = width
        self.height = width

    def set_height(self, height):
        self.height = height
        self.width = height

    def set_side(self, side):
        self.height = side
        self.width = side


