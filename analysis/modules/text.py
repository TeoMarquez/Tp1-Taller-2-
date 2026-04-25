import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

OUTPUT = Path("../reports")


def text_analysis(df):
    review_col = "review"
    rating_col = "mean of stars"

    df["review_length"] = df[review_col].str.len()

    avg_length = df["review_length"].mean()

    df["rating_int"] = df[rating_col].round().clip(1, 10).astype(int)

    plt.figure(figsize=(10, 6))
    sns.histplot(df["review_length"], bins=30, kde=True)
    plt.title("Distribución de longitud de reviews")
    plt.xlabel("Longitud")
    plt.ylabel("Frecuencia")
    plt.grid(True)

    OUTPUT.mkdir(exist_ok=True)
    plt.savefig(OUTPUT / "text_length_distribution.png")
    plt.close()

    avg_by_rating = df.groupby("rating_int")["review_length"].mean()

    table_md = (
        avg_by_rating
        .reset_index()
        .rename(columns={
            "rating_int": "Rating",
            "review_length": "Avg Review Length"
        })
        .to_markdown(index=False)
    )
    
    plt.figure(figsize=(10, 6))
    sns.barplot(x=avg_by_rating.index, y=avg_by_rating.values)
    plt.title("Longitud promedio de reviews por rating")
    plt.xlabel("Rating")
    plt.ylabel("Longitud promedio")

    plt.savefig(OUTPUT / "length_by_rating.png")
    plt.close()

    return f"""
## Análisis de Texto

- *Longitud promedio de reviews:* {avg_length:.2f}

### Distribución de longitudes
![Text Length](text_length_distribution.png)

### Longitud promedio por rating (1–10)
{table_md}

![Length by rating](length_by_rating.png)
"""