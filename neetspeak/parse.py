from ply import yacc
import lexer
import ast

tokens = lexer.tokens

precedence = (
	('left', 'OR'),
	('left', 'AND'),
	('left', 'NOT'),
	('left', 'EQ', 'LT', 'GT', 'LE', 'GE', 'NEQ'),
	('left', 'PLUS', 'MINUS'),
    ('left', 'TIMES', 'DIV', 'MOD'), 
    ('nonassoc', 'UMINUS', 'UPLUS'),
    ('right', 'EXP'), 
)

def p_temp(p):
	'''temp : statement_list'''
	p[0] = ast.TempNode(p[1])

# def p_program(p):
#     '''program : MAIN block'''
#     print(p[0])
#     print(p[1])
#     print(p[2])
#     p[0] = ast.ProgramNode(p[2])

# def p_block(p):
#     '''block : LBRACE statement_list RBRACE
#              | LBRACE RBRACE'''
#     if len(p) == 3:
#         p[0] = ast.BlockNode()
#     elif len(p) == 4:
#         print(p[2])
#         p[0] = ast.BlockNode(p[2])

def p_statement_list(p):
	'''statement_list : statement_list statement
					  | statement'''
	if len(p) == 2:
		p[0] = [p[1]]
	elif len(p) == 3:
		p[0] = p[1] + [p[2]]

def p_statement(p):
	'''statement : PRINT LPAREN expression RPAREN SEMI'''
	p[0] = ast.PrintNode(p[3])

def p_expression(p):
	'''expression : INT
				  | REAL
				  | BOOL
				  | CHAR
				  | STRING'''
	p[0] = p[1]

def p_error(p):
	print(f'syntax error at {p.value}')

parser = yacc.yacc()


def parse(data, debug = 0):
	parser.error = 0
	p = parser.parse(data, debug = debug)
	if parser.error:
		return None
	return p
