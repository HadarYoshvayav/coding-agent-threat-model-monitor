
from pathlib import Path

import pandas as pd


ROOT = Path(__file__).resolve().parents[1]
DATASET_PATH = (
    ROOT / "threat_model" / "test-00000-of-00001.parquet"
)


def main():
    if not DATASET_PATH.exists():
        raise FileNotFoundError(
            f"Dataset not found: {DATASET_PATH}\n"
            "Check the filename and location in GitHub."
        )

    df = pd.read_parquet(DATASET_PATH)

    print("=== Dataset loaded successfully ===")
    print(f"Rows: {len(df)}")
    print(f"Columns: {len(df.columns)}")
    print(f"Column names: {list(df.columns)}")

    print("\n=== Missing values per column ===")
    print(df.isna().sum().to_string())

    if "label" in df.columns:
        print("\n=== Label distribution ===")
        print(df["label"].value_counts(dropna=False).to_string())

    if "category_and_criticality" in df.columns:
        print("\n=== Category distribution ===")
        print(
            df["category_and_criticality"]
            .value_counts(dropna=False)
            .to_string()
        )

    print("\n=== Example record ===")
    print(df.iloc[0].to_string())


if __name__ == "__main__":
    main()
