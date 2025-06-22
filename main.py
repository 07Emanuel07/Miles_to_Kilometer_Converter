# Emanuel Biruk Seifegebreal - 2024 --> This project is for learning purposes

from tkinter import *


def miles_to_km():
    miles = float(miles_input.get())
    km = miles * 1.609
    zero_label.config(text=f"{km}")


window = Tk()
window.title("Mile to Km Converter")
window.config(padx=20, pady=20)

# Entries
miles_input = Entry(width=7)
# Adding some text to begin with
miles_input.insert(END, string="0")
# Gets text in entry
print(miles_input.get())
miles_input.grid(column=1, row=0)

# Labels
miles_label = Label(text="Miles")
miles_label.grid(column=2, row=0)

is_equal_label = Label(text="is equal to")
is_equal_label.grid(column=0, row=1)

zero_label = Label(text="0")

zero_label.grid(column=1, row=1)

km_label = Label(text="Km")
km_label.grid(column=2, row=1)

# Button
button = Button(text="Calculate", command=miles_to_km)
button.grid(column=1, row=2)

window.mainloop()
