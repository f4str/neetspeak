import sys
import lexer
import parse as parser

if len(sys.argv) != 2:
	sys.exit('invalid arguments')

with open(sys.argv[1]) as fd:
	data = fd.read()
program = parser.parse(data)
program.execute()

