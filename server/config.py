# functions to control script configuration file
defaultConfig = {'Server Path=': './\n', 'Server Save Path=': './\n'}			#defaultConfig is a dictionary that contains the information for the default config file
def generate():
	config = open('config', 'w')
	for name, value in defaultConfig.items():
		config.write(name + value)
	config.close()
