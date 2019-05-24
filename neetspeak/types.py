class Object:
    pass


class Bool(Object):
    def __init__(self, value):
        self.value = bool(value)
    
    def and_op(self, other):
        if isinstance(other, Bool):
            return Bool(self.value and other.value)
        else:
            raise SyntaxError


class Number(Object):
    def __add__(self, other):
        if isinstance(other, Number):
            return self.value + other.value
        else:
            raise SyntaxError
    
    def __sub__(self, other):
        if isinstance(other, Number):
            return self.value - other.value
        else:
            raise SyntaxError
    
    def __mul__(self, other):
        if isinstance(other, Number):
            return self.value * other.value
        else:
            raise SyntaxError
    
    def __truediv__(self, other):
        if isinstance(other, Number):
            return self.value / other.value
        else:
            raise SyntaxError
    
    def __mod__(self, other):
        if isinstance(other, Number):
            return self.value % other.value
        else:
            raise SyntaxError
    
    def __pow__(self, other):
        if isinstance(other, Number):
            return self.value ** other.value
        else:
            raise SyntaxError
    def __lt__(self, other):
        if isinstance(other, Number):
            return self.value < other.value
        else:
            raise SyntaxError
    def __gt__(self, other):
        if isinstance(other, Number):
            return self.value > other.value
        else:
            raise SyntaxError
    def __le__(self, other):
        if isinstance(other, Number):
            return self.value <= other.value
        else:
            raise SyntaxError
    def __ge__(self, other):
        if isinstance(other, Number):
            return self.value >= other.value
        else:
            raise SyntaxError
    def __eq__(self, other):
        if isinstance(other, Number):
            return self.value == other.value
        else:
            raise SyntaxError
    def __ne__(self, other):
        if isinstance(other, Number):
            return self.value != other.value
        else:
            raise SyntaxError
        
    def __neg__(self):
        return -self.value
    
    def __pos__(self):
        return +self.value


class Int(Number):
    def __init__(self, value):
        self.value = int(value)
    
    def __truediv__(self, other):
        if isinstance(other, Int):
            return self.value // other.value
        else:
            return super.__truediv__


class Real(Number):
    def __init__(self, value):
        self.value = float(value)


class Char(Object):
    def __init__(self, value):
        self.value = ord(value)

    
class String(Object):
    def __init__(self, value):
        self.value = str(value)

