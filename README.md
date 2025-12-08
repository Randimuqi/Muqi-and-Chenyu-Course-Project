Chicago Crime and Housing Price Dynamics: A Reproducible Integrated Monthly Analysis (2024–2025)
 
Contributors:
- Chenyu Wang (chenyuw6)
- Muqi Su (muqisu2)
 
Contribution Statement

Chenyu Wang led the conceptual development and writing of the project report, including the summary, data profile, data quality assessment, findings, and interpretation of results. Chenyu also performed dataset exploration, evaluated data issues, and validated the analytical logic behind the charts and statistical outputs.
Muqi Su led the technical implementation of the project, including writing the data acquisition scripts, developing the preprocessing and integration pipeline, generating the analysis code, producing visualizations, and organizing the repository structure. Muqi also drafted the initial integration logic and contributed to verifying computational reproducibility.
Both contributors jointly reviewed project decisions, refined the workflow, and ensured consistency across documentation, code, and final outputs.
 
Summary

This project examines the relationship between monthly crime activity and changes in the housing price index (HPI) in Chicago between late 2024 and mid-2025. Public safety and economic conditions are often discussed together, yet it is uncommon to investigate whether short-term fluctuations in crime levels correspond to observable changes in housing markets. Although the available time window is limited, this project provides a transparent, fully reproducible workflow that integrates two public datasets, evaluates their quality, and analyzes their joint temporal patterns.

The project begins with the acquisition of two primary data sources: the City of Chicago’s published crime dataset and the Federal Reserve Bank of St. Louis’s housing price index series accessed via the FRED API. Because both data providers include licensing or redistribution restrictions, the repository does not store raw data. Instead, we provide scripted instructions that allow any user to re-download the datasets directly from their official sources, ensuring legal compliance and reproducibility.

After acquisition, preprocessing steps standardize the structure and time granularity of the datasets. Daily crime records are aggregated into monthly crime counts, while HPI values are converted to a consistent date format to match the crime dataset. Additional cleaning includes handling missing or malformed date values, checking value ranges, verifying schema consistency, and ensuring that aggregated counts align with expectations. These steps help ensure that both datasets are reliable, comparable, and suitable for joint analysis.

A key component of the workflow is the integration of the two datasets using a shared “year-month” key. Only months appearing in both sources are retained, yielding a clean timeline that avoids artificial inflation of sample size. By consolidating the two sources into a unified monthly table, we can explore statistical relationships and visualize broader trends.

Our analysis identifies a moderate positive correlation between monthly crime counts and the housing price index within the overlapping period, with Pearson’s r around 0.48. The scatterplot—including a fitted linear trend—illustrates this upward relationship. Meanwhile, the integrated time-series visualization reveals that both crime counts and HPI rise steadily through the first half of 2025 after an initial decline during the winter months. While the short time span prevents strong causal conclusions, the synchronized upward movement offers insight into how the two indicators may shift in parallel within a short-term economic and social environment.

To better understand the temporal behavior of crime levels, a three-month rolling average was computed. This smoothed curve highlights underlying patterns more clearly by reducing short-term noise. Both the raw monthly crime curve and the rolling average suggest a turning point in early 2025 followed by a gradual increase. This complements the HPI trend, which similarly begins to rise mid-winter and continues upward into the summer.

Beyond the statistical findings, the overarching goal of this project is methodological: to develop a reproducible and transparent workflow that others can execute without ambiguity. All processing steps, from data retrieval to cleaning, integration, visualization, and analysis, are implemented through Python scripts and documented in a structured repository. Final outputs, including integrated datasets and figures, are stored in designated results folders, while Box is used to host larger artifacts that cannot be redistributed in the repository.

Through this work, we learned the importance of consistent data formatting, careful handling of temporal information, and documenting every transformation clearly enough for another researcher to repeat. Future extensions could involve expanding the time span, adding socioeconomic variables such as unemployment or income levels, or exploring predictive modeling. Although limited in duration, the present analysis successfully demonstrates a transparent, reproducible process for examining interactions between crime data and housing market indicators.

Data Profile

This project uses two publicly available datasets representing different aspects of urban conditions in Chicago: crime incidents and the housing price index (HPI). Although both datasets are government- or institution-provided, they differ significantly in structure, granularity, and legal constraints. This section provides an overview of each dataset, its origin, fields, limitations, and any ethical or legal considerations required for proper use.
1. Chicago Crime Dataset (DM1 Crime Data Set – Chicago)

