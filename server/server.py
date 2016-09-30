import sys 

verbose = False
for arg in sys.argv:
	if arg == '-v':
		verbose = True
	elif arg != sys.argv[0]:
		print('error: unkown argument.  Exiting...')
		exit()
exit()
