from customtkinter import *
import customtkinter as ctk

ctk.set_appearance_mode("dark")
ctk.set_default_color_theme("blue")
##Make an Window
app = ctk.CTk()
app.title("Feet to meters converter")
app.geometry("600x200")
app.resizable(False , False)
#function
def convert():
    feet = float (label1_entry.get())
    meters = feet / 3.281
    label2_output.set(meters)

#create widget <error>
lable1 = ctk.CTkLabel(
    master=app , text= "Feets", font=ctk.CTkFont(family="Arial", size=15 , weight="bold")) 
lable1.place( 
    relx=0.5, rely=0.3, anchor="center" )
label1_entry = ctk.CTkEntry(master=app)
label1_entry.place(
    relx=0.7, rely=0.3, anchor="center")
lable2 = ctk.CTkLabel(
    master=app , text= "Meters" , font=ctk.CTkFont(family="Arial", size=15 , weight="bold") )
lable2.place(
    relx=0.5, rely=0.6, anchor="center" )
label2_output = ctk.StringVar()
button1 = ctk.CTkButton(
    master=app, text="Convert" ,command=convert ,width=100 , height=40,font=ctk.CTkFont(family="Arial", size=15 , weight="bold" ) )
button1.place(
    relx=0.7, rely=0.6, anchor="center")

#make widget visable
lable1.grid(row=0 , column=2 ,padx=20, pady=20)
label1_entry.grid(row= 0,column=3 , padx=60, pady=20)
lable2.grid(row=1 , column= 2, padx=20, pady=20)
output_entry = ctk.CTkEntry(master=app, textvariable=label2_output, state="readonly" )
output_entry.grid(row = 1 , column= 3, padx=60, pady=20)
button1.grid(row=2 , column= 3 )

app.mainloop()