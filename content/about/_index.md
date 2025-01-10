---
title: "About the Project"
---


Welcome to the **Personal Health Data Analysis** website. This project is dedicated to understanding how various personal health metrics—specifically daily weight, step counts, gym attendance, and calorie intake—interact over time. By examining these variables, we aim to uncover insights that can help maintain or improve overall health and fitness.


---

## Table of Contents
- **[Motivation](#motivation)**
- **[Main Research Questions](#main-research-questions)**
- **[Tools](#tools)**
- **[Data Source](#data-source)**
- **[Data Processing](#data-processing)**
- **[Data Visualizations](#data-visualizations)**
- **[Data Analysis](#data-analysis)**
- **[Findings](#findings)**
- **[Limitations](#limitations)**
- **[Future Work](#future-work)**

---

## Motivation
- I have been tracking my weight, daily step counts, gym visits, and calorie intake to better understand how these factors are influencing my body weight and overall fitness.

- By performing statistical analyses and visualizing trends, I hope to identify correlations or patterns that can guide healthier lifestyle choices.

- Combining these variables into a single dataset allows for a more holistic perspective on daily habits and how they affect health outcomes.

---

## Main Research Questions
### Calorie Intake and Weight Changes
- How does daily calorie intake correlate with body weight fluctuations?
- Are there calorie patterns linked to weight gain or loss?

### Physical Activity and Weight Management
- What is the relationship between step counts and weight management?
- Does higher physical activity lead to measurable weight maintenance or loss?

### Interplay Between Calorie Intake and Physical Activity
- How do calorie intake and step counts together influence weight changes?
- Which activity and calorie combinations promote optimal weight management?

### Temporal Patterns and Long-Term Trends
- Are there seasonal or weekly variations in calorie intake, step counts, or weight changes?
- Do long-term trends reveal consistent habits?

---

## Tools
- **Pandas**: Used for reading data, cleaning and merging datasets, and general DataFrame manipulations.
- **NumPy**: Provides numerical operations, array handling, and essential math functions.
- **Matplotlib & Seaborn**: Primary libraries for creating static plots (line plots, scatter plots, etc.)
- **Altair**: Enables interactive and dynamic visualizations, allowing for filter widgets and selection tools.
- **SciPy & Statsmodels**: Offers statistical methods and hypothesis testing (e.g., T-tests, correlations) and provides advanced statistical modeling
- **Scikit-learn**: Used for additional machine learning models (e.g., regression, random forest).

---

## Data Source
- **Weight**: Daily measurements using a digital scale (kg).
- **Step Count**: Extracted from the Apple Health app.
- **Gym Attendance**: Manually logged (Yes/No).
- **Calorie Intake**: Logged via MyFitnessPal (kcal).

### Data Format
- **Days**: Day of the week.
- **Weight (kg)**: Daily body weight.
- **Step Count**: Number of steps taken.
- **Gym Attendance**: Recorded as 'Yes' or left blank.
- **Calorie Intake (kcal)**: Total daily calorie intake.

---

## Data Processing
- **Data Cleaning**: Addressing missing values and standardizing data.
- **Feature Engineering**: Creating rolling averages and weight fluctuations.
- **Time-Series Alignment**: Ensuring consistent chronological data.

---

## Data Visualizations
- **Line Charts**: Daily trends in weight, step counts, and calorie intake.
- **Scatter Plots**: Visualizing variable correlations.
- **Interactive Dashboards**: Filterable plots for deeper insights.
- **Histograms**: Distribution of activity and intake data.

---

## Data Analysis
### Weight Changes
- Short-term vs. long-term weight fluctuations.
- Calculated rolling averages and weight differences.

### Step Counts and Physical Activity
- Step count distributions over time.
- Step count thresholds for weight stability.

### Gym Attendance
- Differences in weight and calorie intake between gym and non-gym days.

### Calorie Intake
- Analyzing average calorie intake and correlations with weight changes.

---

## Findings
### Daily Weight Trends
- Observed moderate fluctuations of ~1-2 kg around a central trend.
- Noted occasional spikes in weight following calorie-dense weekends or lower activity periods.

### Correlation Insights
- Highlighted potential moderate positive correlation between calorie intake and weight (indicating higher caloric days might align with higher weight).
- Revealed that high step counts alone did not strongly correlate with rapid weight loss, suggesting a multifactor approach (calorie intake + steps + gym) is needed.

---

## Limitations
### Data Limitations
- Small sample size and potential inaccuracies in manual logging.

### Personal Limitations
- Factors like genetics, hydration, and self-reporting bias.
- Self-reporting bias – Calorie logging may be off due to estimation errors.

---

## Future Work
- **Extended Data Collection**: Long-term monitoring and additional health metrics.
- **Advanced Modeling**: Implementing multivariate time-series forecasting.
- **Integration**: Including external factors like stress and sleep quality.

---

**Thank you for exploring the Personal Health Data Analysis project.**

Refer to the notebooks for detailed workflows and findings. Contributions and feedback are welcome!
