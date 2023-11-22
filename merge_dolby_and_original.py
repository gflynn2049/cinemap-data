import pandas as pd

# Read the CSV files into pandas DataFrames
dolby = pd.read_csv("dolby.csv")
original = pd.read_csv("temp.csv")

# Merge the two DataFrames based on the 'lng' column
merged = pd.merge(original, dolby, on='lng', how='outer', suffixes=('_original', '_dolby'))

# Iterate through the rows of 'dolby' and update 'original'
for index, row in dolby.iterrows():
    # Check if the 'lng' value exists in 'original'
    if row['lng'] in original['lng'].values:
        # Find the index in 'original' where 'lng' matches
        original_index = original.index[original['lng'] == row['lng']].tolist()[0]
        # Iterate through columns and update 'original' if there are differences
        for col in dolby.columns:
            if str(row[col]) != str(original.at[original_index, col]):
                # Check if the existing value is not null or empty before appending
                if pd.notna(original.at[original_index, col]) and str(original.at[original_index, col]) != "":
                    # Append the data from 'dolby' to the same cell in 'original'
                    original.at[original_index, col] = f"{original.at[original_index, col]}\n{row[col]}"
                else:
                    # If the existing value is null or empty, set it to the new value
                    original.at[original_index, col] = row[col]
    else:
        # Append the entire row from 'dolby' to 'original'
        original = pd.concat([original, row.to_frame().T], ignore_index=True)

# Save the updated 'original' DataFrame to a new CSV file
original.to_csv("updated_original.csv", index=False)
