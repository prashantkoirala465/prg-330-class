**PYTHON DATA ANALYSIS LAB**

**Student Performance Dataset**

|  |
| :---- |

1\. What you will learn

* Load a CSV file into a pandas DataFrame.  
* Inspect columns, data types, ranges and basic statistics.  
* Find and handle missing values.  
* Detect duplicate records and repeated StudentID values.  
* Find values that are outside a sensible range.  
* Create useful derived columns.  
* Use filtering, sorting, groupby() and aggregation.  
* Measure relationships between study behaviour and final performance.  
* Create simple charts with pandas/matplotlib.  
* Export a cleaned dataset and a small analysis report.

# **2\. Meet the dataset**

The file used in this lab is student\_performance\_updated\_1000.csv. It contains 1,000 student records and 12 columns. The dataset deliberately contains problems so that you can practice the same checks they would perform before using data in a real project.

| Column | What it represents |
| :---- | :---- |
| **StudentID** | Student identifier; contains missing and repeated IDs |
| **Name** | Student name; contains missing values |
| **Gender** | Male/Female; contains missing values |
| **AttendanceRate** | Attendance measure; mostly in a 70–95 range |
| **StudyHoursPerWeek** | Weekly study hours; contains missing values |
| **PreviousGrade** | Previous academic grade |
| **ExtracurricularActivities** | Number of activities |
| **ParentalSupport** | Low / Medium / High |
| **FinalGrade** | Final academic grade |
| **Study Hours** | Daily study-hours field; includes missing and negative values |
| **Attendance (%)** | Attendance percentage; includes missing and impossible values above 100 |
| **Online Classes Taken** | Boolean-like True/False field; contains missing values |

|  |
| :---- |

# **Module 1 — Load and inspect the data**

## **1 Import pandas**

| import pandas as pd |
| :---- |

| What this doespandas is imported with the short name pd. The alias is a convention used in most pandas examples, so commands such as pd.read\_csv() are easier to type. |
| :---- |

## **2 Read the CSV file**

| df \= pd.read\_csv("student\_performance\_updated\_1000.csv") |
| :---- |

| What this doesread\_csv() reads the CSV file and creates a DataFrame. The variable df is simply the name we give to that DataFrame. |
| :---- |

## **3 Look at the first records**

| df.head() |
| :---- |

| What this doeshead() shows the first five rows by default. It is a quick way to check whether the file loaded correctly and whether the column names look sensible. |
| :---- |

## **4 Check the shape**

| df.shape |
| :---- |

| What this doesshape returns a tuple: (number of rows, number of columns). For this file the starting shape is (1000, 12). |
| :---- |

## **5 Check column names**

| df.columns |
| :---- |

| What this doescolumns returns the labels used by the DataFrame. This is useful before writing filters or selecting specific columns. |
| :---- |

## **6 Check data types**

| df.dtypes |
| :---- |

| What this doesdtypes tells you how pandas currently stores each column. For example, names are object/string-like, while numeric columns are stored as floating-point numbers. |
| :---- |

## **7 Get a compact overview**

| df.info() |
| :---- |

| What this doesinfo() combines useful structural information: row count, column names, non-null counts and data types. It is one of the first commands to run when receiving an unfamiliar dataset. |
| :---- |

## **8 Basic statistics**

| df.describe() |
| :---- |

| What this doesdescribe() summarizes numeric columns using count, mean, standard deviation, minimum, quartiles and maximum. These numbers help you notice unusual ranges before doing deeper analysis. |
| :---- |

## **9 Inspect categorical columns**

| df\["Gender"\].value\_counts(dropna=False)df\["ParentalSupport"\].value\_counts(dropna=False)df\["Online Classes Taken"\].value\_counts(dropna=False) |
| :---- |

| What this doesvalue\_counts() counts how often each category appears. dropna=False keeps missing values visible, which is important during data cleaning. |
| :---- |

#  **Module 2 — Find the problems before fixing them**

A common beginner mistake is to clean data immediately. First measure the problem. That gives you evidence for every cleaning decision.

## **1 Count missing values**

| missing \= df.isna().sum()print(missing) |
| :---- |

| What this doesisna() marks missing cells as True. sum() then counts those True values column by column. This gives a missing-value profile for the entire dataset. |
| :---- |

## **2 Show only columns that contain missing values**

| missing\[missing \> 0\].sort\_values(ascending=False) |
| :---- |

| What this doesThe condition missing \> 0 keeps only columns with at least one missing value. sort\_values() puts the largest missing-value counts first. |
| :---- |

## **3 Calculate missing-value percentages**

| missing\_pct \= (df.isna().sum() / len(df)) \* 100missing\_pct.sort\_values(ascending=False) |
| :---- |

