ADDI x5, x0, 9
MULI x6, x5, 10
SW x5, 10(x6)
LW x7, 10(x6)
# As the Value of x5 is loaded in x7,
# Hence LW and SW are working properly


