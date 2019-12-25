import datatypes as types
import lexer

stack = []
functions = {}

class Node:
	def __init__(self):
		pass
	
	def evaluate(self):
		self.execute()
		
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


class StringNode(Node):
	def __init__(self, value):
		self.value = types.String(value[1:-1])
	
	def index(self, i):
		n = i.evaluate()
		return StringNode('"' + self.value.index(n).value + '"')
	
	def evaluate(self):
		return self.value


class ListNode(Node):
	def __init__(self, value = []):
		self.value = types.List(value)
	
	def append(self, v):
		self.value.append(v)
	
	def index(self, i):
		n = i.evaluate()
		return self.value.index(n)
	
	def evaluate(self):
		for i in range(len(self.value)):
			self.value[i] = self.value[i].evaluate()
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
		elif self.op == '=':
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
	
	def execute(self):
		stack.append({})
		self.block.execute()


class VariableNode(Node):
	def __init__(self, value):
		if value in lexer.tokens:
			raise SyntaxError
		self.value = value
	
	def evaluate(self):
		if self.value in stack[-1]:
			return stack[-1][self.value]
		else:
			for variables in stack:
				if self.value in variables:
					return variables[self.value]
		raise KeyError


class AssignmentNode(Node):
	def __init__(self, var, value):
		self.var = var
		self.value = value
	
	def execute(self):
		stack[-1][self.var.value] = self.value.evaluate()


class IfNode(Node):
	def __init__(self, expression, if_block, else_block = None):
		self.expression = expression
		self.if_block = if_block
		self.else_block = else_block
	
	def execute(self):
		if self.expression.evaluate().value:
			self.if_block.execute()
		elif self.else_block:
			self.else_block.execute()


class WhileNode(Node):
	def __init__(self, expression, block):
		self.expression = expression
		self.block = block
	
	def execute(self):
		while self.expression.evaluate().value:
			self.block.execute()
