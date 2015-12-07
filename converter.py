import tkinter as tk
from tkinter.scrolledtext import ScrolledText


class TextFrame(tk.LabelFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_ui()

    def _init_ui(self):
        self.textbox = ScrolledText(self)
        self.textbox.pack()


class ConverterApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_ui()

    def _init_ui(self):
        self.title("meeplan conversion tool")

        input_frame = TextFrame(self, text="Input", padx=5)
        input_frame.pack()

        output_frame = TextFrame(self, text="Output", padx=5)
        output_frame.pack()


def main():
    app = ConverterApp()
    app.mainloop()


if __name__ == '__main__':
    main()
