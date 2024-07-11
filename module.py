import tkinter 
from functools import partial
from tkinter import filedialog
from tkinter import messagebox
from fonction import *
# creation de la classe pour gerer ma fenetre
class interface:

    def __init__(self,window):
         self.window = window
         
         self.menu(window)
         self.home()
         
    def clearwindow(self):
        for contenu in self.window.winfo_children():
            contenu.destroy()
    
    def home(self):
        
        tkinter.Label(self.window,text="Crypthon",bg="green",fg="white", font=("helvetica","20")).place(x=250,y=190 )
        tkinter.Label(self.window,text="Bienvenu dans mon programme de cryptage de données",bg="green",fg="white", font=("helvetica","15")).place(x=90,y=240 )

         
    def menu(self, *args):
        menuBar = tkinter.Menu(self.window)
        self.window.config(menu= menuBar)
        
        msg=tkinter.Menu(menuBar, font=("ubuntu",12),tearoff=False)
        msg.add_command(label="crypter un message",command=self.cryptMessage)
        msg.add_command(label="decrypter un message",command=self.decryptMessage)
        menuBar.add_cascade(label="message",menu=msg)
        
        files = tkinter.Menu(menuBar, font=("ubuntu",12),tearoff=False)
        files.add_command(label="crypter un fichier",command=self.ihmFileCrypter)
        files.add_command(label="decrypter un fichier",command=self.ihmFiledeCrypter)
        menuBar.add_cascade(label="File",menu=files)

    def cryptMessage(self):
        self.clearwindow()
        self.menu()
        tkinter.Label(self.window,text="SESSION DE CRYPTAGE DU MESSAGE",bg="green",fg="white", font=("helvetica","20")).pack( )

        #le block ci dessous permet d'afficher les elements en rapport avec le message a entré

        tkinter.Label(self.window,text="Entrer le message:",bg="green",fg="white", font=("helvetica","15")).place(x=20,y=100)
        entre_message=tkinter.Entry(self.window,bg="green",fg="white", font=("helvetica","15"),width=40)
        entre_message.place(x=200,y=100)

        #affichage des element en rapport avec la clé de crypatage

        tkinter.Label(self.window,text="Entrer la clé :",bg="green",fg="white", font=("helvetica","15")).place(x=20,y=150)
        entre_cle=tkinter.Entry(self.window,bg="green",fg="white",show ="*",  font=("helvetica","15"),width=35)
        entre_cle.place(x=200,y=150)
        
        # le boutton 
        tkinter.Button(self.window,text="crypter",bg="green",fg="white", font=("helvetica","15"),command=partial(self.get_data,entre_message,entre_cle)).place(x=500,y=220)

        #  la sortie du message crypeté

        tkinter.Label(self.window,text="Message crypté",bg="green",fg="white", font=("helvetica","15")).place(x=20,y=380)
        self.insert = tkinter.Entry(self.window,bg="green",fg="white", font=("helvetica","15"),width=40) 
        self.insert.place(x=200,y=380)

