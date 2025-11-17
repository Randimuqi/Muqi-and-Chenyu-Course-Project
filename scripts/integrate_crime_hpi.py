import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
PROCESSED_DIR = ROOT / "data" / "processed"

crime_path = PROCESSED_DIR / "crime_monthly.csv"
hpi_path = PROCESSED_DIR / "hpi_monthly.csv"

crime_monthly = pd.read_csv(crime_path, parse_dates=["year_month"])
hpi_monthly = pd.read_csv(hpi_path, parse_dates=["year_month"])

print("Crime monthly head:")
print(crime_monthly.head())
print("HPI monthly head:")
print(hpi_monthly.head())

merged = (
    pd.merge(
        crime_monthly,
        hpi_monthly,
        on="year_month",
        how="inner"
    )
    .sort_values("year_month")
)

output_path = PROCESSED_DIR / "crime_hpi_monthly.csv"
merged.to_csv(output_path, index=False)

print("Saved integrated dataset to:", output_path)
print(merged.head())
