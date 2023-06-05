from tkinter import Tk, Button, Entry, Frame

# Hesap makinesi sınıfı
class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Uygulama")
        master.geometry("400x600")
        master.resizable(0, 0)

        # Sekme oluştur
        tab_frame = Frame(master, bg="#f0f0f0", width=400, height=40)
        tab_frame.grid(row=0, column=0, columnspan=2)

        # Hesap makinesi alanı
        self.calc_frame = Frame(master)
        self.calc_frame.grid(row=1, column=0, padx=10, pady=10)

        # Boş alan
        self.empty_frame = Frame(master)
        self.empty_frame.grid(row=1, column=1, padx=10, pady=10)

        # Başlangıçta hesap makinesi alanı aktif
        self.calc_frame.tkraise()

        # Giriş alanı oluştur
        self.entry = Entry(self.calc_frame, width=20, justify="right", font=("Arial", 20))
        self.entry.grid(row=0, column=0, columnspan=4, padx=10, pady=10)

        # Düğmeleri oluştur
        buttons = [
            ("7", 1, 0), ("8", 1, 1), ("9", 1, 2), ("/", 1, 3),
            ("4", 2, 0), ("5", 2, 1), ("6", 2, 2), ("*", 2, 3),
            ("1", 3, 0), ("2", 3, 1), ("3", 3, 2), ("-", 3, 3),
            ("0", 4, 0), (".", 4, 1), ("=", 4, 2), ("+", 4, 3),
            ("Reset", 5, 0, 1, 4)  # Resetleme butonu
        ]

        for button_info in buttons:
            if len(button_info) == 3:
                button_text, row, col = button_info
                rowspan = columnspan = 1
            else:
                button_text, row, col, rowspan, columnspan = button_info

            button = Button(self.calc_frame, text=button_text, width=10, height=3, font=("Arial", 14), bg="#e0e0e0", fg="#333333")
            button.grid(row=row, column=col, padx=5, pady=5, rowspan=rowspan, columnspan=columnspan)
            button.bind("<Button-1>", lambda event, text=button_text: self.on_button_click(text))

        # Sekme düğmesi oluştur
        tab_button = Button(tab_frame, text="Calc", width=10, height=2, font=("Arial", 14))
        tab_button.grid(row=0, column=0, padx=10, pady=5)
        tab_button.configure(command=self.show_calc_frame)

        # Boş alan düğmesi oluştur
        empty_button = Button(tab_frame, text="Empty", width=10, height=2, font=("Arial", 14))
        empty_button.grid(row=0, column=1, padx=10, pady=5)
        empty_button.configure(command=self.show_empty_frame)

    # Düğmelere tıklama olaylarını işle
    def on_button_click(self, text):
        current_entry = self.entry.get()

        if text == "=":
            try:
                result = eval(current_entry)
                self.entry.delete(0, "end")
                self.entry.insert("end", str(result))
            except Exception:
                self.entry.delete(0, "end")
                self.entry.insert("end", "Hatalı İfade!")
        elif text == "C":
            self.entry.delete(0, "end")
        elif text == "Reset":
            self.entry.delete(0, "end")
        else:
            self.entry.insert("end", text)

    # Hesap makinesi alanını göster
    def show_calc_frame(self):
        self.calc_frame.tkraise()

    # Boş alanı göster
    def show_empty_frame(self):
        self.empty_frame.tkraise()

# Ana uygulamayı oluştur
root = Tk()
calculator = Calculator(root)

# Uygulamayı çalıştır
root.mainloop()
