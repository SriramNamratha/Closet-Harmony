from tkinter import *
import basicCode
from PIL import Image,ImageTk

global input_frame
global output_text


def show_input_frame():
    destroy_output_text()
    # Frame for input elements
    global input_frame
    input_frame = Frame(top1, bg="#FBDECC",height=20, width=50)
    input_frame.pack()

    # Input elements
    label_type = Label(input_frame, text="Type:", font=("arial", 16), bg="#FBDECC")
    label_type.grid(row=0, column=0, pady=10, padx=20, sticky="e")

    type_var = StringVar()
    entry_type = Entry(input_frame, textvariable=type_var, font=("arial", 16),bg='#DEA185',width=13)
    entry_type.grid(row=0, column=1, pady=10, padx=1, sticky="w")

    label_color = Label(input_frame, text="Colour:", font=("arial", 16), bg="#FBDECC")
    label_color.grid(row=1, column=0, pady=10, padx=20, sticky="e")

    color_var = StringVar()
    entry_color = Entry(input_frame, textvariable=color_var, font=("arial", 16),bg="#DEA185",width=13)
    entry_color.grid(row=1, column=1, pady=10, padx=1, sticky="w")

    label_occasion = Label(input_frame, text="Occasion:", font=("arial", 16), bg="#FBDECC")
    label_occasion.grid(row=2, column=0, pady=10, padx=20, sticky="e")

    occasion_var = StringVar()
    entry_occasion = Entry(input_frame, textvariable=occasion_var, font=("arial", 16),bg='#DEA185',width=13)
    entry_occasion.grid(row=2, column=1, pady=10, padx=1, sticky="w")

    label_place = Label(input_frame, text="Place:", font=("arial", 16), bg="#FBDECC")
    label_place.grid(row=3, column=0, pady=10, padx=20, sticky="e")

    place_var = StringVar()
    entry_place = Entry(input_frame, textvariable=place_var, font=("arial", 16),bg='#DEA185',width=13)
    entry_place.grid(row=3, column=1, pady=10, padx=1, sticky="w")

    btn_submit = Button(input_frame, text="Submit", font=("arial", 16), fg="black", bg="#DEA185", bd=2,
                        command=lambda: hide_input_frame(type_var, color_var, occasion_var, place_var))
    btn_submit.grid(row=4, columnspan=2, pady=20)

    input_frame.place(x=450, y=250)

def hide_input_frame(type_var, color_var, occasion_var, place_var):
    # Process the input data here
    print("Type:", type_var.get())
    print("Color:", color_var.get())
    print("Occasion:", occasion_var.get())
    print("Place:", place_var.get())
    basicCode.details(type_var.get(), color_var.get(), occasion_var.get(), place_var.get())

    # Clear the input text boxes
    type_var.set('')
    color_var.set('')
    occasion_var.set('')
    place_var.set('')

    # Hide the input frame
    input_frame.destroy()

def destroy_output_text():
    if 'output_text' in globals():
        output_text.destroy()

def create_output_text():
    global output_text
    output_text = Text(top1,bd=0, font=("Arial", 25), wrap=WORD, height=20, width=60, state=DISABLED,bg="#FBDECC")
    output_text.place(x=500, y=150)

def update_output_text(content):
    global output_text
    output_text.config(state=NORMAL)
    output_text.delete(1.0, END)
    output_text.insert("1.0", content)
    output_text.config(state=DISABLED)


