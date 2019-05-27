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

# t_LBRACKET = r'\['
# t_RBRACKET = r'\]'
# t_COMMA = r','
# t_COLON = r':'
# t_IN = r'in'
# t_ASSIGN = r'='
# t_IF = r'if'
# t_ELSE = r'else'
# t_WHILE = r'while'
# t_FOR = r'for'
# t_DO = r'do'

keywords = (
	'AND', 'OR', 'XOR', 'NOT', 
	'PRINT', 'MAIN'
)

tokens = keywords + (
	'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 
	'PLUS', 'MINUS', 'TIMES', 'DIV', 'MOD', 'POW', 
	'EQ', 'LT', 'LE', 'GT', 'GE', 'NE', 
	'SEMI', 
	'REAL', 'INT', 'BOOL', 'CHAR', 'STRING', 
)

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMI = r';'
t_PLUS = r'\+'
t_MINUS = r'-'
t_TIMES = r'\*'
t_DIV = r'/'
t_MOD = r'%'
t_POW = r'\*\*'
t_EQ = r'=='
t_LT = r'<'
t_GT = r'>'
t_LE = r'<='
t_GE = r'>='
t_NE = r'!='
t_NOT = r'not'
t_AND = r'and'
t_OR = r'or'
t_XOR = r'xor'
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

def t_CHAR(t):
	r'\'[^\'\\]\' | \'\\\'\''
	t.value = ast.CharNode(t.value)
	return t

def t_STRING(t):
	r'"(?:[^"\\]+|\\.)*"'
	t.value = ast.StringNode(t.value)
	return t

t_ignore = ' \t\r\n'

def t_error(t):
	print(f'Illegal character {t.value[0]}')
	t.lexer.skip(1)

lex.lex()
