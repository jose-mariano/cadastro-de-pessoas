import sys
from src.controllers import IndexController

if __name__ == '__main__':
    interface = 'GUI'
    if (len(sys.argv) > 1):
        interface = sys.argv[1]

    IndexController(interface).start()
