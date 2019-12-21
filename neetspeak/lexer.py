from ply import lex
import ast

# keywords = (
#     'INT', 'REAL', 'BOOL', 'CHAR', 'VOID', 'STRING', 'OBJECT',
#     'LIST', 'MAP', 'SET',
#     'TRUE', 'FALSE', 'IN',
#     'IF', 'ELSE', 'WHILE', 'FOR', 'DO', 'RETURN',
#     'PRINT'
# )

# tokens = keywords + (
#     'LBRACKET', 'RBRACKET',
#     'COMMA', 'COLON',
#     'ASSIGN',
#     'ID'
# )

# t_COLON = r':'
# t_IN = r'in'
# t_IF = r'if'
# t_ELSE = r'else'
# t_WHILE = r'while'
# t_FOR = r'for'
# t_DO = r'do'

keywords = (
	'AND', 'OR', 'XOR', 'NOT', 
	'END', 'PRINT', 'MAIN'
)

tokens = keywords + (
	'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 'LBRACKET', 'RBRACKET', 
	'PLUS', 'MINUS', 'TIMES', 'DIV', 'MOD', 'POW', 
	'EQ', 'LT', 'LE', 'GT', 'GE', 'NE', 
	'COMMA', 'ASSIGN', 'VARIABLE', 
	'INT', 'REAL', 'BOOL', 'STRING', 
)

reserved = {
	'if': 'IF',
	'else': 'ELSE',
	'while': 'WHILE',
	'in': 'IN',
	'end': 'END',
	'print': 'PRINT',
	'main': 'MAIN',
	'not': 'NOT',
	'and': 'AND',
	'ore': 'OR',
	'xor': 'XOR',
	'true': 'TRUE',
	'false': 'FALSE', 
}

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_LBRACKET = r'\['
t_RBRACKET = r'\]'
t_COMMA = r','
t_PLUS = r'\+'
t_ASSIGN = r':='
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIV = r'/'
t_MOD = r'%'
t_POW = r'\*\*'
t_EQ = r'='
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_NE = r'!='
t_NOT = r'not'
t_AND = r'and'
t_OR = r'or'
t_XOR = r'xor'
t_END = r'end'
t_PRINT = r'print'
t_MAIN = r'main'

def t_REAL(t):
	r'\d*(\d\.|\.\d)\d*([eE][-+]?\d+)?'
	t.value = ast.RealNode(t.value)
	return t

def t_INT(t):
	r'\d+'
	t.value = ast.IntNode(t.value)
	return t

def t_BOOL(t):
	r'true | false'
	t.value = ast.BoolNode(t.value)
	return t

def t_STRING(t):
	r'"(?:[^"\\]+|\\.)*" | \'(?:[^\'\\]+|\\.)*\''
	t.value = ast.StringNode(t.value)
	return t

def t_VARIABLE(t):
	r'[A-Za-z][A-Za-z0-9_]*'
	t.type = reserved.get(t.value, 'VARIABLE')
	return t

t_ignore = ' \t\r\n'

def t_error(t):
	print(f'invalid character {t.value[0]}')
	raise SyntaxError

lex.lex()
