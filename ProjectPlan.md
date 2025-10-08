IS 477 Project Plan
Team number : Chenyu Wang & Muqi Su

Overview
The overall goal of our project is to examine how housing prices and crime rates in Chicago are related over time. By combining two open datasets — the Chicago Police Department’s crime data and the Chicago Home Price Index (HPI) from the Federal Reserve Bank of St. Louis (FRED) — we aim to identify whether changes in housing prices correspond to shifts in public safety.
This project will apply concepts from IS477 such as data collection, integration, and responsible data handling. Through this work, we hope to understand how different types of data (economic and social) can be merged to reveal urban patterns and inform data-driven insights about city life.
Research Questions
Do changes in the Chicago housing price index correlate with monthly variations in crime rates?
Are specific categories of crimes (such as property crimes) more affected by fluctuations in housing prices?
How can integrating economic and social datasets improve our understanding of urban conditions and community well-being?
Team
Our team consists of two members, Chenyu Wang and Muqi Su, who will share responsibilities across research, data integration, and technical implementation.
Chenyu Wang will lead the research and documentation part of the project, including designing research questions, gathering background information, interpreting results, and compiling the final written report. Chenyu Wang will also be responsible for integrating the two datasets once they have been cleaned and aligned.
Muqi Su will focus on the technical implementation. This includes downloading and processing the data through the FRED API and the Chicago Open Data Portal, cleaning and organizing the data in Python, and writing code to join and analyze the datasets. Muqi Su will also create visualizations and assist with preparing the final presentation.
Both team members will work together on project design, result interpretation, and presentation delivery.

Datasets
This project will use two publicly available datasets that represent different but related aspects of life in Chicago: crime incidents and housing prices. By integrating these two data sources, we aim to examine how changes in economic conditions may relate to public safety trends.
The first dataset comes from the City of Chicago Open Data Portal, provided by the Chicago Police Department. It contains detailed records of reported crime incidents within the city over the past year, excluding murders where victim-level data are available separately. Each record includes attributes such as the type of offense, date and time, block-level location (with full addresses masked for privacy), and case status. The data are extracted from the CPD’s CLEAR (Citizen Law Enforcement Analysis and Reporting) system and updated daily from Tuesday through Sunday. The dataset currently includes more than 65,000 records and can be downloaded as a CSV file from the City of Chicago’s official open data site.
This dataset will be used to calculate monthly crime totals and to categorize crimes (for example, violent, property, or other offenses) in order to make them comparable with housing price data. It will serve as the social indicator in our analysis.
(Source: City of Chicago Open Data Portal, “DM1 Crime data set Chicago.” https://data.cityofchicago.org/Public-Safety/DM1-Crime-data-set-chicago/55jb-nki6/about_data)
The second dataset is the Home Price Index (HPI) for Chicago, retrieved from the Federal Reserve Bank of St. Louis (FRED) database. Specifically, we use the S&P CoreLogic Case-Shiller Home Price Index for Chicago (series ID: CHXRHTNSA), which provides monthly measures of housing price changes in the Chicago metropolitan area. The dataset is accessible through the FRED API and can be downloaded in CSV format. It represents an economic indicator of market value fluctuations in residential properties. We will use this dataset to observe how average housing prices change over time and compare those trends with the aggregated monthly crime data.
According to the FRED Terms of Use, the data are freely available for personal, educational, and non-commercial use, as long as proper attribution is included and no endorsement by FRED is implied.
(Source: Federal Reserve Bank of St. Louis, FRED® API Documentation. https://fred.stlouisfed.org/docs/api/fred/)
Together, these two datasets provide complementary views of urban life in Chicago: one from an economic perspective and one from a social perspective. Integrating them will allow us to explore whether there are meaningful connections between city-level housing price trends and crime activity patterns over time.

Project Timeline
The project will follow the class schedule. During Week 7, we will finalize the topic and datasets. In Week 8, we will complete and submit the project plan. Weeks 9 and 10 will be used for downloading, cleaning, and preparing the data. Week 11 will focus on integrating the datasets by month and checking for consistency. Weeks 12 and 13 will be dedicated to analysis, correlation testing, and visualization. Finally, in Weeks 14 and 15, we will revise our report and submit the final deliverables along with a class presentation.

Constraints
One of the main constraints of this project is the granularity mismatch between the two datasets. The Chicago crime dataset provides highly detailed, case-level data with daily timestamps and neighborhood-level locations, while the housing price index (HPI) data from FRED are reported only at the monthly level and represent an aggregate measure for the entire Chicago metropolitan area. To integrate them meaningfully, we must aggregate the crime data by month, which may result in some loss of detail and variability.
Another constraint concerns data completeness and reporting accuracy. The City of Chicago dataset may contain delayed or reclassified cases due to ongoing investigations, and the FRED HPI data are subject to revisions by the data provider. As a result, both sources might include minor discrepancies over time.
A technical constraint is that some API calls and large CSV downloads require stable internet access and local storage capacity, which may limit performance during integration and testing. Finally, this project is limited to publicly available and non-personally identifiable data, which restricts the scope of socioeconomic or demographic variables that could otherwise enhance the analysis.

Gaps
At this early stage, there are several gaps that will require further input as we progress through later course topics:
First, we need to deepen our understanding of data integration techniques — particularly how to handle differences in frequency (daily vs. monthly) and how to structure the resulting integrated dataset efficiently in a relational format. We will likely revisit this after completing the Data Integration and Storage Organization modules.
Second, we currently plan to use basic statistical correlation to test relationships between housing prices and crime counts. However, as the course progresses, we may learn new methods such as regression analysis, data normalization, or multi-source schema design, which could refine our approach.
Third, there may be a gap in contextual interpretation: even if we find correlations, it will be important to understand external factors (for example, seasonality, policy changes, or socioeconomic trends) that may influence both housing prices and crime rates. Additional research or external datasets (such as population or unemployment data) could be added later if time permits.
Lastly, we anticipate needing instructor or TA feedback on whether our integration design and visualization methods align with IS477 project expectations — especially once we begin implementing joins and data cleaning pipelines.

References
City of Chicago. (2025). DM1 Crime data set Chicago. City of Chicago Open Data Portal. Retrieved October 7, 2025, from https://data.cityofchicago.org/Public-Safety/DM1-Crime-data-set-chicago/55jb-nki6/about_data
Federal Reserve Bank of St. Louis. (2025). FRED® API Documentation and Terms of Use. Retrieved October 7, 2025, from https://fred.stlouisfed.org/docs/api/fred/

