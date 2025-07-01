import pandas as pd
import os

# Specify the folder containing CSV files (update this path)
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

# Process each CSV file
for csv_file in csv_files:
    file_path = os.path.join(folder_path, csv_file)
    print(f"\nProcessing file: {csv_file}")

    try:
        # Read the CSV file as plain text
        with open(file_path, 'r', encoding='utf-8') as file:
            lines = file.readlines()

        # Check if file has at least 9 rows (for headers to merge)
        if len(lines) < 9:
            print(f"Warning: '{csv_file}' has only {len(lines)} rows, expected at least 9. Skipping.")
            continue

        # Process lines, splitting by semicolon and padding to 174 columns
        max_cols = 174
        data = []
        for line in lines:
            fields = line.strip().split(';')
            # Pad with empty strings to match max_cols
            fields.extend([''] * (max_cols - len(fields)))
            # Truncate to max_cols if too long
            data.append(fields[:max_cols])

        # Create DataFrame from the processed data
        df = pd.DataFrame(data)

        # Debugging: Print the first 10 rows or all if fewer
        print(f"First {min(10, len(df))} rows of parsed DataFrame for '{csv_file}':")
        print(df.head(min(10, len(df))))

        # Extract rows 4–9 (1-based indexing, so rows 3–8 in DataFrame)
        rows_to_merge = df.iloc[3:9]

        # Debugging: Print the rows being merged
        print(f"\nRows to merge (rows 4–9) for '{csv_file}':")
        print(rows_to_merge)

        # Combine fields in each column across rows 4–9 into a single string
        merged_row = []
        for col in range(max_cols):
            # Get fields for this column from rows 4–9
            col_values = rows_to_merge[col].tolist()
            # Convert to strings, handle NaN/None, and filter out empty strings
            col_values = [str(val) if pd.notnull(val) else '' for val in col_values]
            col_values = [val for val in col_values if val]
            # Join with a space
            merged_field = ' '.join(col_values)
            merged_row.append(merged_field)

        # Debugging: Print the first 10 values of the merged row and its length
        print(f"\nMerged row for '{csv_file}' (first 10 values for preview):")
        print(merged_row[:10])
        print(f"Length of merged row: {len(merged_row)} fields")

        # Prepare the output: merged row + data rows (row 10+)
        output_lines = []
        # Add the merged row as the first line
        output_lines.append(';'.join(merged_row))
        # Add data rows (DataFrame row 9+, original row 10+)
        for _, row in df.iloc[9:].iterrows():
            row_values = [str(val) if pd.notnull(val) else '' for val in row]
            output_lines.append(';'.join(row_values))

        # Debugging: Print the first 5 lines of the output
        print(f"\nFirst {min(5, len(output_lines))} lines of the output for '{csv_file}':")
        for i, line in enumerate(output_lines[:5]):
            print(f"Line {i+1}: {line[:100]}...")  # Truncate for readability

        # Overwrite the original file
        with open(file_path, 'w', encoding='utf-8') as file:
            file.write('\n'.join(output_lines))

        print(f"File '{csv_file}' has been modified successfully.")
        print(f"New structure: Row 1 is merged (rows 4–9 combined, 174 fields), rows 1–9 removed, data rows (original row 10+) follow.")

    except Exception as e:
        print(f"Error processing '{csv_file}': {str(e)}")
        continue

print(f"\nProcessing complete. Processed {len(csv_files)} file(s).")
