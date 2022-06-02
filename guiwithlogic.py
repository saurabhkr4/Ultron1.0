
from calendar import c
import glob
from msilib.schema import ListBox
import opcode
from pprint import pp
from tkinter import *
import tkinter.filedialog, tkinter.messagebox
import os
import tempfile
from tkinter import filedialog
from numpy import cfloat, roots

reg_name=[]
reg_value=[]

# print("DO YOU WANT TO EXECUTE EXPRESSION STEP WISE?\nIf yes, Print 1, else print 0")
# stepwise = int(input())
# if stepwise ==1:
#     stepwise= True
# else:
#     stepwise = False

jjj= 0
iii = 0
def printee(txt):
    global iii
    iii = 0
    if(iii!=len(txt)):
        # print(txt[iii])
        print("_________")
        iii+=1

def isValidLine(llist):
    return listInd(instr, llist[0])<13

# def noOfStalls(cflow,k):
#     return 1
def writtenReg(llist):
    op = listInd(instr, llist[0])
    if op<7 :
        return llist[1]
    if op == 6:
        return llist[2]
    return 'NULL'
def Dependency(cflow,k):
    # 0-> No Stall
    # 1-> 2 Stalls in non-forwarding
    # 2-> 1 Stall  in     forwarding
    # 3-> 1 Stall  in Both -> Branches Stall
    # 4-> 1 Stall in Forwarding, 2 stalls in Non-Forwarding -> Special Load-Add Stall
    lll = cflow[k] 
    op = listInd(instr,lll[0])
    if k>0 and listInd(instr, cflow[k-1][0]) > 7 :
        return 3
    if op<6:
        read1 = lll[2]        
        if k>0:
            if cflow[k-1][0] == 'LW':
                return 4
            if writtenReg(cflow[k-1]) == read1 : # take care with branches
                return 1
        if k>1:
            if writtenReg(cflow[k-2]) == read1 :
                return 2
        if op<3:
            read2 = lll[3]
            if k>0:
                if writtenReg(cflow[k-1]) == read2 :  # take care with branches
                    return 1
            if k>1:
                if writtenReg(cflow[k-2]) == read2 :
                    return 2
    
    elif op == 6:
        if lll[2].find('(') != -1:
            ti = lll[2].replace('(', " ").replace(')'," ")
            ti = ti.split();
            oadd = int(ti[0])
            if(len(ti)>1):
                oin = ti[1]
                # print ("->>>>>",oin, oadd)
                if k>0:
                    if oin == writtenReg(cflow[k-1]) :
                        if Dependency(cflow,k-1)==0:
                            return 1
                        else:
                            return 2
                if k>1:
                    if oin == writtenReg(cflow[k-2])  :
                        return 2
            else:
                print("Wrong Memory Fetch")


    elif op == 7:
        read1 = lll[1]
        val = 0
        if k>0:
            if writtenReg(cflow[k-1]) == read1 :# take care with branches
                return 1
        if k>1:
            if writtenReg(cflow[k-2]) == read1 and  Dependency(cflow,k-2)==0:
                val = 2
        if lll[2].find('(') != -1:
            ti = lll[2].replace('(', " ").replace(')'," ")
            ti = ti.split();
            oadd = int(ti[0])
            if(len(ti)>1):
                oin = ti[1]
                # print ("->>>>>",oin, oadd)
                if k>0:
                    if oin == writtenReg(cflow[k-1]) :
                        return 1
                if k>1:
                    if oin == writtenReg(cflow[k-2]) :
                        return 2
            else:
                print("Wrong Memory Fetch")
        return val
    elif op< 12:        
        read1 = lll[1]
        if k>0:
            if writtenReg(cflow[k-1]) == read1 : # take care with branches
                return 1
        if k>1:
            if writtenReg(cflow[k-2]) == read1 :
                return 2
        read2 = lll[2]
        if k>0:
            if writtenReg(cflow[k-1]) == read2 : # take care with branches
                return 1
        if k>1:
            if writtenReg(cflow[k-2]) == read2 :
                return 2  
    return 0
def t_type(s):
    # print("Operation Peformed")
    return s[1:]
def filter(s):
    s = s.removeprefix('$')
    if(s[0] == 't'):
        rgind = t_type(s)                
        if rgind.isdigit():
            rgind = int(rgind)
            if(rgind < 3):
                rgind = rgind + 5
            else:
                rgind = rgind +25
        # else:
        #     print("")
        # print('x',rgind)
        return rgind
    elif(s[0] == 'x'):
        rgind = t_type(s)
        
        if rgind.isdigit():
            rgind = int(rgind)
        # else:
        #     print("")
        # print('x',rgind)
        return rgind
    elif(s[0] == 'a'):
        rgind = t_type(s)
        
        if rgind.isdigit():
            rgind = 10 + int(rgind)
        # else:
        #     print("")
        # print('x',rgind)
        return rgind
    elif(s[0] == 's'):
        rgind = t_type(s)            
        if rgind.isdigit():
            rgind = int(rgind)
            if rgind<2:
                rgind = rgind + 8
            else:
                rgind = rgind + 16
        # else:
        #     print(rgind)
        # print('x',rgind)
        return rgind        
    elif s.isdecimal():
        rgind = s   
        rgind = int(rgind)
        # print('const',rgind)
        return rgind
