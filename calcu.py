from tkinter import *
from functools import partial
win = Tk()
btb_txt = ["**", "//", "%", "C", "7", "8", "9", "+", "4", "5", "6", "-", "1", "2", "3", "*", ".", "0", "=", "/"]
row_num = 0
col_num = 0
res = Label(win, text="0",width=13,font= ('Epilogue', 35), anchor="e", bg="#000000", fg="#ffffff")
res.grid(row= 0 , column= 0, columnspan=4, sticky="we")
def malupit(ayo):
    if res.cget("text") == "0":
        res.config(text=ayo)
    elif ayo == "=":
        try:
            res.config(text=str(eval(res.cget("text"))))
        except:
            res.config(text="ERROR!", fg="red")
    elif ayo == "C":
        res.config(text="0")
    else:
        res.config(text=res.cget("text") + ayo)
for i in range(len(btb_txt)):
    Button(win, width=13, height=3, text=btb_txt[i], bg="#09ded3",fg="#022626", font= ('Epilogue', 12), command=partial(malupit, btb_txt[i])).grid(row=row_num+2, column= col_num)
    col_num += 1
    if col_num == 4:
        row_num += 1
        col_num = 0
win.title("Malupit na Calculator 2")
win.geometry("508x399+710+300")
win.mainloop()