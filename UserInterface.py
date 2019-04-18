#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 15:29:20 2019

@author: ghadeerelmahdy
"""

import tkinter as tk
import socket
from tkinter import messagebox as mb

playx = 0
playo = 0
flag=1    
text = ""

windowshow=tk.Tk() 
sock  = socket.socket(socket.AF_INET, socket.SOCK_STREAM) #socket number
def setVaraibles(t,s): 
    global text,sock
    text = t
    sock = s 
def getWindow():
   global windowshow
   return windowshow 
    
def getSocket():
    global sock
    return sock
      
def window(player):
    mb.showinfo("windowshow", player+ " wins") 
    send("w")

def send(x):
    global sock
    sock.send(x.encode('utf8'))
    
def checkTurn(text):
    global playx,playo
    if text == "X":
       playx +=1
       if playx != playo :
         lbl2['text']="please wait for player O!"
    if text == "O":
        playo +=1      
        if playx != playo :
         lbl2['text']="please wait for player X!"
           
           
    
def btn1Clicked():
 global text    
 if (btn1['text'] == ""):
     btn1["text"] = text
     send("a")
     checkTurn(text)
   #after updating our text, we should check if anyone wins  
 check()
   
def btn2Clicked():
  global text   
  if (btn2['text'] == ""):
     btn2["text"] = text
     send("b")
     checkTurn(text)
   #after updating our text, we should check if anyone wins  
  check()
   
def btn3Clicked():
  global text   
  if (btn3['text'] == ""):
     btn3["text"] = text
     send("c")
     checkTurn(text)
   #after updating our text, we should check if anyone wins  
  check()        

def btn4Clicked():
 global text    
 if (btn4['text'] == ""):
     btn4["text"] = text
     send("d")
     checkTurn(text)
   #after updating our text, we should check if anyone wins  
 check() 
   
def btn5Clicked():
  global text  
  if (btn5['text'] == ""):
     btn5["text"] = text
     send("e")
     checkTurn(text)
   #after updating our text, we should check if anyone wins  
  check()
   
def btn6Clicked():
  global text  
  if (btn6['text'] == ""):
     btn6["text"] = text
     send('f')
     checkTurn(text)
   #after updating our text, we should check if anyone wins  
  check() 

def btn7Clicked():
  global text  
  if (btn7['text'] == ""):
     btn7["text"] = text
     send('g')
     checkTurn(text)
   #after updating our text, we should check if anyone wins  
  check()   
def btn8Clicked():
  global text  
  if (btn8['text'] == ""):
     btn8["text"] = text
     send('h')
     checkTurn(text)
   #after updating our text, we should check if anyone wins  
  check()
   
def btn9Clicked():
  global text  
  if (btn9['text'] == ""):
     btn9["text"] = text
     send('i')
     checkTurn(text)
   #after updating our text, we should check if anyone wins  
  check() 

def restart(): 
 global flag   
 btn1["text"] = "" 
 btn2["text"] = "" 
 btn3["text"] = "" 
 btn4["text"] = "" 
 btn5["text"] = "" 
 btn6["text"] = ""
 btn7["text"] = "" 
 btn8["text"] = "" 
 btn9["text"] = "" 
 flag =1  
 lbl2["text"]=""
   


def gridButtons():
    btn1.grid(row=0,column=5)
    btn2.grid(row=0,column=6)
    btn3.grid(row=0,column=7)
    btn4.grid(row=1,column=5)
    btn5.grid(row=1,column=6)
    btn6.grid(row=1,column=7)
    btn7.grid(row=2,column=5)
    btn8.grid(row=2,column=6)
    btn9.grid(row=2,column=7)
    btnRestart.grid(row=2,column=9)

def check():
   global flag #for global action
   flag +=1
   if((btn1["text"]==btn2["text"]== btn3["text"]=="X" )or( btn1["text"]==btn2["text"]== btn3["text"]=="O")):
      window(btn1["text"]) 
      mb.showinfo("windowshow", "End of the Game")  
      restart()
   if((btn4["text"]== btn5["text"]== btn6["text"]=="X" )or (btn4["text"]==btn5["text"]== btn6["text"]=="O")):
      window(btn4["text"])
      mb.showinfo("windowshow", "End of the Game")  
      restart()
   if((btn7["text"]== btn8["text"]== btn9["text"]=="X" )or (btn7["text"]== btn8["text"]== btn9["text"]=="O")):
      window(btn7["text"])
      mb.showinfo("windowshow", "End of the Game")  
      restart()
   if((btn1["text"]== btn4["text"]== btn7["text"]=="X" )or (btn1["text"]== btn4["text"]== btn7["text"]=="O")):
      window(btn1["text"])
      mb.showinfo("windowshow", "End of the Game")  
      restart()
   if((btn2["text"]==btn5["text"]== btn8["text"]=="X" )or (btn2["text"]== btn5["text"]==btn8["text"]=="O")):
      window(btn2["text"])
      mb.showinfo("windowshow", "End of the Game")  
      restart()
   if((btn3["text"]== btn6["text"]== btn9["text"]=="X") or( btn3["text"]== btn6["text"]== btn9["text"]=="O")):
      window(btn3["text"])
      mb.showinfo("windowshow", "End of the Game")  
      restart()
   if((btn1["text"]== btn5["text"]==btn9["text"]=="X" )or (btn1["text"]==btn5["text"]==btn9["text"]=="O")):
      window(btn1["text"])
      mb.showinfo("windowshow", "End of the Game")  
      restart()
   if((btn3["text"]== btn5["text"]== btn7["text"]=="X" )or( btn3["text"]== btn5["text"]==  btn7["text"]=="O")):
      window(btn3["text"])
      mb.showinfo("windowshow", "End of the Game")  
      restart() 
   if flag ==6:
       mb.showinfo("windowshow", "Game Over")  
       restart()
       send('go')
  
def combineFun():
    restart()
    send("r")
         
btn1 = tk.Button(windowshow,text="",font=("Times", "10", "bold italic"),width=6,height= 6,command=btn1Clicked)
btn2 = tk.Button(windowshow,text="",font=("Times", "10", "bold italic"),width=6,height= 6,command=btn2Clicked)
btn3 = tk.Button(windowshow,text="",font=("Times", "10", "bold italic"),width=6,height= 6,command=btn3Clicked)
btn4 = tk.Button(windowshow,text="",font=("Times", "10", "bold italic"),width=6,height= 6,command=btn4Clicked)
btn5 = tk.Button(windowshow,text="",font=("Times", "10", "bold italic"),width=6,height= 6,command=btn5Clicked)
btn6 = tk.Button(windowshow,text="",font=("Times", "10", "bold italic"),width=6,height= 6,command=btn6Clicked)
btn7 = tk.Button(windowshow,text="",font=("Times", "10", "bold italic"),width=6,height= 6,command=btn7Clicked)
btn8 = tk.Button(windowshow,text="",font=("Times", "10", "bold italic"),width=6,height= 6,command=btn8Clicked)
btn9 = tk.Button(windowshow,text="",font=("Times", "10", "bold italic"),width=6,height= 6,command=btn9Clicked)
btnRestart = tk.Button(windowshow,text="Restart",bg="blue",font=("Times", "15", "bold italic"),width=6,height=1,command=combineFun)  


lbl1=tk.Label(windowshow,text="",font=("Times", "20", "bold italic"))
lbl1.grid(row=0,column=9)
lbl2= tk.Label(windowshow,text="",font=("Times", "15", "bold italic"))
lbl2.grid(row=1,column=9)      
