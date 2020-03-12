
######IMPORT
import sys
import tkinter 
import win32api



def move_detect():
   

##################################
################ROOT##############
##################################

    root = tkinter.Tk()
    root.iconbitmap('.icon.ico')
    root.configure(bg="black")
    root.title("PASS")
    root.overrideredirect(True)
    root.attributes("-topmost", True)
    root.geometry("{0}x{1}+0+0".format(root.winfo_screenwidth(), root.winfo_screenheight()))
    # use transparency level 0.1 to 1.0 (no transparency)
    root.attributes("-alpha", 0.95)
    

    def validar():
        if password.get() != "PASS": # ESTO SE DEBE MODIFICAR 
            tkinter.Label(root, text="PASSWORD INCORRECTO!", bg="black",fg="red3",font=('Comic Sans MS', 14)).place(x=520,y=450,width=250,height=40)
            
        else:
            root.destroy()

    

       
##############################
#############Widget###########
##############################

    password = tkinter.StringVar() 
    key=tkinter.Entry(root,show='*', textvariable=password ,font=('Arial', 14)).place(x=520,y=350,width=250,height=40)
  
  
    tkinter.Button(root, command=validar, bg="springGreen2",text="Iniciar",font=('Comic Sans MS', 14),).place(x=520,y=600,width=250,height=40)

    

    root.protocol("WM_DELETE_WINDOW", validar)   
    root.mainloop()
    
    

actualpos = win32api.GetCursorPos()
count = 0 

while(True):
    curpos = win32api.GetCursorPos()
    if actualpos != curpos:
        count = count +1
        
        savedpos = curpos
        move_detect()
        break


  
 
