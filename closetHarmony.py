from tkinter import *
from PIL import Image,ImageTk
import menu
window = Tk()
window.geometry("1000x1000+100+100")
window.title("closet harmony/main menu")
window.attributes('-fullscreen',True)
window['bg']="#FBDECC"
label1=Label(text="CLOSET ",font=("Britannic Bold",70),fg="#59242E",bg="#FBDECC")
label1.place(x=170,y=280)
label1=Label(text="HARMONY",font=("Britannic Bold",70),fg="#59242E",bg="#FBDECC")
label1.place(x=90,y=380)
back1=Image.open('pic1.png')
img=back1.resize((900, 750))
my_img=ImageTk.PhotoImage(img)
label=Label(window, image=my_img)
label.place(x=500,y=0)
def direct():
    menu.display(window)
btnmain=Button(window,text="Organise",font=("Arial",20),fg="#FBDECC",bg="#59242E",bd=2,height=1,width=15,command=direct)
btnmain.place(x=160,y=500)
window.mainloop()