| What this doesThe number of missing cells is divided by the total number of rows and multiplied by 100\. Percentages are easier to compare across columns than raw counts alone. |
| :---- |

## **4 Find complete duplicate rows**

| duplicate\_rows \= df.duplicated().sum()print("Duplicate rows:", duplicate\_rows) |
| :---- |

| What this doesduplicated() marks a row as True when the same complete row has appeared earlier. sum() counts those True values. In this dataset there are no completely identical rows. |
| :---- |

## **5 Check duplicate StudentID values**

| duplicate\_ids \= df\["StudentID"\].dropna().duplicated().sum()print("Repeated StudentIDs:", duplicate\_ids) |
| :---- |

| What this doesStudentID is a key-like field, so duplicate IDs deserve a separate check even when complete rows are not duplicated. dropna() avoids treating missing IDs as a repeated student. |
| :---- |

## **6 Display the repeated IDs**

| id\_counts \= df\["StudentID"\].value\_counts()id\_counts\[id\_counts \> 1\] |
| :---- |

| What this doesvalue\_counts() counts every non-missing StudentID. The condition \> 1 keeps only IDs that occur more than once. |
| :---- |

## **7 Find impossible attendance values**

| bad\_attendance \= df\[    (df\["Attendance (%)"\] \< 0\) |    (df\["Attendance (%)"\] \> 100\)\]bad\_attendance\[\["StudentID", "Name", "Attendance (%)"\]\] |
| :---- |

| What this doesThe two conditions identify percentages below 0 or above 100\. The | operator means OR. In this dataset, values of 200 appear in Attendance (%), which cannot represent a normal percentage. |
| :---- |

## **8 Find suspicious study-hour values**

| bad\_study \= df\[df\["Study Hours"\] \< 0\]bad\_study\[\["StudentID", "Name", "Study Hours"\]\] |
| :---- |

| What this doesA study-hours value below zero is not meaningful. This filter isolates those records so that the analyst can decide how to handle them instead of hiding the issue. |
| :---- |

## **9 Check important numeric ranges**

| checks \= {    "AttendanceRate": (0, 100),    "PreviousGrade": (0, 100),    "FinalGrade": (0, 100),    "Attendance (%)": (0, 100),    "Study Hours": (0, 24\)}for col, (low, high) in checks.items():    bad \= df\[col\].notna() & ((df\[col\] \< low) | (df\[col\] \> high))    print(col, ":", bad.sum(), "invalid values") |
| :---- |

| What this doesA dictionary stores a sensible lower and upper limit for each field. The loop applies the same validation pattern to several columns. notna() ensures that missing values are not counted as range errors. |
| :---- |

# **Module 3 — Clean the dataset carefully**

There is no single correct cleaning rule for every dataset. The important part is to make the rule explicit. In this lab we will use simple, explainable rules suitable for a student exercise.

## **1 Make a working copy**

| clean \= df.copy() |
| :---- |

| What this doescopy() creates a separate DataFrame. Keeping the original df unchanged lets you compare the raw data with the cleaned version. |
| :---- |

## **2 Remove exact duplicate rows**

| clean \= clean.drop\_duplicates() |
| :---- |

| What this doesdrop\_duplicates() removes rows that are completely identical. Here this step is mainly included to demonstrate the standard cleaning operation; always check the count before and after. |
| :---- |

## **3 Fix impossible Attendance (%) values**

| clean.loc\[    (clean\["Attendance (%)"\] \< 0\) |    (clean\["Attendance (%)"\] \> 100),    "Attendance (%)"\] \= pd.NA |
| :---- |

| Why use pd.NA?An impossible measurement is not the same thing as a real measurement of zero. Replacing an invalid value with a missing value prevents the bad number from affecting averages or other calculations. |
| :---- |

## **4 Fix negative Study Hours**

| clean.loc\[clean\["Study Hours"\] \< 0, "Study Hours"\] \= pd.NA |
| :---- |

| What this doesNegative study hours are treated as invalid and changed to a missing value. This keeps the cleaning rule transparent and easy to explain. |
| :---- |

## **5 Fill numeric missing values with the median**

| numeric\_cols \= \[    "AttendanceRate",    "StudyHoursPerWeek",    "PreviousGrade",    "ExtracurricularActivities",    "FinalGrade",    "Study Hours",    "Attendance (%)"\]for col in numeric\_cols:    clean\[col\] \= clean\[col\].fillna(clean\[col\].median()) |
| :---- |

| Why median?The median is the middle value after sorting and is less affected by extreme values than the mean. It is a reasonable classroom example for filling missing numeric measurements. In a real project, the choice should depend on the data and the business context. |
| :---- |

## **6 Fill categorical missing values**

