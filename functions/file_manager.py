from openpyxl import load_workbook


def open_excel_file(file_name, sheet_name):
    workbook = load_workbook(file_name, data_only=True)
    worksheet = workbook[sheet_name]
    return worksheet