Source: City of Chicago Open Data Portal

URL: https://data.cityofchicago.org/Public-Safety/DM1-Crime-data-set-chicago/55jb-nki6/about_data

Accessed: October 7, 2025

The crime dataset is maintained by the Chicago Police Department (CPD) and published through the city's official open data portal. It provides detailed incident-level reports, excluding homicide cases that are tracked separately. Each record includes attributes such as offense type, date of occurrence, block-level location (not a full address), arrest status, and other administrative fields. The dataset used in this project contains approximately 65,000 records covering the most recent year.

Because of its size (over 25 MB), the raw dataset is not stored directly in the GitHub repository. Instead, users are instructed to download the CSV from the official portal and place it in the designated data/raw/ directory. This ensures compliance with open-data redistribution rules and keeps the repository lightweight.

Fields used in the project:
- Date of Occurrence (timestamp; used for monthly aggregation)
- Primary Type (crime category)
- Incident ID and administrative attributes (used for validation but not modeling)

Ethical / Legal Considerations:

The dataset does not contain personally identifiable information (PII). Block-level masking ensures privacy by removing exact addresses. According to the portal’s terms, the data is free for non-commercial use with attribution to the City of Chicago. No sensitive or restricted data is handled in this project.

Limitations:
- Crime records are sometimes updated or reclassified after initial reporting, which can introduce minor inconsistencies.
- Daily timestamps require careful parsing due to formatting irregularities.
- The time span available for analysis is limited to roughly one year.

2. Chicago Housing Price Index (CHXRHTNSA – Case–Shiller HPI)

Source: Federal Reserve Bank of St. Louis (FRED)

URL: https://fred.stlouisfed.org/docs/api/fred/

Accessed: October 7, 2025

The housing price index (HPI) data come from the S&P CoreLogic Case–Shiller index series, accessed through the FRED API. This index represents seasonally unadjusted monthly changes in single-family home prices in the Chicago metropolitan area. It is a high-quality economic indicator widely used in financial and urban studies.

The dataset used in this project was downloaded as a CSV from FRED. Compared to the crime dataset, the HPI contains only two main columns: a monthly date (observation_date) and the index value (CHXRHTNSA). Because the dataset is small and freely shareable for academic use, it is stored directly in the repository under data/raw/.

Fields used in the project:
- observation_date (monthly timestamp)
- HPI value (numeric index representing home prices)

Ethical / Legal Considerations:

The FRED Terms of Use allow personal, educational, and non-commercial use with attribution. Redistribution of raw data is not prohibited, but the project still provides proper citation and encourages users to retrieve the dataset programmatically through the provided script for reproducibility.

Limitations:

- The dataset is aggregated at the metropolitan level; it does not reflect neighborhood-level price differences.
- Monthly resolution limits the complexity of temporal analysis when matched with daily crime events.
- The available overlapping period with the crime data restricts the sample size.

3. Combined Considerations for Integration

Both datasets represent different systems—public safety vs. economic conditions—with distinct structures. The integration of the two required creating a shared year-month key. Proper cleaning was essential because:

- Crime timestamps required conversion into monthly buckets.
- HPI timestamps were already monthly but needed type standardization.
- The datasets do not cover the exact same date ranges, so only overlapping months were retained.

The resulting integrated dataset contains:
- year_month (datetime month)
- crime_count (aggregated monthly total)
- hpi_value (monthly index)

This final dataset is small, clean, and suitable for reproducible analysis.

We reviewed the Terms of Use of both the Chicago Data Portal and the FRED API and confirm that our usage of the datasets complies fully with their stated licenses and conditions.
 
Data Quality

Assessing data quality is essential before conducting any statistical analysis or drawing conclusions about the relationship between crime levels and housing prices. This section documents the quality checks performed on both datasets, the issues identified, and the steps we took to address or mitigate them. Our assessment focuses on completeness, consistency, temporal coherence, schema validity, and handling of anomalous observations.

1. Quality of the Chicago Crime Dataset

The raw crime dataset includes approximately 65,000 incident-level records across the most recent year. Because the dataset is collected operationally by the Chicago Police Department, several characteristics required attention:

(a) Completeness and missing values

The dataset is generally complete, but a small number of records contain missing or malformed timestamps in the Date of Occurrence field. Since our analysis requires aggregating all incidents to monthly totals, missing dates cannot be used. These records were safely excluded during the monthly aggregation process, and their exclusion does not meaningfully affect the overall monthly pattern.

