from tkinter import *
from tkinter import ttk
from tkinter import font
from tkinter import colorchooser,filedialog,messagebox

showStatusbar=True
showToolbar=True
fontFamily="Arial"
url=""
fontSize=12
textChanged=False

class FindDialog(Toplevel):
    def __init__(self,parent,*args,**kwargs):
        Toplevel.__init__(self, parent, *args, **kwargs)
        self.parent = parent
        self.geometry("450x200+550+200")
        self.title("Find")
        self.resizable(False,False)
        txtFind=Label(self,text="Find: ")
        txtFind.place(x=20,y=20)
        txtReplace=Label(self,text="Replace :")
        txtReplace.place(x=20,y=60)
        self.findInput=Entry(self,width=30)
        self.replaceInput=Entry(self,width=30)
        self.findInput.place(x=100,y=20)
        self.replaceInput.place(x=100,y=60)
        self.btnFind=Button(self,text="Find",command=self.parent.findWords)
        self.btnReplace=Button(self,text="Replace",command=self.parent.replaceWords)
        self.btnFind.place(x=200,y=90)
        self.btnReplace.place(x=240,y=90)

class MainMenu(Menu):
    def __init__(self,parent,*args,**kwargs):
        Menu.__init__(self,parent,*args,**kwargs)
        self.parent=parent

        ###############File Menu#################
        self.new_icon=PhotoImage(file='icons/new.png')
        self.open_icon=PhotoImage(file='icons/open.png')
        self.save_icon=PhotoImage(file='icons/save_icon.png')
        self.exit_icon=PhotoImage(file='icons/exit.png')

        self.file=Menu(self,tearoff=0)
        self.file.add_command(label='New',image=self.new_icon,compound=LEFT,accelerator="Ctrl+N",command=self.parent.newFile)
        self.file.add_command(label='Open',accelerator="Ctrl+O",image=self.open_icon,compound=LEFT,
                              command=self.parent.openFile)
        self.file.add_command(label='Save',accelerator="Ctrl+S",image=self.save_icon,compound=LEFT,
                              command=self.parent.saveFile)
        self.file.add_command(label='Save as',accelerator="Ctrl+Alt+S",command=self.parent.saveAsFile)
        self.file.add_command(label='Exit',image=self.exit_icon,compound=LEFT,
                              command=self.parent.exitFunc)

        ########################Edit Menu#############################
        self.edit=Menu(self,tearoff=0)
        self.edit.add_command(label='Copy',accelerator="Ctrl+C",command=lambda :self.parent.texteditor.event_generate("<Control c>"))
        self.edit.add_command(label='Paste',accelerator="Ctrl+V",command=lambda :self.parent.texteditor.event_generate("<Control v>"))
        self.edit.add_command(label='Cut',accelerator="Ctrl+X",command=lambda :self.parent.texteditor.event_generate("<Control x>"))
        self.edit.add_command(label='Clear All',accelerator="Ctrl+Alt+C",command=lambda :self.parent.texteditor.delete(1.0,END))
        self.edit.add_command(label='Find',accelerator="Ctrl+F",command=self.parent.find)

        ###########################View Menu############################
        global showStatusbar
        global showToolbar
        self.view=Menu(self,tearoff=0)
        self.view.add_checkbutton(onvalue=True, offvalue=False,label="Tool Bar",variable=showToolbar,
                                  command=self.parent.hideToolbar)
        self.view.add_checkbutton(onvalue=1, offvalue=0,label="Status Bar",variable=showStatusbar,
                                  command=self.parent.hideStatusbar)

        ##########################Themes Menu############################
        self.themes=Menu(self,tearoff=0)
        self.color_list = {
            'Default': '#000000.#FFFFFF',# first one is font color second one is background color
            'Tomato' :'#ffff00.#ff6347',
            'LimeGreen' :'#fffff0.#32cd32',
            'Magenta' : '#fffafa.#ff00ff',
            'RoyalBlue':'#ffffbb.#4169e1',
            'MediumBlue':'#d1e7e0.#0000cd',
            'Dracula' :'#ffffff.#000000',
        }
        self.theme_choice=StringVar()
        for i in sorted(self.color_list):
            self.themes.add_radiobutton(label=i, variable=self.theme_choice,command=self.changeTheme)

        self.add_cascade(label='File',menu=self.file)
        self.add_cascade(label='Edit', menu=self.edit)
        self.add_cascade(label='View',menu=self.view)
        self.add_cascade(label='Templates',menu=self.themes)
        self.about=Menu(self,tearoff=0)
        self.add_cascade(label="About",command=self.parent.aboutMessage)

    def changeTheme(self):
        selected_theme=self.theme_choice.get()
        fg_bg_color=self.color_list.get(selected_theme)
        print(fg_bg_color)
        foreground_color,background_color=fg_bg_color.split('.')
        self.parent.texteditor.config(background=background_color,fg=foreground_color)

