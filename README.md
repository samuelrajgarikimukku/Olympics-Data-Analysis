# Olympic Games Data Analysis Application

This repository contains an end-to-end data analysis and visualization application built on historical Olympic Games data. The project focuses on transforming raw athlete-level data into structured analytical outputs and presenting them through an interactive web interface.

The application is designed to support exploratory analysis of participation trends, medal distributions, country performance, and athlete characteristics across Summer Olympic Games.

## Project Overview
The project uses publicly available Olympic datasets to build a clean analytical pipeline and an interactive dashboard. The system is divided into three clear layers:
1. Data preprocessing and feature preparation
2. Analytical and aggregation logic
3. Interactive visualization and user interface

This structure allows the same dataset to be reused across multiple analytical views without duplicating logic.

## Dataset Description
The project uses two primary datasets:
- **athlete_events.csv** \
Contains athlete-level records including name, age, sex, height, weight, sport, event, year, city, and medal information.
- **noc_regions.csv** \
Maps National Olympic Committee (NOC) codes to country or region names.

Only Summer Olympics data is retained for analysis.

## Data Preprocessing
The preprocessing stage prepares raw data for reliable analysis.
Key steps include:
- Filtering records to Summer Olympics only
- Merging athlete data with region information using NOC codes
- Removing duplicate rows to prevent double counting
- One-hot encoding medal outcomes (Gold, Silver, Bronze) for aggregation.

This logic is implemented in preprocessor.py and produces a clean dataframe that serves as the base for all analysis.

## Analytical Capabilities

All analytical computations are implemented in a dedicated helper module to keep the application modular and maintainable.

**Medal Tally Analysis**
- Overall medal tally by country
- Medal tally filtered by specific Olympic year
- Country-specific medal performance across all years
- Computation of gold, silver, bronze, and total medals

**Overall Olympic Trends**
- Number of participating nations over time
- Number of events over time
- Number of athletes over time
- Heatmap showing event counts per sport across Olympic editions
- Identification of most successful athletes by medal count

**Country-wise Analysis**
- Year-wise medal trends for a selected country
- Heatmap of sports where a country has won medals
- Top athletes from a country based on medal count

**Athlete-wise Analysis**
- Age distribution of all athletes and medalists
- Age distribution of gold medalists across major sports
- Height vs weight analysis, segmented by medal type and gender 
- Gender participation trends (men vs women) over Olympic history

All aggregations handle duplicates carefully to ensure statistical correctness.

## Application Interface

The interactive dashboard is built using Streamlit.

Features include:
- Sidebar-based navigation between analysis modes
- Dropdown filters for year, country, and sport
- Dynamic charts and tables that update based on user selection
- Combination of tabular views, line charts, heatmaps, distributions, and scatter plots

The main application logic is implemented in app.py.

## Visualizations Used

The project uses multiple visualization libraries based on the type of insight required:

- **Plotly Express** for interactive line charts
- **Matplotlib and Seaborn** for heatmaps and scatter plots
- **Plotly Figure Factory** for distribution plots

## Screenshots and Application Outputs
Add screenshots of the running application here.

-  Application Home / Sidebar Navigation
  -  (Insert screenshot here)
- Medal Tally View
  - (Insert screenshot here)
- Overall Analysis – Trends and Heatmaps
  - (Insert screenshot here)
- Country-wise Analysis
  - (Insert screenshot here)
- Athlete-wise Analysis
  - (Insert screenshot here)

## Project Structure
```
.
├── app.py                # Streamlit application entry point
├── preprocessor.py       # Data cleaning and preprocessing logic
├── helpper.py            # Analytical and aggregation functions
├── requirements.txt      # Project dependencies
├── data/
│   ├── athlete_events.csv
│   ├── noc_regions.csv
│   └── image.jfif
```

## Installation and Setup

1. Clone the repository
2. Create and activate a virtual environment
3. Install dependencies
```python
pip install -r requirements.txt
```
4. Run the application
```python
streamlit run app.py
```

## Deployment

The application is deployed on Render and is accessible as a hosted web application.
The deployed version allows users to explore the full analytical functionality without running the project locally.

Live Application: <[Olympic Data Analysis](https://olympics-data-analysis-2-21z9.onrender.com/)>

## Technical Scope and Outcomes

This project demonstrates:

- Practical data cleaning and preprocessing on real-world datasets
- Reliable aggregation and analytical logic using pandas
- Modular code organization for analytics projects
- Development of an interactive analytical dashboard
- Use of multiple visualization techniques to communicate insights

The application serves as a reusable foundation for exploratory sports analytics and similar data-driven dashboards.
