import tkinter as tk
from tkinter import ttk

# Define conversion rate constants
USD_TO_EUR = 0.82
USD_TO_GBP = 0.72
EUR_TO_USD = 1.22
GBP_TO_USD = 1.39

# Define a function to calculate the exchange rate
def calculate_exchange():
    amount = float(amount_entry.get())
    from_currency = from_currency_combobox.get()
    to_currency = to_currency_combobox.get()
    
    if from_currency == "USD" and to_currency == "EUR":
        converted_amount = amount * USD_TO_EUR
    elif from_currency == "USD" and to_currency == "GBP":
        converted_amount = amount * USD_TO_GBP
    elif from_currency == "EUR" and to_currency == "USD":
        converted_amount = amount * EUR_TO_USD
    elif from_currency == "GBP" and to_currency == "USD":
        converted_amount = amount * GBP_TO_USD
    else:
        converted_amount = amount
        
    result_label.config(text=f"{converted_amount:.2f} {to_currency}")
        
# Create the main window
window = tk.Tk()
window.title("Currency Exchange")

# Create the UI elements
amount_label = ttk.Label(window, text="Amount:")
amount_label.grid(column=0, row=0, padx=5, pady=5)

amount_entry = ttk.Entry(window)
amount_entry.grid(column=1, row=0, padx=5, pady=5)

from_currency_label = ttk.Label(window, text="From Currency:")
from_currency_label.grid(column=0, row=1, padx=5, pady=5)

from_currency_combobox = ttk.Combobox(window, values=["USD", "EUR", "GBP"])
from_currency_combobox.grid(column=1, row=1, padx=5, pady=5)
from_currency_combobox.current(0)

to_currency_label = ttk.Label(window, text="To Currency:")
to_currency_label.grid(column=0, row=2, padx=5, pady=5)

to_currency_combobox = ttk.Combobox(window, values=["USD", "EUR", "GBP"])
to_currency_combobox.grid(column=1, row=2, padx=5, pady=5)
to_currency_combobox.current(1)

convert_button = ttk.Button(window, text="Convert", command=calculate_exchange)
convert_button.grid(column=1, row=3, padx=5, pady=5)

result_label = ttk.Label(window, text="")
result_label.grid(column=1, row=4, padx=5, pady=5)

# Start the event loop
window.mainloop()