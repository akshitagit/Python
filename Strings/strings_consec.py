import itertools
import os

a = "aabccba"
def remove_consecutive_duplicates(string):
    for i in string:
        length = len(i)
        if 1 < length < 1000:
            print(f"The string is the correct length - {length}")
            str_fixed = (''.join( i for i, _ in itertools.groupby(i)))
            print(str_fixed)
            print(f"The new non-consecutive length is - {len(str_fixed)}")
        else: 
            print(f"The string is the incorrect length - {length}")

root_dir = os.path.dirname(os.path.abspath(__file__))
with open(root_dir+'/add.txt', 'r') as f:
    words = f.readlines()
    words = [x.strip() for x in words]
print(words)

remove_consecutive_duplicates(words)