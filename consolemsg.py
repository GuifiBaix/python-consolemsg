#!/usr/bin/env python3

def printStdError(*args) :
	import sys
	sys.stderr.write(' '.join(str(arg) for arg in args))
	sys.stderr.write('\n')
	sys.stderr.flush()

def color(color, message) :
	return "\033[{0}m{1}\033[0m".format(color,message)

def success(message) :
	import sys
	printStdError(color('32;1', ">> "+message))

def step(message) :
	import sys
	printStdError(color('34;1', ":: "+message))

def error(message) :
	import sys
	printStdError(color('31;1', "Error: "+message))

def warn(message) :
	import sys
	printStdError(color('33', "Warning: "+message))

def fail(message, code=-1) :
	error(message)
	import sys
	sys.exit(code)


if __name__ == "__main__":
	step('Testing common messages')
	success('Success!')
	warn('This might be dangerous')
	error('Something bad happened')
	fail('Something very bad happened and i will die')


