# Personal Health Data Analysis

Welcome to the **Personal Health Data Analysis** repository. This project is dedicated to understanding how various personal health metrics—specifically daily weight, step counts, gym attendance, and calorie intake—interact over time. By examining these variables, we aim to uncover insights that can help maintain or improve overall health and fitness.

In this repository, you will find:

- **`data_process.ipynb`**: Notebook focusing on data cleaning, feature engineering, handling missing values, and preparing the dataset for analysis.  
- **`data_analysis.ipynb`**: Notebook providing exploratory data analysis (EDA), statistical tests, correlations, and machine learning models to address key research questions.  
- **`data_visualization.ipynb`**: Notebook containing detailed plots, charts, and interactive visualizations to illustrate the dataset’s trends and findings.  

---

## Table of Contents

- **[Motivation](#motivation)**  
- **[Main Research Questions](#main-research-questions)**  
  - [Calorie Intake and Weight Changes](#calorie-intake-and-weight-changes)  
  - [Physical Activity and Weight Management](#physical-activity-and-weight-management)  
  - [Interplay Between Calorie Intake and Physical Activity](#interplay-between-calorie-intake-and-physical-activity)  
  - [Temporal Patterns and Long-Term Trends](#temporal-patterns-and-long-term-trends)  
- **[Tools](#tools)**  
- **[Data Source](#data-source)**  
  - [Format](#format)  
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

---

## Motivation
- **I have been tracking my weight, daily step counts, gym visits, and calorie intake** to better understand how these factors are influencing my body weight and overall fitness.
- **By performing statistical analyses and visualizing trends**, I hope to identify correlations or patterns that can guide healthier lifestyle choices.
- **Combining these variables into a single dataset** allows for a more holistic perspective on daily habits and how they affect health outcomes.

---

## Main Research Questions

### Calorie Intake and Weight Changes
- **How does daily calorie intake correlate with fluctuations in body weight?**  
- **Are there specific calorie-consumption patterns that precede weight gain or loss?**

### Physical Activity and Weight Management
- **What is the relationship between daily step counts and changes in weight?**  
- **Does higher physical activity, reflected in greater step counts, lead to measurable weight loss or maintenance?**

### Interplay Between Calorie Intake and Physical Activity
- **How do calorie intake and step counts, when considered together, influence weight changes over time?**  
- **Which combinations of calorie consumption and physical activity appear optimal for weight management?**

### Temporal Patterns and Long-Term Trends
- **Are there seasonal or day-of-the-week effects on calorie intake, step counts, or weight changes?**  
- **How do these metrics evolve over a longer period, and do certain habits emerge repeatedly?**

---

## Tools
- **Pandas** – Used for reading data, cleaning and merging datasets, and general DataFrame manipulations.  
- **NumPy** – Provides numerical operations, array handling, and essential math functions.  
- **Matplotlib and Seaborn** – Primary libraries for creating static plots (line plots, scatter plots, bar plots, histograms, etc.).  
- **Altair** – Enables interactive and dynamic visualizations, allowing for filter widgets and selection tools.  
- **Scipy** – Offers statistical methods and hypothesis testing (e.g., T-tests, correlations).  
- **Statsmodels** – Provides advanced statistical modeling (e.g., linear regression, logistic regression).  
- **Scikit-learn** – Used for additional machine learning models (e.g., regression, random forest).

---

## Data Source
- **Personal weight** measured daily with a digital scale (units: kilograms).  
- **Step count** extracted from the health program which is embedded in iphone device.  
- **Gym attendance** manually labeled as “Yes” or left blank for non-attendance.  
- **Calorie (kcal)** intake logged through a calorie-counting application (manual data entry).

### Format
- **Days** – The day of the week (e.g., Monday, Tuesday).  
- **Weight(kg)** – Daily body weight, in kilograms.  
- **Step_count** – Number of steps taken each day.  
- **Gym** – Indicates gym session with “Yes” or “No.”  
- **Calorie(kcal)** – Total daily calorie intake, measured in kilocalories (kcal).

---

## Data Processing
- **Data Cleaning**  
  - **Removed** or **imputed missing values** for steps or calories if records were incomplete.  
  - **Standardized** the “Gym” field by converting blanks to “No” for consistency.
- **Feature Engineering**  
  - **Generated new columns** like 7-day rolling averages for steps or weight.  
  - **Computed** day-to-day weight changes to track short-term fluctuations.
- **Time-Series Alignment**  
  - **Ensured** each row represented a single calendar day.  
  - **Checked** for out-of-order dates, duplicates, or incorrect day labels.

---

## Data Visualizations
- **Line Charts**  
  - **Show** daily trends in weight, step counts, or calories over time.  
  - **Highlight** variations on specific days (weekends vs. weekdays).
- **Scatter Plots**  
  - **Plot** weight vs. calorie intake, color-coded by gym attendance.  
  - **Examine** relationships among multiple variables (e.g., step count, weight, and calories).
- **Interactive Dashboards**  
  - **Enable** the user to filter data by minimum step counts or calorie ranges.  
  - **Refine** the visual output dynamically to see how subgroups of the data differ.
- **Histograms**  
  - **Visualize** the distribution of daily step counts or calorie intake.  
  - **Identify** common daily activity or dietary ranges.

---

## Data Analysis

### Weight Changes
- **Explored** short-term vs. long-term weight fluctuations.  
- **Calculated** rolling averages and daily/weekly differences to see if weight followed specific patterns.

### Step Counts and Physical Activity
- **Analyzed** how step count distributions shift over time.  
- **Investigated** whether certain step count thresholds corresponded to stable or decreasing weight.

### Gym Attendance
- **Examined** gym vs. non-gym days for differences in average weight, calorie intake, and step counts.  
- **Performed** T-tests or group comparisons to check if there was a significant effect on daily weight changes.

### Calorie Intake
- **Measured** average, minimum, and maximum daily calorie intakes.  
- **Correlated** daily calorie data with weight changes, including day-lag effects (e.g., if high-calorie days preceded weight gains).

---

## Findings

### Daily Weight Trends
- **Observed** moderate fluctuations of ~1-2 kg around a central trend.  
- **Noted** occasional spikes in weight following calorie-dense weekends or lower activity periods.

### Correlation Insights
- **Highlighted** potential moderate positive correlation between calorie intake and weight (indicating higher caloric days might align with higher weight).  
- **Revealed** that high step counts alone did not strongly correlate with rapid weight loss, suggesting a multifactor approach (calorie intake + steps + gym) is needed.

---

## Limitations

### Data Limitations
- **Small sample size** – The dataset covers only a limited timeframe, which may not capture longer-term patterns.  
- **Potential inaccuracies** in manual logging of calories and gym attendance.

### Personal Limitations
- **Individual metabolism** – Weight changes can be influenced by genetic factors, hydration, or untracked factors (e.g., stress, sleep).  
- **Self-reporting bias** – Calorie logging may be off due to estimation errors.

---

## Future Work
- **Extended Data Collection**  
  - **Gather** data over more months or years to strengthen findings and minimize short-term anomalies.  
  - **Record** additional health metrics such as water intake, sleep duration, or heart rate.
- **Advanced Modeling**  
  - **Employ** multi-variate time-series techniques for forecasting weight changes.  
  - **Explore** machine learning methods (e.g., Random Forest, Gradient Boosting) to predict days of potential weight gain based on calorie and activity inputs.
- **Integration**  
  - **Combine** external factors such as weather or stress levels to see how they impact physical activity or eating habits.

---

**Thank you for visiting the Personal Health Data Analysis project.**  
Please refer to the individual notebooks (`data_process.ipynb`, `data_analysis.ipynb`, and `data_visualization.ipynb`) for the complete workflow, visual examples, interactive charts, and machine learning models used in this analysis. If you have any questions or suggestions, feel free to open an issue or submit a pull request!
