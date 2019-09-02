class Object:
	def __del__(self):
		del self.value
	
	def __repr__(self):
		return self.value.__repr__()
	
	def __str__(self):
		return self.value.__str__()
	
	def add_op(self, other):
		raise SyntaxError
	
	def sub_op(self, other):
		raise SyntaxError
	
	def mul_op(self, other):
		raise SyntaxError
	
	def div_op(self, other):
		raise SyntaxError
	
	def mod_op(self, other):
		raise SyntaxError
	
	def pow_op(self, other):
		raise SyntaxError
	
	def lt_op(self, other):
		raise SyntaxError
	
	def gt_op(self, other):
		raise SyntaxError
	
	def le_op(self, other):
		raise SyntaxError
	
	def ge_op(self, other):
		raise SyntaxError
	
	def eq_op(self, other):
		raise SyntaxError
	
	def ne_op(self, other):
		raise SyntaxError
	
	def and_op(self, other):
		raise SyntaxError
	
	def or_op(self, other):
		raise SyntaxError
	
	def not_op(self):
		raise SyntaxError
	
	def neg_op(self):
		raise SyntaxError
	
	def pos_op(self):
		raise SyntaxError


class Bool(Object):
	def __init__(self, value):
		self.value = bool(value)
	
	def __str__(self):
		return 'true' if self.value else 'false'
	
	def and_op(self, other):
		if isinstance(other, Bool):
			return Bool(self.value and other.value)
		else:
			raise SyntaxError
	
	def or_op(self, other):
		if isinstance(other, Bool):
			return Bool(self.value or other.value)
		else:
			raise SyntaxError
	
	def not_op(self):
		return Bool(not self.value)
	
	def eq_op(self, other):
		if isinstance(other, Bool):
			return Bool(self.value == other.value)
		else: 
			raise SyntaxError
	
	def ne_op(self, other):
		if isinstance(other, Bool):
			return Bool(self.value != other.value)
		else:
			raise SyntaxError


