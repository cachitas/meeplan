import pytest

from converter import convert_spreadsheet_to_doku_table


def test_conversion():
    sample_text_from_spreadsheet = ('1/26/2016\t\tValentina\n'
                                    '1/19/2016\tJeb\t\n'
                                    '1/12/2016\t\tJeb\n'
                                    '1/5/2016\tAnnual Report\t\n'
                                    '12/15/2015\tBill\t')

    result = convert_spreadsheet_to_doku_table(sample_text_from_spreadsheet)

    assert result == [
        '| Dec 15  | Bill            |                 |                 |',
        '| Jan 05  | Annual Report   |                 |                 |',
        '| Jan 12  |                 | Jeb             |                 |',
        '| Jan 19  | Jeb             |                 |                 |',
        '| Jan 26  |                 | Valentina       |                 |'
    ]


def test_conversion_of_empty_textbox():
    sample_text_from_spreadsheet = ''

    with pytest.raises(ValueError):
        convert_spreadsheet_to_doku_table(sample_text_from_spreadsheet)
