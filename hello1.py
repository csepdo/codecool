import sys

try:
    username = sys.argv[1]
    if  username in sys.argv:
        print ('Hello '+username+'!')
except IndexError:
    print('Hello world!')