class TextEditor(Text):
    def __init__(self,parent,*args,**kwargs):
        Text.__init__(self,parent,*args,**kwargs)
        self.parent=parent
        self.config(wrap='word')
        self.pack(expand=YES, fill=BOTH)
        self.config(relief=FLAT)
        # xscrollbar=Scrollbar(self,orient=HORIZONTAL)
        # xscrollbar.pack(side=BOTTOM,fill=X)
        # yscrollbar=Scrollbar(self,orient=VERTICAL)
        # yscrollbar.pack(side=RIGHT,fill=Y)
        # xscrollbar.config(command=self.xview)
        # yscrollbar.config(command=self.yview)
        scroll_bar=Scrollbar(self,bd=5,relief=SUNKEN)
        self.configure(yscrollcommand=scroll_bar.set)
        scroll_bar.config(command=self.yview)
        scroll_bar.pack(side=RIGHT,fill=Y)



class StatusBar(Label):
    def __init__(self,parent,*args,**kwargs):
        Label.__init__(self,parent,*args,**kwargs)
        self.parent=parent
        self.pack(side=BOTTOM)
        self.config(text='Status Bar')


class ToolBar(Label):
    def __init__(self,parent,*args,**kwargs):
        Label.__init__(self,parent,*args,**kwargs)
        self.parent=parent
        self.pack(side=TOP,fill=X)

        ################################################################
        self.cbFont=ttk.Combobox(self)
        self.cbFontSize=ttk.Combobox(self)
        self.cbFont.pack(side=LEFT, padx=(5,10))
        self.cbFontSize.pack(side=LEFT)
        ################################################################
        self.boldIcon=PhotoImage(file='icons/bold.png')
        btnBold=Button(self,image=self.boldIcon,command=self.parent.changeBold)
        btnBold.pack(side=LEFT,padx=5)
        ################################################################
        self.italicIcon = PhotoImage(file='icons/italic.png')
        btnItalic = Button(self, image=self.italicIcon,command=self.parent.changeItalic)
        btnItalic.pack(side=LEFT, padx=5)
        ################################################################
        self.underlineIcon = PhotoImage(file='icons/under_line.png')
        btnUnderline = Button(self, image=self.underlineIcon,command=self.parent.changeUnderline)
        btnUnderline.pack(side=LEFT, padx=5)
        ################################################################
        self.fontcolorIcon = PhotoImage(file='icons/color.png')
        btnfontColor = Button(self, image=self.fontcolorIcon,command=self.parent.changeFontColor)
        btnfontColor.pack(side=LEFT, padx=5)
        ################################################################
        self.alignLeftIcon = PhotoImage(file='icons/alignleft.png')
        btnalignLeft = Button(self, image=self.alignLeftIcon,command=self.parent.alignLeft)
        btnalignLeft.pack(side=LEFT, padx=5)
        ################################################################
        self.alignCenterIcon = PhotoImage(file='icons/aligncenter.png')
        btnalignCenter = Button(self, image=self.alignCenterIcon,command=self.parent.alignCenter)
        btnalignCenter.pack(side=LEFT, padx=5)
        ################################################################
        self.alignRightIcon = PhotoImage(file='icons/alignright.png')
        btnalignRight = Button(self, image=self.alignRightIcon,command=self.parent.alignRight)
        btnalignRight.pack(side=LEFT, padx=5)

        ##########################################################################

        fonts=font.families()
        fontList=[]
        fontSizeList=[]

        for i in range(8,80):
            fontSizeList.append(i)
        for i in fonts:
            fontList.append(i)

        self.fontVar=StringVar()
        self.cbFont.config(values=fontList,textvariable=self.fontVar)
        self.cbFont.current(0)
        self.cbFontSize.config(values=fontSizeList)
        self.cbFontSize.current(4)

        self.cbFont.bind("<<ComboboxSelected>>", self.parent.getFont)
        self.cbFontSize.bind("<<ComboboxSelected>>", self.parent.getFontSize)


