# Week 02 Notes: NumPy and Pandas

## NumPy quick reference
| Task | Code |
|---|---|
| Create | `np.array([1, 2, 3])`, `np.arange(1, 11)`, `np.zeros((3, 4))` |
| Shape and type | `a.shape`, `a.dtype`, `a.ndim` |
| Slice | `a[2:5]`, `a[::-1]`, `m[1, 2]`, `m[:, 1]` |
| Filter | `a[a > 30]` |
| Statistics | `a.mean()`, `np.median(a)`, `a.std()`, `m.mean(axis=0)` |

- `axis=0` works down the columns, `axis=1` works across the rows.
- Broadcasting lets arrays of different shapes work together without loops.

## Pandas quick reference
| Task | Code |
|---|---|
| Load and inspect | `pd.read_csv(path)`, `df.head()`, `df.info()`, `df.describe()`, `df.shape` |
| Select | `df["col"]`, `df.loc[rows, cols]`, `df.iloc[rows, cols]` |
| Filter and sort | `df[df["score"] > 90]`, `df.sort_values("score")` |
| Missing values | `df.isnull().sum()`, `df.dropna(subset=[...])`, `df.fillna(value)` |
| Duplicates | `df.duplicated().sum()`, `df.drop_duplicates()` |
| Group | `df.groupby("city")["score"].mean()` |
| Merge | `pd.merge(a, b, on="key", how="left")` |

## Cleaning decisions (car dataset)
| Problem | Decision | Why |
|---|---|---|
| 1,202 duplicate rows | remove | the copies matched in every column, and some appeared about 30 times |
| Numbers stored as text | split off the number, keep the unit separately | text cannot be averaged |
| `torque` in many formats | drop the column | too messy for this task |
| Mileage or power of 0 | treat as missing | impossible for a car |
| `km_driven` over 1,000,000 or under 100 | remove 3 rows | not believable |
| Missing specifications | remove the rows | the gaps come together, so filling would invent a car |
| Very high prices | keep | real luxury cars |

## Mistakes to avoid
- Never edit the raw file.
- Check for duplicates and spelling variants before filtering or grouping.
- Write down why for every cleaning choice.