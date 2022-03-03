from atexit import register
from dis import Instruction

memory = []*32700
reg = [0]*32

reg[0] = 0  # think on how to make it immutable

def listInd( ll, ele):
    if ll.count(ele):
        return ll.index(ele)
    else:
        return -1

instr = ['add','sub','bne','jal','lw','sw']

# x = '' # The string is declared
# for line in iter(input, x):
#     pass

# print (x)

import sys
s = sys.stdin.read()

ll = s.split('\n')

for i in ll:
    print(i);
print("\n")
# for i in range(len(ll)):
#     print(ll[i])

# lww = [[0]*10]*10
lww = [[]*10]*10
for i in range(len(ll)):
    lww[i] = ll[i].split()
    lww[i].pop(0)
    for j in lww[i]:
        j = j[1:]
        j = j.replace(',', '', )
        print(j , j[1:])
    
for i in lww:
    print (i)