class Int(Object):
	def __init__(self, value):
		self.value = int(value)
	
	def add_op(self, other):
		if isinstance(other, Int):
			return Int(self.value + other.value)
		elif isinstance(other, Real):
			return Real(self.value + other.value)
		elif isinstance(other, (Int, Char)):
			return Char(chr(self.value + other.value))
		else:
			raise SyntaxError
	
	def sub_op(self, other):
		if isinstance(other, Int):
			return Int(self.value - other.value)
		elif isinstance(other, Real):
			return Real(self.value - other.value)
		elif isinstance(other, (Int, Char)):
			return Char(chr(self.value - other.value))
		else:
			raise SyntaxError
	
	def mul_op(self, other):
		if isinstance(other, Int):
			return Int(self.value * other.value)
		elif isinstance(other, Real):
			return Real(self.value * other.value)
		else:
			raise SyntaxError
	
	def div_op(self, other):
		if isinstance(other, Int):
			return Int(self.value // other.value)
		elif isinstance(other, Real):
			return Real(self.value / other.value)
		else:
			raise SyntaxError
	
	def mod_op(self, other):
		if isinstance(other, Int):
			return Int(self.value % other.value)
		elif isinstance(other, Real):
			return Real(self.value % other.value)
		else:
			raise SyntaxError
	
	def pow_op(self, other):
		if isinstance(other, Int):
			return Int(self.value ** other.value)
		elif isinstance(other, Real):
			return Real(self.value ** other.value)
		else:
			raise SyntaxError
	
	def lt_op(self, other):
		if isinstance(other, (Int, Real)):
			return Bool(self.value < other.value)
		else:
			raise SyntaxError
	
	def gt_op(self, other):
		if isinstance(other, (Int, Real)):
			return Bool(self.value > other.value)
		else:
			raise SyntaxError
	
	def le_op(self, other):
		if isinstance(other, (Int, Real)):
			return Bool(self.value <= other.value)
		else:
			raise SyntaxError
	
	def ge_op(self, other):
		if isinstance(other, (Int, Real)):
			return Bool(self.value >= other.value)
		else:
			raise SyntaxError
	
	def eq_op(self, other):
		if isinstance(other, (Int, Real)):
			return Bool(self.value == other.value)
		else:
			raise SyntaxError
	
	def ne_op(self, other):
		if isinstance(other, (Int, Real)):
			return Bool(self.value != other.value)
		else:
			raise SyntaxError
	
	def neg_op(self):
		return Int(-self.value)
	
	def pos_op(self):
		return Int(+self.value)


class Real(Object):
	def __init__(self, value):
		self.value = float(value)
	
	def add_op(self, other):
		if isinstance(other, (Int, Real)):
			return Real(self.value + other.value)
		else:
			raise SyntaxError
	
	def sub_op(self, other):
		if isinstance(other, (Int, Real)):
			return Real(self.value - other.value)
		else:
			raise SyntaxError
	
	def mul_op(self, other):
		if isinstance(other, (Int, Real)):
			return Real(self.value * other.value)
		else:
			raise SyntaxError
	
	def div_op(self, other):
		if isinstance(other, (Int, Real)):
			return Real(self.value / other.value)
		else:
			raise SyntaxError
	
	def mod_op(self, other):
		if isinstance(other, (Int, Real)):
			return Real(self.value % other.value)
		else:
			raise SyntaxError
	
	def pow_op(self, other):
		if isinstance(other, (Int, Real)):
			return Real(self.value ** other.value)
		else:
			raise SyntaxError
	
	def lt_op(self, other):
		if isinstance(other, (Int, Real)):
			return Bool(self.value < other.value)
		else:
			raise SyntaxError
	
	def gt_op(self, other):
		if isinstance(other, (Int, Real)):
			return Bool(self.value > other.value)
		else:
			raise SyntaxError
	
	def le_op(self, other):
		if isinstance(other, (Int, Real)):
			return Bool(self.value <= other.value)
		else:
			raise SyntaxError
	
	def ge_op(self, other):
		if isinstance(other, (Int, Real)):
			return Bool(self.value >= other.value)
		else:
			raise SyntaxError
	
	def eq_op(self, other):
		if isinstance(other, (Int, Real)):
			return Bool(self.value == other.value)
		else:
			raise SyntaxError
	
	def ne_op(self, other):
		if isinstance(other, (Int, Real)):
			return Bool(self.value != other.value)
		else:
			raise SyntaxError
	
	def neg_op(self):
		return Real(-self.value)
	
	def pos_op(self):
		return Real(+self.value)


class Char(Object):
	def __init__(self, value):
		self.value = ord(value)
	
	def __str__(self):
		return "'" + chr(self.value) + "'"
	
	def add_op(self, other):
		if isinstance(other, (Int, Char)):
			return Char(chr(self.value + other.value))
		else:
			raise SyntaxError
	
	def sub_op(self, other):
		if isinstance(other, (Int, Real)):
			return Char(chr(self.value - other.value))
		else:
			raise SyntaxError
	
	def lt_op(self, other):
		if isinstance(other, (Int, Char)):
			return Bool(self.value < other.value)
		else:
			raise SyntaxError
	
	def gt_op(self, other):
		if isinstance(other, (Int, Char)):
			return Bool(self.value > other.value)
		else:
			raise SyntaxError
	
	def le_op(self, other):
		if isinstance(other, (Int, Char)):
			return Bool(self.value <= other.value)
		else:
			raise SyntaxError
	
	def ge_op(self, other):
		if isinstance(other, (Int, Char)):
			return Bool(self.value >= other.value)
		else:
			raise SyntaxError
	
	def eq_op(self, other):
		if isinstance(other, (Int, Char)):
			return Bool(self.value == other.value)
		else:
			raise SyntaxError
	
	def ne_op(self, other):
		if isinstance(other, (Int, Char)):
			return Bool(self.value != other.value)
		else:
			raise SyntaxError

	
class String(Object):
	def __init__(self, value):
		self.value = str(value)
	
	def __str__(self):
		return '"' + self.value + '"'
	
	def add_op(self, other):
		if isinstance(other, String):
			return String(self.value + other.value)
		elif isinstance(other, Char):
			return String(self.value + chr(other.value))
		else:
			raise SyntaxError
	
	def mul_op(self, other):
		if isinstance(other, Int):
			return String(self.value * other.value)
		else:
			raise SyntaxError
	
	def lt_op(self, other):
		if isinstance(other, String):
			return Bool(self.value < other.value)
		else:
			raise SyntaxError
	
	def gt_op(self, other):
		if isinstance(other, String):
			return Bool(self.value > other.value)
		else:
			raise SyntaxError
	
	def le_op(self, other):
		if isinstance(other, String):
			return Bool(self.value <= other.value)
		else:
			raise SyntaxError
	
	def ge_op(self, other):
		if isinstance(other, String):
			return Bool(self.value >= other.value)
		else:
			raise SyntaxError
	
	def eq_op(self, other):
		if isinstance(other, String):
			return Bool(self.value == other.value)
		else:
			raise SyntaxError
	
	def ne_op(self, other):
		if isinstance(other, String):
			return Bool(self.value != other.value)
		else:
			raise SyntaxError
	
	def index(self, i):
		if isinstance(i, Int):
			return Char(self.value[i.value])
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
	
	def add_op(self, other):
		if isinstance(other, List):
			return List(self.value + other.value)
		else:
			raise SyntaxError
	
	def mul_op(self, other):
		if isinstance(other, Int):
			return List(self.value * other.value)
		else:
			raise SyntaxError
	
	def lt_op(self, other):
		if isinstance(other, List):
			return Bool(self.value < other.value)
		else:
			raise SyntaxError
	
	def gt_op(self, other):
		if isinstance(other, List):
			return Bool(self.value > other.value)
		else:
			raise SyntaxError
	
	def le_op(self, other):
		if isinstance(other, List):
			return Bool(self.value <= other.value)
		else:
			raise SyntaxError
	
	def ge_op(self, other):
		if isinstance(other, List):
			return Bool(self.value >= other.value)
		else:
			raise SyntaxError
	
	def eq_op(self, other):
		if isinstance(other, List):
			return Bool(self.value == other.value)
		else:
			raise SyntaxError
	
	def ne_op(self, other):
		if isinstance(other, List):
			return Bool(self.value != other.value)
		else:
			raise SyntaxError
	
	def append(self, other):
		return List(self.value.append(other))
	
	def index(self, i):
		if isinstance(i, Int):
			return self.value[i.value]
		else:
			raise SyntaxError