def isLabel(s):
    return s.find(':')!=-1
N__ = 1024
memory = [0]*N__
mll = set()
reg = [0]*32
pc = 0
def printreg():
    # print(list(range(32)))
    # for cfl in cflow.keys():
    #     print(cfl,'-',cflow[cfl])
    global pc
    reg[0] = 0
    pc_value.config(text= str(pc))
    for  i in range(32):
        reg_value[i].config(text=str(reg[i]))
        # reg_value[i].config(expand=1)
        # reg_value[i].config(padx =60)

        # if reg[i]>10:
        #     reg_value[i].config(padx = 54)
        # elif reg[i]>100:
        #     reg_value[i].config(padx = 38)
        # elif reg[i]>100000:
        #     reg_value[i].config(padx = 33)

        '''if reg[i]!=0:
            print('x', end ='')
            print(i,'=',reg[i], end = " | ")'''
        

        # if i<1:
        #     strj = ""
        # elif i<10:
        #     strj= ","
        # else:
        #     strj = ", "
        # print(strj,reg[i], end = "")
    print("pc =",pc)   


def listInd( ll, ele):
    if ll.count(ele):
        return ll.index(ele)
    else:
        return 100000

instr = ['ADD','SUB','MUL','ADDI','SUBI','MULI','LW','SW','BNE','BEQ','BGE','BLT','JAL','.text','.data','end']
cflow = dict()
target = dict()
targetinv = dict()
big = []
ppview = []
# pc = 0
def clearBig():
    global big,cflow,target,targetinv,jjj,pc,NonFor,forw, mll
    big = []
    ppview = []
    cflow = dict() 
    target = dict()
    targetinv = dict()
    myList.delete(0,END) 
    jjj = 0
    pc = 0
    NonFor = list()
    forw  = list()
    mll = set()




def setpc0():
    global pc
    pc = 0
    pc_value.config(text= str(pc))

# def print_area(txt): 
#     temp_file = tempfile.mktemp('.asm')
#     open(temp_file, 'w').write(txt)
#     os.startfile(temp_file)

root = Tk()
root.configure(background = "floral white")
# root.pack_propagate(0)
# reg_name=[]
# reg_value=[]

#PC
pc_label = Label(root, text="PC", padx = 48, pady=6, bd = 3, font=("Arial",11),bg ="gray4", fg="white", relief=RIDGE)
pc_label.grid(row=0, column =0)
pc_value =Label(root, text="0",padx = 60, pady=4,bg="#282823",fg="white",bd=3, font=("Arial,11"), relief=RIDGE)
pc_value.grid(row=0, column =1)


#Clear Button
def clearReg():
    # global pc
    # pc = 0
    setpc0()
    print("pc=",pc)
    pc_value.config(text= str(pc))
    for i in range (32):
        #make the values of elements in the backend register zero
        #register[i] = 0
        reg[i] = 0
        reg_value[i].config(text="0")
        reg_value[i].config(padx=60)

clearButton = Button(root, text = "CLEAR",padx=96,pady=1,bg="#F8E907",bd=1, fg="black",font=("calibri",14), command=clearReg, relief=RAISED )
clearButton.grid(row=0, column =2, columnspan =2)

#Binary and Hexadecimal Button

radixCount = 0
def buttonColor():
    global radixCount
    if radixCount==1:
        binaryButton.config(bg="#8DB437", fg="black")
        hexaButton.config(bg="skyblue", fg="black")
        decimalButton.config(bg="skyblue", fg="black")
    elif radixCount==2:
        binaryButton.config(bg="skyblue", fg="black")
        hexaButton.config(bg="#8DB437", fg="black")
        decimalButton.config(bg="skyblue", fg="black")
    elif radixCount==3:
        binaryButton.config(bg="skyblue", fg="black")
        hexaButton.config(bg="skyblue", fg="black")
        decimalButton.config(bg="#8DB437", fg="black")

#decimal to Binary
def decimalToBinary(n):
    return bin(n).replace("0b", "")

#decimal to Hexadecimal
def decimalToHexadecimal(n):
    return hex(n).replace("0x", "")




def binaryCommand():
    #write code and call function to make the register values binary

    for i in range(32):
        reg_value[i].config(text = str(decimalToBinary(reg[i])))

    global radixCount
    radixCount = 1
    buttonColor()

def hexaCommand():
    #write code and call function to make the register values hexadecimal
    for i in range(32):
        reg_value[i].config(text= str(decimalToHexadecimal(reg[i])))
    
    global radixCount
    radixCount = 2
    buttonColor()

