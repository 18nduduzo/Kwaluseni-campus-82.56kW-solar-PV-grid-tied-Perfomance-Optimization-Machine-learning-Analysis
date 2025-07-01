# Solar PV System Data Analysis

This repository contains Python scripts for analyzing data from the University of Eswatini’s 82.56 kW solar PV system located at Kwaluseni campus. The project aims to optimize system performance, support maintenance planning, and enhance sustainability goals by processing and modeling solar energy data.

## Project Overview
The solar PV system, consisting of 258 monocrystalline panels (320 W each), SMA Tripower and Sunny Island inverters, and a 48V VRLA battery bank, faces challenges such as a faulty cluster controller, non-functional panel arrays, and missing predictive tools. This repository includes codes to:
- Process time-series data (energy output, irradiance, temperature) collected via the SMA Data Manager M.
- Perform data cleaning, quality control, and feature engineering.
- Implement machine learning models (LSTM and Prophet) for energy prediction and forecasting.
- Visualize trends and performance metrics to guide interventions.

## Getting Started

### Prerequisites
- Python 3.8 or higher
- Required libraries: `pandas`, `numpy`, `scikit-learn`, `tensorflow`, `prophet`, `matplotlib`, `seaborn`
- Install dependencies using:
  ```bash
  pip install -r requirements.txt
  ```

### Installation
1. Clone the repository:
   ```bash
   git clone https://github.com/your-username/solar-pv-data-analysis.git
   ```
2. Navigate to the project directory:
   ```bash
   cd solar-pv-data-analysis
   ```
3. Install the required packages (see `requirements.txt`).

### Usage
- Place your solar PV data (CSV format) in the `data/` folder.
- Run the main analysis script:
  ```bash
  python main.py
  ```
- Explore individual scripts (e.g., `data_cleaning.py`, `ml_prediction.py`) for specific tasks.

## File Structure
- `data/`: Contains raw and processed datasets (e.g., energy output, irradiance).
- `src/`: Python scripts for data analysis.
  - `data_cleaning.py`: Handles missing data and normalization.
  - `ml_prediction.py`: Implements LSTM and Prophet models.
  - `visualization.py`: Generates plots for performance trends.
- `requirements.txt`: Lists dependencies.
- `README.md`: This file.

## Contributing
Feel free to fork this repository, submit issues, or create pull requests for improvements. Contributions to enhance data processing, model accuracy, or visualization are welcome.

## License
This project is licensed under the MIT License - see the [LICENSE](LICENSE) file for details.

## Contact
For questions or collaboration, contact [nduduzohlophe84@gmail.com](mailto:your-email@example.com).
