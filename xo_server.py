#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Created on Thu Apr 18 14:07:14 2019

@author: ghadeerelmahdy
"""

import UserInterface as ui
import socket
import threading as th
from tkinter import messagebox as mb
    
flag=1
player=1
windowshow = ui.getWindow()
windowshow.title("server")
windowshow.geometry("400x300")


s = ui.getSocket()
s.setsockopt(socket.SOL_SOCKET,socket.SO_REUSEADDR,1) #LEVEL(3LA MOSTWA EL SOCKET) , OPTION(REUSE ADDRESS), VALUE OF OPTION
host= "127.0.0.1"
port = 7000
s.bind((host,port))
s.listen(5)


def recieveThread (s):
    while True:
      message = s.recv(500).decode("utf8")
      if message  =='a': 
          ui.btn1["text"] = "X"
          ui.lbl2['text']="player X is waiting for you"
      if message  == 'b' : 
          ui.btn2["text"] = "X"
          ui.lbl2['text']="player X is waiting for you"
      if message  == 'c' : 
          ui.btn3["text"] = "X"
          ui.lbl2['text']="player X is waiting for you"
      if message  == 'd' : 
          ui.btn4["text"] = "X" 
          ui.lbl2['text']="player X is waiting for you"
      if message  == 'e' : 
          ui.btn5["text"] = "X"
          ui.lbl2['text']="player X is waiting for you"
      if message  == 'f' : 
          ui.btn6["text"] = "X"
          ui.lbl2['text']="player X is waiting for you"
      if message  == 'g' : 
          ui.btn7["text"] = "X"
          ui.lbl2['text']="player X is waiting for you"
      if message  == 'h' : 
          ui.btn8["text"] = "X"
          ui.lbl2['text']="player X is waiting for you"
      if message  == 'i' : 
          ui.btn9["text"] = "X"
          ui.lbl2['text']="player X is waiting for you"
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


c , ad = s.accept()
  
ui.lbl1["text"] = "Start Playing with"+ad[0]
 
ui.setVaraibles("O",c)

rec=th.Thread(target=recieveThread,args=(c,))
rec.start()

windowshow.mainloop()


        
s.close() 