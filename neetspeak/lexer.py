from ply import lex
import ast

# keywords = (
#     'INT', 'REAL', 'BOOL', 'CHAR', 'VOID', 'STRING', 'OBJECT',
#     'LIST', 'MAP', 'SET',
#     'TRUE', 'FALSE', 'AND', 'OR', 'XOR', 'NOT', 'IN',
#     'IF', 'ELSE', 'WHILE', 'FOR', 'DO', 'RETURN',
#     'PRINT'
# )

# tokens = keywords + (
#     'LBRACKET', 'RBRACKET',
#     'COMMA', 'COLON',
#     'PLUS', 'MINUS', 'TIMES', 'DIVIDE', 'ASSIGN',
#     'MODULUS', 'DIV', 'POWER',
#     'EQ', 'LT', 'LE', 'GT', 'GE', 'NEQ',
#     'ID'
# )

# t_LBRACKET = r'\['
# t_RBRACKET = r'\]'
# t_COMMA = r','
# t_COLON = r':'
# t_PLUS = r'\+'
# t_MINUS = r'-'
# t_TIMES = r'\*'
# t_DIVIDE = r'/'
# t_DIV = r'//'
# t_MOD = r'%'
# t_EXP = r'\*\*'
# t_EQ = r'=='
# t_LT = r'<'
# t_GT = r'>'
# t_LE = r'<='
# t_GE = r'>='
# t_NEQ = r'!='
# t_NOT = r'not'
# t_AND = r'and'
# t_OR = r'or'
# t_IN = r'in'
# t_ASSIGN = r'='
# t_IF = r'if'
# t_ELSE = r'else'
# t_WHILE = r'while'
# t_FOR = r'for'
# t_DO = r'do'

keywords = (
	'PRINT', 'MAIN'
)

tokens = keywords + (
    'LPAREN', 'RPAREN', 'LBRACE', 'RBRACE', 
    'SEMICOLON', 
    'INTEGER', 'DECIMAL', 'CHARACTER', 
    'STRING', 
)

t_LPAREN = r'\('
t_RPAREN = r'\)'
t_LBRACE = r'\{'
t_RBRACE = r'\}'
t_SEMICOLON = r';'
t_PRINT = r'print'
t_MAIN = r'main'

def t_INTEGER(t):
    r'\d+'
    t.value = ast.IntegerNode(t.value)
    return t

def t_DECIMAL(t):
    r'\d*(\d\.|\.\d)\d*([eE]-?\d+)?'
    t.value = ast.DecimalNode(t.value)
    return t

# def t_BOOLEAN(t):
#     r'true | false'
#     t.value = None
#     return t

def t_CHARACTER(t):
    r'\'[^"\\]\' | \'\\\'\''
    t.value = ast.CharacterNode(t.value)
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
