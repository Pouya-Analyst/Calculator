import tkinter as tk
window = tk.Tk()
window.geometry("300x450")
window.title("Calculator")
window.iconbitmap("calculator_3534.ico")
window.resizable(False, False)

def click(number):
   display.insert(tk.END, number)

def op_click(op):
    display.insert(tk.END, op)

def equal():
    x = display.get()
    try:
      result = eval(x)
      display.delete(0, tk.END) 
      display.insert(tk.END, result)
    except SyntaxError:
        display.delete(0, tk.END) 
        display.insert(tk.END, "Error")
    except SyntaxError:
     display.delete(0, tk.END) 
     display.insert(tk.END, "Error")
    except ZeroDivisionError:
     display.delete(0,tk.END) 
     display.insert(tk.END, "Error")

def clear_button():
    display.delete(0,tk.END) 

display = tk.Entry(window, border=15, font=('Dosis SemiBold',20), justify='right')
Button1 = tk.Button(window, text="1", font=('Dosis SemiBold',15), command=lambda c=1:click(c))
Button2 = tk.Button(window, text="2", font=('Dosis SemiBold',15), command=lambda c=2:click(c)) 
Button3 = tk.Button(window, text="3", font=('Dosis SemiBold',15), command=lambda c=3:click(c))
Button4 = tk.Button(window, text="4", font=('Dosis SemiBold',15), command=lambda c=4:click(c))
Button5 = tk.Button(window, text="5", font=('Dosis SemiBold',15), command=lambda c=5:click(c))
Button6 = tk.Button(window, text="6", font=('Dosis SemiBold',15), command=lambda c=6:click(c))
Button7 = tk.Button(window, text="7", font=('Dosis SemiBold',15), command=lambda c=7:click(c))
Button8 = tk.Button(window, text="8", font=('Dosis SemiBold',15), command=lambda c=8:click(c))
Button9 = tk.Button(window, text="9", font=('Dosis SemiBold',15), command=lambda c=9:click(c))
Button0 = tk.Button(window, text="0", font=('Dosis SemiBold',15), command=lambda c=0:click(c))
ButtonSum = tk.Button(window, text="+", font=('Dosis SemiBold',15), command=lambda o='+':op_click(o))
ButtonSub = tk.Button(window, text="-", font=('Dosis SemiBold',15), command=lambda o='-':op_click(o))
ButtonMul = tk.Button(window, text="*", font=('Dosis SemiBold',15), command=lambda o='*':op_click(o))
ButtonDiv = tk.Button(window, text="/", font=('Dosis SemiBold',15), command=lambda o='/':op_click(o))
ButtonEqual =tk.Button(window, text="=", font=('Dosis SemiBold',15), command=equal)
ButtonC =tk.Button(window, text="C", font=('Dosis SemiBold',15), command=clear_button)

display.grid(row=0, column=0, columnspan=4, sticky="news")

Button7.grid(row=1, column=0, sticky="news", padx=2, pady=2)
Button8.grid(row=1, column=1, sticky="news", padx=2, pady=2)
Button9.grid(row=1, column=2, sticky="news", padx=2, pady=2)
ButtonSum.grid(row=1, column=3, sticky="news", padx=2, pady=2)

Button4.grid(row=2, column=0, sticky="news", padx=2, pady=2)
Button5.grid(row=2, column=1, sticky="news", padx=2, pady=2)
Button6.grid(row=2, column=2, sticky="news", padx=2, pady=2)
ButtonSub.grid(row=2, column=3, sticky="news", padx=2, pady=2)

Button1.grid(row=3, column=0, sticky="news", padx=2, pady=2)
Button2.grid(row=3, column=1, sticky="news", padx=2, pady=2) 
Button3.grid(row=3, column=2, sticky="news", padx=2, pady=2)
ButtonMul.grid(row=3, column=3, sticky="news", padx=2, pady=2)

ButtonC.grid(row=4, column=0, sticky="news", padx=2, pady=2)
Button0.grid(row=4, column=1, sticky="news", padx=2, pady=2)
ButtonEqual.grid(row=4, column=2, sticky="news", padx=2, pady=2)
ButtonDiv.grid(row=4, column=3,  sticky="news", padx=2, pady=2)

for i in range(0, 5):
    for j in range(0, 4):
        window.rowconfigure(i, weight=1)
        window.columnconfigure(j, weight=1)
    




window.mainloop()    