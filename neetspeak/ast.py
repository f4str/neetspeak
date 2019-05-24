import types

class Node:
	def __init__(self):
		pass
	
	def evaluate(self):
		pass
		
	def execute(self):
		self.evaluate()


class IntNode(Node):
	def __init__(self, value):
		self.value = types.Int(value)
	
	def evaluate(self):
		return self.value


class RealNode(Node):
	def __init__(self, value):
		self.value = types.Real(value)
	
	def evaluate(self):
		return self.value


class BoolNode(Node):
	def __init__(self, value):
		self.value = types.Bool(value == 'true')
	
	def evaluate(self):
		return self.value


class CharNode(Node):
	def __init__(self, value):
		self.value = types.Char(value[1:-1])
	
	def evaluate(self):
		return self.value


class StringNode(Node):
	def __init__(self, value):
		self.value = types.String(value[1:-1])
	
	def evaluate(self):
		return self.value


class PrintNode(Node):
	def __init__(self, value):
		self.value = value
	
	def execute(self):
		if isinstance(self.value, CharacterNode):
			value = "'" + self.value.evaluate() + "'"
		elif isinstance(self.value, StringNode):
			value = '"' + self.value.evaluate() + '"'
		elif isinstance(self.value, BooleanNode):
			value = 'true' if self.value.evaluate() else 'false'
		else:
			value = self.value.evaluate()
		print(value)


class UopNode(Node):
	def __init__(self, op, value):
		self.op = op
		self.value = value
	
	def evaluate(self):
		val = self.value.evaluate()
		if self.op == 'not'
			return not val.value
		elif self.op == '-':
			return -val
		elif self.op == '+':
			return +val
		else:
			raise SyntaxError

class BinopNode(Node):
	def __init__(self, op, v1, v2):
		self.op = op
		self.v1 = v1
		self.v2 = v2
	
	def evaluate(self):
		val1 = self.v1.evaluate()
		val2 = self.v2.evaluate()
		if self.op == '+':
			return val1 + val2
		elif self.op == '-':
			return val1 - val2
		elif self.op == '*':
			return val1 * val2
		elif self.op == '/':
			return val1 / val2
		elif self.op == '%':
			return val1 & val2
		elif self.op == '**':
			return val1 ** val2
		elif self.op == 'and':
			return val1.value and val2.value
		elif self.op == 'or':
			return val1.value or val2.value
		elif self.op in {'xor', '!='}:
			return val1 != val2
		elif self.op == '==':
			return val1 == val2
		elif self.op == '<':
			return val1 < val2
		elif self.op == '>':
			return val1 > val2
		elif self.op == '<=':
			return val1 <= val2
		elif self.op == '>=':
			return val1 >= val2
		else:
			raise SyntaxError

class TempNode(Node):
	def __init__(self, sl):
		self.sl = sl
	
	def execute(self):
		for s in self.sl:
			s.execute()

class BlockNode(Node):
	def __init__(self, sl = None):
		self.sl = sl
	
	def execute(self):
		if self.sl:
			for s in self.sl:
				s.execute()


class ProgramNode(Node):
	def __init__(self, block):
		self.block = block
	
	def __init__(self):
		self.block.execute()

