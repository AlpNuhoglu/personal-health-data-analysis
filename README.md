# Personal Health Data Analysis

## Description

This project will be an analysis of my own personal health data, focusing on daily weight measurements, step counts, gym visits, and calorie intake. The goal is to gain insights into how these variables interact with one another and affect my overall health and fitness.

## Table of Contents

- **[Motivation](#motivation)**  
- **[Main Research Questions](#main-research-questions)**  
  - [Calorie Intake and Weight Changes](#calorie-intake-and-weight-changes)  
  - [Physical Activity and Weight Management](#physical-activity-and-weight-management)  
  - [Interplay Between Calorie Intake and Physical Activity](#interplay-between-calorie-intake-and-physical-activity)  
  - [Temporal Patterns and Long-Term Trends](#temporal-patterns-and-long-term-trends)
- **[Tools](#tools)**  
- **[Data Source](#data-source)**  
- **[Data Processing](#data-processing)**  
- **[Data Visualizations](#data-visualizations)**  
- **[Data Analysis](#data-analysis)**  
  - [Weight Changes](#weight-changes)  
  - [Step Counts and Physical Activity](#step-counts-and-physical-activity)  
  - [Gym Attendance](#gym-attendance)  
  - [Calorie Intake](#calorie-intake)
- **[Findings](#findings)**  
  - [Daily Weight Trends](#daily-weight-trends)  
  - [Correlation Insights](#correlation-insights)
- **[Limitations](#limitations)**  
  - [Data Limitations](#data-limitations)  
  - [Personal Limitations](#personal-limitations)
- **[Future Work](#future-work)**  

## Motivation

I have been tracking my weight, daily steps, gym attendance, and calorie intake to better understand how these factors are influencing my body weight and overall fitness. By analyzing this dataset, I hope to identify patterns, correlations, and potential areas for improvement to maintain a healthier lifestyle.

## Main Research Questions

### Calorie Intake and Weight Changes
- **How does my daily calorie intake correlate with fluctuations in my body weight?**
- **Are there specific patterns or trends in calorie consumption that precede weight gain or loss?**

### Physical Activity and Weight Management
- **What is the relationship between my daily step count and changes in my weight?**
- **Does increased physical activity (as measured by steps) significantly contribute to weight loss or maintenance?**

### Interplay Between Calorie Intake and Physical Activity
- **How do calorie intake and step count interact to influence my weight over time?**
- **Can we identify optimal combinations of calorie consumption and physical activity that promote healthy weight management?**

### Temporal Patterns and Long-Term Trends
- **Are there any seasonal or temporal trends in my data that affect calorie intake, step count, or weight?**
- **How have my health metrics evolved over the duration of data collection?**

## Tools

- **Jupyter Notebook** for exploratory data analysis and documentation.  
- **Pandas** for data cleaning, filtering, and merging.  
- **Matplotlib** and **Seaborn** for creating visualizations.  
- **Numpy** for mathematical operations.  
- **Scipy** for statistical analysis.

## Data Source

The data was collected manually and with the help of mobile applications.  
- **Weight (kg):** Recorded using a digital scale each morning.  
- **Step Count:** Logged via a wearable fitness device or smartphone.  
- **Gym Attendance:** Manually noted (“Yes” if a session was completed, otherwise blank).  
- **Calorie (kcal):** Tracked using a calorie-counting app.  

### Format

The dataset includes the following columns:

1. **Days** – The day of the week.  
2. **Weight(kg)** – Daily weight measurement in kilograms.  
3. **Step_count** – Number of steps taken each day.  
4. **Gym** – Indicates whether there was a gym session or not.  
5. **Calorie(kcal)** – Total calories consumed that day.

## Data Processing

- **Data Cleaning:** Handled any missing values, inconsistencies, and typographical errors.  
- **Feature Engineering:** Created additional features or adjusted existing ones to facilitate analysis (e.g., day grouping, rolling averages).  
- **Date Handling:** Aligned the records with calendar dates to ensure consistency for time-series analyses.

## Data Visualizations

- Plots such as line charts, bar charts, and scatter plots to show trends in weight, step counts, and calories over time.  
- Comparative visuals to see differences in days with gym attendance vs. non-gym days.  
- Heatmaps or correlation plots to understand relationships between variables (weight, steps, calorie intake).

## Data Analysis

### Weight Changes
Explore fluctuations in daily weight to identify possible patterns, such as trends following periods of high or low calorie intake or changes after gym days.

### Step Counts and Physical Activity
Analyze how daily step counts vary and whether reaching certain thresholds correlates with stable or reduced weight.

### Gym Attendance
Compare gym vs. non-gym days to see if there's a noticeable difference in calorie consumption or average weight changes on days with workouts.

### Calorie Intake
Investigate the range, average, and distribution of daily calorie intake and see if there are direct effects on short-term weight changes.

## Findings

### Daily Weight Trends
Summarize how the weight has changed day-to-day, including any noticeable spikes or drops.

### Correlation Insights
Highlight any strong correlations discovered, for instance between step counts and weight or calorie intake and weight fluctuations.

## Limitations

### Data Limitations
- Small sample size covering only a limited period.  
- Potential inaccuracies in manual data entry.

### Personal Limitations
- Individual body composition and metabolism can vary.  
- Other untracked factors (e.g., sleep, stress) may also affect weight.

## Future Work

- **Extended Data Collection:** Gather more data for improved reliability of insights.  
- **Incorporate Additional Variables:** Track other fitness-related metrics (e.g., sleep quality, workout intensity).  
- **Advanced Analysis Techniques:** Apply machine learning models for predictive insights on weight changes or calorie targets.
