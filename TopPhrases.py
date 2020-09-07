from functools import partial
from collections import Counter
import sys
cnt = Counter()

CHUNK_SIZE = 1024*1000000
### Reading the input from command line ####
filename = sys.argv[1]
num=0
with open(filename, 'rb') as file:
    for chunk in iter(partial(file.read, CHUNK_SIZE), b''):
            num=num+1
            if(num%101==1):
                print(num)
            try:
                c=Counter(chunk.decode('utf8').split('|'))
            except:
                c=Counter(chunk.split('|'))
            cnt+=c
            
print (cnt.most_common(100000))
