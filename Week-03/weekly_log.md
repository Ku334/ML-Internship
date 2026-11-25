# Week 03 Log: Data Visualization, EDA and Math Essentials

## What I Did
- Learned the main plot types with matplotlib and seaborn: line chart, histogram, boxplot, scatter plot, bar chart and heatmap.
- Practised them on the cleaned used-car data from Week 2 in `visualization_practice.ipynb`.
- Wrote an EDA notebook (`eda_cars.ipynb`) with 9 plots covering distributions, outliers, correlations and class balance.
- Summarized 7 findings in plain language, each with a real number.
- Wrote notes on mean, median, variance, standard deviation, correlation and the idea of a derivative.

## What I Learned
- The plot depends on the column types: one number gives a histogram, a category and a number gives a boxplot, two numbers give a scatter plot, and one category gives a bar chart.
- Start with a question, then choose the plot and the columns.
- Car prices are right-skewed, so the median (420,000) describes a typical car better than the mean (526,071).
- An outlier is not always an error. The very expensive cars are real luxury cars, so I kept them.
- A log scale makes data with a huge range readable, such as prices from 30,000 to 10,000,000.
- `e+06` in a table is scientific notation, only a way of displaying a number.
- Engine power has the strongest link with price (0.69), while kilometres driven is weak (-0.20).
- Correlation is not cause: automatic cars cost about twice as much, but they are also more powerful and newer.
- The categories are unbalanced: CNG and LPG are only 1.3% of the cars, and manual cars are 91.5%.

## Main Findings
1. Prices are right-skewed: median 420,000, mean 526,071.
2. About 4.5% of cars are price outliers, and they are real luxury cars.
3. Power links most with price (0.69).
4. Automatic cars cost about twice as much, but other factors are mixed in.
5. Diesel has the highest median price (525,000).
6. The categories are unbalanced, so results for small groups are less reliable.

## What Confused Me
- Why a particular column is used in a particular plot. I learned to start from a question and the column types.
- How `groupby` works. It helped to think of sorting cards into piles and averaging each pile.
- Scientific notation in the tables and on the axes.
- How a boxplot is built (median, box, whiskers, outlier dots) and why a log scale was needed.
- Getting stuck in the Git pager (`END`), which I fixed with one setting.

## Next Week
Week 04: Machine Learning Basics and Linear Regression (mini project).