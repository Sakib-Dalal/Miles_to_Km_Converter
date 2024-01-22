import tkinter

# Window
window = tkinter.Tk()
window.title("Miles to Km Converter")
window.minsize(width=200, height=100)
window.config(padx=10, pady=30)

# Entry
Input = tkinter.Entry(width=10)
Input.grid(column=2, row=3)

# Miles Label
Label1 = tkinter.Label(text="Miles", font=("Arial", 16, "bold"))
Label1.grid(column=4, row=3)

# is equal to Label
Label2 = tkinter.Label(text="is equal to: ", font=("Arial", 16, "bold"))
Label2.grid(column=0, row=4)

# Output Label
Output = tkinter.Label(text="0", font=("Arial", 16, "bold"))
Output.grid(column=2, row=4)

# Km Label
Label3 = tkinter.Label(text="Km", font=("Arial", 16, "bold"))
Label3.grid(column=4, row=4)


# Button Command
def Calculate_Km():
    user_input = Input.get()
    user_input = float(user_input) * 1.60934
    Output["text"] = str(user_input)


# Calculate Button
Button = tkinter.Button(text="Calculate", font=("Arial", 16, "bold"), command=Calculate_Km)
Button.grid(column=2, row=5)


window.mainloop()