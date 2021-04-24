from tkinter import *
import subprocess as sub

sub.call(['gui.py','htmlfilename.htm'],shell=True)
p = sub.Popen('./clone.py',stdout=sub.PIPE,stderr=sub.PIPE)
output, errors = p.communicate()

root = Tk()
text = Text(root)
text.pack()
text.insert(END, output)
root.mainloop()