import pandas as pd
import os

# Specify the folder containing CSV files
folder_path = 'data1'  # Replace with your folder path, e.g., './csv_files'

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

# Process each CSV file to check for duplicate headers
for csv_file in csv_files:
    file_path = os.path.join(folder_path, csv_file)
    print(f"\nChecking file: {csv_file}")

    try:
        # Read only the first row of the CSV file to get headers
        df = pd.read_csv(file_path, sep=';', nrows=1)

        # Get the headers (column names)
        headers = df.columns.tolist()

        # Debugging: Print the number of headers
        print(f"Number of headers in '{csv_file}': {len(headers)}")

        # Check for duplicate headers
        header_counts = pd.Series(headers).value_counts()
        duplicates = header_counts[header_counts > 1]

        if not duplicates.empty:
            print(f"Duplicate headers found in '{csv_file}':")
            for header, count in duplicates.items():
                print(f" - '{header}' appears {count} times")
        else:
            print(f"No duplicate headers found in '{csv_file}'.")

        # Optionally, print the first 10 headers for inspection
        print(f"First 10 headers for '{csv_file}':")
        print(headers[:10])

    except Exception as e:
        print(f"Error processing '{csv_file}': {str(e)}")
        continue

print(f"\nDuplicate check complete. Processed {len(csv_files)} file(s).")
