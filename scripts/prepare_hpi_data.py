import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"
PROCESSED_DIR = ROOT / "data" / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

hpi_path = RAW_DIR / "CHXRHTNSA.csv"

hpi = pd.read_csv(hpi_path)

print("Columns in HPI dataset:")
print(hpi.columns)

DATE_COL_CANDIDATES = {"observation_date", "DATE", "date"}
VALUE_COL_CANDIDATES = {"CHXRHTNSA", "VALUE"}

date_col = None
for col in hpi.columns:
    if col.strip().upper() in {c.upper() for c in DATE_COL_CANDIDATES}:
        date_col = col
        break

if date_col is None:
    raise ValueError("Could not find date column in HPI dataset.")

value_col = None
for col in hpi.columns:
    if col.strip().upper() in {c.upper() for c in VALUE_COL_CANDIDATES}:
        value_col = col
        break

if value_col is None:
    raise ValueError("Could not find value column in HPI dataset.")

print(f"Using date column: {date_col}, value column: {value_col}")

hpi[date_col] = pd.to_datetime(hpi[date_col])
hpi["year_month"] = hpi[date_col].dt.to_period("M").dt.to_timestamp()

hpi_monthly = (
    hpi[["year_month", value_col]]
    .rename(columns={value_col: "hpi_value"})
    .sort_values("year_month")
)

output_path = PROCESSED_DIR / "hpi_monthly.csv"
hpi_monthly.to_csv(output_path, index=False)

print("Saved monthly HPI data to:", output_path)
print(hpi_monthly.head())
