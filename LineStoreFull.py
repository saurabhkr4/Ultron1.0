# It will take All instructions Line wise till we  get -1, and Store it a list
# After that we will Implement each Code Line wise.




def t_type(s):
    # print("Operation Peformed")
    return s[1:]

def isLabel(s):
    return s.find(':')!=-1

memory = []*300
reg = [0]*32

def printreg():
    print(list(range(32)))
    reg[0] = 0
    for  i in range(32):
        if i<1:
            str = ""
        elif i<10:
            str= ","
        else:
            str = ", "
        print(str,reg[i], end = "")
    print("\n","pc =",pc)


# reg[0] = 0  # think on how to make it immutable

def listInd( ll, ele):
    if ll.count(ele):
        return ll.index(ele)
    else:
        return 1000

instr = ['ADD','SUB','MUL','ADDI','SUBI','MULI','LW','SW','BNE','BEQ','JAL']
pc = 0;
target = dict()
targetinv = dict()
big = []

while 1:
    ooo = input()
    if ooo == '-1':
        break
    if ooo == '' or (ooo.split())[0][0] == '#':
        continue
    big.append(ooo)
    if isLabel(ooo):
        ooo = list(ooo.split(':'))
        target[ooo[0]] = pc
        targetinv[pc] = ooo[0]
    pc = pc+1

print(big)
print(target)
pc = 0
while pc<len(big):
    
    
    # s = 'add $t0, $t12, $t73'
    
    s = big[pc]
    pc = pc+1
    if s =='-1':
        break
    if s == '':
        continue
    # else:
    #     pc = pc + 1
    p = (s.replace(',', ''))
    print (p)
    llist = p.split();

    print (llist)
    l = len(llist);
    t = []
    for i in range(1,l):
        t.append(llist[i].replace('$',''))
    opp = listInd(instr, llist[0])
    if opp ==-1:
        print("ok")
    #     # if isLabel(llist[0]): # check if its label
    #     #      p2lp = (list(llist.split(':')))[0]
    #     #      target[p2lp] = pc
    elif opp<6:
        for i in range(0,l-1):
            # print(t[i])
            if(t[i][0] == 't'):
                rgind = t_type(t[i])                
                if rgind.isdigit():
                    rgind = int(rgind)
                    if(rgind < 3):
                        rgind = rgind + 5
                    else:
                        rgind = rgind +25
                else:
                    print("Something's fishy")
                print('x',rgind)
            elif(t[i][0] == 'a'):
                rgind = t_type(t[i])
                
                if rgind.isdigit():
                    rgind = 10 + int(rgind)
                else:
                    print("Something's fishy")
                print('x',rgind)
            elif(t[i][0] == '#'):
                break
            elif(t[i][0] == 's'):
                rgind = t_type(t[i])            
                if rgind.isdigit():
                    rgind = int(rgind)
                    if rgind<2:
                        rgind = rgind + 8
                    else:
                        rgind = rgind + 16
                else:
                    print("Something's fishy")
                print('x',rgind)
                
            elif t[i].isdecimal():
                rgind = t[i]   
                rgind = int(rgind)
                print('const',rgind)

            if(i==0):
                rd = rgind
            elif(i==1):
                rs1 = rgind
            elif(i==2):
                rs2 = rgind
        if(rd>31 or rs1> 31 or rd>31):
            print("REGISTERS OUT OF INDEX")
            continue

        if(opp==0):
            reg[rd] = reg[rs1] + reg[rs2]
        elif(opp==1):
            reg[rd] = reg[rs1] - reg[rs2]
        elif opp ==2:
            reg[rd] = reg[rs1] * reg[rs2]            
        elif opp==3:
            reg[rd] = reg[rs1] + rs2
        elif opp==4:
            reg[rd] = reg[rs1] - rs2
        elif opp==5:
            reg[rd] = reg[rs1] * rs2
    elif opp == 8 or opp == 9:
        for i in range(0,l-1):
            # print(t[i])
            if(t[i][0] == 't'):
                rgind = t_type(t[i])                
                if rgind.isdigit():
                    rgind = int(rgind)
                    if(rgind < 3):
                        rgind = rgind + 5
                    else:
                        rgind = rgind +25
                else:
                    print("Something's fishy")
                print('x',rgind)
            elif(t[i][0] == 'a'):
                rgind = t_type(t[i])
                
                if rgind.isdigit():
                    rgind = 10 + int(rgind)
                else:
                    print("Something's fishy")
                print('x',rgind)
            elif(t[i][0] == '#'):
                break
            elif(t[i][0] == 's'):
                rgind = t_type(t[i])            
                if rgind.isdigit():
                    rgind = int(rgind)
                    if rgind<2:
                        rgind = rgind + 8
                    else:
                        rgind = rgind + 16
                else:
                    print(t[i])
                print('x',rgind)
                
            elif t[i].isdecimal():
                rgind = t[i]   
                rgind = int(rgind)
                print('const',rgind)

            if(i==0):
                rc1 = rgind
            elif(i==1):
                rc2 = rgind
        if(rc1>31 or rc2> 31):
            print("REGISTERS OUT OF INDEX")
            continue
        if opp == 8:
            if(reg[rc1] != reg[rc2]):
                pc = target[t[2]]
        elif opp == 9:
            if(reg[rc1] == reg[rc2]):
                pc = target[t[2]]
    elif opp == 10:
        print("t[0]:",t[0])
        pc = target[t[0]] 
        
    printreg()

