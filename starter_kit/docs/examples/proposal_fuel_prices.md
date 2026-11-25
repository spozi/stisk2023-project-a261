# Project proposal (Checkpoint 1): EXAMPLE

This is the proposal behind the fuel-price example in the starter kit. Use it as a model; this topic and dataset are not available for your project. A real team of five owns five graphs or panels, not three.

## 1. Working title

How often do pump prices change, and by how much?

## 2. Who will use it, and what will they decide?

A household that drives to work and school and sets aside a fixed amount for fuel each month. The dashboard helps them decide how much margin to leave in that budget.

## 3. Questions

1. How often did the announced prices of RON95, RON97 and diesel change in each year from 2017 to 2026?
2. How large is a typical weekly change, and how large are the biggest?
3. Do RON97 and diesel prices tend to change in the same weeks?

## 4. Data

| Dataset | Publisher | Link to the file (direct download) | Licence | Rows × columns | What one row is |
|---|---|---|---|---|---|
| Price of Petroleum & Diesel (`fuelprice`) | Ministry of Finance, on data.gov.my | <https://storage.data.gov.my/commodities/fuelprice.csv> | CC BY 4.0 | 975 × 10 | One announcement date and one series type (price, or weekly change), with one column per fuel |

- Numeric columns: `ron95`, `ron97`, `diesel`, `ron95_budi95` (RM per litre).
- Category and date columns: `series_type`, `date`.
- Problems already seen:
  1. Two kinds of row in one file: prices and weekly changes.
  2. Newer series (BUDI 95, SKPS, diesel schemes) are empty before they began.
  3. Announcements are not always a week apart (monthly at the end of 2018).
- Personal data: no. The file holds national prices only.

## 5. Product

- Option chosen: **A, dashboard**
- Layout: a row of value boxes (latest prices), a wide trend chart, then two charts and a "What this shows" card; a second page about the data.

| Graph or panel | Kind | Question it answers | Owner |
|---|---|---|---|
| Value boxes: latest prices | headline numbers | context for all three | Role 5 |
| Price per litre at each announcement | trend | 1 | Role 1 |
| % of announcements with a change, by year | comparison | 1 | Role 3 |
| Size of each RON97 change | distribution | 2 | Role 4 |
| Correlation of RON97 and diesel changes (in the text) | relationship | 3 | Role 2 |
