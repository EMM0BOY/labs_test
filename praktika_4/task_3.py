import pandas as pd

tr_types = pd.read_csv("data/tr_types.csv", sep=";")
sample = tr_types.sample(n=25, random_state=242)

contains_spisanie = sample["tr_description"].str.contains(
    "списание", case=False, na=False
)
proportion = contains_spisanie.mean()

result = round(proportion, 1)
print(f"{result:.1f}")
