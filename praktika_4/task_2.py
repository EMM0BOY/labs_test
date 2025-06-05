import pandas as pd

# Чтение данных из файлов
tr_mcc_codes = pd.read_csv('data/tr_mcc_codes.csv', sep=',')
tr_types = pd.read_csv('data/tr_types.csv', sep=';')
transactions = pd.read_csv('data/transactions.csv', sep='\t', nrows=1000000)
gender_train = pd.read_csv('data/gender_train.csv', sep=',')

# Проверка содержимого датафреймов
print("TR_MCC_CODES:")
print(tr_mcc_codes.head())
print("\nИнформация о tr_mcc_codes:")
print(tr_mcc_codes.info())

print("\nTR_TYPES:")
print(tr_types.head())
print("\nИнформация о tr_types:")
print(tr_types.info())

print("\nTRANSACTIONS (первые 1 000 000 строк):")
print(transactions.head())
print("\nИнформация о transactions:")
print(transactions.info())

print("\nGENDER_TRAIN:")
print(gender_train.head())
print("\nИнформация о gender_train:")
print(gender_train.info())