# def isComment(s):
#     return  s.split('#')
#     return len(s) ==1

# while 1:
#     s = input("Enter: ")
#     print(isComment(s))

# It will take All instructions Line wise till we  get -1, and Store it a list
# After that we will Implement each Code Line wise.
from tkinter import *
import tkinter.filedialog, tkinter.messagebox
import os
import tempfile
from tkinter import filedialog
# from numpy import roots

reg_name=[]
reg_value=[]



iii = 0
def printee(txt):
    global iii
    iii = 0
    if(iii!=len(txt)):
        print(txt[iii])
        print("_________")
        iii+=1




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
        else:
            print("Something's fishy")
        print('x',rgind)
        return rgind
    elif(s[0] == 'x'):
        rgind = t_type(s)
        
        if rgind.isdigit():
            rgind = int(rgind)
        else:
            print("Something's fishy")
        print('x',rgind)
        return rgind
    elif(s[0] == 'a'):
        rgind = t_type(s)
        
        if rgind.isdigit():
            rgind = 10 + int(rgind)
        else:
            print("Something's fishy")
        print('x',rgind)
        return rgind
    elif(s[0] == 's'):
        rgind = t_type(s)            
        if rgind.isdigit():
            rgind = int(rgind)
            if rgind<2:
                rgind = rgind + 8
            else:
                rgind = rgind + 16
        else:
            print("Something's fishy")
        print('x',rgind)
        return rgind        
    elif s.isdecimal():
        rgind = s   
        rgind = int(rgind)
        print('const',rgind)
        return rgind
def isLabel(s):
    return s.find(':')!=-1
N__ = 1024
memory = [0]*N__
reg = [0]*32

def printreg():
    print(list(range(32)))
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
        # elif reg[i]>1000:
        #     reg_value[i].config(padx = 33)

        


        if i<1:
            strj = ""
        elif i<10:
            strj= ","
        else:
            strj = ", "
        print(strj,reg[i], end = "")
    print("\n","pc =",pc)   # PC


def listInd( ll, ele):
    if ll.count(ele):
        return ll.index(ele)
    else:
        return 1000

instr = ['ADD','SUB','MUL','ADDI','SUBI','MULI','LW','SW','BNE','BEQ','BGE','BLT','JAL']

target = dict()
targetinv = dict()
big = []
pc = 0
def print_area(listt):
    pc = 0
    for z in range(len(listt)):
        ooo = listt[z]        
        if ooo == '' or (ooo.split())[0][0] == '#':
            continue
        big.append(ooo)
        if isLabel(ooo):
            ooo = list(ooo.split(':'))
            target[ooo[0]] = pc                 # PC
            targetinv[pc] = ooo[0]              # PC
        pc = pc+1

    print(big)
    print(target)
    pc = 0


    while pc<len(big):                          # PC
        
        s = big[pc]     # PC
        pc = pc+1       # PC
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
        if opp ==1000:
            print("Its ok")
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
                elif(t[i][0] == 'x'):
                    rgind = t_type(t[i])
                    
                    if rgind.isdigit():
                        rgind = int(rgind)
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
            if(int(rd)>31 or int(rs1)> 31 or int(rd)>31):
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
        elif opp == 6 or opp ==7 : 
            for i in range(0,l-1):            
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
                elif(t[i][0] == 'x'):
                    rgind = t_type(t[i])
                    
                    if rgind.isdigit():
                        rgind = int(rgind)
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
                elif t[i].find('(') != -1:
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
                print ('reg[',rreg,']=', reg[rreg])
                print ('memory[',rmem,']=', memory[rmem])
        elif opp >= 8 and opp <= 11:
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
                elif(t[i][0] == 'x'):
                    rgind = t_type(t[i])
                    
                    if rgind.isdigit():
                        rgind = int(rgind)
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
                    pc = target[t[2]]       # PC
            elif opp == 9:
                if(reg[rc1] == reg[rc2]):
                    pc = target[t[2]]       # PC
            elif opp == 10:
                if(reg[rc1] >= reg[rc2]):
                    pc = target[t[2]]
            elif opp == 11:
                if(reg[rc1] < reg[rc2]):
                    pc = target[t[2]]
        elif opp == 12:
            print("t[0]:",t[0])
            pc = target[t[0]]               # PC
            
        printreg()
        printee(listt)


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
    global pc
    pc = 0
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


