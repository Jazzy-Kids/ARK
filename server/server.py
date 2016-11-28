# Python 3.x
import sys 
import config

verbose = False
generateConfig = False
configFile = config.configParser()

helpText = "\nThis is a python script to manage an ark server.\n\n-h\tDisplays help text.\n-v\tVerbose mode(not working).\n-c\tGenerates a new config file for the script."

# Check for arguments
for arg in sys.argv:
	if arg == '-v':
		verbose = True
	elif arg == '-c':
		generateConfig = True
		configFile.generate()
	elif arg == '-h':
		print(helpText)
		exit()
		
	elif arg != sys.argv[0]:
		print('error: unkown argument.  Exiting...')
		exit()
configFile.load()

print("Welcome to the ark management script")
while(True):
	command = input()
	command = command.upper()

	if command == "QUIT" or command == "Q":
		print('\nQuitting...')
		exit()
	elif command == "CONFIG GENERATE"	 or 			command == "C":
		print('\nGenerating Config...')
		configFile.generate()
	elif command == "START" or command == "S":
		print("\nStarting Server...")
		startServer()
	
	else:
		print('\nPlease enter a command')
	

exit()
