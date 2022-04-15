    .text
ADDI  x7, x0, 100
ADDI x4, x0,10
ADDI x1, x0,  5
ADDI  x8, x0, 2
ADD x3, x2, x1
ADDI x3, x3, 10
BNE x3, x4, loop
loop:
    ADDI x5, x4, 1
    ADD x5, x5, x5