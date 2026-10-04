# Concept Presentation

**Daraz Top Sales Products — Analysis of Watches, Bags & Accessories**

PRG-330 Final Project
Team: **Prashant** · **Ananta** · **Manish**

---

## 1. Title

**Daraz Top Sales Products — Analysis of Watches, Bags & Accessories**

A data analysis project on 1,078 products listed on Daraz, covering watches, bags and
accessories for men, women and kids.

---

## 2. Data Source

| | |
| :---- | :---- |
| **Source** | Kaggle — *Daraz Top Sales Products Dataset 2024* |
| **Uploaded by** | `muhammadmurtazasani` |
| **Link** | https://www.kaggle.com/datasets/muhammadmurtazasani/daraz-top-sales-products-dataset-2024 |
| **File used** | `Watches Bags Accessories.csv` |
| **Website scraped** | daraz.pk (all 1,078 product links verified) |
| **Currency** | Pakistani Rupees (Rs) |

### The four required points

| Point | Answer |
| :---- | :---- |
| **Number of rows** | **1,078** |
| **Number of columns** | **11** |
| **Missing values** | **102 cells (0.86% of the data)** |
| **Duplicate values** | **14 duplicate rows (1.3%)** → 1,064 rows remain |

### Where the missing values are

| Column | Missing |
| :---- | ----: |
| Sold Count | 34 |
| Original Price | 68 |
| All other 9 columns | 0 |

### The columns

`Title`, `Rating in Stars`, `Rating Count`, `Sold Count`, `Voucher`, `Delivery`,
`Currency`, `Current Price`, `Original Price`, `Link`, `Category`

There are **7 categories**: Womens Bags, Mens Accessories, Mens Watches, Womens Watches,
Kids Watches, Mens Bags, Womens Accessories.

### The main point to make

Only **1 of the 11 columns** (`Rating Count`) arrives as a usable number. The other 10 are
stored as text:

* prices look like `Rs. 520`
* ratings look like `4.6/5`
* sold counts look like `6K Sold`

This is why data cleaning is the backbone of our project, not a side step.

---

## 3. Modules Explanation

### (a) Variables & fundamentals

* **Variables** to hold the table and the results: `df`, `summary`, `counts`, `prices`
* **Strings** for all the text cleaning, for example removing `Rs. ` and `/5`
* **Floats** for prices, ratings and discounts
* **Integers** for counts of products and ratings
* **Lists** to collect values while looping: `sold_numbers`, `groups`, `has_voucher`,
  `categories`

### (b) Conditionals

We use `if / elif / else` in four places, each one because it is actually needed:

1. Inside `sold_to_number()` — check for `K` and multiply by 1000, and catch missing values
2. Inside `price_group()` — sort each product into Budget, Mid or Expensive
3. In the voucher loop — `0` becomes "No", anything else becomes "Yes"
4. In the category loop — label a category above or below the overall median price

### (c) Loops

Four `for` loops:

1. Convert every sold count from text to a number
2. Apply the price group to every product
3. Build the voucher yes/no column
4. Print a summary line for each category we are comparing

### (d) Functions

Two functions, both written because a one-line command could not do the job:

| Function | What it does | Why a function was needed |
| :---- | :---- | :---- |
| `sold_to_number(text)` | `"6K Sold"` → 6000, `"452 Sold"` → 452 | `str.replace()` cannot decide whether to multiply |
| `price_group(price)` | returns Budget / Mid / Expensive | needs a three-way decision |

### (e) Pandas, NumPy, Matplotlib + Seaborn

**What we use now:**

* **Pandas** — `read_csv`, `head`, `info`, `describe`, `isnull`, `duplicated`,
  `drop_duplicates`, `value_counts`, `groupby`, `agg`, `to_numeric`, `str.replace`,
  `median`, `mean`, `corr`, `nlargest`
* **Matplotlib** — bar chart, horizontal bar chart, pie chart, histogram, scatter plot,
  and a two-panel subplot

**We do not currently use NumPy or Seaborn.** This was a deliberate choice, because our
project guidelines say to prefer Pandas and Matplotlib and not to add Seaborn or Plotly
just because the sample notebook uses them.

> **Question to ask the professor:** the board lists NumPy and Seaborn. Should we add them,
> or is Pandas plus Matplotlib acceptable?

If he wants them added, it is a small change rather than a rewrite:

* **Seaborn** would improve the category bar charts and let us add a correlation heatmap
* **NumPy** would handle the numeric arrays behind the price grouping

---

## 4. Expected Outcomes

1. **A cleaned dataset** — 1,078 rows reduced to 1,064, with 4 text columns converted into
   real numbers, 2 unusable columns dropped, and a discount column that we calculate
   ourselves.
2. **Category comparison** — which of the 7 categories has the most listings, which are
   expensive, and which actually sell.
3. **A price-group breakdown** — how much of this part of Daraz is budget versus premium.
4. **An answer on what drives sales** — whether price, free delivery or vouchers make
   products sell more.
5. **Around 8 charts**, each answering a question we stated, not added for decoration.
6. **4 to 7 written findings** taken strictly from the outputs.

### One result we can already preview

Price and sales appear to be **unrelated**, with a correlation of **0.002**. Kids Watches is
the cheapest category but sells the least, while Mens Bags sells over five times more.
Being cheap does not make a product sell.

---

## 5. Challenges We May Face

1. **Numbers stored as text.**
   Ten of the eleven columns are text. `6K Sold` needs a function, not a simple replace.
   This is the single biggest obstacle in the project.

2. **One column holding three different things.**
   `Voucher` mixes counts (`3 Vouchers`), amounts (`Rs.1500 Off`) and percentages
   (`5% Off`). These cannot be compared with each other, so we reduce the column to a
   yes/no and accept the loss of detail rather than invent a false scale.

3. **Deciding what to do with missing values.**
   34 sold counts and 68 original prices are blank. We plan to leave them blank, because
   inventing a sales figure would corrupt the result.

4. **Skewed prices.**
   The mean price is Rs 702 but the median is Rs 522, pulled up by a few expensive watches.
   Using the mean would misrepresent every category comparison, so we use the median and
   explain why.

5. **Dataset size.**
   1,078 rows clears the 1,000 minimum but is not large. We also checked a Daraz dataset
   with 169,499 rows and found it was 90% duplicates hiding only 1,871 real products, so we
   chose the smaller honest one over the bigger misleading one.

6. **The data is from Pakistan, not Nepal.**
   There is no Daraz Nepal dataset on Kaggle. We searched the Kaggle API directly, not just
   Google, and only Pakistan and Bangladesh datasets exist.

7. **A negative result is still a result.**
   Our strongest finding is that price does not predict sales. We need to present that as a
   genuine finding rather than treat it as a failure to find something.

---

## How we divided the work

| Part | What it covers | Presented by |
| :---- | :---- | :---- |
| **Part 1** | Introduction, dataset description, loading and understanding the data | **Prashant** |
| **Part 2** | Cleaning the data and the basic analysis | **Ananta** |
| **Part 3** | Loops and conditions, the graphs, findings and conclusion | **Manish** |

---

## Two questions to settle today

1. **NumPy and Seaborn** — does he want them included, or is Pandas plus Matplotlib fine?
2. **Pakistan vs Nepal** — is Pakistani Daraz data acceptable? If Nepal is required, no
   Kaggle dataset exists, so a non-Kaggle source would need to be allowed.

Both are cheap to change now and expensive to change the week before submission.
