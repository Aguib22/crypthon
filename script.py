#coding:utf-8
#GBwPRFPwXDRFyLLRwPLT
import tkinter
from module import interface

if __name__=="__main__":
    
    window = tkinter.Tk()
    window.title('AS_crypt')
    window.geometry("650x500")
    window.minsize(650,500)
    window.maxsize(800,700)
    window.config(bg='green')
    #OKSv:DEANJKvWCQExKQ
    interface = interface(window)
   

    window.mainloop()  

