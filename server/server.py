# Python 3.x
import sys 
import config

verbose = False
generateConfig = False
configFile = config.configParser()
# Check for arguments
for arg in sys.argv:
	if arg == '-v':
		verbose = True
	elif arg == '-c':
		generateConfig = True
		configFile.generate()
		
	elif arg != sys.argv[0]:
		print('error: unkown argument.  Exiting...')
		exit()
configFile.load()


exit()