# la session de decryptage du message

    def decryptMessage(self):
        self.clearwindow()
        self.menu()
        tkinter.Label(self.window,text="SECSSION DE DECRYPTAGE DU MESSAGE",bg="green",fg="white", font=("helvetica","20")).pack( )

        #le block ci dessous permet d'afficher les elements en rapport avec le message a entré

        tkinter.Label(self.window,text="Entrer le message:",bg="green",fg="white", font=("helvetica","15")).place(x=20,y=100)
        entre_message=tkinter.Entry(self.window,bg="green",fg="white", font=("helvetica","15"),width=40)
        entre_message.place(x=200,y=100)

        #affichage des element en rapport avec la clé de decrypatage

        tkinter.Label(self.window,text="Entrer la clé :",bg="green",fg="white", font=("helvetica","15")).place(x=20,y=150)
        entre_cle=tkinter.Entry(self.window,bg="green",fg="white",show ="*",  font=("helvetica","15"),width=35)
        entre_cle.place(x=200,y=150)
        
        # le boutton 
        tkinter.Button(self.window,text="Decrypter",bg="green",fg="white", font=("helvetica","15"),command=partial(self.get_data,entre_message,entre_cle,False)).place(x=500,y=220)

        #  la sortie du message decrypeté

        tkinter.Label(self.window,text="Message decrypté",bg="green",fg="white", font=("helvetica","15")).place(x=20,y=380)
        self.insert = tkinter.Entry(self.window,bg="green",fg="white", font=("helvetica","15"),width=40) 
        self.insert.place(x=200,y=380)

    def get_data(self,entre_message,entre_cle,sicrypt=True):
        message=entre_message.get()
        cle =entre_cle.get()
        message_crypter = ""
        if cle =="":
                messagebox.showerror("","la clé de criptage est oblgatoire")
        else:
            if sicrypt:
                message_crypter = crypt(message,cle)
            else:
                message_crypter = decrypt(message,cle)

            self.insert.delete(0,tkinter.END)
            self.insert.insert(0,message_crypter)
        
    def ihmFileCrypter(self):
        self.clearwindow()
        self.menu()
        tkinter.Label(self.window,text="Cryptage de fichier",bg="green",fg="white", font=("helvetica","20")).pack()
        
        tkinter.Label(self.window,text="File",bg="green",fg="white", font=("helvetica","15")).place(x=20,y=100)
        self.filePath =tkinter.Entry(self.window,bg="green",fg="white", font=("helvetica","15"),width=30)
        self.filePath.place(x=100,y=100)
        
        parcourir = tkinter.Button(self.window,text="Parcourir",bg="white",fg="green",font=("helvetica","15"),command=self.parcourir)
        parcourir.place(x=500,y=90)
        
        tkinter.Label(self.window,text="Entrer la clé :",bg="green",fg="white", font=("helvetica","15")).place(x=20,y=150)
        self.entre_cle=tkinter.Entry(self.window,bg="white",fg="green",show ="*",  font=("helvetica","15"),width=35)
        self.entre_cle.place(x=200,y=150)
        
        btn_crypteFile = tkinter.Button(self.window,text="crypter",bg="white",fg="green",font=("helvetica","15"),width=40,command=self.crypteFile)
        btn_crypteFile.place(x=100,y=220)
        
    def parcourir(self):
        filePath = filedialog.askopenfilename()
        self.filePath.delete(0,tkinter.END)
        self.filePath.insert(0,filePath)
        
    def crypteFile(self):
            contenu_crypter=""
            fil_path = self.filePath.get()
            key = self.entre_cle.get()
            if key =="":
                messagebox.showerror("","la clé de criptage est oblgatoire")
            else:
                if fil_path:
                    msg = messagebox.askyesno("","voulez-vous vraiment cripter le fichier ?")
                    if msg > 0:
                        with open(fil_path ,'r') as file:
                            contenu =  file.readlines()
                        
                        for content in contenu:
                            contenu_crypter+= crypt(content,key)+"\n"
                        ch_contenuCrypter = fil_path
                        
                        with open(ch_contenuCrypter,'w') as filecrypter:
                            filecrypter.write(contenu_crypter)
                        self.filePath.delete(0,tkinter.END)
                        self.entre_cle.delete(0,tkinter.END)
                        
                else:
                    messagebox.showerror("","auncun fichier n'a été indiquer!")
                
    def ihmFiledeCrypter(self):
        self.clearwindow()
        self.menu()
        tkinter.Label(self.window,text="Decryptage de fichier",bg="green",fg="white", font=("helvetica","20")).pack()
        
        tkinter.Label(self.window,text="File",bg="green",fg="white", font=("helvetica","15")).place(x=20,y=100)
        self.filePath =tkinter.Entry(self.window,bg="green",fg="white",font=("helvetica","15"),width=30)
        self.filePath.place(x=100,y=100)
        
        parcourir = tkinter.Button(self.window,text="Parcourir",bg="white",fg="green",font=("helvetica","15"),command=self.parcourir)
        parcourir.place(x=500,y=90)
        
        tkinter.Label(self.window,text="Entrer la clé :",bg="green",fg="white",font=("helvetica","15")).place(x=20,y=150)
        self.entre_cle=tkinter.Entry(self.window,bg="white",fg="green",show ="*",  font=("helvetica","15"),width=35)
        self.entre_cle.place(x=200,y=150)
        
        btn_crypteFile = tkinter.Button(self.window,text="decrypter",bg="white",fg="green",font=("helvetica","15"),width=40,command=self.decrypteFile)
        btn_crypteFile.place(x=100,y=220)
    
    def decrypteFile(self):
        contenu_decrypter=""
        fil_path = self.filePath.get()
        key = self.entre_cle.get()
        if key == "":
            messagebox.showerror("","la clé de criptage est oblgatoire")
        else:
            if fil_path:
                msg = messagebox.askyesno("","voulez-vous vraiment decripter le fichier ?")
                if msg > 0:
                    with open(fil_path ,'r') as file:
                        contenu =  file.readlines()
                    
                    for content in contenu:
                        contenu_decrypter += decrypt(content,key)+"\n"
                    ch_contenudeCrypter = fil_path
                    
                    with open(ch_contenudeCrypter,'w') as fileDecrypter:
                        fileDecrypter.write(contenu_decrypter)
                    self.filePath.delete(0,tkinter.END)
                    self.entre_cle.delete(0,tkinter.END)
                    
            else:
                messagebox.showerror("","auncun fichier n'a été indiquer!")