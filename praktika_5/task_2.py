import pandas as pd
import seaborn as sns
import matplotlib.pyplot as plt


def plot_pivot_table(pivot_table):
    plt.figure(figsize=(9, 11))
    sns.heatmap(
        pivot_table,
        cmap="YlGnBu",
        annot=True,
        fmt=".3g",
        annot_kws={"size": 14},
    )
    plt.xticks(fontsize=15)
    plt.yticks(rotation=0, fontsize=15)
    plt.xlabel("Bucket", fontsize=18)
    plt.ylabel("Hour", fontsize=18)
    plt.title("Gender analysis per bucket and hour", fontsize=20)
    plt.show()


data = {
    "Hour": [10, 11, 12, 10, 11, 12],
    "Bucket": ["Very High", "Very High", "Very High", "Income", "Income", "Income"],
    "Gender": ["Male", "Male", "Female", "Female", "Male", "Female"],
    "Value": [150, 200, 100, 300, 250, 400],
}
df = pd.DataFrame(data)
pivot_table = df.pivot_table(
    index="Hour", columns=["Bucket", "Gender"], values="Value", aggfunc="sum"
)

plot_pivot_table(pivot_table)

"""График подтверждает оба утверждения
   мужчины тратят больше в категории высоких трат,
   а женщины получают больше доходов."""
