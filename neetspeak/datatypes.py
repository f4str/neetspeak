class Object:
	def __del__(self):
		del self.value
	
	def __repr__(self):
		return self.value.__repr__()
	
	def __str__(self):
		return self.value.__str__()
	
	def __add__(self, other):
		raise SyntaxError
	
	def __sub__(self, other):
		raise SyntaxError
	
	def __mul__(self, other):
		raise SyntaxError
	
	def __truediv__(self, other):
		raise SyntaxError
	
	def __mod__(self, other):
		raise SyntaxError
	
	def __pow__(self, other):
		raise SyntaxError
	
	def __lt__(self, other):
		raise SyntaxError
	
	def __gt__(self, other):
		raise SyntaxError
	
	def __le__(self, other):
		raise SyntaxError
	
	def __ge__(self, other):
		raise SyntaxError
	
	def __eq__(self, other):
		raise SyntaxError
	
	def __ne__(self, other):
		raise SyntaxError
	
	def __and2__(self, other):
		raise SyntaxError
	
	def __or2__(self, other):
		raise SyntaxError
	
	def __not__(self):
		raise SyntaxError
	
	def __neg__(self):
		raise SyntaxError
	
	def __pos__(self):
		raise SyntaxError
	
	def __or__(self, other):
		raise SyntaxError
	
	def __and__(self, other):
		raise SyntaxError
	
	def __xor__(self, other):
		raise SyntaxError
	
	def __lshift__(self, other):
		raise SyntaxError
	
	def __rshift__(self, other):
		raise SyntaxError
	
	def __invert__(self):
		raise SyntaxError


class Bool(Object):
	def __init__(self, value):
		self.value = bool(value)
	
	def __str__(self):
		return 'true' if self.value else 'false'
	
	def __and2__(self, other):
		if isinstance(other, Bool):
			return Bool(self.value and other.value)
		else:
			raise SyntaxError
	
	def __or2__(self, other):
		if isinstance(other, Bool):
			return Bool(self.value or other.value)
		else:
			raise SyntaxError
	
	def __not__(self):
		return Bool(not self.value)
	
	def __eq__(self, other):
		if isinstance(other, Bool):
			return Bool(self.value == other.value)
		else: 
			raise SyntaxError
	
	def __ne__(self, other):
		if isinstance(other, Bool):
			return Bool(self.value != other.value)
		else:
			raise SyntaxError


