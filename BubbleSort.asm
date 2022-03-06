##-------------------------------Bubble Sort -----------------------------------------#
#In the given bubble sort program we are sorting 5 integers 
#which are loaded in registers x26 to x30.
#The sorted integers are stored in the
#registers x26 to x30 after running the file.

.text
# x1 = 100
ADDI x1, x0, 100
ADDI x4, x0, 4
SW   x4, 0(x1)      # A[0] = 4
ADDI x4, x0, 5
SW   x4, 1(x1)      # A[1] = 5
ADDI x4, x0, 1
SW   x4, 2(x1)      # A[2] = 1
ADDI x4, x0, 2
SW   x4, 3(x1)      # A[3] = 2
ADDI x4, x0, 3
SW   x4, 4(x1)      # A[4] = 3
# A = {5,4,3,2,1}
printArray:
ADDI x1, x0, 100
LW   x26, 0(x1)      # x16 = A[0] 
LW   x27, 1(x1)      # x17 = A[1] 
LW   x28, 2(x1)      # x18 = A[2] 
LW   x29, 3(x1)      # x19 = A[3] 
LW   x30, 4(x1)      # x20 = A[4] 

ADDI x5, x0, 5      # size = 5

# i-> x9, j-> x10, n->x5
bubbleSort:
ADDI x9, x0, 0

oloop:
BGE x9, x5, oexit
ADDI x10, x5, 0
SUBI x10, x10, 1
iloop:
BGE x9, x10, iexit
# x13 -> *A, x14->*A[j], *x15->A[i]
#            x16-> A[j],  x17->A[i]
swap:
ADDI x13, x1, 0
ADD x14, x13, x9
ADD x15, x13, x10
LW  x16, 0(x14)
LW  x17, 0(x15)
BGE x17, x16, skip

# x18-> temp
ADDI x18, x17, 0
ADDI x17, x16, 0
ADDI x16, x18, 0
SW x16, 0(x14)
SW x17, 0(x15)
skip:
SUBI x10, x10, 1
JAL iloop
iexit:
ADDI x9, x9, 1
JAL oloop
oexit:


printSortedArray:

ADDI x1, x0, 100
LW   x16, 0(x1)      # x16 = A[0] 
LW   x17, 1(x1)      # x17 = A[1] 
LW   x18, 2(x1)      # x18 = A[2] 
LW   x19, 3(x1)      # x19 = A[3] 
LW   x20, 4(x1)      # x20 = A[4] 
# A = {1,2,3,4,5}