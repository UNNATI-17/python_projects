from tkinter import*
window = Tk()
window.title("Currency Convertor: GeeksForGeeks")
LIGHT_BLUE = "#ADD8E6"



window.minsize(width=200,height=200)
heading_label = Label(text="Currency Convertor: GeeksForGeeks", font="BOLD")
heading_label.grid(row=0,column=0)
ammount_label = Label(text="Amount: ",justify=LEFT)
ammount_label.grid(row=1, column= 0)
From_currency_label = Label(text="From currency: ",justify=LEFT)
From_currency_label.grid(row=2,column=0)
To_currency_label = Label(text="To currency: ", justify=LEFT)
To_currency_label.grid(row=3,column=0)

ammount_entry = Entry(width=20)
ammount_entry.grid(row=1, column=1)
ammount_entry.focus()


currencies = ["USD","EUR","INR","JPY","AUD","GBP"]
From_currency_var = StringVar()
From_currency_var.set(currencies[0])
From_currency_dropdown = OptionMenu(window,From_currency_var, *currencies)
From_currency_dropdown.grid(row=2, column=1)
From_currency_dropdown.config(width=14)

To_currency_var = StringVar()
To_currency_var.set(currencies[2])
To_currency_dropdown = OptionMenu(window,To_currency_var,*currencies)
To_currency_dropdown.grid(row=3, column=1)
To_currency_dropdown.config(width=14)

convert_button = Button(text="Convert",width=15,bg=LIGHT_BLUE)
convert_button.grid(row=4,column=1)

converted_amount_label = Label(text="Converted Amount: ")
converted_amount_label.grid(row=5,column=0)

converted_amount_entry = Entry(width=20)
converted_amount_entry.grid(row=5,column=1)

clear_button = Button(text="Clear All",bg=LIGHT_BLUE)
clear_button.grid(row=6,column=1)



























window.mainloop()