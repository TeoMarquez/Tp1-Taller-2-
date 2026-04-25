import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

OUTPUT = Path("../reports")

def extra_visualization(df):
    rating_col = "mean of stars"

    df["rating_int"] = df[rating_col].round().clip(1, 10).astype(int)

    count_by_rating = df["rating_int"].value_counts().sort_index()

    plt.figure(figsize=(10, 6))

    plt.bar(count_by_rating.index, count_by_rating.values, label="Cantidad de reviews")

    plt.plot(
        count_by_rating.index,
        count_by_rating.values,
        marker="o",
        linestyle="-",
        label="Tendencia"
    )

    plt.title("Cantidad de reviews según rating")
    plt.xlabel("Rating (1–10)")
    plt.ylabel("Cantidad de reviews")
    plt.xticks(range(1, 11))
    plt.grid(axis="y", linestyle="--", alpha=0.7)
    plt.legend()

    OUTPUT.mkdir(exist_ok=True)
    plt.savefig(OUTPUT / "rating_distribution_clean.png")
    plt.close()

    return f"""
## Visualización adicional

Se muestra la cantidad de reviews por rating, junto con una línea de tendencia para facilitar la interpretación.

![Distribución de ratings](rating_distribution_clean.png)
"""