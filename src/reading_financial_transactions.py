import pandas as pd


csv_file = "transactions.csv"
xlsx_file = "transactions_excel.xlsx"


def read_csv(file_path):
    """
    Чтение CSV-файла
    """
    return pd.read_csv(file_path)


def read_xlsx(file_path):
    """
    Чтение XLSX-файла
    """
    return pd.read_excel(file_path)


csv_data = read_csv(csv_file)
xlsx_data = read_xlsx(xlsx_file)

print("CSV Data:")
print(csv_data.head())

print("\nXLSX Data:")
print(xlsx_data.head())