| clean\["Gender"\] \= clean\["Gender"\].fillna("Unknown")clean\["ParentalSupport"\] \= clean\["ParentalSupport"\].fillna("Unknown")clean\["Online Classes Taken"\] \= clean\["Online Classes Taken"\].fillna(False)clean\["Name"\] \= clean\["Name"\].fillna("Unknown") |
| :---- |

| What this doesText columns need a different strategy from numeric columns. Here we preserve the missingness information for text fields by using an explicit category. For the Boolean-like field, False is used as a simple exercise rule; in a real analysis you should confirm whether missing means 'No' before making that replacement. |
| :---- |

## **7 Handle missing StudentID values**

| clean\["StudentID"\].isna().sum() |
| :---- |

| Important decisionDo not invent student IDs just because the column is missing. If StudentID is a required key in the real system, those records should normally be matched back to the source system. For this classroom exercise, you can keep them as missing while continuing with non-ID analysis. |
| :---- |

## **8 Recheck the cleaning**

| print("Rows:", len(clean))print("Missing values:")print(clean.isna().sum())print("Invalid attendance:",      ((clean\["Attendance (%)"\] \< 0\) |       (clean\["Attendance (%)"\] \> 100)).sum())print("Negative study hours:",      (clean\["Study Hours"\] \< 0).sum()) |
| :---- |

| What this doesA cleaning step is not finished until you verify the result. The final checks confirm whether the rules actually removed the problems they were designed to address. |
| :---- |

#  **Module 4 — Ask questions of the cleaned data**

Now the interesting part starts. Instead of running random commands, write a question first and then choose pandas operations that answer it.

## **Question 1: What is the average final grade?**

| clean\["FinalGrade"\].mean() |
| :---- |

| What this doesSelecting one column returns a pandas Series. mean() calculates its arithmetic average. |
| :---- |

## **Question 2: Who are the highest-performing students?**

| top\_students \= clean.sort\_values(    "FinalGrade", ascending=False)top\_students\[\["StudentID", "Name", "FinalGrade"\]\].head(10) |
| :---- |

| What this doessort\_values() orders the DataFrame by FinalGrade. ascending=False puts the largest grades first. head(10) then shows the first ten records. |
| :---- |

## **Question 3: How many students are in each gender group?**

| clean\["Gender"\].value\_counts() |
| :---- |

| What this doesvalue\_counts() produces a frequency table. It is useful for understanding the composition of a categorical variable. |
| :---- |

## **Question 4: Does parental support relate to final grade?**

| clean.groupby("ParentalSupport")\["FinalGrade"\].agg(    \["count", "mean", "median", "min", "max"\]).round(2) |
| :---- |

| What this doesgroupby() separates the data into groups. Selecting FinalGrade tells pandas which measurement to summarize. agg() calculates several statistics for every support group. |
| :---- |

## **Question 5: What happens when study hours are grouped?**

| clean\["StudyBand"\] \= pd.cut(    clean\["Study Hours"\],    bins=\[0, 1, 2, 3, 4, 5\],    labels=\["0–1", "1–2", "2–3", "3–4", "4–5"\],    include\_lowest=True)clean.groupby("StudyBand", observed=True)\["FinalGrade"\].mean().round(2) |
| :---- |

| What this doespd.cut() converts a continuous number into useful ranges. This makes it easier to compare groups such as 0–1 hours, 1–2 hours and so on. The groupby() step then calculates the average final grade for each band. |
| :---- |

## **Question 6: Which students have low attendance and low grades?**

| at\_risk \= clean\[    (clean\["Attendance (%)"\] \< 70\) &    (clean\["FinalGrade"\] \< 70\)\]at\_risk\[\["StudentID", "Name", "Attendance (%)", "FinalGrade"\]\] |
| :---- |

| What this doesThe & operator means AND. A student must satisfy both conditions to appear in the result. Parentheses around each condition are required when combining pandas filters. |
| :---- |

## **Question 7: Does previous grade move with final grade?**

| clean\[\["PreviousGrade", "FinalGrade"\]\].corr() |
| :---- |

| What this doescorr() calculates pairwise correlation for numeric columns. A positive correlation means that higher values tend to occur with higher values, while a value near zero indicates a weaker linear relationship. Correlation does not prove causation. |
| :---- |

#  **Module 5 — Visualize the findings**

Charts should answer a question. Do not add a chart just because a chart is possible.

## **1 Final grade distribution**

| import matplotlib.pyplot as pltclean\["FinalGrade"\].plot(    kind="hist",    bins=10,    edgecolor="black")plt.title("Distribution of Final Grades")plt.xlabel("Final Grade")plt.ylabel("Number of Students")plt.show() |
| :---- |

| What this doesA histogram groups numeric values into intervals. It helps you see where most final grades fall and whether the distribution is concentrated or spread out. |
| :---- |

## **2 Average final grade by parental support**

| clean.groupby("ParentalSupport")\["FinalGrade"\].mean().plot(    kind="bar")plt.title("Average Final Grade by Parental Support")plt.xlabel("Parental Support")plt.ylabel("Average Final Grade")plt.xticks(rotation=0)plt.show() |
| :---- |

| What this doesThe grouped mean creates one value per support category. A bar chart makes those category averages easy to compare. |
| :---- |

## **3 Study hours and final grade**

| clean.plot(    x="Study Hours",    y="FinalGrade",    kind="scatter")plt.title("Study Hours vs Final Grade")plt.xlabel("Study Hours")plt.ylabel("Final Grade")plt.show() |
| :---- |

| What this doesA scatter plot places one student at each combination of study hours and final grade. It is useful for looking for patterns, clusters and unusual points. |
| :---- |

#  **Module 6 — Build a small report**

## **1 Create a summary table**

| summary \= clean.groupby("ParentalSupport").agg(    Students=("FinalGrade", "count"),    Average\_Final\_Grade=("FinalGrade", "mean"),    Average\_Attendance=("Attendance (%)", "mean"),    Average\_Study\_Hours=("Study Hours", "mean")).round(2)summary |
| :---- |

| What this doesNamed aggregations create readable output columns. Instead of producing a large statistical table, we select the measurements that are useful for the question we are asking. |
| :---- |

## **2 Export the cleaned data**

| clean.to\_csv(    "student\_performance\_cleaned.csv",    index=False) |
| :---- |

| What this doesto\_csv() writes the DataFrame to a CSV file. index=False prevents pandas from adding the DataFrame's row index as an extra column. |
| :---- |

## **3 Export the summary**

| summary.to\_csv(    "student\_performance\_summary.csv") |
| :---- |

| What this doesThe grouped summary is saved separately so that it can be opened in Excel or shared without sending the full student-level dataset. |
| :---- |

|  |
| :---- |

#  **Your challenge**

Try these without copying the answer from the previous sections. Write the question in plain English first, then write the pandas code.

**Challenge 1 —** Find the five students with the lowest FinalGrade. Display StudentID, Name and FinalGrade.

**Challenge 2 —** Calculate the average FinalGrade for students who took online classes and those who did not.

**Challenge 3 —** Find the average FinalGrade for each Gender.

**Challenge 4 —** Create a table showing count, mean and median for FinalGrade by ParentalSupport.

**Challenge 5 —** Find students whose Attendance (%) is below the dataset median and whose FinalGrade is above the dataset median.

**Challenge 6 —** Find the 10 most frequently repeated StudentID values.

**Challenge 7 —** Calculate the percentage of students in each ParentalSupport category.

**Challenge 8 —** Create a new column called PerformanceLevel: Below 60 \= Needs Improvement, 60–74 \= Developing, 75–89 \= Good, 90+ \= Excellent.

**Challenge 9 —** Create a bar chart of average FinalGrade by PerformanceLevel.

**Challenge 10 —** Calculate the correlation between StudyHoursPerWeek, AttendanceRate, PreviousGrade and FinalGrade. Which relationships deserve further investigation?

#  **Data-quality checklist**

* Did you check the number of rows and columns?  
* Did you inspect data types?  
* Did you count missing values?  
* Did you check complete duplicate rows?  
* Did you check whether key fields such as StudentID repeat?  
* Did you check numeric ranges?  
* Did you identify impossible values before replacing them?  
* Did you keep a copy of the raw DataFrame?  
* Did you explain why you chose each missing-value strategy?  
* Did you verify the cleaned result?  
* Did you check whether your analysis answers a real question?  
* Did you label charts clearly?  
* Did you save the cleaned output separately from the raw data?

#  **Quick reference — pandas commands used**

| Command | Purpose |
| :---- | :---- |
| **pd.read\_csv()** | Read a CSV file into a DataFrame |
| **head()** | Preview the first rows |
| **shape** | Return rows and columns |
| **columns** | Return column labels |
| **dtypes** | Show data types |
| **info()** | Compact structural summary |
| **describe()** | Numeric descriptive statistics |
| **isna()** | Identify missing values |
| **sum()** | Count True values or add numeric values |
| **duplicated()** | Detect repeated rows/values |
| **drop\_duplicates()** | Remove exact duplicate rows |
| **value\_counts()** | Count categories |
| **sort\_values()** | Sort rows by a column |
| **groupby()** | Split data into groups |
| **agg()** | Apply several summary functions |
| **mean()** | Calculate arithmetic mean |
| **median()** | Calculate middle value |
| **corr()** | Calculate pairwise correlation |
| **pd.cut()** | Create intervals/bands |
| **fillna()** | Replace missing values |
| **to\_csv()** | Write a DataFrame to CSV |

