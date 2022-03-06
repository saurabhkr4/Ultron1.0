from tkinter import *
import tkinter.filedialog, tkinter.messagebox
import os
import tempfile

i = 0
def print_area(txt):
    global i
    if(i!=len(txt)):
        print(txt[i])
        i+=1

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
#     def __init__(self, *args, **kwargs):
#         Text.__init__(self, *args, **kwargs)  # pass all args to superclass
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