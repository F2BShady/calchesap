from tkinter import Tk, Button, Entry, Frame

# Hesap makinesi sınıfı
class Calculator:
    def __init__(self, master):
        self.master = master
        master.title("Hesap Makinesi")
        master.geometry("600x400")

        # Giriş alanı oluştur
        self.entry = Entry(master, width=30, justify="right")
        self.entry.grid(row=0, column=0, columnspan=4)

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

            button = Button(master, text=button_text, width=10, height=3)
            button.grid(row=row, column=col, padx=5, pady=5, rowspan=rowspan, columnspan=columnspan)
            button.bind("<Button-1>", lambda event, text=button_text: self.on_button_click(text))

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

# Ana uygulamayı oluştur
root = Tk()
calculator = Calculator(root)

# Uygulamayı çalıştır
root.mainloop()
