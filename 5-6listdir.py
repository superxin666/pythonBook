import os
from time import sleep
import tkinter
from tkinter import *

class DirList(object):
    def __init__(self,initdir=None):
        self.top = Tk()
        self.label = Label(self.top, text='Directory Lister v1.1').pack()

        self.cwd = StringVar(self.top)

        self.dirl = Label(self.top, fg='blue', font=('Helvetica', 12, 'bold')).pack()

        self.dirfm = Frame(self.top)
        self.dirsb = Scrollbar(self.dirfm)
        self.dirsb.pack(side=RIGHT, fill=Y)
        self.dirs = Listbox(self.dirfm, height=15, width=50, yscrollcommand=self.dirsb.set)
        self.dirs.bind('<Double-1>', self.setDirAndGo)
        self.dirsb .config(command=self.dirs.yview())
        self.dirs.pack(side=LEFT, fill=BOTH)
        self.dirfm.pack()

        self.dirn = Entry(self.top, width='50', textvariable=self.cwd)
        self.dirn.bind('<Return>', self.doLS)
        self.dirn.pack()

        self.bfm = Frame(self.top)
        self.clr = Button(self.bfm, text='Clear', command=self.clrDir, activebackground='blue', activeforeground='white')
        self.ls = Button(self.bfm, text='List Dirctory', command=self.doLS, activebackground='green', activeforeground='white')
        self.quit = Button(self.bfm, text="Quit", command=self.top.quit, activebackground='red', activeforeground='white')
        self.clr.pack(side=LEFT)
        self.ls.pack(side=LEFT)
        self.quit.pack(side=LEFT)
        self.bfm.pack()

        if initdir:
            self.cwd.set(os.curdir)
            self.doLS()

    def clrDir(self, ev=None):
        self.cwd.set('')
    def setDirAndGo(self,ev=None):
        self.last = self.cwd.get()
        self.dirs.config(selectbackground='red')
        check = self.dirs.get(self.dirs.curselection())
        if not check:
            check = os.curdir;
        self.cwd.set(check)
        self.doLS()
    def doLS(self, ev=NONE):
        error = ''
        tdir = self.cwd.get()
        if not tdir:
            tdir = os.curdir
        if not os.path.exists(tdir):
            error = tdir +':no such file'
        elif not os.path.isdir(tdir):
            error = tdir+':not a directory'

        if error:
            self.cwd.set(error)
            self.top.update()
            sleep(2)
            if not (hasattr(self, 'last') and self.last):
                self.last = os.curdir
            self.cwd.set(self.last)
            self.dirs.config(selectbackground='LightSkyBlue')
            self.top.update()
            return

        self.cwd.set('FETCHING DIRECTORY CONTENTS')
        self.top.update()
        dirlist = os.listdir(tdir)
        dirlist.sort()
        os.chdir(tdir)

        # self.dirl.config(text=os.getcwd())
        self.dirs.delete(0, END)
        self.dirs.insert(END, os.curdir)
        self.dirs.insert(END, os.pardir)
        for eachFile in dirlist:
            self.dirs.insert(END, eachFile)
        self.cwd.set(os.curdir)
        self.dirs.config(selectbackground='LightSkyBlue')

def main():
    d = DirList(os.curdir)
    mainloop()

if __name__ == '__main__':
    main()



