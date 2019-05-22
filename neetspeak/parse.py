from ply import yacc
import lexer
import ast

tokens = lexer.tokens

precedence = (
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
    '''statement : PRINT LPAREN expression RPAREN SEMICOLON'''
    p[0] = ast.PrintNode(p[3])

def p_expression(p):
    '''expression : INTEGER
                  | DECIMAL
                  | CHARACTER
                  | STRING'''
    p[0] = p[1]

def p_error(p):
    if not p:
        print('syntax error')

parser = yacc.yacc()


def parse(data, debug = 0):
	parser.error = 0
	p = parser.parse(data, debug = debug)
	if parser.error:
		return None
	return p