def display(window):
    global top1

    def display_color_segregate():
        input_frame.destroy()
        destroy_output_text()
        create_output_text()
        content = basicCode.display_colorseg_outfits()
        colorstring = "COLOUR SEGREGATION FOR YOUR CLOSET \n\n"
        for tup in content:
            colorstring = colorstring + tup[0] + " " + ":\n"
            for outfit in tup[1]:
                colorstring = colorstring + outfit + "\n"
            colorstring = colorstring+"\n"
        print(colorstring)
        update_output_text(colorstring)

    def display_category_segregate():
        input_frame.destroy()
        destroy_output_text()
        create_output_text()
        content = basicCode.display_catseg_outfits()
        catstring = "CATEGORY SEGREGATION FOR YOUR CLOSET \n\n"
        for tup in content:
            catstring = catstring + tup[0] + " " + ":\n"
            for outfit in tup[1]:
                catstring = catstring + outfit + "\n"
            catstring = catstring+"\n"
        print(catstring)
        update_output_text(catstring)

    def display_occasion_segregate():
        input_frame.destroy()
        destroy_output_text()
        create_output_text()
        content = basicCode.display_ocaseg_outfits()
        ocastring = "OCCASION SEGREGATION FOR YOUR CLOSET \n\n"
        for tup in content:
            ocastring = ocastring + tup[0] + " " + ":\n"
            for outfit in tup[1]:
                ocastring = ocastring + outfit + "\n"
            ocastring = ocastring+"\n"
        print(ocastring)
        update_output_text(ocastring)

    def display_place_segregate():
        input_frame.destroy()
        destroy_output_text()
        create_output_text()
        content = basicCode.display_placeseg_outfits()
        placestring = "KNOW WHAT'S WHERE \n\n"
        for tup in content:
            placestring = placestring + tup[0] + " " + ":\n"
            for outfit in tup[1]:
                placestring = placestring + outfit + "\n"
            placestring = placestring+"\n"
        print(placestring)
        update_output_text(placestring)

    def next_two():
        two ="THE NEXT TWO DAILY WEAR OUTFITS\n\n"
        input_frame.destroy()
        destroy_output_text()
        create_output_text()
        content = basicCode.display_next_two_days_outfits()
        for outfit in content:
            two = two + outfit+"\n"
        print(two)
        update_output_text(two)

    top1 = Toplevel(window)
    top1.geometry("750x750+100+100")
    top1.title("CLOSET HARMONY/menu")
    top1.attributes('-fullscreen', True)
    top1['bg'] = "#FBDECC"

    back1=Image.open('pic2.png')
    img=back1.resize((400, 350))
    my_img=ImageTk.PhotoImage(img)
    label=Label(top1, image=my_img)
    label.place(x=820,y=220)

    label1 = Label(top1, text="MENU", font=("Britannic Bold", 70), fg="#59242E", bg="#FBDECC")
    label1.place(x=180, y=100)

    btn_add_outfits = Button(top1, text="Add Outfits", font=("Arial", 20), fg="#59242E", bg="#DEA185", bd=2,
                             height=1, width=15, command=show_input_frame)
    btn_add_outfits.place(x=160, y=250)

    btn_next_outfits = Button(top1, text="Next Two Outfits", font=("Arial", 20), fg="#59242E", bg="#DEA185", bd=2,
                              height=1, width=15, command=next_two)
    btn_next_outfits.place(x=160, y=320)

    btn_color_segregate = Button(top1, text="Color Segregate", font=("Arial", 20), fg="#59242E", bg="#DEA185", bd=2,
                                 height=1, width=15, command=display_color_segregate)
    btn_color_segregate.place(x=160, y=390)

    btn_category_segregate = Button(top1, text="Category Segregate", font=("Arial", 20), fg="#59242E", bg="#DEA185",
                                    bd=2, height=1, width=15, command=display_category_segregate)
    btn_category_segregate.place(x=160, y=460)

    btn_occasion_segregate = Button(top1, text="Occasion Segregate", font=("Arial", 20), fg="#59242E", bg="#DEA185",
                                    bd=2, height=1, width=15, command=display_occasion_segregate)
    btn_occasion_segregate.place(x=160, y=530)

    btn_know_whats_where = Button(top1, text="Know what's where", font=("Arial", 20), fg="#59242E", bg="#DEA185", bd=2,
                                  height=1, width=15, command=display_place_segregate)
    btn_know_whats_where.place(x=160, y=600)

    top1.mainloop()