def decimalCommand():

    for i in range(32):
        reg_value[i].config(text= str(reg[i]))

    global radixCount
    radixCount = 3
    buttonColor()


binaryButton = Button(root, text="Binary",pady=64,bg="skyblue", fg="black", command = binaryCommand)
binaryButton.grid(row=1, column = 4, rowspan=4)
hexaButton = Button(root, text="Hexa  ",pady=64, bg="skyblue", fg="black", command = hexaCommand)
hexaButton.grid(row=5, column = 4, rowspan=4)
decimalButton = Button(root, text="Deci  ",padx=3,pady=64, bg="skyblue", fg="black", command = decimalCommand)
decimalButton.grid(row=9, column = 4, rowspan=4)

#creating the Labels for register names
reg_name.append(Label(root, text="zero(x0)", padx = 32, pady=6, bd = 3, font=("Arial",11),bg ="gray9", fg="white", relief=RIDGE))

reg_name.append(Label(root, text="ra(x1)", padx = 40, pady=6, bd = 3, font=("Arial",11),bg ="gray4", fg="white", relief=RIDGE))
reg_name.append(Label(root, text ="sp(x2)",padx = 38, pady=6, bd = 3, font=("Arial",11),bg ="gray4", fg="white", relief=RIDGE))
reg_name.append(Label(root, text ="gp(x3)",padx = 38, pady=6, bd = 3, font=("Arial",11),bg ="gray4", fg="white", relief=RIDGE))
reg_name.append(Label(root, text ="tp(x4)",padx = 40, pady=6, bd = 3, font=("Arial",11),bg ="gray4", fg="white", relief=RIDGE))

for i in range(3):
    reg_name.append(Label(root, text ="t"+str(i)+"(x"+str(i+5)+")",padx = 42, pady=6, bd = 3, font=("Arial",11),bg ="gray4", fg="white", relief=RIDGE))

reg_name.append(Label(root, text ="s0(x8)",padx = 40, pady=6, bd = 3, font=("Arial",11),bg ="gray4", fg="white", relief=RIDGE))
reg_name.append(Label(root, text ="s1(x9)",padx = 40, pady=6, bd = 3, font=("Arial",11),bg ="gray4", fg="white", relief=RIDGE))

for i in range(8):
    reg_name.append(Label(root, text ="a"+str(i)+"(x"+str(i+10)+")",padx = 36, pady=6, bd = 3, font=("Arial",11),bg ="gray4", fg="white", relief=RIDGE))

for i in range (10):
    reg_name.append(Label(root, text="s"+str(i+2)+"(x"+str(i+18)+")", padx = 36, pady=6, bd = 3, font=("Arial",11),bg ="gray4", fg="white", relief=RIDGE))

reg_name[26].config(padx="32")
reg_name[27].config(padx="32")

for i in range (4):
    reg_name.append(Label(root, text="t"+str(i+3)+"(x"+str(i+28)+")", padx = 38, pady=6, bd = 3, font=("Arial",11),bg ="gray4", fg="white", relief=RIDGE))
    
#placing the reg_name 
for i in range(32):
    # reg_name[i].pack_propagate(0)
    if i>15:
        reg_name[i].grid(row=i-15, column = 2)
    else:
        reg_name[i].grid(row=i+1, column = 0)

#Labels for values in the registers
for i in range(32):
    reg_value.append(Label(root, text="0",padx = 60, pady=4,bg="#282823",fg="white",bd=3, font=("Arial,4"), relief=RIDGE))

for i in range(32):
    # reg_value[i].pack_propagate(0)
    if i>15:
        reg_value[i].grid(row=i-15,column=3)
    else:
        reg_value[i].grid(row=i+1,column=1)


# separator = ttk.Separator(root, orient='vertical')
# separator.pack(fill='y')


#Creating a seperator
seperator = Label(root,bg = "floral white",padx = 8, pady = 100)
seperator.grid(row = 1, column = 5, rowspan = 10)


#creating the textbox
global j
j=1
def highLight():
    # t.delete('2.0','3.0')
    # t.insert('2.0',"yellow\n")
    # k = len(t.get('2.0',"2.end"))
    # print(k)
    global j
    t.tag_add("x",str(j)+".0",str(j)+".0+1lines")
    t.tag_config("x",background="white",foreground="black")
    if j>=2:
            t.tag_add("y",str(j-1)+".0",str(j-1)+".0+1lines")
            t.tag_config("y",background="gray11",foreground="white")    
    j=j+1

 

#Creating new frame
textFrame = Frame(root, bd =2,bg = "floral white", width = 800, height = 600)
textFrame.grid(row = 0, column = 6, rowspan =16)


#TextBox
t = Text(textFrame, height=30, width=75)
t.config(highlightcolor="red",bg= "gray11",fg="white", font=("Console", 12),insertbackground='white')
t.place(x=4, y=50)