(b) Temporal consistency

The timestamp column contains dates in mixed formats depending on the exporting system. Some rows include "2025-01-03" while others follow a "01/03/2025 05:32" format. These inconsistencies were resolved by coercing all timestamps into a single datetime type. After standardization, each row could be reliably assigned to a monthly bucket.

(c) Range and outlier checks

Monthly crime counts for most months exceed 15,000, except for September 2024, which showed only 629 incidents. This extreme deviation strongly suggests a partial reporting month rather than a true drop in crime. Since including this month would distort the analysis—especially the correlation—we excluded all months prior to October 2024. After filtering, the integrated dataset contains only full, reliable months.

(d) Schema and field validity

Administrative fields such as case numbers, IUCR codes, and location descriptions were not needed for analysis but were inspected for type validity. No structural corruption or mismatched schema entries were found. The dataset adheres to the Open Data Portal’s standard crime schema.

2. Quality of the Housing Price Index (HPI) Dataset

The HPI dataset is much smaller and cleaner than the crime dataset, but we evaluated it along the same dimensions.

(a) Completeness

No missing months were found within the period covered in our analysis. Each month contains exactly one HPI value, as expected for a monthly index.

(b) Format and consistency

Dates are consistently formatted in YYYY-MM-DD format, and all values represent numeric index values. No type conversion issues occurred.

(c) Range checks

HPI values fall within a narrow, expected range around 190–200 for the Chicago metro area during 2024–2025. No aberrant spikes or discontinuities were detected.

3. Quality of Integration

Because the two datasets differ fundamentally in granularity, careful integration was necessary.

(a) Temporal alignment

Daily crime data had to be converted to monthly aggregates before integration. After aggregation, both datasets shared the same temporal unit, allowing for clean merging.

(b) Overlapping months

The crime dataset covered September 2024 through August 2025, while the HPI dataset contained a broader timeline. But because September 2024 was incomplete, we selected only the overlapping complete months:

October 2024 – August 2025 (11 months).

This filtering increased coherence and prevented outliers from influencing results.

(c) Duplicate or missing keys

No duplicate months were found in either dataset after cleaning. The merged table contains exactly one row per month.

4. Anomalies and How They Were Addressed

(a) Incomplete September 2024 crime data

This was the single major anomaly. Instead of attempting imputation or partial reconstruction, we excluded the month entirely—an approach justified by the dataset’s operational monitoring nature.

(b) Small variations from reporting delays

Some crime counts may change slightly over time due to reclassification or late reporting. Our analysis used a static snapshot downloaded on a known date. This was documented in our provenance notes.

(c) No anomalies in HPI

The HPI dataset exhibited no apparent errors.

5. Overall Quality Assessment

After performing cleaning, filtering, and standardization, both datasets were assessed to be of sufficiently high quality for exploratory analysis. The integrated dataset is consistent, complete across the selected timeframe, and free from structural issues. All transformations were documented in scripts to ensure full reproducibility.

Findings

The integrated dataset covering October 2024 through August 2025 allowed us to explore how monthly crime levels and Chicago’s Housing Price Index (HPI) moved over time and whether a meaningful statistical relationship existed between them. Although the time span is relatively short, the combined data provided an opportunity to observe how two different indicators, which are public safety and economic conditions, shifted during the same period. More importantly, merging the datasets into a consistent monthly format made it possible to examine their patterns side by side instead of treating them as unrelated streams of information. Even within this limited window, several noteworthy patterns emerged from the analysis and provided a foundation for future investigations.

The first finding concerns the temporal behavior of both variables. The time-series visualization shows that crime levels experienced a steady decline from October 2024 into early 2025 before rising again throughout the spring and summer months. This pattern aligns with well-documented seasonal trends in many U.S. cities, where colder winter temperatures are typically associated with lower outdoor activity and consequently lower reported crime. By contrast, crime rates often increase as temperatures warm, which is consistent with the uptick we observed beginning around March 2025. The HPI followed a somewhat similar trajectory: after a small decline around the end of 2024, the index rose steadily from February onward. While these parallel movements do not imply causation, the similarity in timing suggests that both crime activity and housing prices may be responding to broader underlying conditions during this period, such as economic recovery patterns, shifting consumer confidence, or seasonal changes affecting population mobility.

