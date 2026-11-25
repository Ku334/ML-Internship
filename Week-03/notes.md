# Week 03 Notes: Math Essentials for EDA

I use the same small list of numbers for every example: `2, 4, 4, 4, 5, 5, 7, 9` (8 numbers).

---

## Mean (the average)

The mean is what I get when I add all the values and divide by how many there are.
For my list: (2+4+4+4+5+5+7+9) / 8 = 40 / 8 = **5**.

The mean uses every value, so one extreme value pulls it a long way. If I add a 900 to the list, the mean jumps to about **116**.

In my car data, the mean price is 526,071, which is higher than the median (420,000), because a few very expensive cars pull it up.

---

## Median (the middle value)

The median is the value in the middle after I sort the list. If there are two middle values, I take their average.
For my list, the middle two are 4 and 5, so the median is **4.5**.

An extreme value barely moves the median. With the 900 added, the median is still **4.5**, while the mean became 116.
That is why I use the median to describe a "typical" value when the data is skewed, like car prices.

---

## Variance

Variance tells me how spread out the values are.
To get it, I find how far each value is from the mean, square each distance, and average the squares.

| Value | Distance from mean (5) | Squared |
|---|---|---|
| 2 | -3 | 9 |
| 4 | -1 | 1 |
| 4 | -1 | 1 |
| 4 | -1 | 1 |
| 5 | 0 | 0 |
| 5 | 0 | 0 |
| 7 | 2 | 4 |
| 9 | 4 | 16 |
| **Total** | | **32** |

Variance = 32 / 8 = **4**.

I square the distances for two reasons. Without squaring, the negative and positive distances cancel out and add up to 0.
Squaring also makes big distances count more than small ones.
The problem is that the units are squared too (for prices, "rupees squared"), so the number is hard to picture.

---

## Standard deviation

The standard deviation is the square root of the variance. It puts the spread back in the **same units** as the data.
For my list: the square root of 4 is **2**. This means a typical value is about 2 away from the mean.

A small standard deviation means the values sit close together, and a large one means they are spread out.

There are two versions, and both are correct:
- **numpy** divides by n (8) and gives **2.0**. I use this when my data is the whole group I care about.
- **pandas** divides by n - 1 (7) and gives **2.138**. This is the "sample" version, for when my data is only a sample of a bigger group.

When I write `df["col"].std()` in pandas, I get the sample version. That is the usual choice in data work.

---

## Correlation

Correlation is a number between **-1 and 1** that tells me how strongly two columns move together in a straight line.

- Close to **+1**: they rise together.
- Close to **-1**: one goes up while the other goes down.
- Close to **0**: no clear straight-line link.

Example: `x = 1, 2, 3, 4, 5` and `y = 2, 4, 5, 4, 5` give a correlation of about **0.77**, a fairly strong positive link.

In my car data, price and engine power have a correlation of **0.69**, and price and kilometres driven have **-0.20**.

**Correlation is not cause.** Automatic cars cost about twice as much as manual cars (median 850,000 against 400,000),
but they are also more powerful and newer, so I cannot say the gearbox alone makes them cost more.
Two things can move together because a third thing affects both.

---

## Derivative (the idea only)

A derivative tells me **how fast something is changing** at one exact point. It is the slope of the curve at that point.

Example: for f(x) = x squared, I can find the slope at x = 3 by measuring over a smaller and smaller step:

| Step size h | Slope = (f(3 + h) - f(3)) / h |
|---|---|
| 1 | 7.000 |
| 0.1 | 6.100 |
| 0.001 | 6.001 |

The slope gets closer and closer to **6**, which is the derivative at x = 3.

Why it matters for machine learning: a model measures how wrong it is (its error). The slope tells it which direction to change a number so the error gets smaller.
I will see this idea again in linear regression.

---

## Quick reference

| Idea | Question it answers | Code |
|---|---|---|
| mean | what is the average? | `df["col"].mean()` |
| median | what is the middle value? | `df["col"].median()` |
| variance | how spread out is it? (squared units) | `df["col"].var()` |
| standard deviation | how spread out is it? (same units) | `df["col"].std()` |
| correlation | do two columns move together? | `df[["a", "b"]].corr()` |
