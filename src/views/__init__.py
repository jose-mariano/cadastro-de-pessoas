from src.views.CLI import CLI
from src.views.GUI import GUI

def getInterface(interfaceType, controller):
	types = {
		"CLI": CLI,
		"GUI": GUI,
		"default": GUI
	}

	if (interfaceType not in types.keys()):
		return types["default"](controller)

	return types[interfaceType](controller)

