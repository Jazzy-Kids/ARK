# functions to control script configuration file
import sys


class configParser:

    defaultConfig = {'Server Path=': './\n', 'Server Save Path=': './\n', 'Server Script=': 'start.bat\n'}			#defaultConfig is a dictionary that contains the information for the default config file
    configText = {}

    def load(self):
    	with open('config', 'r+') as config:
    	    for text in config:
    		    strarray = text.split('=')
    		    self.configText[strarray[0] + '='] = strarray[1]
        print(self.configText)


    def generate(self):
        config = open('config', 'w')
        for name, value in self.defaultConfig.items():
    	    config.write(name + value)

	config.close()
	
    def append(self, name, value):
    	with open('config', 'a') as config:
    		config.write(name + "=" + value)
    		self.configText[name] = value

    def change(self, name, value):
    	if name in self.configText:
    		self.configText[name] = value
    		print(self.configText[name])
    		
    	else:
    	    print("ERROR: value " + name + " not found")
    	    return
    	
    	with open('config', 'w') as config:
	    for textName, textValue in self.configText.items():
	    config.write(textName + textValue)
	
	def read(self, name):
	    return self.defaultConfig[name]
