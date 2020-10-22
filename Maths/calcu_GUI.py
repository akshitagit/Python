from functools import partial
import tkinter as tk


class kalkulatorepic(tk.Tk):
    def __init__(self):
        tk.Tk.__init__(self)
        self.title("Kalkulator EPIC")
        self.GaweTombol()
        self.penentu = False

    def GaweTombol(self):
        self.layar = tk.Entry(self, width=25)
        self.layar.grid(row=0, column=0, columnspan=5)

        btn_list = [
            '1', '2', '3',
            '4', '5', '6',
            '7', '8', '9',
            '0', '+', '-',
            'C/D', '/', '*',
            '='
        ]
        baris = 1
        kolom = 0
        for penampung in btn_list:
            perintah = partial(self.hitung, penampung)
            if penampung == '=':
                tk.Button(self, text='=', width=30, command=perintah).grid(row=baris, column=kolom, columnspan=7)
            else :
                tk.Button(self, text=penampung, width=7, command=perintah).grid(row=baris, column=kolom)
            kolom += 1
            if kolom > 2:
                kolom = 0
                baris += 1

    def hitung(self, key):
        if key == '=':
            self.penentu = True
            try:
                result = eval(self.layar.get())
                self.layar.delete(0, tk.END)
                self.layar.insert(tk.END, str(result))
            except:
                self.layar.insert(tk.END, "-> Error!")
        elif key == 'C/D':
            self.layar.delete(0, tk.END)
        else:
            if self.penentu :
                self.layar.delete(0, tk.END)
                self.penentu = False
            self.layar.insert(tk.END, key)

panggil = kalkulatorepic()
panggil.mainloop()