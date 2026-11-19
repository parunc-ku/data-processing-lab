# OOP Data Processing Lab

## Lab Overview
This lab builds a small object-oriented data-processing library in Python.
Data is loaded from CSV files into `Table` objects (a list of dictionaries),
which support filtering, aggregation and joining. A simple `DB` class stores
several tables so they can be looked up by name. The test code in
`data_processing.py` loads cities and countries, then answers questions such
as "average temperature of Italian cities" or "cities below 5°C in non-EU
countries" by combining `filter`, `aggregate` and `join`.

- **Commit 3:** `DataLoader` and `Table` (`filter`, `aggregate`).
- **Commit 4:** `DB` (`insert`, `search`) and `Table.join`.

## Project Structure
```
oop_lab_1/
│
├── README.md             # This file
├── Cities.csv            # Cities dataset (city, country, latitude, longitude, temperature)
├── Countries.csv         # Countries dataset (country, population, EU, coastline)
└── data_processing.py    # DataLoader, DB, Table and the test code
```

## Design Overview

### `DataLoader`
- **Attributes:** `base_path` (`Path`): folder containing the data files
  (defaults to the folder of the script).
- **Methods:**
  - `__init__(base_path=None)`: sets `base_path`.
  - `load_csv(filename)`: reads `base_path/filename` and returns a list of
    dicts, one per row. All values are strings.

### `Table`
A named table. A row is a dict; the table is a list of rows.
- **Attributes:**
  - `table_name` (`str`): name used to look the table up in a `DB`.
  - `table` (`list[dict]`): the rows.
- **Methods:**
  - `__init__(table_name, table)`: stores the name and rows.
  - `filter(condition)`: `condition` takes a row and returns a bool. Returns a
    **new** `Table` (named `<name>_filtered`) with the matching rows, so calls
    can be chained and the original is untouched.
  - `aggregate(function, aggregation_key)`: passes the list of values in one
    column to `function` (e.g. `min`, `max`, or an average lambda). Values are
    converted to `float` when possible; non-numeric columns stay strings.
  - `join(other_table, common_key)`: inner join on a shared column. For each
    row in this table, every row in `other_table` with the same `common_key`
    value is merged into it (the key column appears once). Rows without a match
    are dropped. Returns a **new** `Table`. `other_table` is indexed in a
    dictionary first, so the join is O(n + m) rather than comparing every pair.
  - `__str__()`: `"<table_name>:<rows>"`.

### `DB`
A tiny in-memory database holding tables.
- **Attributes:** `database` (`list[Table]`): the stored tables.
- **Methods:**
  - `__init__()`: creates an empty database.
  - `insert(table)`: adds a `Table`.
  - `search(table_name)`: returns the table with that name, or `None`.

## How to Test and Run
1. Requires Python 3 (standard library only).
2. Put `Cities.csv` and `Countries.csv` in the same folder as
   `data_processing.py`.
3. Run:
   ```
   python data_processing.py
   ```
4. The script inserts both tables into a `DB`, then prints: cities in Italy and
   their average temperature, non-EU countries, the number of countries with a
   coastline, the first 5 rows of the cities-countries join, cold cities
   (below 5.0°C) in non-EU countries, and the min/max temperature of cities in
   landlocked EU countries. Compare the output with the expected output
   provided in the lab.