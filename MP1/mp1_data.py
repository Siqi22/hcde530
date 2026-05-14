import pyreadr
import pandas as pd

result = pyreadr.read_r("clean_yrbs_2023.rda")

# See what objects are inside the .rda file
print(result.keys())

# Extract the first dataframe/object
df = list(result.values())[0]

# Save to CSV
df.to_csv("clean_yrbs_2023.csv", index=False)

print("CSV file saved successfully!")