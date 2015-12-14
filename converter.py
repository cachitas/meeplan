import datetime
import tkinter as tk
from tkinter import ttk
from tkinter.scrolledtext import ScrolledText


DOKU_ROW_TEMPLATE = (
    '| {day:8}'
    '| {labmeeting:16}'
    '| {journalclub:16}'
    '| {threemin:16}'
    '|'
)


class TextFrame(ttk.LabelFrame):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_ui()

    def _init_ui(self):
        self.textbox = ScrolledText(self, width=70, height=10)
        self.textbox.bind("<1>", lambda event: self.textbox.focus_set())
        self.textbox.pack(expand=True, fill='both')


class ConverterApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self._init_ui()

    def _init_ui(self):
        self.title("meeplan conversion tool")

        self.input_frame = TextFrame(self, text="Input")
        self.input_frame.grid(row=0, column=0, sticky='nswe')

        self.output_frame = TextFrame(self, text="Output")
        self.output_frame.textbox.config(state='disabled')
        self.output_frame.grid(row=0, column=1, sticky='nswe')

        convert_btn = ttk.Button(self, text='Convert to Doku wiki table',
                                 command=self.convert)
        convert_btn.grid(row=1, column=0, columnspan=2, sticky='we')

        self.rowconfigure(0, weight=1)
        self.columnconfigure(0, weight=1)

    def convert(self):
        # Read input text minus the trailing newline
        text = self.input_frame.textbox.get('1.0', 'end-1c')

        try:
            doku_table_rows = convert_spreadsheet_to_doku_table(text)
        except ValueError as e:
            print(e)
            return

        self.output_frame.textbox.config(state='normal')
        for row in doku_table_rows:
            self.output_frame.textbox.insert('end', row + '\n')
        self.output_frame.textbox.config(state='disabled')


def convert_spreadsheet_to_doku_table(spreadsheet_text):

    if spreadsheet_text == '':
        raise ValueError('Missing text to convert')

    # We want an ordered list of [(day, name1, ...), ...]
    row_data = [line.split('\t') for line in spreadsheet_text.split('\n')]

    # Convert dates to datetime.date objects for future sorting and repr
    for elements in row_data:
        elements[0] = datetime.datetime.strptime(
            elements[0], "%m/%d/%Y").date()

    # Sort by date (the first element)
    row_data.sort(key=lambda elemets: elemets[0])

    doku_table_rows = []

    for data in row_data:
        row_dict = {}
        row_dict['day'] = data[0].strftime('%b %d')
        try:
            row_dict['labmeeting'] = data[1]
        except IndexError:
            row_dict['labmeeting'] = ''
        try:
            row_dict['journalclub'] = data[2]
        except IndexError:
            row_dict['journalclub'] = ''
        try:
            row_dict['threemin'] = data[3]
        except IndexError:
            row_dict['threemin'] = ''

        doku_table_rows.append(DOKU_ROW_TEMPLATE.format(**row_dict))

    return doku_table_rows


def main():
    app = ConverterApp()
    app.mainloop()


if __name__ == '__main__':
    main()
