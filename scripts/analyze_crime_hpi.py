from pathlib import Path
import numpy as np
import pandas as pd
import matplotlib.pyplot as plt


ROOT = Path(__file__).resolve().parents[1]
PROCESSED_DIR = ROOT / "data" / "processed"
RESULTS_DIR = ROOT / "results"
FIG_DIR = RESULTS_DIR / "figures"

RESULTS_DIR.mkdir(parents=True, exist_ok=True)
FIG_DIR.mkdir(parents=True, exist_ok=True)



data_path = PROCESSED_DIR / "crime_hpi_monthly.csv"

df = pd.read_csv(
    data_path,
    parse_dates=["year_month"]
).sort_values("year_month")

print("Head of integrated monthly data (raw):")
print(df.head())
print()

print(f"Number of months in raw data: {len(df)}")


raw_corr = df["crime_count"].corr(df["hpi_value"])
print(f"Pearson correlation on raw data (including 2024-09): {raw_corr:.4f}")
print()



cutoff_date = pd.Timestamp("2024-10-01")
df_filtered = df[df["year_month"] >= cutoff_date].copy()

print(f"Number of months after filtering from {cutoff_date.date()}: {len(df_filtered)}")
print("Head of filtered data:")
print(df_filtered.head())
print()


corr = df_filtered["crime_count"].corr(df_filtered["hpi_value"])
print(
    "Pearson correlation between crime_count and hpi_value "
    f"(from {cutoff_date.date()} onward): {corr:.4f}"
)
print()


fig, ax1 = plt.subplots(figsize=(10, 5))

ax1.plot(
    df_filtered["year_month"],
    df_filtered["crime_count"],
    label="Monthly crime count",
)
ax1.set_xlabel("Year-Month")
ax1.set_ylabel("Crime count")

ax2 = ax1.twinx()
ax2.plot(
    df_filtered["year_month"],
    df_filtered["hpi_value"],
    linestyle="--",
    label="HPI value",
)
ax2.set_ylabel("HPI")

fig.autofmt_xdate()
plt.title("Monthly crime count and HPI in Chicago (2024-10 to 2025-08)")

lines_1, labels_1 = ax1.get_legend_handles_labels()
lines_2, labels_2 = ax2.get_legend_handles_labels()
ax1.legend(lines_1 + lines_2, labels_1 + labels_2, loc="upper left")

time_series_path = FIG_DIR / "crime_hpi_timeseries_filtered.png"
plt.tight_layout()
plt.savefig(time_series_path)
plt.close()
print("Saved filtered time series plot to:", time_series_path)


x = df_filtered["hpi_value"].values
y = df_filtered["crime_count"].values

plt.figure(figsize=(6, 5))
plt.scatter(x, y, label="Monthly observations")


slope, intercept = np.polyfit(x, y, 1)
x_line = np.linspace(x.min(), x.max(), 100)
y_line = slope * x_line + intercept
plt.plot(x_line, y_line, linestyle="--", label="Linear trend")

plt.xlabel("HPI value")
plt.ylabel("Crime count")
plt.title("Crime count vs HPI value (2024-10 to 2025-08)")
plt.legend()

plt.text(
    0.05,
    0.95,
    f"Pearson r = {corr:.3f}",
    transform=plt.gca().transAxes,
    ha="left",
    va="top",
)

scatter_path = FIG_DIR / "crime_hpi_scatter_filtered.png"
plt.tight_layout()
plt.savefig(scatter_path)
plt.close()
print("Saved filtered scatter plot with trendline to:", scatter_path)


df_filtered = df_filtered.sort_values("year_month")
df_filtered["crime_roll3"] = df_filtered["crime_count"].rolling(3).mean()

plt.figure(figsize=(10, 5))
plt.plot(
    df_filtered["year_month"],
    df_filtered["crime_count"],
    label="Monthly crime count",
    alpha=0.5,
)
plt.plot(
    df_filtered["year_month"],
    df_filtered["crime_roll3"],
    label="3-month rolling average (crime)",
    linewidth=2,
)
plt.xlabel("Year-Month")
plt.ylabel("Crime count")
plt.title("Monthly crime count and 3-month rolling average (2024-10 to 2025-08)")
plt.legend()
plt.gcf().autofmt_xdate()

rolling_path = FIG_DIR / "crime_count_rolling3.png"
plt.tight_layout()
plt.savefig(rolling_path)
plt.close()
print("Saved rolling-average crime plot to:", rolling_path)


summary_path = RESULTS_DIR / "crime_hpi_summary.csv"
df_filtered[["year_month", "crime_count", "hpi_value", "crime_roll3"]].to_csv(
    summary_path,
    index=False,
)
print("Saved summary table to:", summary_path)


print("\nAnalysis finished.")
