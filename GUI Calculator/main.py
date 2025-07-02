import customtkinter as ctk

# Window Creation
window = ctk.CTk()
window.title("Simple Calculator")
window.geometry("330x600")
window.configure(fg_color="black")

# Display Screen Creation
display = ctk.CTkLabel(window, text="", anchor="e", height=60, width= 300, font= ("Arial", 32, "bold"), text_color="white", fg_color="black")
display.place(x=10, y=50)

# Button Creation
def print_number(num):
   current = display.cget("text")
   display.configure(text= current + str(num))

box_1 = ctk.CTkButton(window, text="1", height=45, width=70, corner_radius=15, fg_color="orange", text_color="white",
    font=("Arial", 28, "bold"), command=lambda: print_number(1))
box_1.place(x=10, y=190)

box_2 = ctk.CTkButton(window, text="2", height=45, width=70, corner_radius=15, fg_color="orange", text_color="white",
    font=("Arial", 28, "bold"), command=lambda: print_number(2))
box_2.place(x=90, y=190)

box_3 = ctk.CTkButton(window, text="3", height=45, width=70, corner_radius=15, fg_color="orange", text_color="white",
    font=("Arial", 28, "bold"), command=lambda: print_number(3))
box_3.place(x=170, y=190)

box_4 = ctk.CTkButton(window, text="+", height=45, width=70, corner_radius=15, fg_color="orange", text_color="white",
    font=("Arial", 28, "bold"), command=lambda: print_number("+"))
box_4.place(x=250, y=190)

box_5 = ctk.CTkButton(window, text="4", height=45, width=70, corner_radius=15, fg_color="orange", text_color="white",  font=("Arial", 28, "bold"), command=lambda: print_number(4))
box_5.place(x=10, y=250)

box_6 = ctk.CTkButton(window, text="5", height=45, width=70, corner_radius=15, fg_color="orange", text_color="white",  font=("Arial", 28, "bold"), command=lambda: print_number(5))
box_6.place(x=90, y=250)

box_7 = ctk.CTkButton(window, text="6", height=45, width=70, corner_radius=15, fg_color="orange", text_color="white",  font=("Arial", 28, "bold"), command=lambda: print_number(6))
box_7.place(x=170, y=250)

box_8 = ctk.CTkButton(window, text="-",  height=45, width=70, corner_radius=15, fg_color="orange", text_color="white",  font=("Arial", 28, "bold"), command=lambda: print_number("-"))
box_8.place(x=250, y=250)

box_9 = ctk.CTkButton(window, text="7", height=45, width=70, corner_radius=15, fg_color="orange", text_color="white",  font=("Arial", 28, "bold"), command=lambda: print_number(7))
box_9.place(x=10, y=310)

box_10 = ctk.CTkButton(window, text="8", height=45, width=70, corner_radius=15, fg_color="orange", text_color="white",  font=("Arial", 28, "bold"), command=lambda: print_number(8))
box_10.place(x=90, y=310)

box_11 = ctk.CTkButton(window, text="9", height=45, width=70, corner_radius=15, fg_color="orange", text_color="white",  font=("Arial", 28, "bold"), command=lambda: print_number(9))
box_11.place(x=170, y=310)

box_12 = ctk.CTkButton(window, text="÷", height=45, width=70, corner_radius=15, fg_color="orange", text_color="white",  font=("Arial", 28, "bold"), command=lambda: print_number("÷"))
box_12.place(x=250, y=310)

box_13 = ctk.CTkButton(window, text="(", height=45, width=70, corner_radius=15, fg_color="orange", text_color="white",  font=("Arial", 28, "bold"), command=lambda: print_number("("))
box_13.place(x=10, y=370)

box_14 = ctk.CTkButton(window, text="0", height=45, width=70, corner_radius=15, fg_color="orange", text_color="white",  font=("Arial", 28, "bold"), command=lambda: print_number(0))
box_14.place(x=90, y=370)

box_15 = ctk.CTkButton(window, text=")", height=45, width=70, corner_radius=15, fg_color="orange", text_color="white",  font=("Arial", 28, "bold"), command=lambda: print_number(")"))
box_15.place(x=170, y=370)

box_16= ctk.CTkButton(window, text="×", height=45, width=70, corner_radius=15, fg_color="orange", text_color="white",  font=("Arial", 28, "bold"), command=lambda: print_number("×"))
box_16.place(x=250, y=370)

box_17= ctk.CTkButton(window, text="C", height=45, width=150, corner_radius=15, fg_color="orange", text_color="white",  font=("Arial", 28, "bold"), command=lambda: display.configure(text=""))
box_17.place(x=10, y=430)

box_19= ctk.CTkButton(window, text="=", height=45, width=150, corner_radius=15, fg_color="orange", text_color="white",  font=("Arial", 28, "bold"), command=lambda: print_number("="))
box_19.place(x=170, y=430)

# Actual Calculation
def calculate():
    expression = display.cget("text")
    expression = expression.replace("×", "*").replace("÷", "/")
    try:
        result = str(eval(expression))
        display.configure(text=result)
    except:
        display.configure(text="ERROR")

box_19.configure(command=calculate)


window.mainloop()