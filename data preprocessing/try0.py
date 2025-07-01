import pandas as pd

# Specify the path to your daily CSV file
file_path = '20191007.csv'  # Update with full path if needed (e.g., '/content/20191007.csv' for Colab)

try:
    # Load the CSV file
    data = pd.read_csv(file_path, parse_dates=[0])  # Assume first column is timestamp; adjust if needed
    headers = list(data.columns)
    first_five_rows = data.head(5).to_dict('records')  # Get first 5 rows as list of dicts

    # Generate LaTeX code for PDF
    latex_content = r"""
\documentclass[a4paper,12pt]{article}
\usepackage[utf8]{inputenc}
\usepackage[T1]{fontenc}
\usepackage{lmodern}
\usepackage{enumitem}
\usepackage{geometry}
\usepackage{longtable}
\usepackage{booktabs}
\geometry{margin=1in}

\begin{document}

\begin{center}
    \textbf{\Large Data from 20191007.csv}
\end{center}

\section*{Column Headers}
\begin{itemize}
"""
    # Add each header as an item in the list
    for header in headers:
        latex_content += f"    \\item {header}\n"

    latex_content += r"""
\end{itemize}

\section*{First 5 Rows}
\begin{longtable}{"""
    # Define table columns based on number of headers
    latex_content += "|l" * len(headers) + "|}\n"
    latex_content += r"    \hline" + "\n"
    # Add table header
    latex_content += "    " + " & ".join([f"\\textbf{{{h}}}" for h in headers]) + r" \\ \hline" + "\n"
    latex_content += r"    \endfirsthead" + "\n"
    latex_content += r"    \hline" + "\n"
    latex_content += "    " + " & ".join([f"\\textbf{{{h}}}" for h in headers]) + r" \\ \hline" + "\n"
    latex_content += r"    \endhead" + "\n"

    # Add first 5 rows to table
    for row in first_five_rows:
        row_values = []
        for h in headers:
            value = str(row[h]).replace("_", r"\_")  # Escape underscores for LaTeX
            row_values.append(value)
        latex_content += "    " + " & ".join(row_values) + r" \\ \hline" + "\n"

    latex_content += r"""
\end{longtable}

\end{document}
"""

    # Save LaTeX code to a .tex file
    with open('data_20191007.tex', 'w') as f:
        f.write(latex_content)

    print("LaTeX file 'data_20191007.tex' created successfully.")
    print("Column Headers:", headers)
    print("First 5 Rows:")
    print(data.head(5))
    print("\nTo generate the PDF:")
    print("1. If local: Install TeX Live (https://www.tug.org/texlive/) and run 'latexmk -pdf data_20191007.tex'.")
    print("2. If on Colab or no LaTeX: Upload 'data_20191007.tex' to Overleaf (https://www.overleaf.com) and compile.")

except FileNotFoundError:
    print(f"Error: The file '{file_path}' was not found. Please check the file path.")
except KeyError as e:
    print(f"Error: Issue with columns, possibly {e}. Check the column names in your CSV.")
except Exception as e:
    print(f"An unexpected error occurred: {e}")
