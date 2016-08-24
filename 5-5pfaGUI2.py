from functools import partial as pto
from tkinter import Tk,  Button, X
from tkinter.messagebox import showinfo, showerror, showwarning


WARN = 'warn'
CRIT = 'crit'
REGU = 'regu'

SIGNS = {
    'do enter':CRIT,
    "reailroad":REGU,
    'wrong way':CRIT,
    'merging traffic':WARN,
    'one way':REGU,
}

critCB = lambda: showerror('Errow', 'Errow Button Pressed!')
warnCB = lambda: showwarning("Warning", 'Warning Button Pressed!')
infoCB = lambda: showinfo('Info', 'Info Button Pressed!')

top = Tk()
top.title('Road Signs')
top.geometry('300x200')
Button(top, text='quit', command=top.quit(), bg='red', fg='white').pack()

Mybotton = pto(Button, top)
CritButton = pto(Mybotton,command=critCB, bg='white', fg='red')
WarnButton = pto(Mybotton, command=warnCB,bg='goldenrod1')
ReguButton = pto(Mybotton, command=infoCB,bg='white')

for eachSign in SIGNS:
    signType = SIGNS[eachSign]
    cmd = '%sButton(text=%r%s).pack(fill=X, expand=1)' % (signType.title(), eachSign, '.upper()' if signType == CRIT else '.title()')
    eval(cmd)
top.mainloop()