#Function for opening a file
global currFile
def openTxt():
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
    t.delete("1.0","end")

#load Bubble Sort file
def loadBubbleSort():
    t.delete("1.0","end")
    t.insert(INSERT,"##-------------------------------Bubble Sort -----------------------------------------#\n"+
    "#In the given bubble sort program we are sorting 5 integers\n" +
    "#which are loaded in registers x26 to x30.\n"+
    "#The sorted integers are stored in the\n"+
    "#registers x26 to x30 after running the file.\n\n"+

    ".text\n"+
    "# x1 = 100\n"+
    "ADDI x1, x0, 100\n"+
    "ADDI x4, x0, 4\n"+
    "SW   x4, 0(x1)      # A[0] = 4\n"+
    "ADDI x4, x0, 5\n"+
    "SW   x4, 1(x1)      # A[1] = 5\n"+
    "ADDI x4, x0, 1\n"+
    "SW   x4, 2(x1)      # A[2] = 1\n"+
    "ADDI x4, x0, 2\n"+
    "SW   x4, 3(x1)      # A[3] = 2\n"+
    "ADDI x4, x0, 3\n"+
    "SW   x4, 4(x1)      # A[4] = 3\n"+
    "# A = {5,4,3,2,1}\n"+
    "printArray:\n"+
    "ADDI x1, x0, 100\n"+
    "LW   x26, 0(x1)      # x16 = A[0]\n" +
    "LW   x27, 1(x1)      # x17 = A[1]\n" +
    "LW   x28, 2(x1)      # x18 = A[2]\n" +
    "LW   x29, 3(x1)      # x19 = A[3]\n" +
    "LW   x30, 4(x1)      # x20 = A[4]\n\n" +

    "ADDI x5, x0, 5      # size = 5\n\n"+

    "# i-> x9, j-> x10, n->x5\n"+
    "bubbleSort:\n"+
    "ADDI x9, x0, 0\n\n"+

    "oloop:\n"+
    "BGE x9, x5, oexit\n"+
    "ADDI x10, x5, 0\n"+
    "SUBI x10, x10, 1\n"+
    "iloop:\n"+
    "BGE x9, x10, iexit\n"+
    "# x13 -> *A, x14->*A[j], *x15->A[i]\n"+
    "#            x16-> A[j],  x17->A[i]\n"+
    "swap:\n"+
    "ADDI x13, x1, 0\n"+
    "ADD x14, x13, x9\n"+
    "ADD x15, x13, x10\n"+
    "LW  x16, 0(x14)\n"+
    "LW  x17, 0(x15)\n"+
    "BGE x17, x16, skip\n\n"+

    "# x18-> temp\n"+
    "ADDI x18, x17, 0\n"+
    "ADDI x17, x16, 0\n"+
    "ADDI x16, x18, 0\n"+
    "SW x16, 0(x14)\n"+
    "SW x17, 0(x15)\n"+
    "skip:\n"+
    "SUBI x10, x10, 1\n"+
    "JAL iloop\n"+
    "iexit:\n"+
    "ADDI x9, x9, 1\n"+
    "JAL oloop\n"+
    "oexit:\n\n"+


    "printSortedArray:\n"+

    "ADDI x1, x0, 100\n"+
    "LW   x16, 0(x1)      # x16 = A[0] \n"+
    "LW   x17, 1(x1)      # x17 = A[1]\n" +
    "LW   x18, 2(x1)      # x18 = A[2] \n"+
    "LW   x19, 3(x1)      # x19 = A[3] \n"+
    "LW   x20, 4(x1)      # x20 = A[4] \n"+
    "# A = {1,2,3,4,5}\n"
    )




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







