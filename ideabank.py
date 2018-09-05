import sys
def print_file():
    with open ('ideabank.txt', 'r') as ideabank:
        print('Your Ideabank:')
        for i, line in enumerate(ideabank):
            print('{}. {}'.format(i+1, line.strip()))
if len(sys.argv) == 1:    
    new_idea = input('What is your new idea: ')
    with open ('ideabank.txt', 'a') as ideabank:
        ideabank.write(new_idea + '\n')
    print_file()
else:
    if sys.argv[1] == '--list':
        print_file()
    #elif sys.argv[1] == '--del'
    #    n = sys.argv [2]
    #    with open('ideabank.txt', 'w') as ideabank:
    #        if i == n:

