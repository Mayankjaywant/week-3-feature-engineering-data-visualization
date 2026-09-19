# Week 3 – Feature Engineering and Data Visualization

## Internship Task
This repository contains the Week 3 work for **Feature Engineering and Data Visualization** in the context of digital governance and public digital services.

### Objective
- Explore service-performance data.
- Create meaningful derived features.
- Visualize distributions, relationships, and service-level trends.
- Connect data patterns with digital-service performance.

## Repository Structure
```text
week-3-feature-engineering-data-visualization/
│
├── sample_digital_services.csv
├── engineered_digital_services.csv
├── feature_engineering_visualization.py
├── requirements.txt
├── README.md
└── visualizations/
    ├── processing_days_distribution.png
    ├── digital_adoption_vs_satisfaction.png
    └── resolution_rate_by_service.png
```

## Features Created
1. **resolution_rate_pct** = resolved requests / total requests × 100
2. **requests_per_staff** = total requests / staff count
3. **service_efficiency_score** = combined indicator using resolution rate, satisfaction, digital adoption, and processing time

## Visualizations
- Histogram: processing-time distribution
- Scatter plot: digital adoption vs citizen satisfaction
- Bar chart: average resolution rate by service

## Important Note
The included CSV is a **demonstration dataset created for the task**. If the internship provides an official dataset, replace the CSV and rerun the script while keeping the same feature-engineering logic where appropriate.

## Run
```bash
pip install -r requirements.txt
python feature_engineering_visualization.py
```