The scatter plot with a fitted linear trendline revealed a moderate positive correlation between crime and HPI. After excluding September 2024, which is an incomplete month with abnormally low counts, the Pearson correlation coefficient for the remaining months was approximately 0.48. This indicates that months with higher housing prices tended to coincide with higher crime counts within this dataset. Although the correlation is not strong enough to justify predictive modeling or any causal claims, the fact that the two variables move in the same direction for much of the period is still meaningful. It suggests a shared influence, such as macroeconomic conditions or seasonal cycles, that affects both indicators simultaneously. Interpreting this value requires caution, especially given the short dataset, but it nonetheless demonstrates a statistically recognizable relationship.

To further clarify the structure of the crime data, we computed a three-month rolling average. This calculation smooths short-term fluctuations and reveals the underlying trajectory of the crime curve. The smoothed series shows a clear low point around January–February 2025, followed by a steady upward trend through the summer. This smoothing is especially helpful because monthly crime counts can be noisy due to policy changes, reporting inconsistencies, or short-term events. By filtering out month-to-month spikes, the rolling average highlights that the broader pattern is not random but follows a predictable seasonal rhythm. This reinforces the interpretation that the crime increase observed later in the year is part of a larger trend rather than an isolated jump.

Finally, the decision to exclude September 2024 was validated by the analysis. With only 629 reported crimes, which is far below every other month in the dataset, it was clear that the month contained incomplete reporting rather than reflecting true crime levels. Including it would have artificially distorted both the visualizations and the correlation coefficient, making the relationship appear weaker or more irregular than it actually was. Removing the data point improved the statistical coherence of the analysis and ensured that findings were based on consistent monthly information.

Overall, the findings indicate that Chicago’s crime levels and its housing price index exhibited broadly similar upward momentum in the first half of 2025. Although the correlation is modest and limited in scope, the results demonstrate the value of merging socioeconomic and public-safety indicators into a unified dataset. Even a relatively small dataset can reveal insights that are not visible when the variables are analyzed separately.

Future Work

While this project demonstrates a clear and reproducible workflow for integrating and analyzing crime and housing price data, several opportunities exist for extending and improving the analysis. The present study is intentionally scoped to fit the constraints of a course project, but expanding the dataset, refining the analytical tools, and incorporating additional perspectives would allow for more meaningful and generalizable conclusions. The ideas below outline realistic next steps that future researchers or future versions of this project could pursue.

1. Extending the Time Span

The most immediate improvement would be expanding the time coverage beyond a single year. Crime levels and housing markets often evolve along multi-year cycles shaped by broader social and economic trends. With a longer dataset, it would be possible to explore seasonal decomposition, identify recurring annual patterns, and assess whether the moderate correlation observed in this study persists consistently over time. Longer datasets would also allow for lagged analyses—for instance, whether changes in crime precede shifts in housing prices or vice versa. This type of temporal modeling is not feasible within the limited window we analyzed but would become possible with two to five years of data.

2. Adding More Crime Attributes

In this project, we aggregated all crimes into monthly totals. However, not all crime categories behave the same way. Property crimes, violent crimes, and theft may each react differently to housing market conditions. Segmenting crime data into categories could reveal relationships masked when data is aggregated. For example, property crime may correlate more strongly with economic indicators than violent crime. Implementing this extension would require additional cleaning and classification but remains well within the scope of future analysis.

3. Incorporating Additional Socioeconomic Indicators

Housing and crime do not exist in isolation. Including indicators such as unemployment rate, consumer sentiment, inflation, or mortgage rates could reveal whether broader economic changes explain the observed relationship between crime and HPI. For instance, rising interest rates might slow housing demand independently of crime patterns. Incorporating even one or two additional variables could deepen the analysis and allow for multivariate correlations instead of relying solely on pairwise comparisons.

4. Spatial Analysis

This project treats Chicago as a single aggregated unit. However, crime patterns can vary dramatically across neighborhoods. Similarly, housing markets differ between communities experiencing investment and those undergoing decline. A spatial extension could involve neighborhood-level crime counts merged with ZIP-code-level HPI data or relevant proxies. Visualizations such as heat maps or spatial clustering could uncover geographic inequalities hidden in citywide averages.

5. Causal Modeling

Although causal inference is outside the scope of this course, future work could explore whether one variable leads the other. Tools such as Granger causality tests, VAR models, or difference-in-differences could help evaluate temporal ordering or causal pathways. These methods require longer and more stable time series but could transform the preliminary correlation observed here into a more meaningful narrative about urban dynamics.