class MainApplication(Frame):
    def __init__(self,parent,*args,**kwargs):
        Frame.__init__(self,parent,*args,**kwargs)
        self.parent=parent
        self.pack(fill=BOTH,expand=True)

        #Creating widget
        self.main_menu=MainMenu(self)
        self.toolbar = ToolBar(self)
        self.texteditor=TextEditor(self)
        self.statusbar=StatusBar(self)



        #Parent menu configuration
        self.parent.config(menu=self.main_menu)

        #setting focus
        self.texteditor.focus()
        self.texteditor.configure(font='arial 12')
        self.texteditor.bind('<<Modified>>',self.changed)

    def aboutMessage(self,*args):
        messagebox.showinfo("About","This is our about page\nhave a question\ncontact us volkan@gmail.com")
    def exitFunc(self,*args):
        global url,textChanged

        try:
            if textChanged ==True:
                mbox=messagebox.askyesnocancel("Warning","Do you want to save the file")

                if mbox is True:
                    if url !="":
                        content=self.texteditor.get(1.0,END)
                        with open(url,'w',encoding='utf-8') as file:
                            file.write(content)
                            self.parent.destroy()
                    else:
                        content2=str(self.texteditor.get(1.0,END))
                        url=filedialog.asksaveasfile(mode='w',defaultextension=".txt",
                                             filetypes=(("Text file","*.txt"),("All files","*.*")))
                        url.write(content2)
                        url.close()
                if mbox is False:
                    self.parent.destroy()
            else:
                self.parent.destroy()

        except:
            return

    def saveAsFile(self,*args):
        try:
            content =str(self.texteditor.get(1.0,END))
            url=filedialog.asksaveasfile(mode='w',defaultextension=".txt",
                                             filetypes=(("Text file","*.txt"),("All files","*.*")))
            url.write(content)
            url.close()
            self.parent.title("NotePad - Now Editing "+str(url.split('/')[-1]))
        except:
            return
    def saveFile(self,*args):
        global url
        try:
            if url !="":
                content=str(self.texteditor.get(1.0,END))
                with open(url,'w',encoding='utf-8') as file:
                    file.write(content)
            else:
                url=filedialog.asksaveasfile(mode='w', defaultextension=".txt",
                                             filetypes=(("Text file","*.txt"),("All files","*.*")))
                content2=str(self.texteditor.get(1.0,END))
                url.write(content2)
                url.close()
        except:
            return

    def openFile(self,*args):
        global url
        url=filedialog.askopenfilename(initialdir="/",title="Select a file to open",
                                       filetypes=(("Text file","*.txt"),("All Files","*.*")))

        try:
            with open(url,'r') as file:
                self.texteditor.delete("1.0",END)
                self.texteditor.insert('1.0',file.read())

        except:
            return

        self.parent.title("NotePad - Now Editing "+str(url.split('/')[-1]))
        print(url.split('/'))


    def newFile(self,*args):
        global url
        try:
            url=""
            self.texteditor.delete(1.0,END)
        except:
            pass

    def changed(self,*args):
        global textChanged
        flag=self.texteditor.edit_modified()
        textChanged =True
        print(flag)
        if flag:
            words=len(self.texteditor.get(1.0, 'end-1c').split())
            letters=len(self.texteditor.get(1.0, 'end-1c'))
            self.statusbar.config(text="Characters " +str(letters)+ "   Words: " +str(words))

        self.texteditor.edit_modified(False)



    def getFont(self,*args):
        global fontFamily
        fontFamily=self.toolbar.cbFont.get()
        print(fontFamily)
        self.texteditor.configure(font=(fontFamily,fontSize))


    def getFontSize(self,*args):
        global fontSize
        fontSize=self.toolbar.cbFontSize.get()
        self.texteditor.configure(font=(fontFamily,fontSize))

    def changeBold(self,*arg):
        text_pro=font.Font(font=self.texteditor['font'])
        print(text_pro.actual('weight'))
        if text_pro.actual('weight')=='normal':
            self.texteditor.configure(font=(fontFamily,fontSize,'bold'))
        elif text_pro.actual('weight')=='bold':
            self.texteditor.configure(font=(fontFamily, fontSize, 'normal'))


    def changeItalic(self,*args):

        text_pro=font.Font(font=self.texteditor['font'])
        print(text_pro.actual())

        if text_pro.actual('slant')=='roman':
            self.texteditor.configure(font=(fontFamily,fontSize, 'italic'))

        elif text_pro.actual('slant')=='italic':
            self.texteditor.configure(font=(fontFamily,fontSize, 'roman'))

    def changeUnderline(self,*args):
        text_pro = font.Font(font=self.texteditor['font'])
        print(text_pro.actual())

        if text_pro.actual('underline')==0:
            self.texteditor.configure(font=(fontFamily,fontSize, 'underline'))
        elif text_pro.actual('underline')==1:
            self.texteditor.configure(font=(fontFamily,fontSize, 'normal'))

    def changeFontColor(self,*args):
        color = colorchooser.askcolor()
        print(color)
        self.texteditor.configure(fg=color[1])

    def alignLeft(self):
        content = self.texteditor.get(1.0, 'end')
        self.texteditor.tag_config('left',justify=LEFT)
        self.texteditor.delete(1.0, END)
        self.texteditor.insert(INSERT, content, 'left')


    def alignCenter(self):
        content = self.texteditor.get(1.0, 'end')
        self.texteditor.tag_config('center', justify=CENTER)
        self.texteditor.delete(1.0,END)
        self.texteditor.insert(INSERT,content,'center')

    def alignRight(self,*args):
        content = self.texteditor.get(1.0, 'end')
        self.texteditor.tag_config('right', justify=RIGHT)
        self.texteditor.delete(1.0, END)
        self.texteditor.insert(INSERT, content, 'right')

    def find(self,*args):
        self.find=FindDialog(self)

    def findWords(self,*args):
        word=self.find.findInput.get()
        print(word)
        self.texteditor.tag_remove('match','1.0',END)
        matches=0
        if word:
            start_pos='1.0'
            while True:
                start_pos=self.texteditor.search(word,start_pos,stopindex=END)
                if not start_pos:
                    break
                end_pos='{}+{}c'.format(start_pos,len(word))
                self.texteditor.tag_add('match',start_pos,end_pos)
                matches +=1
                start_pos=end_pos
                self.texteditor.tag_config('match',foreground='red',background='yellow')

    def replaceWords(self,*args):
        replaceText=self.find.replaceInput.get()
        word=self.find.findInput.get()
        content=self.texteditor.get(1.0,END)
        newValue=content.replace(word,replaceText)
        self.texteditor.delete(1.0,END)
        self.texteditor.insert(1.0,newValue)


    def hideToolbar(self,*args):
        global showToolbar
        if showToolbar==True:
            self.toolbar.pack_forget()
            showToolbar=False
        else:
            self.texteditor.pack_forget()
            self.statusbar.pack_forget()
            self.toolbar.pack(side=TOP,fill=X)
            self.texteditor.pack(expand=YES,fill=BOTH)
            self.statusbar.pack(side=BOTTOM)
            showToolbar=True


    def hideStatusbar(self,*args):
        global showStatusbar
        if showStatusbar==True:
            self.statusbar.pack_forget()
            showStatusbar=False
        else:
            self.statusbar.pack()
            showStatusbar=True


if __name__=="__main__":
    root=Tk()
    root.title("Text Editor")
    MainApplication(root).pack(side=TOP,fill=BOTH,expand=True)
    root.iconbitmap('icons/icon.ico')
    root.geometry("1250x850")
    root.mainloop()
