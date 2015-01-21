#!/usr/bin/env python3

def color(color, message) :
	return "\033[{0}m{1}\033[0m".format(color,message)

def step(message) :
	import sys
	print(color('34;1', ":: "+message), file=sys.stderr)

def error(message) :
	import sys
	print(color('31;1', "Error: "+message), file=sys.stderr)

def warn(message) :
	import sys
	print(color('33', "Atenció: "+message), file=sys.stderr)

def fail(message, code=-1) :
	error(message)
	import sys
	sys.exit(code)


if __name__ == "__main__":
	step('Testing common messages')
	warn('Això és un avís')
	error('Això és un error')
	fail('Això és un error fatal i ara es sortira')


