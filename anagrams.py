import sys
from itertools import groupby
file = sys.argv[1]
with open (file, 'r') as f:
    anagrams = f.read().splitlines()
    anagram_groups = [list(group) for key, group in groupby(sorted(anagrams,key=sorted),sorted)]
    print('\n'.join('{}. {}'.format(*k) for k in enumerate(anagram_groups)))