# CricSheet Match Data Analysis Project

This project analyzes cricket match data from CricSheet.org, performing data scraping, processing, database storage, SQL analysis, and data visualization.

## Project Overview

The project consists of five main stages, each implemented in a separate Python script:

1.  **Web Scraping:** Downloads JSON data from CricSheet.org.
2.  **Data Processing:** Extracts relevant information from the downloaded JSON data, cleans it, and transforms it into CSV format.
3.  **Database Storage:** Stores the processed CSV data into a MySQL database.
4.  **SQL Query Analysis:** Executes SQL queries on the database to extract insights and perform analysis.
5.  **Data Visualization:** Generates visualizations (line charts, bar charts, histograms, box plots) to visually represent the data and analysis results.

## Project Structure

The project is organized as follows:

cricsheet_match_data_analysis/ ├── data/ │ ├── csv/ # CSV files generated from data processing │ └── image/ # Images generated from data visualization ├── cricsheet_json/ # Raw JSON files downloaded from CricSheet ├── project.ini # Configuration file for database credentials ├── database_3.py # Script for database storage ├── data_processing_2.py # Script for data processing ├── data_visualization_5.py # Script for data visualization ├── main.py # Main script to run the entire project ├── sql_query_analyse_4.py # Script for SQL query analysis └── web_scraping_1.py # Script for web scraping


## Script Descriptions

Here's a detailed explanation of each script:

### `web_scraping_1.py`

*   **Purpose:** This script uses Selenium to automate web browsing and download JSON files containing cricket match data from CricSheet.org.
*   **Functionality:**
    *   Opens the CricSheet matches page.
    *   Finds the download links for ODI, T20, and Test match JSON files.
    *   Downloads the JSON files and saves them in the `cricsheet_json` folder.
    * uses headless option for run script
* **Dependencies**
    * selenium
    * requests
    * webdriver

### `data_processing_2.py`

*   **Purpose:** This script reads the downloaded JSON files, processes the data, and transforms it into CSV format.
*   **Functionality:**
    *   Reads JSON files from the `cricsheet_json` folder.
    *   Extracts relevant information about each match (teams, players, scores, overs, winners, etc.).
    *   Cleans the data (handles missing values, etc.).
    *   Transforms the data into a tabular format.
    *   Saves the processed data as CSV files (odis.csv, t20s.csv, tests.csv) in the `data/csv` folder.
* **Dependencies**
    * json
    * pandas

### `database_3.py`

*   **Purpose:** This script loads the processed CSV data into a MySQL database.
*   **Functionality:**
    *   Reads the CSV files from the `data/csv` folder.
    *   Connects to a MySQL database using credentials from `project.ini`.
    *   Creates tables (odi\_matches, t20\_matches, test\_matches) in the database.
    *   Inserts the data from the CSV files into the corresponding tables.
* **Dependencies**
    * pymysql
    * sqlalchemy
    * pandas
    * utills (project.ini file path read)

### `sql_query_analyse_4.py`

*   **Purpose:** This script executes SQL queries on the database to analyze the data.
*   **Functionality:**
    *   Connects to the MySQL database.
    *   Runs a series of predefined SQL queries on each of the three tables.
    *   Queries include finding top scorers, total runs, win counts, head-to-head match statistics, etc.
    *   Prints the results of each query to the console.
* **Dependencies**
    * pymysql
    * sqlalchemy
    * pandas
    * utills (project.ini file path read)

### `data_visualization_5.py`

*   **Purpose:** This script generates visualizations to represent the data visually.
*   **Functionality:**
    *   Reads CSV files from the `data/csv` folder.
    *   Creates the `data/image` directory (if it doesn't exist).
    *   Generates various types of plots for each match type (ODI, T20, Test):
        *   Line charts: Overs vs. Total Runs
        *   Bar charts: Team vs. Winners
        *   Histograms: Team Frequency
        *   Box plots: Runs distribution.
    *   Saves each plot as a PNG image in the `data/image` folder.
* **Dependencies**
    * matplotlib
    * pandas
    * os

### `main.py`

*   **Purpose:** This is the main entry point of the project. It executes all the other scripts in the correct order.
*   **Functionality:**
    *   Defines a list of the script file names.
    *   Iterates through the list, running each script using `subprocess.run()`.
    *   Prints messages to the console indicating which script is running and when it completes.
*   Ensures that each script completes successfully before proceeding to the next one.

## `project.ini` file

* This file contain database configuration such as
    * host
    * port
    * user_name
    * password
    * database

## How to Run the Project

1.  **Clone the Repository:**

    ```bash
    git clone <repository_url>
    cd cricsheet_match_data_analysis
    ```
2.  **Install Dependencies:**

    ```bash
    pip install -r requirements.txt
    ```

    **requirements.txt**

    ```
    selenium==4.17.2
    pymysql==1.1.0
    sqlalchemy==2.0.25
    pandas==2.1.4
    matplotlib==3.8.2
    requests==2.31.0
    ```
3.  **Set up Database:**

    *   Make sure you have MySQL installed and running.
    *   Create a database with name as in your `project.ini` file.
    *   Update the database credentials (`host`, `port`, `user_name`, `password`, `database`) in the `project.ini` file.

4.  **Run the Main Script:**

    ```bash
    python main.py
    ```

    This will run all the scripts in order: web scraping, data processing, database storage, SQL analysis, and data visualization.

5. **Check output**
    * `cricsheet_json` folder have json files
    * `data/csv` folder have csv files
    * `data/image` folder have all plots files.

## Output

* **Console Output:**
    * The `sql_query_analyse_4.py` script will print SQL query result to console.
    * `main.py` file will print all run status of each file.
*   **Data:**
    *   `cricsheet_json` folder: Raw JSON files from CricSheet.
    *   `data/csv` folder: Processed CSV files (odis.csv, t20s.csv, tests.csv).
    *   MySQL database: Tables (odi\_matches, t20\_matches, test\_matches) with the processed data.
    * `data/image` folder : plots of data.

## Notes

*   This project requires an active internet connection for web scraping.
*   Make sure you have sufficient disk space, as the downloaded JSON files and generated CSV/image files can be large.
*   Error handling has been implemented in each script, but it is good practice to monitor the output in case of issues.

## Future Enhancements

*   More advanced data analysis (e.g., player performance analysis, prediction models).
*   Interactive dashboards for data visualization.
*   Automated data updates from CricSheet.
*   improved user Interface.

---