# Pipeline Screen
pipeFrame = Frame(root,bd = 3, relief = RIDGE,width = 50)
pipeFrame.grid(row=16,column=6,rowspan=5)

scroll_x = Scrollbar(pipeFrame,orient = HORIZONTAL)
scroll_y = Scrollbar(pipeFrame,orient = VERTICAL)
scroll_x.pack(side = BOTTOM, fill= X)
scroll_y.pack(side = RIGHT, fill= Y)
myList = Listbox(pipeFrame,width=70,height= 7,font = ('arial', 14,),bg = 'darkblue', fg = 'white', xscrollcommand=scroll_x.set,yscrollcommand= scroll_y.set)
myList.pack()

scroll_x.config(command=myList.xview)
scroll_y.config(command=myList.yview)




#Function for opening a file
global currFile
def openTxt():
    setpc0()
    clearBig()
    clearReg()
    print("pc=",pc)
    asmFile = filedialog.askopenfilename(title = "Open .asm File", filetypes=((".asm Files", "*.asm"),))
    global currFile
    currFile = asmFile
    asmFile = open(asmFile,'r')
    stuff = asmFile.read()
    #set linenumber = 0
    t.delete("1.0","end")
    t.insert(END,stuff)
    asmFile.close()

#Function for saving file
def saveTxt():
    asmFile = open(currFile,'w')
    asmFile.write(t.get(1.0,END))

#Function for clearing the text area
def clrText():
    #set linenumber = 0
    clearBig()
    t.delete("1.0","end")

#load Bubble Sort file
def loadBubbleSort():
    setpc0()
    clearBig()
    t.delete("1.0","end")
    t.insert(INSERT,
'''
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
            JAL ra, iloop
        iexit:
            ADDI x9, x9, 1
            JAL ra, oloop

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
    # A = {1,2,3,4,5}'''
    )




