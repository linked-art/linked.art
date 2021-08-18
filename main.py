def define_env(env):

	@env.filter
	def regex_replace(source, regex, replace):
		try:
			repl = re.compile(regex)
		except:
			print("ERROR: Failing regex: %s" % regex)
			return source
		return repl.sub(replace, source)

	@env.filter
	def regex_replace_fn(source, regex, fnname):
		try:
			repl = re.compile(regex)
		except:
			print("ERROR: Failing regex: %s" % regex)
			return source
		try:
			fn = globals()[fnname]
		except:
			print("ERROR: No such function '%s'" % fnname)
		return repl.sub(fn, source)
  
