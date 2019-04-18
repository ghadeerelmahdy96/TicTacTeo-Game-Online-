#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 14:06:41 2019

@author: ghadeerelmahdy
"""


import threading as th
import UserInterface as ui
from tkinter import messagebox as mb
    
flag=1

windowshow = ui.getWindow()
windowshow.title("client")
windowshow.geometry("400x300")
s = ui.getSocket()

ui.setVaraibles("X",s)

def recieveThread (s):
    while True:
      message = s.recv(500).decode("utf8")
      if message  == 'a': 
          ui.btn1["text"] = "O"
          ui.lbl2['text']="player O is waiting for you"
      if message  == 'b' : 
          ui.btn2["text"] = "O"
          ui.lbl2['text']="player O is waiting for you"
      if message  == 'c' : 
          ui.btn3["text"] = "O"
          ui.lbl2['text']="player O is waiting for you"
      if message  == 'd' : 
          ui.btn4["text"] = "O"
          ui.lbl2['text']="player O is waiting for you"
      if message  == 'e' : 
          ui.btn5["text"] = "O" 
          ui.lbl2['text']="player O is waiting for you"
      if message  == 'f' : 
          ui.btn6["text"] = "O"  
          ui.lbl2['text']="player O is waiting for you" 
      if message  == 'g' : 
          ui.btn7["text"] = "O" 
          ui.lbl2['text']="player O is waiting for you" 
      if message  == 'h' : 
          ui.btn8["text"] = "O" 
          ui.lbl2['text']="player O is waiting for you"
      if message  == 'i' : 
          ui.btn9["text"] = "O"
          ui.lbl2['text']="player O is waiting for you" 
      if message  == 'r' : 
          ui.restart()     
      if message == 'w':
          mb.showinfo(windowshow,"Other side wins")
          ui.restart()
      if message =='go':
          mb.showinfo(windowshow,"Game Over")
          ui.restart()
          ui.send("r")
         
 
ui.btn1
ui.btn2
ui.btn3
ui.btn4
ui.btn5
ui.btn6
ui.btn7
ui.btn8
ui.btn9

ui.gridButtons()


host= "127.0.0.1"
port = 7000
s.connect((host,port))

rec=th.Thread(target=recieveThread,args=(s,))
rec.start()

windowshow.mainloop()


        
s.close() 