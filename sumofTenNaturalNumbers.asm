ADDI x2, x3, 11 # n =11
loop:  # this is label
BEQ x1, x2, skip # if(i==11) goto skip
ADD x3, x3, x1 # sum = sum + i
# This is a comment
Unknown statement
ADDI x1, x1, 1 # i++;
JAL loop # goto loop
skip:  # this is label
