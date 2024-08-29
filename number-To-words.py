import num2words as n2w
from tkinter import * 

def num_to_words():
    given_num = float(num.get())
    num_word = n2w.num2words(given_num)
    display.config(text = str(num_word).capitalize())

root = Tk()
root.title("Number to Words")
root.geometry("650x400")

num = StringVar()

title = Label(root,text="Number to words converter",
              fg = "Blue",font=("Arial",20,'bold')).place(x=220,y=10)

formats_table = Label(root,text="Formats Supported:",
                      fg = "black",font=("arial",10,'bold')).place(x=100,y=70)

pos_format_table = Label(root,text="1. Positives :",
                      fg = "black",font=("arial",10,'bold')).place(x=200,y=90)

neg_format_table = Label(root,text="2. Negatives :",
                      fg = "black",font=("arial",10,'bold')).place(x=200,y=110)

float_format_table = Label(root,text="3. Zeros :",
                      fg = "black",font=("arial",10,'bold')).place(x=200,y=130)

zero_format_table = Label(root,text="4. Floating points/decimals/fractions ",
                      fg = "black",font=("arial",10,'bold')).place(x=200,y=150)

num_entry_lable = Label(root, text="Enter a number :",
               fg="Blue", font=("Arial", 15, 'bold')).place(x=50, y=200)
num_entry = Entry(root,textvariable=num,width=30).place(x=220, y=200)



btn = Button(master=root, text="calculate",fg="black", font=("Arial", 10, 'bold')
             ,command=num_to_words).place(x=280,y=230)

display = Label(root, text="",fg="black", font=("Arial", 10, 'bold'))
display.place(x=10, y=300)


photo = PhotoImage(file = "number.png")
root.iconphoto(False, photo)

root.mainloop()