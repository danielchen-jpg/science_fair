# Science Fair Project - Python Practice
# September 13, 2026
# Goal: Practice Python fundamentals and basic data analysis

# --------------------------------------------------
# 1. VARIABLES
# --------------------------------------------------

county = "Pulaski County"
agricultural_exports = 1000000
tariff_rate = 0.10

print("County:", county)
print("Agricultural exports:", agricultural_exports)
print("Tariff rate:", tariff_rate)


# --------------------------------------------------
# 2. BASIC CALCULATION
# --------------------------------------------------

potential_effect = agricultural_exports * tariff_rate

print("Potential modeled effect:", potential_effect)


# --------------------------------------------------
# 3. LISTS
# --------------------------------------------------

counties = ["Pulaski", "Benton", "Washington", "Craighead"]

print("\nCounties:")
print(counties)


# --------------------------------------------------
# 4. DICTIONARIES
# --------------------------------------------------

agricultural_values = {
    "Pulaski": 1000000,
    "Benton": 2500000,
    "Washington": 1800000,
    "Craighead": 3000000
}

print("\nAgricultural values:")
print(agricultural_values)


# --------------------------------------------------
# 5. FOR LOOP
# --------------------------------------------------

print("\nCounty values:")

for county, exports in agricultural_values.items():
    print(county, exports)


# --------------------------------------------------
# 6. IF STATEMENT
# --------------------------------------------------

print("\nAgricultural exposure:")

for county, exports in agricultural_values.items():

    if exports > 2000000:
        exposure = "High"
    else:
        exposure = "Lower"

    print(county, ":", exposure)


# --------------------------------------------------
# 7. FUNCTION
# --------------------------------------------------

def calculate_effect(exports, tariff):
    effect = exports * tariff
    return effect


print("\nPotential effects:")

for county, exports in agricultural_values.items():

    effect = calculate_effect(exports, tariff_rate)

    print(county, ":", effect)


# --------------------------------------------------
# 8. PANDAS
# --------------------------------------------------

import pandas as pd

data = {
    "County": ["Pulaski", "Benton", "Washington", "Craighead"],
    "Agricultural_Value": [1000000, 2500000, 1800000, 3000000]
}

df = pd.DataFrame(data)

print("\nDataFrame:")
print(df)


# --------------------------------------------------
# 9. BASIC DATA ANALYSIS
# --------------------------------------------------

average_value = df["Agricultural_Value"].mean()
maximum_value = df["Agricultural_Value"].max()
minimum_value = df["Agricultural_Value"].min()

print("\nBasic statistics:")
print("Average:", average_value)
print("Maximum:", maximum_value)
print("Minimum:", minimum_value)


# --------------------------------------------------
# 10. APPLY A CALCULATION TO THE DATA
# --------------------------------------------------

df["Potential_Effect"] = df["Agricultural_Value"] * tariff_rate

print("\nData with modeled effect:")
print(df)