def print_area(listt):
    # pc = 0
    clearBig()
    global pc
    setpc0()
    print("pc=",pc)
    for z in range(len(listt)):
        ooo = listt[z]        
        if ooo == '' or (ooo.split())[0][0] == '#':
            continue
        big.append(ooo)
        if isLabel(ooo):
            ooo = list(ooo.split(':'))
            ooo = ooo[0].split()
            target[ooo[0]] = pc                 
            targetinv[pc] = ooo[0]              
        pc = pc+1

    print(big)
    print(target)
    # pc = 0
    setpc0()

    while pc<len(big): 
        # global stepwise                         
        # if(stepwise):
        #     algebra = input()
        #     if algebra == 'ultron':
        #         stepwise = False
        s = big[pc]
        pc = pc+1
        global jjj
        
        
        if s =='-1':
            break
        if s == '':
            continue
        # else:
        #     pc = pc + 1
        p = (s.replace(',', ' '))
        print (p)
        llist = p.split()
        if isValidLine(llist):
            global cflow
            cflow[jjj] = llist
            jjj = jjj + 1
        # print (llist)
        l = len(llist);
        t = []
        for i in range(1,l):
            # hashind = llist[i].find('#')
            # if (hashind!=-1):
            #     llist[i] = llist[i][:hashind+1]
            t.append(llist[i].replace('$',''))
        opp = listInd(instr, llist[0].upper())
        
        if opp ==100000:
            print("Its ok")            
        #     #      target[p2lp] = pc
        elif opp<6:
            for i in range(0,l-1):
                rgind = filter(t[i])
                if(i==0):
                    rd = rgind
                elif(i==1):
                    rs1 = rgind
                elif(i==2):
                    rs2 = rgind
            if(int(rd)>31 or int(rs1)> 31 or int(rd)>31):
                print("REGISTERS OUT OF INDEX")
                continue

            if(opp==0):
                reg[rd] = reg[rs1] + reg[rs2]
                print("reg[",rd,"] = ",reg[rd],sep="")
                
            elif(opp==1):
                reg[rd] = reg[rs1] - reg[rs2]
                print("reg[",rd,"] = ",reg[rd],sep="")
            elif opp ==2:
                reg[rd] = reg[rs1] * reg[rs2]
                print("reg[",rd,"] = ",reg[rd],sep="")            
            elif opp==3:
                reg[rd] = reg[rs1] + rs2
                print("reg[",rd,"] = ",reg[rd],sep="")
            elif opp==4:
                reg[rd] = reg[rs1] - rs2
                print("reg[",rd,"] = ",reg[rd],sep="")
            elif opp==5:
                reg[rd] = reg[rs1] * rs2
                print("reg[",rd,"] = ",reg[rd],sep="")
        elif opp == 6 or opp ==7 : 
            for i in range(0,l-1):            

                rgind = filter(t[i])
                if t[i].find('(') != -1:
                    ti = t[i].replace('(', " ").replace(')'," ")
                    ti = ti.split();
                    oadd = int(ti[0])
                    if(len(ti)>1):
                        oin = int(filter(ti[1]))
                        # print ("->>>>>",oin, oadd)
                    else:
                        print("Wrong Memory Fetch")
                        continue
                if(i==0):
                    rreg = rgind
                    print (i,"=i,rreg=",rreg)
                elif(i==1):
                    if(oin <32):
                        rmem = oadd + reg[oin] 
                    else:
                        print("REGISTERS OUT OF INDEX")
                        continue    
            if(rreg > 31 or rmem >= N__):
                print("REGISTERS OUT OF INDEX")
                continue
                
            if opp == 6:
                reg[rreg] = memory[rmem]
                print ('memory[',rmem,']=', memory[rmem])
                print ('reg[',rreg,']=', reg[rreg])
            elif opp == 7:
                memory[rmem] = reg[rreg]
                global mll
                mll.add(rmem)
                print ('reg[',rreg,']=', reg[rreg])
                print ('memory[',rmem,']=', memory[rmem])
        elif opp >= 8 and opp <= 11:
            for i in range(0,l-1):

                rgind = filter(t[i])
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
                    print("Jumped to",t[2])     
            elif opp == 9:
                if(reg[rc1] == reg[rc2]):
                    pc = target[t[2]]
                    print("Jumped to",t[2])        
            elif opp == 10:
                if(reg[rc1] >= reg[rc2]):
                    pc = target[t[2]]
                    print("Jumped to",t[2]) 
            elif opp == 11:
                if(reg[rc1] < reg[rc2]):
                    pc = target[t[2]]
                    print("Jumped to",t[2]) 
        elif opp == 12:
            print("t[0]:",t[1],"\nJumped to",t[1])
            pc = target[t[1]]
            reg[1] = pc
            
        printreg()        
        print('No of Steps-',jjj)
        printee(listt)
    print('Memory-')
    if len(mll) == 0:
        print('NULL')
    for rmem in mll:
        print ('memory[',rmem,']=', memory[rmem])

    stepcount = len(cflow)
    print('cfl:')
    for u in range(stepcount):
        print(u,'-',Dependency(cflow, u),'-',cflow[u])
    
    NonFor = [['   ' for Pranav in range(5*(stepcount))] for Saurabh in range(stepcount)]
    forw   = [['   ' for Saurabh in range(5*(stepcount))] for Pranav in range(stepcount)]
    clk = 1
    for u in range(stepcount):
        dep = Dependency(cflow,u)        
        
        if dep == 3 :
            NonFor [u][clk] = 'Stl'
            clk = clk +1 
            
            if u>0 and NonFor[u-1][clk] == 'Stl':
                NonFor [u][clk] = 'Stl'
                clk = clk +1 
            
        if u>0 and NonFor[u-1][clk] == 'Stl' and NonFor[u-1][clk+1] == 'Stl' and NonFor[u-1][clk+3] == 'Stl' and NonFor[u-1][clk+4] == 'Stl':
            print('DETECTED-----------------')
            NonFor[u][clk]   = 'Stl'
            clk = clk+1
            NonFor[u][clk]   = 'Stl'
            clk = clk+1
             
            # if dep == 3:
            #     NonFor [u][clk] = 'Stl'
            #     clk = clk +1                

            if u>0 and NonFor[u-1][clk] == 'IF ':
                clk  = clk + 1
            NonFor[u][clk] =   'IF '
            NonFor [u][clk+1] = 'Stl'  
            clk = clk + 1       
            NonFor [u][clk+1] = 'Stl'  
            clk = clk + 1     
            NonFor[u][clk+1] = 'ID '
            
            if dep == 2:                
                NonFor[u][clk+2] = 'Stl'
                clk = clk + 1
                NonFor[u][clk+2] = 'EXE'
                NonFor[u][clk+3] = 'MEM'
                NonFor[u][clk+4] = 'WB '
                clk = clk - 4
            elif dep == 1 or dep == 4:                
                NonFor[u][clk+2] = 'Stl'
                clk = clk + 1
                NonFor[u][clk+2] = 'Stl'
                clk = clk + 1

                NonFor[u][clk+2] = 'EXE'
                NonFor[u][clk+3] = 'MEM'
                NonFor[u][clk+4] = 'WB '
                clk = clk -5
            else:

                NonFor[u][clk+2] = 'EXE'
                NonFor[u][clk+3] = 'MEM'
                NonFor[u][clk+4] = 'WB '          
                clk = clk - 3
        elif u>0 and NonFor[u-1][clk] == 'Stl' and NonFor[u-1][clk+1] == 'Stl' and NonFor[u-1][clk+3] == 'Stl':

            NonFor[u][clk]   = 'Stl'
            clk = clk+1
            NonFor[u][clk]   = 'Stl'
            clk = clk+1
            # if dep == 3:
            #     NonFor [u][clk] = 'Stl'
            #     clk = clk +1
                

            if u>0 and NonFor[u-1][clk] == 'IF ':
                clk  = clk + 1
            NonFor[u][clk] =   'IF '
            NonFor [u][clk+1] = 'Stl'            
            NonFor[u][clk+2] = 'ID '
            clk = clk + 1 # terror
            if dep == 2:                
                NonFor[u][clk+2] = 'Stl'
                clk = clk + 1
                NonFor[u][clk+2] = 'EXE'
                NonFor[u][clk+3] = 'MEM'
                NonFor[u][clk+4] = 'WB '
                clk = clk -3
            elif dep == 1 or dep == 4:                
                NonFor[u][clk+2] = 'Stl'
                clk = clk + 1
                NonFor[u][clk+2] = 'Stl'
                clk = clk + 1
                NonFor[u][clk+2] = 'EXE'
                NonFor[u][clk+3] = 'MEM'
                NonFor[u][clk+4] = 'WB '
                clk = clk -4
            else:
                NonFor[u][clk+2] = 'EXE'
                NonFor[u][clk+3] = 'MEM'
                NonFor[u][clk+4] = 'WB '          
                clk = clk - 2
        elif u>0 and NonFor[u-1][clk] == 'Stl' and NonFor[u-1][clk+1] == 'Stl':
            NonFor[u][clk]   = 'Stl'
            clk = clk+1
            NonFor[u][clk]   = 'Stl'
            clk = clk+1
            # if dep == 3:
            #     NonFor [u][clk] = 'Stl'
            #     clk = clk +1

            if u>0 and NonFor[u-1][clk] == 'IF ':
                clk  = clk + 1
            NonFor[u][clk] =   'IF '

            NonFor[u][clk+1] = 'ID '
            if dep == 2:                
                NonFor[u][clk+2] = 'Stl'
                clk = clk + 1
                NonFor[u][clk+2] = 'EXE'
                NonFor[u][clk+3] = 'MEM'
                NonFor[u][clk+4] = 'WB '
                clk = clk -2
            elif dep == 1 or dep == 4:                
                NonFor[u][clk+2] = 'Stl'
                clk = clk + 1
                NonFor[u][clk+2] = 'Stl'
                clk = clk + 1
                NonFor[u][clk+2] = 'EXE'
                NonFor[u][clk+3] = 'MEM'
                NonFor[u][clk+4] = 'WB '
                clk = clk -3
            else:
                NonFor[u][clk+2] = 'EXE'
                NonFor[u][clk+3] = 'MEM'
                NonFor[u][clk+4] = 'WB '
          
                clk = clk - 1
        elif u>0 and NonFor[u-1][clk+1] == 'Stl' and NonFor[u-1][clk+2] == 'Stl':
            # if dep == 3:
            #     NonFor [u][clk] = 'Stl'
            #     clk = clk +1
            if u>0 and NonFor[u-1][clk] == 'IF ':
                clk  = clk + 1
            NonFor[u][clk] =   'IF '
            NonFor[u][clk+1]   = 'Stl'
            clk = clk+1
            NonFor[u][clk+1]   = 'Stl'
            clk = clk+1            
            NonFor[u][clk+1] = 'ID '
            if dep == 2:
                
                NonFor[u][clk+2] = 'Stl'
                clk = clk + 1
                NonFor[u][clk+2] = 'EXE'
                NonFor[u][clk+3] = 'MEM'
                NonFor[u][clk+4] = 'WB '
                clk = clk -2
            elif dep == 1 or dep == 4: 
                print('special')               
                NonFor[u][clk+2] = 'Stl'
                clk = clk + 1
                NonFor[u][clk+2] = 'Stl'
                clk = clk + 1
                NonFor[u][clk+2] = 'EXE'
                NonFor[u][clk+3] = 'MEM'
                NonFor[u][clk+4] = 'WB '
                clk = clk -3
            else:
                NonFor[u][clk+2] = 'EXE'
                NonFor[u][clk+3] = 'MEM'
                NonFor[u][clk+4] = 'WB '
          
                clk = clk - 1
        elif u>0 and NonFor[u-1][clk] == 'Stl':
            NonFor[u][clk]   = 'Stl'
            clk = clk+1
            # if dep == 3:
            #     NonFor [u][clk] = 'Stl'
            #     clk = clk +1
            if u>0 and NonFor[u-1][clk] == 'IF ':
                clk  = clk + 1
            NonFor[u][clk] =   'IF '
            NonFor[u][clk+1] = 'ID '
            if dep == 2:
                
                NonFor[u][clk+2] = 'Stl'
                clk = clk + 1
                NonFor[u][clk+2] = 'EXE'
                NonFor[u][clk+3] = 'MEM'
                NonFor[u][clk+4] = 'WB '
                clk = clk -1
            elif dep == 1 or dep == 4:    
                        
                NonFor[u][clk+2] = 'Stl'
                clk = clk + 1
                NonFor[u][clk+2] = 'Stl'
                clk = clk + 1
                NonFor[u][clk+2] = 'EXE'
                NonFor[u][clk+3] = 'MEM'
                NonFor[u][clk+4] = 'WB '
                clk = clk -2
            else:
                NonFor[u][clk+2] = 'EXE'
                NonFor[u][clk+3] = 'MEM'
                NonFor[u][clk+4] = 'WB '          


        elif u>0 and NonFor[u-1][clk+1] == 'Stl':
            
            # NonFor[u][clk] = 'IF '
            # NonFor[u][clk+1]   = 'Stl'
            # clk = clk+1
            # NonFor[u][clk+1] = 'ID '
            # NonFor[u][clk+2] = 'EXE'
            # NonFor[u][clk+3] = 'MEM'
            # NonFor[u][clk+4] = 'WB '
            # # NonFor[u][clk+5] = 'WB '

            # if dep == 3:
            #     NonFor [u][clk] = 'Stl'
            #     clk = clk +1
            NonFor[u][clk] =  'IF '
            NonFor[u][clk+1]   = 'Stl'
            clk = clk+1
            NonFor[u][clk+1] = 'ID '
            if dep == 2:
                
                NonFor[u][clk+2] = 'Stl'
                clk = clk + 1
                NonFor[u][clk+2] = 'EXE'
                NonFor[u][clk+3] = 'MEM'
                NonFor[u][clk+4] = 'WB '
                clk = clk -1
            elif dep == 1 or dep == 4:                
                NonFor[u][clk+2] = 'Stl'
                clk = clk + 1
                NonFor[u][clk+2] = 'Stl'
                clk = clk + 1
                NonFor[u][clk+2] = 'EXE'
                NonFor[u][clk+3] = 'MEM'
                NonFor[u][clk+4] = 'WB '
                clk = clk -2
            else:
                NonFor[u][clk+2] = 'EXE'
                NonFor[u][clk+3] = 'MEM'
                NonFor[u][clk+4] = 'WB '          

        else:
            if u>0 and NonFor[u-1][clk] == 'IF ':
                clk = clk + 1
            # NonFor[u][clk]   = 'IF '
            # NonFor[u][clk+1] = 'ID '
            # NonFor[u][clk+2] = 'EXE'
            # NonFor[u][clk+3] = 'MEM'
            # NonFor[u][clk+4] = 'WB '
            # clk = clk+1

            # if dep == 3:
            #     NonFor [u][clk] = 'Stl'
            #     clk = clk +1
            if u>0 and NonFor[u-1][clk] == 'IF ':
                clk  = clk + 1
            NonFor[u][clk] =   'IF '
            NonFor[u][clk+1] = 'ID '
            if dep == 2:
                NonFor[u][clk+2] = 'Stl'
                clk = clk + 1
                NonFor[u][clk+2] = 'EXE'
                NonFor[u][clk+3] = 'MEM'
                NonFor[u][clk+4] = 'WB '
                
            elif dep == 1 or dep == 4:                
                NonFor[u][clk+2] = 'Stl'
                clk = clk + 1
                NonFor[u][clk+2] = 'Stl'
                clk = clk + 1
                NonFor[u][clk+2] = 'EXE'
                NonFor[u][clk+3] = 'MEM'
                NonFor[u][clk+4] = 'WB '
                clk = clk -1
            else:
                NonFor[u][clk+2] = 'EXE'
                NonFor[u][clk+3] = 'MEM'
                NonFor[u][clk+4] = 'WB ' 
                clk = clk + 1         

        # NonFor[u][clk-1] = 'IF '
        # NonFor[u][clk]   = 'ID '
        # if dep >0 :
        #     NonFor[u][clk+1] = 'Stl'
        #     clk = clk+1
        #     if dep ==1 :
        #         NonFor[u][clk+1] = 'Stl'
        #         clk = clk+1
        
        #     if u > 0:
        #         past = listInd(NonFor[u-1],'WB ')
        #         pastclk = clk
        #         if clk <past and past != 100000:
        #             clk = past
        #             for r in range(pastclk+1,clk+1):
        #                 NonFor[u][r] = 'Stl'

        # NonFor[u][clk+1] = 'EXE'
        # NonFor[u][clk+2] = 'MEM'
        # NonFor[u][clk+3] = 'WB '
        # clk = clk+1
        
    # def stall(cflow,forw,u,clk):
    print("CLOCK CYCLES without Forwarding: ", listInd(NonFor[-1], 'WB '))   
    clockpulsesNonFor =  listInd(NonFor[-1], 'WB ')
    StallsNonFor = clockpulsesNonFor - stepcount - 4
    


    
    clk = 1
    for u in range(stepcount):
        dep = Dependency(cflow,u)
        if(dep<3):
            
            if u>0 and forw[u-1][clk] == 'Stl':
                forw[u][clk]   = 'Stl'
                clk = clk+1
                forw[u][clk] =   'IF '
                forw[u][clk+1] = 'ID '
                forw[u][clk+2] = 'EXE'
                forw[u][clk+3] = 'MEM'
                forw[u][clk+4] = 'WB '
                # forw[u][clk+5] = 'WB '
            elif u>0 and forw[u-1][clk+1] == 'Stl':
                
                forw[u][clk] = 'IF '
                forw[u][clk+1]   = 'Stl'
                clk = clk+1
                forw[u][clk+1] = 'ID '
                forw[u][clk+2] = 'EXE'
                forw[u][clk+3] = 'MEM'
                forw[u][clk+4] = 'WB '
                # forw[u][clk+5] = 'WB '
            else:
                if u>0 and forw[u-1][clk] == 'IF ':
                    clk = clk + 1
                forw[u][clk]   = 'IF '
                forw[u][clk+1] = 'ID '
                forw[u][clk+2] = 'EXE'
                forw[u][clk+3] = 'MEM'
                forw[u][clk+4] = 'WB '
                clk = clk+1

        elif dep == 3:
            forw[u][clk]   = 'Stl'
            clk = clk + 1
            forw[u][clk]   = 'IF '
            forw[u][clk+1] = 'ID '
            forw[u][clk+2] = 'EXE'
            forw[u][clk+3] = 'MEM'
            forw[u][clk+4] = 'WB '
            clk = clk+1

        elif dep == 4:            
            
            forw[u][clk]   = 'IF '
            forw[u][clk+1] = 'ID '
            forw[u][clk+2] = 'Stl'
            clk = clk+1
            forw[u][clk+2] = 'EXE'
            forw[u][clk+3] = 'MEM'
            forw[u][clk+4] = 'WB '
    print("CLOCK CYCLES with Forwarding: ", listInd(forw[-1], 'WB ') )   
    clockpulsesFor =  listInd(forw[-1], 'WB ')
    StallsFor = clockpulsesFor - stepcount - 4
     
    for pranav,saurabh in enumerate(NonFor):
        pranav = str(pranav+1)
        while len(pranav)<3:
            pranav = pranav + ' '
        saurabh[0]= pranav
    for pranav,saurabh in enumerate(forw):
        pranav = str(pranav+1)
        while len(pranav)<3:
            pranav = pranav + ' '
        saurabh[0]= pranav
    print('NON-FORWARDING-')
    ppview.append('NON-FORWARDING-\n')
    for y in NonFor:
        u = 0
        uip = ''
        while(u<5*stepcount and y[u]!='WB '):
            print(y[u], end ='|')
            uip += y[u].replace(' ','_')+ '|'
            u = u+1
        print('WB ')
        uip+= 'WB '
        ppview.append(uip)
    # #
    # for y in NonFor:
    #     print(y)
    # #

    print('\n________________________\n\nFORWARDING-')
    ppview.append('________________________')
    ppview.append('________________________')
    ppview.append('FORWARDING-')
    for y in forw:
        u = 0
        uip = ''
        while(u<5*stepcount and y[u]!='WB '):
            print(y[u], end = '|')
            uip += y[u].replace(' ','_')+'|'
            u = u+1
        print('WB ')
        uip += 'WB '
        ppview.append(uip)
    print("CLOCK CYCLES without Forwarding: ", listInd(NonFor[-1], 'WB '))   
    print("CLOCK CYCLES with Forwarding:    ", listInd(forw[-1], 'WB ') )
    
    print('\nNumber of Stalls without Forwarding: ', StallsNonFor)
    print('Number of Stalls in Forwarding:      ',StallsFor )
    for r in ppview:
        myList.insert(END,r)




#Run Button
runButton = Button(textFrame,bg="#B5DD50", text="Run",padx=20,pady=4,command = lambda:print_area(t.get('1.0',END).splitlines()))
runButton.place(x=264, y=0)

#Open Button
openButton = Button(textFrame,bg="#B5DD50", text="Open File",padx=20,pady=4, command = openTxt)
openButton.place(x=4, y=0)

#saveFile Button
saveButton = Button (textFrame,bg="#B5DD50",text="Save File",padx=20,pady=4, command = saveTxt)
saveButton.place(x=104, y=0)

#clr button for textbox
clrButton = Button (textFrame,bg="#B5DD50",text="Clr",padx=20,pady=4, command = clrText)
clrButton.place(x=199, y=0)

#Bubble Sort File Button
runButton = Button(textFrame,bg="#B5DD50", text="Bubble Sort",padx=20,pady=4,command = loadBubbleSort)
runButton.place(x=335, y=0)

# create a toplevel menu  
# menubar = Menu(textFrame)  
# menubar.add_command(label="Hello!")  
# menubar.add_command(label="Quit!")  
  
# # # # display the menu  
# # # menubar.grid(row=0, column = 6)
# textFrame.config(menu=menubar ) 

root.mainloop()







