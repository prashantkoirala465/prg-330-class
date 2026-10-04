# Daraz Final Project — Professor-Requested Modular Structure

This package follows the requested structure:

- **One main notebook:** `final_project.ipynb`
- **Separate `.py` modules** for course concepts and analysis
- The notebook visibly creates each module with `%%writefile`, then imports and uses it
- **Only the real Daraz datasource is used**. There is no synthetic/sample dataset anywhere.

## Files

1. `module01_variables.py` — variables and data types from the real datasource
2. `module02_loops.py` — loops on actual Category/missing-value data
3. `module03_conditions.py` — `if/elif/else` on actual price, delivery and voucher fields
4. `module04_functions.py` — reusable cleaning functions applied to real rows
5. `module05_cleaning.py` — complete cleaning pipeline and CSV output
6. `module06_pandas_analysis.py` — Pandas grouping, aggregation and summaries
7. `module07_numpy_analysis.py` — NumPy percentiles, IQR, arrays and correlation
8. `module08_visualization.py` — Matplotlib charts from real cleaned data
9. `module09_findings.py` — findings/limitations computed from real data
10. `final_project.ipynb` — creates/imports the modules and runs the complete analysis
11. `Watches Bags Accessories.csv` — original datasource

## Run order

Open `final_project.ipynb` from this folder and choose **Run All**.

The notebook writes the `.py` modules, imports them, cleans the actual datasource, writes `daraz_cleaned_data.csv` and `daraz_analysis_ready.csv`, performs Pandas and NumPy analysis, produces visualizations, and generates findings.

## Important

The filenames use `module01_...` rather than `01_...` because normal Python `import` statements require valid Python identifiers and cannot directly import a module name beginning with a number.
