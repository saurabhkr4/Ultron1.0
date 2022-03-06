##-------------------------------Bubble Sort ---------------------------------------#
# In the given bubble sort program we are sorting 5 integers 
# It shows sorted integers from x18 to x22
# and unsorted from x27 to x31
.text
# x6 = 100
ADDI x6, x0, 100
ADDI x7, x0, 4
SW   x7, 0(x6)      # A[0] = 4
ADDI x7, x0, 5
SW   x7, 1(x6)      # A[1] = 5
ADDI x7, x0, 1
SW   x7, 2(x6)      # A[2] = 1
ADDI x7, x0, 2
SW   x7, 3(x6)      # A[3] = 2
ADDI x7, x0, 3
SW   x7, 4(x6)      # A[4] = 3
# A = {5,4,3,2,1}
printArray:     # Here we are actually loading the values in registers instead of printing
ADDI x6, x0, 100
LW   x27, 0(x6)      # x27 = A[0] 
LW   x28, 1(x6)      # x28 = A[1] 
LW   x29, 2(x6)      # x29 = A[2] 
LW   x30, 3(x6)      # x30 = A[3] 
LW   x31, 4(x6)      # x31 = A[4] 

ADDI x8, x0, 5      # size = 5

# i-> x9, j-> x19, n->x8
bubbleSort:
ADDI x9, x0, 0

oloop:
BGE x9, x8, oexit
ADDI x19, x8, 0
SUBI x19, x19, 1
iloop:
BGE x9, x19, iexit
# x23 -> *A, x24->*A[j], *x25->A[i]
#            x21-> A[j],  x22->A[i]
swap:
ADDI x23, x6, 0
ADD x24, x23, x9
ADD x25, x23, x19
LW  x21, 0(x24)
LW  x22, 0(x25)
BGE x22, x21, skip

# x18-> temp
ADDI x18, x22, 0
ADDI x22, x21, 0
ADDI x21, x18, 0
SW x21, 0(x24)
SW x22, 0(x25)
skip:
SUBI x19, x19, 1
JAL iloop
iexit:
ADDI x9, x9, 1
JAL oloop
oexit:

ADDI x23, x0, 0
ADDI x24, x0, 0
ADDI x25, x0, 0

printSortedArray:
# Here we are actually loading the values in registers instead of printing
ADDI x6, x0, 100
LW   x18, 0(x6)      # x18 = A[0] 
LW   x19, 1(x6)      # x19 = A[1] 
LW   x20, 2(x6)      # x20 = A[2] 
LW   x21, 3(x6)      # x21 = A[3] 
LW   x22, 4(x6)      # x22 = A[4] 
# A = {1,2,3,4,5}