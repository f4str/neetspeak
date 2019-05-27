import datatypes as types

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
		print(self.value.evaluate())


class UnaryOperationNode(Node):
	def __init__(self, op, value):
		self.op = op
		self.value = value
	
	def evaluate(self):
		val = self.value.evaluate()
		if self.op == 'not':
			return val.not_op()
		elif self.op == '-':
			return val.neg_op()
		elif self.op == '+':
			return val.pos_op()
		else:
			raise SyntaxError


class BinaryOperationNode(Node):
	def __init__(self, op, v1, v2):
		self.op = op
		self.v1 = v1
		self.v2 = v2
	
	def evaluate(self):
		val1 = self.v1.evaluate()
		val2 = self.v2.evaluate()
		if self.op == '+':
			return val1.add_op(val2)
		elif self.op == '-':
			return val1.sub_op(val2)
		elif self.op == '*':
			return val1.mul_op(val2)
		elif self.op == '/':
			return val1.div_op(val2)
		elif self.op == '%':
			return val1.mod_op(val2)
		elif self.op == '**':
			return val1.pow_op(val2)
		elif self.op == 'and':
			return val1.and_op(val2)
		elif self.op == 'or':
			return val1.or_op(val2)
		elif self.op in {'xor', '!='}:
			return val1.ne_op(val2)
		elif self.op == '==':
			return val1.eq_op(val2)
		elif self.op == '<':
			return val1.lt_op(val2)
		elif self.op == '>':
			return val1.gt_op(val2)
		elif self.op == '<=':
			return val1.le_op(val2)
		elif self.op == '>=':
			return val1.ge_op(val2)
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

