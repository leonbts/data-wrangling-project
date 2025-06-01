# SpaceX Launch Analysis

## Project Overview

This project analyzes SpaceX launch data using the SpaceX API to explore patterns, success rates, and payload characteristics. The analysis also includes launch site information to provide regional context. The goal is to uncover insights about launch success factors and trends over time.

## Installation

1. Clone the repository:
   ```bash
   git clone https://github.com/yourusername/spacex-launch-analysis.git
   cd spacex-launch-analysis
   ```
2. Install the required Python packages:
   ```bash
   pip install -r requirements.txt
   ```

## Usage

- The main exploratory analysis is performed in the `notebooks/eda.ipynb` Jupyter notebook.
- Python source files with data fetching and cleaning functions are located in the `src/` directory.
- To fetch fresh data from the SpaceX API, run the API handler functions in `src/api_handler.py`.
- Data cleaning and preparation functions can be found and used from `src/cleaning.py`.

## Data Sources

- **SpaceX API** (https://api.spacexdata.com/v4/launches) — Provides launch, payload, rocket, and launchpad data.
- Additional data about launch sites was merged for enhanced analysis.

## Summary of Analyses

- Data wrangling and cleaning performed on SpaceX launch and launchpad data.
- Exploratory Data Analysis (EDA) included:
  - Launch success rate trends over time
  - Success rate by rocket type
  - Payload mass correlation with success
  - Launch sites and their regional success rates
- Hypothesis testing performed to examine relationships between payload/orbit categories and launch success, with results indicating no significant dependency.

## Repository Structure

├── data/ # Contains the datasets as CSV files (if needed)
├── notebooks/ # Jupyter notebooks for analysis
│ └── eda.ipynb
├── src/ # Source code for API handling and data cleaning
│ ├── api_handler.py
│ └── cleaning.py
├── .gitignore
├── README.md
└── requirements.txt

## Acknowledgments

- SpaceX API for providing comprehensive launch data.
- Public data sources merged to enhance the analysis.