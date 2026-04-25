import pandas as pd
from pathlib import Path

from modules.ratings import ratings_analysis
from modules.text import text_analysis
from modules.cases import cases_analysis
from modules.visualization import extra_visualization

DATA_PATH = Path("../data/dataset.csv")
REPORT_PATH = Path("../reports/report.md")


def load_data():
    return pd.read_csv(DATA_PATH)


def save_report(content: str):
    REPORT_PATH.parent.mkdir(parents=True, exist_ok=True)
    with open(REPORT_PATH, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    print("Cargando datos...")
    df = load_data()

    report = []
    report.append("# Reporte del análisis del dataset\n")
    report.append("--- \n")
    print("Generando análisis...")

    report.append(ratings_analysis(df))
    report.append("--- \n")
    print("Generando análisis de rating...")

    report.append(text_analysis(df))
    report.append("--- \n")
    print("Generando análisis de texto...")

    report.append(cases_analysis(df))
    report.append("--- \n")
    print("Generando análisis de casos...")
    
    report.append(extra_visualization(df))
    report.append("--- \n")
    print("Generando análisis extra...")

    save_report("\n".join(report))

    print("Reporte generado")


if __name__ == "__main__":
    main()