class Int(Object):
	def __init__(self, value):
		self.value = int(value)
	
	def __add__(self, other):
		if isinstance(other, Int):
			return Int(self.value + other.value)
		elif isinstance(other, Real):
			return Real(self.value + other.value)
		else:
			raise SyntaxError
	
	def __sub__(self, other):
		if isinstance(other, Int):
			return Int(self.value - other.value)
		elif isinstance(other, Real):
			return Real(self.value - other.value)
		else:
			raise SyntaxError
	
	def __mul__(self, other):
		if isinstance(other, Int):
			return Int(self.value * other.value)
		elif isinstance(other, Real):
			return Real(self.value * other.value)
		else:
			raise SyntaxError
	
	def __truediv__(self, other):
		if isinstance(other, Int):
			return Int(self.value // other.value)
		elif isinstance(other, Real):
			return Real(self.value / other.value)
		else:
			raise SyntaxError
	
	def __mod__(self, other):
		if isinstance(other, Int):
			return Int(self.value % other.value)
		elif isinstance(other, Real):
			return Real(self.value % other.value)
		else:
			raise SyntaxError
	
	def __pow__(self, other):
		if isinstance(other, Int):
			return Int(self.value ** other.value)
		elif isinstance(other, Real):
			return Real(self.value ** other.value)
		else:
			raise SyntaxError
	
	def __lt__(self, other):
		if isinstance(other, (Int, Real)):
			return Bool(self.value < other.value)
		else:
			raise SyntaxError
	
	def __gt__(self, other):
		if isinstance(other, (Int, Real)):
			return Bool(self.value > other.value)
		else:
			raise SyntaxError
	
	def __le__(self, other):
		if isinstance(other, (Int, Real)):
			return Bool(self.value <= other.value)
		else:
			raise SyntaxError
	
	def __ge__(self, other):
		if isinstance(other, (Int, Real)):
			return Bool(self.value >= other.value)
		else:
			raise SyntaxError
	
	def __eq__(self, other):
		if isinstance(other, (Int, Real)):
			return Bool(self.value == other.value)
		else:
			raise SyntaxError
	
	def __ne__(self, other):
		if isinstance(other, (Int, Real)):
			return Bool(self.value != other.value)
		else:
			raise SyntaxError
	
	def __neg__(self):
		return Int(-self.value)
	
	def __pos__(self):
		return Int(+self.value)
	
	def __or__(self, other):
		if isinstance(other, Int):
			return Int(self.value | other.value)
		else:
			raise SyntaxError
	
	def __and__(self, other):
		if isinstance(other, Int):
			return Int(self.value & other.value)
		else:
			raise SyntaxError
	
	def __xor__(self, other):
		if isinstance(other, Int):
			return Int(self.value ^ other.value)
		else:
			raise SyntaxError
	
	def __lshift__(self, other):
		if isinstance(other, Int):
			return Int(self.value << other.value)
		else:
			raise SyntaxError
	
	def __rshift__(self, other):
		if isinstance(other, Int):
			return Int(self.value >> other.value)
		else:
			raise SyntaxError
	
	def __invert__(self):
		return Int(~self.value)


class Real(Object):
	def __init__(self, value):
		self.value = float(value)
	
	def __add__(self, other):
		if isinstance(other, (Int, Real)):
			return Real(self.value + other.value)
		else:
			raise SyntaxError
	
	def __sub__(self, other):
		if isinstance(other, (Int, Real)):
			return Real(self.value - other.value)
		else:
			raise SyntaxError
	
	def __mul__(self, other):
		if isinstance(other, (Int, Real)):
			return Real(self.value * other.value)
		else:
			raise SyntaxError
	
	def __truediv__(self, other):
		if isinstance(other, (Int, Real)):
			return Real(self.value / other.value)
		else:
			raise SyntaxError
	
	def __mod__(self, other):
		if isinstance(other, (Int, Real)):
			return Real(self.value % other.value)
		else:
			raise SyntaxError
	
	def __pow__(self, other):
		if isinstance(other, (Int, Real)):
			return Real(self.value ** other.value)
		else:
			raise SyntaxError
	
	def __lt__(self, other):
		if isinstance(other, (Int, Real)):
			return Bool(self.value < other.value)
		else:
			raise SyntaxError
	
	def __gt__(self, other):
		if isinstance(other, (Int, Real)):
			return Bool(self.value > other.value)
		else:
			raise SyntaxError
	
	def __le__(self, other):
		if isinstance(other, (Int, Real)):
			return Bool(self.value <= other.value)
		else:
			raise SyntaxError
	
	def __ge__(self, other):
		if isinstance(other, (Int, Real)):
			return Bool(self.value >= other.value)
		else:
			raise SyntaxError
	
	def __eq__(self, other):
		if isinstance(other, (Int, Real)):
			return Bool(self.value == other.value)
		else:
			raise SyntaxError
	
	def __ne__(self, other):
		if isinstance(other, (Int, Real)):
			return Bool(self.value != other.value)
		else:
			raise SyntaxError
	
	def __neg__(self):
		return Real(-self.value)
	
	def __pos__(self):
		return Real(+self.value)

	
class String(Object):
	def __init__(self, value):
		self.value = str(value)
	
	def __str__(self):
		return '"' + self.value + '"'
	
	def __add__(self, other):
		if isinstance(other, String):
			return String(self.value + other.value)
		elif isinstance(other, (Int, Real)):
			return String(self.value + str(other.value))
		else:
			raise SyntaxError
	
	def __mul__(self, other):
		if isinstance(other, Int):
			return String(self.value * other.value)
		else:
			raise SyntaxError
	
	def __lt__(self, other):
		if isinstance(other, String):
			return Bool(self.value < other.value)
		else:
			raise SyntaxError
	
	def __gt__(self, other):
		if isinstance(other, String):
			return Bool(self.value > other.value)
		else:
			raise SyntaxError
	
	def __le__(self, other):
		if isinstance(other, String):
			return Bool(self.value <= other.value)
		else:
			raise SyntaxError
	
	def __ge__(self, other):
		if isinstance(other, String):
			return Bool(self.value >= other.value)
		else:
			raise SyntaxError
	
	def __eq__(self, other):
		if isinstance(other, String):
			return Bool(self.value == other.value)
		else:
			raise SyntaxError
	
	def __ne__(self, other):
		if isinstance(other, String):
			return Bool(self.value != other.value)
		else:
			raise SyntaxError
	
	def index(self, i):
		if isinstance(i, Int):
			if i.value > 0:
				return String(self.value[i.value - 1])
			else:
				raise SyntaxError
		else:
			raise SyntaxError


class List(Object):
	def __init__(self, value):
		self.value = value
	
	def __str__(self):
		return str(self.value)
	
	def __len__(self):
		return len(self.value)
	
	def __getitem__(self, key):
		return self.value[key]
	
	def __setitem__(self, key, value):
		self.value[key] = value
	
	def __add__(self, other):
		if isinstance(other, List):
			return List(self.value + other.value)
		else:
			raise SyntaxError
	
	def __mul__(self, other):
		if isinstance(other, Int):
			return List(self.value * other.value)
		else:
			raise SyntaxError
	
	def __lt__(self, other):
		if isinstance(other, List):
			return Bool(self.value < other.value)
		else:
			raise SyntaxError
	
	def __gt__(self, other):
		if isinstance(other, List):
			return Bool(self.value > other.value)
		else:
			raise SyntaxError
	
	def __le__(self, other):
		if isinstance(other, List):
			return Bool(self.value <= other.value)
		else:
			raise SyntaxError
	
	def __ge__(self, other):
		if isinstance(other, List):
			return Bool(self.value >= other.value)
		else:
			raise SyntaxError
	
	def __eq__(self, other):
		if isinstance(other, List):
			return Bool(self.value == other.value)
		else:
			raise SyntaxError
	
	def __ne__(self, other):
		if isinstance(other, List):
			return Bool(self.value != other.value)
		else:
			raise SyntaxError
	
	def append(self, other):
		return List(self.value.append(other))
	
	def index(self, i):
		if isinstance(i, Int):
			if i.value > 0:
				return self.value[i.value - 1]
			else:
				raise SyntaxError
		else:
			raise SyntaxError
