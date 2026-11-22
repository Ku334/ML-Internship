# Week 02 Log: NumPy and Pandas

## What I Did
- Practised NumPy: creating arrays, indexing and slicing, broadcasting and basic statistics (`axis=0` and `axis=1`).
- Practised Pandas on a students dataset: loading a CSV, inspecting it, filtering, sorting, groupby, merging, and handling missing values and duplicates.
- Cleaned a real, messy used-car dataset (CarDekho, about 8,100 listings) in `data_cleaning.ipynb`.
- Saved the raw file and the cleaned file separately, so the original data is never changed.
- Fixed my notebook setup so the terminal and the notebook use the same virtual environment.

## What I Learned
- NumPy works on whole arrays at once (vectorization), so no loops are needed.
- `loc` selects by label and `iloc` by position.
- Messy data gives wrong answers quietly: one impossible score of 1000 raised the average, and a filter on `"Female"` missed other spellings.
- Text with units (like `"1248 CC"`) must be converted to numbers before it can be used.
- Duplicates, missing values and impossible values each need their own decision, and the reason matters as much as the code.
- Merge types: `left` keeps every row of the main table, `inner` keeps only matches, `outer` keeps everything.
- `assert` stops the notebook if a rule I expect to be true is false.

## Cleaning Results (car dataset)
- Started with 8,128 rows, ended with 6,699 rows and 14 columns.
- Removed 1,202 duplicate rows. This lowered the average price from about 638,000 to about 526,000, because the copies were mostly expensive cars.
- Dropped the `torque` column (441 formats, two units).

## What Confused Me
- `SettingWithCopyWarning` and when pandas copies data.
- Why my notebook was using the wrong Python until I selected the venv.
- Git rejecting my push because GitHub had a commit I did not have, and finishing the half-done merge.
- Regular expressions (`import re`), so I used simpler `split()` in the final notebook.

## Next Week
Week 03: Data Visualization and EDA (Matplotlib and Seaborn).