#Convertor Valutar - 1.0
from tkinter import *
from tkinter import ttk
from tkinter import messagebox
import tkinter as tk
import requests
import datetime as dt
 
class CurrencyConverter:
 
    def __init__(self, url):
        self.url = 'https://api.exchangerate.host/latest'
        self.response = requests.get(url)
        self.data = self.response.json()
        self.rates = self.data.get('rates')
 
    def convert(self, amount, base_currency, des_currency):
        if base_currency != 'EUR':
            amount = amount/self.rates[base_currency]
 
        # Setam 2 zecimale
        amount = round(amount*self.rates[des_currency], 2)
        # Adaugam virgula dupa 3 cifre
        amount = '{:,}'.format(amount)
        return amount
 
 
class Main(tk.Tk):
 
    def __init__(self, converter):
        tk.Tk.__init__(self)
        self.title('Convertor valutar')
        self.geometry('400x400')
        self.config(bg='#3A3B3C')
        self.CurrencyConverter = converter
 
        # Create title label
        self.title_label = Label(self, text='Convertor valutar', bg='#3A3B3C', fg='red', font=('Times New Roman', 20), relief='sunken')
        self.title_label.place(x=200, y=35, anchor='center')
 
        # Create date label
        self.date_label = Label(self, text=f'Actualizat in data de: {dt.datetime.now():%d %B}', bg='#3A3B3C', fg='white', font=('calibri', 10))
        self.date_label.place(x=120, y=400, anchor='sw')
 
        # Create amount label
        self.amount_label = Label(self, text='Introdu valoare pe care vrei sa o convertesti: ', bg='#3A3B3C', fg='white', font=('franklin gothic book', 12))
        self.amount_label.place(x=200, y=80, anchor='center')
 
        # Create amount entry box
        self.amount_entry = Entry(self)
        self.amount_entry.config(width=25)
        self.amount_entry.place(x=200, y=110, anchor='center')
 
        # Create 'from' label
        self.base_currency_label = Label(self, text='Din: ', bg='#3A3B3C', fg='white', font=('franklin gothic book', 15))
        self.base_currency_label.place(x=200, y=140, anchor='center')
 
        # Create dropdown menus
        self.currency_variable1 = StringVar(self)
        self.currency_variable2 = StringVar(self)
        self.currency_variable1.set('EUR')
        self.currency_variable2.set('RON')
 
        self.currency_combobox1 = ttk.Combobox(self, width=20, textvariable=self.currency_variable1, values=list(self.CurrencyConverter.rates.keys()), state='readonly')
        self.currency_combobox1.place(x=200, y=170, anchor='center')
 
        self.currency_combobox2 = ttk.Combobox(self, width=20, textvariable=self.currency_variable2, values=list(self.CurrencyConverter.rates.keys()), state='readonly')
        self.currency_combobox2.place(x=200, y=230, anchor='center')
 
        # Create 'convert' button
        self.convert_button = Button(self, text='Convert', bg='#52595D', fg='black', command=self.processed)
        self.convert_button.place(x=150, y=270, anchor='center')
 
        self.switch_button = Button(self, text='Switch', bg='#52595D', fg='black', command=self.switch_currency)
        self.switch_button.place(x=200, y=200, anchor='center')
 
 
        # Create 'clear' button
        self.clear_button = Button(self, text='Clear', bg='red', fg='black', command=self.clear)
        self.clear_button.place(x=240, y=270, anchor='center')
 
        # Create converted result field
        self.final_result = Label(self, text='', bg='#52595D', fg='white', font=('calibri', 12), relief='sunken', width=40)
        self.final_result.place(x=200, y=310, anchor='center')
 
    def clear(self):
        clear_entry = self.amount_entry.delete(0, END)
        clear_result = self.final_result.config(text='')
        return clear_entry, clear_result
 
    def switch_currency(self):
      self.currency_variable1, self.currency_variable2 = self.currency_variable2, self.currency_variable1
      self.currency_combobox1.config(textvariable=self.currency_variable1)
      self.currency_combobox2.config(textvariable=self.currency_variable2)   
    # Create a function to perform
    def processed(self):
        try:
            given_amount = float(self.amount_entry.get())
            given_base_currency = self.currency_variable1.get()
            given_des_currency = self.currency_variable2.get()
            converted_amount = self.CurrencyConverter.convert(given_amount, given_base_currency, given_des_currency)
            # Add comma every 3 numbers
            given_amount = '{:,}'.format(given_amount)
 
            self.final_result.config(text=f'{given_amount} {given_base_currency} = {converted_amount} {given_des_currency}')
 
        # Create warning message box
        except ValueError:
            convert_error = messagebox.showwarning('WARNING!', 'Please Fill the Amount Field (integer only)!')
            return convert_error
 
 
 
if __name__ == '__main__':
    converter = CurrencyConverter('https://api.exchangerate.host/latest')
    Main(converter)
    mainloop()