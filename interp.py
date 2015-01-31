def interp(expr):
	def interp0(expr, env):
		if isinstance(expr, str):						#variable
			return env[expr]
		elif isinstance(expr, (int, float)):			#numerics
			return expr
		elif len(expr) == 3 and expr[0] == 'lambda':	#lambda
			return ('closure', expr[1], expr[2], env)
		elif len(expr) == 2:							#invocation
			v1, v2= interp0(expr[0], env), interp0(expr[1], env)
			if len(v1) == 4:
				clos, param, body, envirn = v1
				if clos == 'closure':
					env_new = envirn.copy()
					env_new[param] = v2
					return interp0(body, env_new)
		elif len(expr) == 3:							#calculation(+-x/)
			op, e1, e2 = expr
			v1, v2 = interp0(e1, env), interp0(e2, env)
			if op == '+': return v1+v2
			if op == '-': return v1-v2
			if op == '*': return v1*v2
			if op == '/': return v1/v2
	return interp0(expr, {})

if __name__ == '__main__':

	# should all be 6

	print interp(('+', 4, 2))

	print interp(('*', 2, 3))

	print interp(('*', 2, ('-', 7, 4)))

	print interp(('/', ('*', 24, 2), ('+', 2, 6)))

	print interp((('lambda', ('x'), ('*', 2, 'x')), 3))

	print interp(((('lambda', ('x'), ('lambda', ('y'), ('*', 'x', 'y'))), 2), 3))

	print interp(((('lambda', ('y'), ('lambda', ('x'), ('*', 'y', 2))), 3), 1000))

	print interp((('lambda', ('y'), (('lambda', ('x'), ('*', 'y', 2)), 1000)), 3))
	
	print interp((('lambda', ('y'), ((('lambda', ('y'), ('lambda', ('x'), ('*', 'y', 2))), 3), 0)), 4))
