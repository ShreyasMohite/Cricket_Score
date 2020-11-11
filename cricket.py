from tkinter import *
import tkinter.messagebox
import threading
from pycricbuzz import *
import json
import threading





class Cricket():
    def __init__(self,root):
        self.root=root
        self.root.title("Cricket Matches")
        self.root.geometry("500x350")
        self.root.iconbitmap("logo561.ico")
        self.root.resizable(0,0)

       


        def on_enter1(e):
            but_send['background']="black"
            but_send['foreground']="cyan"
  
        def on_leave1(e):
            but_send['background']="SystemButtonFace"
            but_send['foreground']="SystemButtonText"

        def on_enter2(e):
            but_clear['background']="black"
            but_clear['foreground']="cyan"
  
        def on_leave2(e):
            but_clear['background']="SystemButtonFace"
            but_clear['foreground']="SystemButtonText"




       
        def browse():
            try:
                clear()
                with open("C:/TEMP/cricketscore.json","w",encoding='utf-8') as fa:
                    cri=Cricbuzz()
                    matches=cri.matches()
                    for m in matches:
                        s=json.dumps(m,indent=4)
                        fa.write(s)

                with open('C:\\TEMP\\cricketscore.json', encoding='utf-8') as data_file:
                    x=json.dumps(data_file.read(),indent=4)
                    data = json.loads(x)
                    ss=str(data)
                    text.insert("end",ss)
            except:
                tkinter.messagebox.showerror("Error","Network Error")


        
        def thread_score():
            t=threading.Thread(target=browse)
            t.start()



                    




        def clear():
            text.delete("1.0","end")




#=======================frame================================#
        mainframe=Frame(self.root,width=500,height=350,relief="ridge",bd=3)
        mainframe.place(x=0,y=0)

        firstframe=Frame(mainframe,width=494,height=100,relief="ridge",bd=3,bg="#876cd5")
        firstframe.place(x=0,y=0)

        secondframe=Frame(mainframe,width=494,height=243,relief="ridge",bd=3)
        secondframe.place(x=0,y=100)

#========================firstframe===========================================#
        
        but_send=Button(firstframe,width=13,text="Matches",font=('times new roman',12),cursor="hand2",command=thread_score)
        but_send.place(x=60,y=28)
        but_send.bind("<Enter>",on_enter1)
        but_send.bind("<Leave>",on_leave1)

        but_clear=Button(firstframe,width=13,text="Clear",font=('times new roman',12),cursor="hand2",command=clear)
        but_clear.place(x=290,y=28)
        but_clear.bind("<Enter>",on_enter2)
        but_clear.bind("<Leave>",on_leave2)

#=========================secondframe==========================================#
        
        scol=Scrollbar(secondframe,orient="vertical")
        scol.place(relx=1, rely=0, relheight=1, anchor='ne')
        
        text=Text(secondframe,height=12,width=58,font=('times new roman',12),yscrollcommand=scol.set,relief="sunken",bd=3,fg="black")      
        text.place(x=0,y=0)
        scol.config(command=text.yview)
       




if __name__ == "__main__":
    root=Tk()
    app=Cricket(root)
    root.mainloop()
