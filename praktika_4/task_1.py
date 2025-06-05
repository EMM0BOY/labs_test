import pandas as pd

s = pd.Series(data=['9', 3, 7.1, 'hi!', 8, -52, 12.42, 's123', 15.13, 92], 
              index=range(8, 28, 2))
int_elements = s[s.apply(lambda x: isinstance(x, int))]
variance = int(round(int_elements.var(ddof=1)))

print("Целочисленные элементы:", list(int_elements))
print("Дисперсия (округленная до целого):", variance)