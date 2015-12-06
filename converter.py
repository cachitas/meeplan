import tkinter as tk


class ConverterApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)

        self._init_ui()

    def _init_ui(self):
        self.title("meeplan conversion tool")

        input_lbl = tk.Label(self, text="Input")
        input_lbl.pack()

        input_txt = tk.Text(self)
        input_txt.pack()

        output_lbl = tk.Label(self, text="Output")
        output_lbl.pack()

        output_txt = tk.Text(self)
        output_txt.pack()


def main():
    app = ConverterApp()
    app.mainloop()


if __name__ == '__main__':
    main()
