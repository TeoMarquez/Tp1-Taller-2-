import matplotlib.pyplot as plt
import seaborn as sns
from pathlib import Path

OUTPUT = Path("../reports")


def ratings_analysis(df):
    rating_col = "mean of stars"

    avg_rating = df[rating_col].mean()

    # gráfico
    plt.figure(figsize=(8, 5))
    sns.histplot(df[rating_col], bins=20)
    plt.title("Distribución de Ratings")
    plt.xlabel("Rating")
    plt.ylabel("Frecuencia")

    OUTPUT.mkdir(exist_ok=True)
    plt.savefig(OUTPUT / "rating_distribution.png")
    plt.close()

    return f"""
## Análisis de Ratings

### Métricas principales

- *Puntuación promedio:* {avg_rating:.2f}

### Distribución de ratings

![Distribución de ratings](rating_distribution.png)
"""