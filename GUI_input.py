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

iii = 0
def printee(txt):
    global iii
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
    for  i in range(32):
        if i<1:
            str = ""
        elif i<10:
            str= ","
        else:
            str = ", "
        print(str,reg[i], end = "")
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
root.title("Printing Demo")
root.geometry("900x600")

lbl_print = Label(root, text = "Printing Area: ",font=("Consolas",20),fg="blue").place(x=100, y =20)
Font_tuple = ("Consolas", 11)
text_area = Text(root, bg="gray9", fg= "white",insertbackground = "white", font = Font_tuple )
text_area.place(x=100,y=100,width=680,height=380)
btn_print = Button(root, text="Print",bg = "Cyan4", fg="white",
 activebackground="LightCyan3",command=lambda:print_area(text_area.get('1.0',END).splitlines())) #activebackground="LightCyan3",command=lambda:print_area(text_area.get('1.0',END).splitlines()))
btn_print.place(x=380,y=500)

#text_area.tag_configure("red", foreground="red")
# apply the tag "red" 
#text_area.highlight_pattern("word", "red")
# img = PhotoImage(file="C:/Users/saura/OneDrive/Desktop/FileDialogue/pik2.png")
# download = Button(root, text="Download", image = img)
# download.place(x=380,y=500)
# download.pack()





# class TextWidget(Text):
#     def _init_(self, *args, **kwargs):
#         Text._init_(self, *args, **kwargs)  # pass all args to superclass
#         self.filename = ''
#         self._filetypes = [
#             ('Text', '*.txt'),
#             ('All files', '*'),
#         ]

#     def save_file(self, whatever = None):
#         if (self.filename == ''):
#             self.save_file_as()
#         else:
#             f = open(self.filename, 'w')
#             f.write(self.get('1.0', 'end')) # change every 'self' that refers to the Text, to self.text
#             f.close()
#             tkinter.messagebox.showinfo('FYI', 'File Saved.')

#     def save_file_as(self, whatever = None):
#         self.filename = tkinter.filedialog.asksaveasfilename(defaultextension='.txt',
#                                                              filetypes = self._filetypes)
#         f = open(self.filename, 'w')
#         f.write(Text.get('1.0', END))
#         f.close()
#         tkinter.messagebox.showinfo('FYI', 'File Saved')   
def save_file_as():
    filename = tkinter.filedialog.asksaveasfilename(defaultextension='.txt')
    f = open(filename, 'w')
    f.write(text_area.get('1.0', END))
    f.close()
    tkinter.messagebox.showinfo('FYI', 'File Saved')

save = Button(root, text="Save",bg = "Cyan4", fg="white",
 activebackground="LightCyan3",command=save_file_as)
save.place(x=440,y=500)
root.mainloop()