import pandas as pd

tr_mcc_codes = pd.read_csv("data/tr_mcc_codes.csv", sep=",")
tr_types = pd.read_csv("data/tr_types.csv", sep=";")
transactions = pd.read_csv("data/transactions.csv", sep="\t", nrows=1000000)
customers_gender_train = pd.read_csv("data/customers_gender_train.csv", sep=",")

merged = transactions.merge(tr_types, on="tr_type", how="inner").merge(
    tr_mcc_codes, on="mcc_code", how="inner"
)

merged = merged.merge(customers_gender_train, on="customer_id", how="left")

positive_amount = merged[merged["amount"] > 0]
print(f"Количество строк после фильтрации: {len(positive_amount)}")
positive_amount["tr_hour"] = positive_amount["tr_datetime"].apply(
    lambda x: x.split()[1].split(":")[0] if len(x.split()) > 1 else x.split(":")[0]
)

positive_amount["amount_bucket"] = pd.cut(
    positive_amount["amount"],
    bins=[0, 1000, 5000, 10000, 50000, float("inf")],
    labels=["0-1k", "1k-5k", "5k-10k", "10k-50k", "50k+"],
)

pivot_table = positive_amount.pivot_table(
    index="tr_hour",
    columns="amount_bucket",
    values="gender",
    aggfunc="count",
    fill_value=0,
)

print("\nСводная таблица:")
print(pivot_table)