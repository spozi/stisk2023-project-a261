# Data card: EXAMPLE (fuel prices)

A model data card for the starter-kit example. Your own card describes your own data.

## 1. Provenance

| Dataset | Publisher | Link | Licence | Downloaded (from MANIFEST.json) |
|---|---|---|---|---|
| Price of Petroleum & Diesel (`fuelprice`) | Ministry of Finance (MOF), published on data.gov.my | <https://data.gov.my/data-catalogue/fuelprice> (file: `storage.data.gov.my/commodities/fuelprice.csv`) | CC BY 4.0 | 2026-11-25 |

The catalogue says the file is updated weekly, so a later download will have more rows. Our results use the copy recorded in `MANIFEST.json`.

## 2. What one row is

- **Raw file:** one announcement date and one series type: `level` (the price) or `change_weekly` (the change since the previous announcement), with one column per fuel.
- **`data/processed/fuel_prices.csv`:** the price of one fuel at one announcement.

## 3. Coverage

30 March 2017 to 19 November 2026: 488 announcements, so 975 raw rows (488 price rows and 487 change rows; the first announcement has no change). National prices only: no states, stations or brands.

## 4. Fields used

| Column | Meaning (from the catalogue) | Type and unit | Missing values | Notes |
|---|---|---|---|---|
| `date` | The date the price took effect | date, YYYY-MM-DD | none | |
| `series_type` | Price (`level`) or weekly change (`change_weekly`) | category | none | The catalogue lists `change-weekly`, but the file uses `change_weekly` |
| `ron95`, `ron97` | Price per litre of RON95 and RON97 petrol | RM per litre | none | |
| `diesel` | Price per litre of diesel, Peninsular Malaysia | RM per litre | none | |
| `ron95_budi95` | RON95 price under the BUDI 95 subsidy | RM per litre | 428 of 488 price rows | Empty before 30 September 2025, when the scheme began |

Not used: `diesel_eastmsia`, `ron95_skps`, `diesel_skds` and `diesel_budi` (other regions and schemes).

## 5. How the data were collected

Not a survey: these are the retail prices the government announces. Since April 2017 they have been set weekly under the Automatic Pricing Mechanism, except for a period at the end of 2018 when they were announced monthly. The catalogue also notes three caveats:
- announcements moved from Fridays to Wednesdays on 3 March 2021;
- the Peninsular diesel subsidy was removed on 10 June 2024 (RM 2.15 to RM 3.35);
- from 30 September 2025, RON95 cost RM 2.60 for the general market, RM 1.99 under BUDI 95 (up to 300 litres a month) and RM 2.05 under SKPS.

## 6. Checks and problems found

| Check or problem | Evidence | What we did | Why |
|---|---|---|---|
| Two kinds of row in one file | 488 `level` and 487 `change_weekly` rows | Kept the price rows; a check confirms that every published change equals the difference in prices | One source of truth; the check catches a mismatch if the publisher's two series ever disagree |
| Series that start late | 428 empty BUDI 95 prices, all before 30 Sep 2025 | Dropped those rows after reshaping | The price did not exist yet. Filling with 0 would pull every average down |
| Uneven gaps between announcements | 7 gaps longer than 8 days (4 at the end of 2018) and 8 shorter than 7 days | Called it "change since the previous announcement"; used percentages per year | A "weekly" change is not always one week |
| Part-years | 2017 starts in March; 2026 ends in November | Compare years by percentage of announcements, not counts | Counts would make part-years look calm |
| Prices out of range | All prices RM 1.25 to RM 6.72 | Check: every price between RM 0.50 and RM 10 | Catches a typing error such as 372 instead of 3.72 |

## 7. Limits and fair use

- **Can support:** how often, and by how much, the announced prices changed, and whether two fuels tended to change together.
- **Cannot support:** what drivers actually paid or how much they bought; why prices changed (world oil prices and exchange rates are not in the data); anything about East Malaysia diesel or individual stations.
- **Personal information:** none.
