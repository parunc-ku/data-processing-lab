# OOP Data Processing Lab (Commit 3)

## Lab Overview
This lab converts a procedural CSV-analysis script into object-oriented code.
A `DataLoader` class reads a CSV file into a list of dictionaries, and a
`Table` class wraps that data and provides reusable operations (`filter` and
`aggregate`) that can be chained. The test code at the bottom of
`data_processing.py` uses them to answer questions about world cities
(average temperature, cities per country, and so on).

## Project Structure
```
oop_lab_1/
│
├── README.md             # This file
├── Cities.csv            # The dataset
└── data_processing.py    # DataLoader, Table and the test code
```

## Design Overview

### `DataLoader`
- **Attributes:** `base_path` (`Path`): folder containing the data files.
  Defaults to the folder of the script.
- **Methods:**
  - `__init__(base_path=None)`: sets `base_path`.
  - `load_csv(filename)`: opens `base_path/filename` and returns a list of
    dicts, one per row (all values are strings).

### `Table`
- **Attributes:**
  - `table_name` (`str`): name of the table.
  - `table` (`list[dict]`): the rows.
- **Methods:**
  - `__init__(table_name, table)`: stores the name and rows.
  - `filter(condition)`: `condition` is a function taking a row and returning
    a bool. Returns a **new** `Table` with the matching rows, so the original
    is unchanged and calls can be chained, e.g.
    `t.filter(...).aggregate(...)`.
  - `aggregate(function, aggregation_key)`: collects the values of one column
    and passes them to `function` (e.g. `max`, or `lambda x: sum(x)/len(x)`).
    Values are converted to `float` when possible; non-numeric columns
    such as `country` are passed as strings.
  - `__str__()`: readable representation of the table.

## How to Test and Run
1. Requires Python 3 (standard library only).
2. Put `Cities.csv` in the same folder as `data_processing.py`.
3. Run:
   ```
   python data_processing.py
   ```
   The script builds a `Table` from `Cities.csv` and prints the results of the
   provided tests: average temperature, cities in Germany, cities in Spain
   above 12°C, number of unique countries, average temperature in Germany
   and maximum temperature in Italy.