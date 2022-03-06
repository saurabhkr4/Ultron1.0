.text
	# x1 = 100
	ADDI x1, x0, 100
	ADDI x4, x0, 5
	SW   x4, 0(x1)      # A[0] = 5
	ADDI x4, x0, 4
	SW   x4, 1(x1)      # A[1] = 4
	ADDI x4, x0, 3
	SW   x4, 2(x1)      # A[2] = 3
	ADDI x4, x0, 2
	SW   x4, 3(x1)      # A[3] = 2
	ADDI x4, x0, 1
	SW   x4, 4(x1)      # A[4] = 1
    # A = {5,4,3,2,1}
    ADDI x5, x0, 5      # size = 5
    
    # i-> x9, j-> x10, n->x5
    bubbleSort:
    

    printArray:
    
    