import getpass

try:
    username=getpass.getuser()
    print('Hello '+username+'!')
except:
    print('Hello world!')