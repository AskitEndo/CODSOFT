import tkinter as tk

calculation = ""

def add_to_calation(symbol):
    global calculation
    calculation += str(symbol)
    text_result.delete(1.0,"end")
    text_result.insert(1.0,calculation)


def evaluate_calculation():
    global calculation
    try:
        calculation=str(eval(calculation))
        text_result.delete(1.0,"end")
        text_result.insert(1.0,calculation)

    except:
        clear_field()
        text_result.insert(1.0,"Error")


def clear_field():
    global calculation
    calculation = ""
    text_result.delete(1.0,"end")


root = tk.Tk()
root.geometry("300x275")
root.title("CalculationDIY")

text_result = tk.Text(root, height=2, width=16, font=("ariel", 24))
text_result.grid(columnspan=5)


btn_1 = tk.Button(root, text="1", command=lambda: add_to_calation(1), width=5, font=("ariel",14))
btn_1.grid(row=2, column=1)

btn_2 = tk.Button(root, text="2", command=lambda: add_to_calation(2), width=5, font=("ariel",14))
btn_2.grid(row=2, column=2)

btn_3 = tk.Button(root, text="3", command=lambda: add_to_calation(3), width=5, font=("ariel",14))
btn_3.grid(row=2, column=3)

btn_4 = tk.Button(root, text="4", command=lambda: add_to_calation(4), width=5, font=("ariel",14))
btn_4.grid(row=3, column=1)

btn_5 = tk.Button(root, text="5", command=lambda: add_to_calation(5), width=5, font=("ariel",14))
btn_5.grid(row=3, column=2)

btn_6 = tk.Button(root, text="6", command=lambda: add_to_calation(6), width=5, font=("ariel",14))
btn_6.grid(row=3, column=3)

btn_7 = tk.Button(root, text="7", command=lambda: add_to_calation(7), width=5, font=("ariel",14))
btn_7.grid(row=4, column=1)

btn_8 = tk.Button(root, text="8", command=lambda: add_to_calation(8), width=5, font=("ariel",14))
btn_8.grid(row=4, column=2)

btn_9 = tk.Button(root, text="9", command=lambda: add_to_calation(9), width=5, font=("ariel",14))
btn_9.grid(row=4, column=3)

btn_0 = tk.Button(root, text="0", command=lambda: add_to_calation(0), width=5, font=("ariel",14))
btn_0.grid(row=5, column=2)

btn_plus = tk.Button(root, text="+", command=lambda: add_to_calation("+"), width=5, font=("ariel",14))
btn_plus.grid(row=2, column=4)
 
btn_min = tk.Button(root, text="-", command=lambda: add_to_calation("-"), width=5, font=("ariel",14))
btn_min.grid(row=3, column=4)
 
btn_mul = tk.Button(root, text="*", command=lambda: add_to_calation("*"), width=5, font=("ariel",14))
btn_mul.grid(row=4, column=4)
 
btn_div= tk.Button(root, text="/", command=lambda: add_to_calation("/"), width=5, font=("ariel",14))
btn_div.grid(row=5, column=4)

btn_ob= tk.Button(root, text="(", command=lambda: add_to_calation("("), width=5, font=("ariel",14))
btn_ob.grid(row=5, column=1)

btn_cb= tk.Button(root, text=")", command=lambda: add_to_calation(")"), width=5, font=("ariel",14))
btn_cb.grid(row=5, column=3)

btn_equals= tk.Button(root, text="=", command=evaluate_calculation, width=11, font=("ariel",14))
btn_equals.grid(row=6, column=1, columnspan=2)

btn_clearg= tk.Button(root, text="clr", command=clear_field, width=11, font=("ariel",14))
btn_clearg.grid(row=6, column=3, columnspan=2)
 
root.mainloop()