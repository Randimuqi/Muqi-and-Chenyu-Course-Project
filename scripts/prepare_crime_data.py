import pandas as pd
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
RAW_DIR = ROOT / "data" / "raw"
PROCESSED_DIR = ROOT / "data" / "processed"
PROCESSED_DIR.mkdir(parents=True, exist_ok=True)

crime_path = RAW_DIR / "DM1_Crime_data_set_chicago_20251007.csv"

df = pd.read_csv(crime_path)

print("Columns in crime dataset:")
print(df.columns)

df.columns = df.columns.str.strip()

DATE_COL_CANDIDATES = {
    "DATE  OF OCCURRENCE",
    "DATE OF OCCURRENCE",
    "DATE_OF_OCCURRENCE",
    "Date",
}

date_col = None
for col in df.columns:
    if col.strip().upper() in {c.upper() for c in DATE_COL_CANDIDATES}:
        date_col = col
        break

if date_col is None:
    raise ValueError(
        "Could not find the date column. "
        "Update DATE_COL_CANDIDATES in prepare_crime_data.py to match your column name."
    )

print(f"Using date column: {date_col}")

df[date_col] = pd.to_datetime(df[date_col])

df["year_month"] = df[date_col].dt.to_period("M").dt.to_timestamp()

crime_monthly = (
    df.groupby("year_month")
      .size()
      .reset_index(name="crime_count")
      .sort_values("year_month")
)

output_path = PROCESSED_DIR / "crime_monthly.csv"
crime_monthly.to_csv(output_path, index=False)

print("Saved monthly crime counts to:", output_path)
print(crime_monthly.head())
