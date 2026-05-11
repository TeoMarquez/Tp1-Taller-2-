import pandas as pd
from datetime import datetime
from pathlib import Path
import argparse

DATA_PATH = Path("data/dataset.csv")
DEFAULT_REPORT_PATH = Path("reports/exploration_report.md")


def load_data(path: Path) -> pd.DataFrame:
    try:
        return pd.read_csv(path)
    except FileNotFoundError:
        print(f"[ERROR] No se encontró el archivo: {path}")
        raise SystemExit(1)
    except pd.errors.EmptyDataError:
        print(f"[ERROR] El archivo está vacío: {path}")
        raise SystemExit(1)
    except Exception as e:
        print(f"[ERROR] No se pudo leer el CSV: {e}")
        raise SystemExit(1)


def generate_markdown_report(df: pd.DataFrame) -> str:
    lines = []

    lines.append("# Dataset Exploration Report\n")
    lines.append(f"**Generated at:** {datetime.now()}\n")

    lines.append("## Dataset Shape")
    lines.append(f"- **Rows:** {df.shape[0]}")
    lines.append(f"- **Columns:** {df.shape[1]}\n")

    lines.append("## Columns")
    for col in df.columns:
        lines.append(f"- `{col}`")
    lines.append("")

    lines.append("## Data Types")
    lines.append("```")
    lines.append(df.dtypes.to_string())
    lines.append("```\n")

    lines.append("## Missing Values")
    lines.append("```")
    lines.append(df.isnull().sum().to_string())
    lines.append("```\n")

    lines.append("## Numeric Summary")
    lines.append("```")
    lines.append(df.describe().to_string())
    lines.append("```\n")

    lines.append("## Full Summary (including categorical)")
    lines.append("```")
    lines.append(df.describe(include="all").to_string())
    lines.append("```\n")

    lines.append("## Sample Rows")
    lines.append("```")
    lines.append(df.head().to_string())
    lines.append("```\n")

    return "\n".join(lines)


def save_report(content: str, path: Path, overwrite: bool) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)

    if path.exists() and not overwrite:
        print("El reporte ya existe. Usa --overwrite para sobrescribir.")
        return

    with open(path, "w", encoding="utf-8") as f:
        f.write(content)


def main():
    parser = argparse.ArgumentParser(description="Exploración de dataset de reviews")
    parser.add_argument("--overwrite", action="store_true", help="Sobrescribir el reporte si ya existe")
    parser.add_argument("--timestamp", action="store_true", help="Guardar el reporte con timestamp")

    args = parser.parse_args()

    df = load_data(DATA_PATH)

    if args.timestamp:
        timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
        report_path = Path(f"reports/exploration_report_{timestamp}.md")
    else:
        report_path = DEFAULT_REPORT_PATH

    report = generate_markdown_report(df)
    save_report(report, report_path, overwrite=args.overwrite)

    print(f"Reporte generado en: {report_path.resolve()}")


if __name__ == "__main__":
    main()