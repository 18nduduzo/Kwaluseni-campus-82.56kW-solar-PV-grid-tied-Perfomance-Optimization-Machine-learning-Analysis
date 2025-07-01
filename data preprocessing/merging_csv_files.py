import pandas as pd
import os

# Specify the folder containing CSV files
folder_path = 'data1'  # Relative path to data1 folder
output_file = 'merged_output.csv'  # Output file name

# Ensure the folder exists
if not os.path.isdir(folder_path):
    print(f"Error: Folder '{folder_path}' does not exist.")
    exit(1)

# Get list of CSV files
csv_files = [f for f in os.listdir(folder_path) if f.lower().endswith('.csv')]
if not csv_files:
    print(f"No CSV files found in '{folder_path}'.")
    exit(1)

print(f"Found {len(csv_files)} CSV file(s): {csv_files}")

# Initialize an empty list to store DataFrames
all_dataframes = []

# Process each CSV file
for csv_file in csv_files:
    file_path = os.path.join(folder_path, csv_file)
    print(f"\nProcessing file: {csv_file}")

    try:
        # Read the CSV file, assuming semicolon delimiter
        df = pd.read_csv(file_path, sep=';')

        # Get the name of the first column
        if not df.empty and len(df.columns) > 0:
            date_time_column = df.columns[0]  # Use the first column as the date/time column
            print(f"Using first column '{date_time_column}' as date/time column.")
        else:
            print(f"Error: No columns found in '{csv_file}'. Skipping.")
            continue

        # Convert the date_time column to datetime with specific format
        try:
            df[date_time_column] = pd.to_datetime(df[date_time_column], format='%d.%m.%Y %H:%M', errors='coerce')
            if df[date_time_column].isna().all():
                print(f"Warning: All values in '{date_time_column}' for '{csv_file}' could not be parsed as datetime. Skipping.")
                continue
        except Exception as e:
            print(f"Error parsing '{date_time_column}' in '{csv_file}': {str(e)}. Skipping.")
            continue

        # Append the DataFrame to the list
        all_dataframes.append(df)
        print(f"Successfully loaded '{csv_file}' with {len(df)} data rows.")

    except Exception as e:
        print(f"Error processing '{csv_file}': {str(e)}")
        continue

# Check if any valid DataFrames were loaded
if not all_dataframes:
    print("No valid CSV files were processed. Exiting.")
    exit(1)

# Concatenate all DataFrames
print("\nMerging all CSV files...")
merged_df = pd.concat(all_dataframes, ignore_index=True)

# Sort by the first column (date/time) in ascending order
date_time_column = merged_df.columns[0]  # Use the first column for sorting
print(f"Sorting data by '{date_time_column}' in ascending order...")
merged_df = merged_df.sort_values(by=date_time_column, na_position='last')

# Debugging: Print the first 5 rows of the merged and sorted DataFrame
print(f"\nFirst {min(5, len(merged_df))} rows of merged and sorted DataFrame:")
print(merged_df[[date_time_column] + merged_df.columns.tolist()[1:10]].head(min(5, len(merged_df))))

# Save the merged DataFrame to a new CSV file
try:
    merged_df.to_csv(output_file, sep=';', index=False, encoding='utf-8')
    print(f"\nMerged CSV file saved as '{output_file}' with {len(merged_df)} data rows.")
except Exception as e:
    print(f"Error saving merged CSV file: {str(e)}")
    exit(1)

print("\nMerging and sorting complete.")
