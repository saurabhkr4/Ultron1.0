# CODE FOR COMPUTING SUM OF FIRST 10 NATURAL NUMBERS
ADDI x5, x6, 11  # n = 11
loop:            # this is a label
    BEQ x7, x5, skip # if(i==11) goto skip
    ADD x6, x6, x7   # sum = sum + i
    # This is a comment to check emulator's response to a comment

    ADDI x7, x7, 1   # i++;
    JAL ra, loop         # goto loop
skip:            # this is a label

# Here, Register x6 will show output as 55 
