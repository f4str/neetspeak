from ply import yacc
import lexer
import ast

tokens = lexer.tokens

precedence = (
	('left', 'ASSIGN'),
	('left', 'OR'),
	('left', 'AND'),
	('left', 'NOT'),
	('left', 'EQ', 'LT', 'GT', 'LE', 'GE', 'NE'),
	('left', 'BITOR'),
	('left', 'BITXOR'),
	('left', 'BITAND'),
	('left', 'PLUS', 'MINUS'),
	('left', 'TIMES', 'DIV', 'MOD'), 
	('nonassoc', 'UMINUS', 'UPLUS', 'UINVERT'),
	('right', 'POW'), 
	('left', 'INDEX'),
	('left', 'LBRACKET'),
	('left', 'LPAREN'),
	('left', 'LBRACE')
)

def p_program(p):
	'''program : MAIN block END'''
	p[0] = ast.ProgramNode(block = p[2])

def p_block(p):
	'''block : statement_list'''
	p[0] = ast.BlockNode(sl = p[1])

def p_statement_list(p):
	'''statement_list : statement_list statement
					  | statement'''
	if len(p) == 2:
		p[0] = [p[1]]
	elif len(p) == 3:
		p[0] = p[1] + [p[2]]

def p_statement(p):
	'''statement : PRINT LPAREN expression RPAREN
				 | expression ASSIGN expression
				 | if_else END
				 | while END
				 | for END'''
	if len(p) == 3:
		p[0] = p[1]
	elif len(p) == 4:
		p[0] = ast.AssignmentNode(var = p[1], value = p[3])
	elif len(p) == 5:
		p[0] = ast.PrintNode(p[3])

def p_if_else(p):
	'''if_else : IF expression THEN block
			   | IF expression THEN block ELSE block
			   | IF expression THEN block ELSEIF elseif'''
	if len(p) == 5:
		p[0] = ast.IfNode(expression = p[2], if_block = p[4])
	elif len(p) == 7:
		p[0] = ast.IfNode(expression = p[2], if_block = p[4], else_block = p[6])

def p_else_if(p):
	'''elseif : expression THEN block
			  | expression THEN block ELSE block
			  | expression THEN block ELSEIF elseif'''
	if len(p) == 4:
		p[0] = ast.IfNode(expression = p[1], if_block = p[3])
	elif len(p) == 6:
		p[0] = ast.IfNode(expression = p[1], if_block = p[3], else_block = p[5])

def p_while(p):
	'''while : WHILE expression DO block'''
	p[0] = ast.WhileNode(expression = p[2], block = p[4])

def p_for(p):
	'''for : FOR expression ASSIGN expression TO expression DO block
		   | FOR expression ASSIGN expression DOWNTO expression DO block'''
	p[0] = ast.ForNode(var = p[2], start = p[4], direction = p[5], end = p[6], block = p[8])

def p_expression(p):
	'''expression : LPAREN expression RPAREN
				  | INT
				  | REAL
				  | BOOL
				  | STRING
				  | list'''
	if len(p) == 2:
		p[0] = p[1]
	elif len(p) == 4:
		p[0] = p[2]

def p_variable(p):
	'''expression : VARIABLE'''
	p[0] = ast.VariableNode(p[1])

def p_unary_operation(p):
	'''expression : MINUS expression %prec UMINUS
				  | PLUS expression %prec UPLUS
				  | NOT expression %prec NOT
				  | INVERT expression &prec UINVERT'''
	p[0] = ast.UnaryOperationNode(op = p[1], value = p[2])

def p_binary_operation(p):
	'''expression : expression PLUS expression
				  | expression MINUS expression
				  | expression TIMES expression
				  | expression DIV expression
				  | expression MOD expression
				  | expression POW expression
				  | expression EQ expression
				  | expression NE expression
				  | expression LT expression
				  | expression GT expression
				  | expression LE expression
				  | expression GE expression
				  | expression AND expression
				  | expression OR expression
				  | expression XOR expression
				  | expression BITOR expression
				  | expression BITAND expression
				  | expression BITXOR expression
				  | expression LSHIFT expression
				  | expression RSHIFT expression'''
	p[0] = ast.BinaryOperationNode(op = p[2], v1 = p[1], v2 = p[3])

def p_index(p):
	'''expression : expression LBRACKET expression RBRACKET %prec INDEX'''
	if isinstance(p[1], (ast.StringNode, ast.ListNode)):
		p[0] = p[1].index(p[3])
	else:
		raise SyntaxError

def p_list(p):
	'''list : LBRACKET list_in RBRACKET
			| LBRACKET RBRACKET'''
	if len(p) == 3:
		p[0] = ast.ListNode()
	elif len(p) == 4:
		p[0] = ast.ListNode(value = p[2])

def p_list_in(p):
	'''list_in : list_in COMMA expression
			   | expression'''
	if len(p) == 2:
		p[0] = [p[1]]
	elif len(p) == 4:
		p[0] = p[1] + [p[3]]

def p_error(p):
	print(f'syntax error at {p}')
	raise SyntaxError


parser = yacc.yacc()

def parse(data, debug = 0):
	parser.error = 0
	p = parser.parse(data, debug = debug)
	if parser.error:
		return None
	return p