6. Improved Workflow Automation

The current workflow uses clear scripts for acquisition, integration, and analysis. Future work could incorporate full automation through Snakemake or Makefiles, enabling a single-command end-to-end run. This is especially valuable for long-term maintenance or collaborative projects where reproducibility is essential.

7. Interactive Visualization

As a final enhancement, future versions of the project could include interactive dashboards—using Plotly, Tableau, or similar tools—to allow users to explore crime and housing trends dynamically. Such tools improve communication with policymakers or community stakeholders and make the analysis more engaging and accessible.

Together, these extensions would significantly expand the scope and interpretive power of the project, transforming a semester-long assignment into a more comprehensive study of the interactions between city safety and housing market conditions.

Reproducing the Workflow

This section provides a complete sequence of steps required for any user or grader to reproduce our results from scratch. The workflow is fully scripted, and all operations—from data acquisition to integration, analysis, and visualization—can be repeated without modification as long as the directory structure is preserved.

1. Clone the Repository

git clone <your_repository_url>

cd Muqi-and-Chenyu-Course-Project

Ensure that the folder structure includes the following directories:

data/raw/

data/processed/

results/

results/figures/

scripts/

2. Set Up the Python Environment

We recommend using a virtual environment to ensure dependency isolation:

python3 -m venv .venv

source .venv/bin/activate # macOS/Linux

# or .venv\Scripts\activate # Windows PowerShell
 
Install required packages:

pip install pandas numpy matplotlib
 
3. Download Raw Data

Because the original datasets contain redistribution restrictions, raw files are not included in the repository.

Users must manually download them and place them into the correct folder.

(a) Chicago Crime Dataset

Download from:

https://data.cityofchicago.org/Public-Safety/DM1-Crime-data-set-chicago/55jb-nki6/about_data

Place the CSV into:

data/raw/DM1_Crime_data_set_chicago_20251007.csv
 
(b) Chicago Housing Price Index (HPI)

Download from FRED:

https://fred.stlouisfed.org/series/CHXRHTNSA

Save the file as:

data/raw/CHXRHTNSA.csv
 
4. Run Preprocessing Scripts

(a) Prepare Crime Data

python scripts/prepare_crime_data.py

This script:

- Parses timestamps
- Normalizes columns
- Aggregates crime counts to monthly totals
- Saves output to:
data/processed/crime_monthly.csv
 
(b) Prepare HPI Data

python scripts/prepare_hpi_data.py
 
Output saved to:

data/processed/hpi_monthly.csv
 
5. Integrate the Two Datasets

python scripts/integrate_crime_hpi.py
 
This generates the combined dataset:

data/processed/crime_hpi_monthly.csv
 
6. Run the Analysis Pipeline

python scripts/analyze_crime_hpi.py
 
This will produce:

results/figures/crime_hpi_timeseries_filtered.png

results/figures/crime_hpi_scatter_filtered.png

results/figures/crime_count_rolling3.png

results/crime_hpi_summary.csv
 
These represent the final outputs used in the Findings section of the report.
 
7. Access Box-hosted Final Outputs

The project includes a Box folder containing processed artifacts that cannot be uploaded due to redistribution constraints.
 
Users should download the folder and place its contents under:

data/raw/ (for raw data)

data/processed/ (for intermediate results)
 
8. Reproduce Entire Workflow

Once all data are in place, the entire workflow can be reproduced by running:

python scripts/prepare_crime_data.py

python scripts/prepare_hpi_data.py

python scripts/integrate_crime_hpi.py

python scripts/analyze_crime_hpi.py
 
The results will be regenerated exactly—including figures and summary tables.
 
References

City of Chicago. (2025). DM1 Crime data set Chicago. City of Chicago Open Data Portal.Retrieved October 7, 2025, from https://data.cityofchicago.org/Public-Safety/DM1-Crime-data-set-chicago/55jb-nki6/about_data

Federal Reserve Bank of St. Louis. (2025). FRED® API Documentation and Terms of Use. Retrieved October 7, 2025, from https://fred.stlouisfed.org/docs/api/fred/

Python Software Foundation. (2025). Python (Version 3.11) [Software].
https://www.python.org/

Microsoft Corporation. (2025). Visual Studio Code (Version 1.xx) [Software].
https://code.visualstudio.com/
