from tkinter import *
import random

countd={"WIN":0,"LOST":0,"TIE":0}
s="                 "
colors={"ROCK":"grey","PAPER":"orange","SCISSORS":"blue",s:"#e8e8e8",'WIN':"green","LOST":"red",'TIE':"brown"}
root=Tk()
root.title('RPS Game')
root.geometry("400x300")
def pcchoice():
    choice=""
    li=["SCISSORS","ROCK","PAPER"]
    return li[(random.randint(1,3))-1]

def showstat(t1,t2,t3):
    Label_Game=Label(root,text=t1,fg="white",bg=colors[t1])
    Label_Game.grid(row=8,column=0,pady=10)
    Label_Game=Label(root,text=t2,fg="white",bg=colors[t2])
    Label_Game.grid(row=8,column=1,pady=10)
    Label_Game=Label(root,text=t3,fg="white",bg=colors[t3])
    Label_Game.grid(row=8,column=2,pady=10)

def analyse(t1,t2):
    if t1==t2:
        return "TIE"
    t=tuple([t1,t2])
    li=[("PAPER","ROCK"),("SCISSORS","PAPER"),("ROCK","SCISSORS")]
    if t in li:
        return "WIN"
    return "LOST"
def showcount(t1,t2,t3):
    Label_cWIN=Label(root,text=t1).grid(row=11,column=1)
    Label_cLOST=Label(root,text=t2).grid(row=13,column=1)
    Label_cTIE=Label(root,text=t3).grid(row=15,column=1)

def countstat(t):
    global countd
    countd[t]+=1
    showcount(s,s,s)
    showcount(countd["WIN"],countd["LOST"],countd["TIE"])


def game(input):
    showstat(s,s,s)
    t1=input
    t2=pcchoice()
    t3=analyse(t1,t2)
    showstat(t1,t2,t3)
    countstat(t3)

#display buttons and Heading on the root window

#Heading "ROCK PAPER SCISSORS"
Label_Head=Label(root,text="Rock Paper Scissors",font=100,fg="white",bg="blue",width=50)
Label_Head.grid(row=0,column=0,columnspan=6,rowspan=2)

#Buttons for ROCK, PAPER ,SCISSORS
btn_Rock=Button(root,text="ROCK",command=lambda:game("ROCK"),fg="white",bg="Grey")
btn_Paper=Button(root,text="PAPER",command=lambda:game("PAPER"),fg="white",bg="orange")
btn_Scissors=Button(root,text="SCISSORS",command=lambda:game("SCISSORS"),fg="white",bg="blue")
btn_Rock.grid(row=4,column=0,padx=25,pady=25)
btn_Paper.grid(row=4,column=1,padx=25,pady=25)
btn_Scissors.grid(row=4,column=2,padx=25,pady=25)
Label_u=Label(root,text="You").grid(row=6,column=0,pady=5)
Label_p=Label(root,text="Computer").grid(row=6,column=1,pady=5)
Label_s=Label(root,text="Status").grid(row=6,column=2,pady=5)
Label_WIN=Label(root,text="WIN").grid(row=11,column=0,pady=5)
Label_LOST=Label(root,text="LOST").grid(row=13,column=0,pady=5)
Label_TIE=Label(root,text="TIE").grid(row=15,column=0,pady=5)

root.mainloop()
