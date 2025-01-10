"""
extract_macplus_attendance.py

Detailed sample script for a scenario where MAC+ attendance logs are stored
in a local CSV file (gym_attendance.csv) that the user (John Doe) updates manually.

Usage:
  1. Place 'gym_attendance.csv' in a local '.gitignored' folder (e.g., './data/')
     to ensure it is never committed to your public repository.
  2. (Optional) Create an '.env' file to store MACFIT credentials or tokens
     if you decide to automate retrieval in the future. The file is also ignored.
  3. Import this script and call 'fetch_gym_attendance()' in your main analysis
     notebook (e.g., 'data_analysis.ipynb') to retrieve attendance data.
  4. Merge or join this data with your daily logs (weight, steps, calorie intake).

Note:
  - This approach preserves privacy: your script logic is public, but your actual
    attendance records and any login credentials remain private and never pushed.

Example .gitignore snippet:
  data/
  .env
  *.csv
  *.xlsx

Sample CSV Structure (gym_attendance.csv):
  date,gym,notes
  2025-01-15,Yes,"Morning workout"
  2025-01-16,No,
  2025-01-17,Yes,"Evening cardio"

Author: John Doe
"""

import os
import csv
from datetime import datetime
from dotenv import load_dotenv

def fetch_gym_attendance(csv_path: str = "data/gym_attendance.csv"):
    """
    Retrieve attendance data from a locally stored CSV file.

    Parameters
    ----------
    csv_path : str
        The relative or absolute path to the gym attendance CSV file.
        By default, it is set to 'data/gym_attendance.csv', which should be
        ignored by .gitignore.

    Returns
    -------
    list of dict
        A list of attendance records, where each record is a dictionary with
        keys like 'date', 'gym', and 'notes'. The 'date' field can be converted
        to a datetime object if needed, and 'gym' is typically "Yes" or "No".
        'notes' is optional and can hold extra info about each visit.

    Notes
    -----
    1. If you later develop an automated method (e.g., reading from an API or
       a hidden endpoint), you can replace or supplement this CSV logic here.
    2. If you plan to store any MACFIT credentials, place them in .env:
         MACFIT_USER="john_doe"
         MACFIT_PASS="secret_password"
       and load them with `load_dotenv()`. Currently, we are not using them.
    3. This function logs a message if the file is not found, returning an
       empty list so that your analysis script can handle missing data gracefully.
    """

    # OPTIONAL: For future automation, load environment variables here if needed
    # load_dotenv()
    # user = os.getenv("MACFIT_USER")
    # password = os.getenv("MACFIT_PASS")
    # (For now, we rely on a local CSV, so no direct login is performed.)

    attendance_records = []

    try:
        with open(csv_path, mode="r", encoding="utf-8") as f:
            reader = csv.DictReader(f)
            for row in reader:
                # Attempt to parse the date for more structured usage
                raw_date = row.get("date", "")
                try:
                    # For example, the date format might be YYYY-MM-DD
                    parsed_date = datetime.strptime(raw_date, "%Y-%m-%d").date()
                except ValueError:
                    # If parsing fails, leave it as raw string
                    parsed_date = raw_date

                record = {
                    "date": parsed_date,
                    "gym": row.get("gym", "No").strip(),
                    "notes": row.get("notes", "").strip()
                }
                attendance_records.append(record)

    except FileNotFoundError:
        print(f"[Warning] File not found: {csv_path}")
        print("Make sure you have created 'gym_attendance.csv' in your local 'data/' folder.")
        attendance_records = []

    return attendance_records

def main():
    """
    Simple driver function to demonstrate how this script works in standalone mode.

    - Attempts to load 'gym_attendance.csv' from the default path.
    - Prints the total number of records found and displays each record.
    - If no records are found, warns the user to check for CSV presence.
    """

    # In a real project, you might allow the user to pass a custom path:
    # e.g. records = fetch_gym_attendance(csv_path="data/specific_gym_file.csv")
    records = fetch_gym_attendance()

    if not records:
        print("[Info] No attendance records loaded. Check if 'gym_attendance.csv' exists and has data.")
    else:
        print(f"[Info] Loaded {len(records)} MAC+ attendance records from local CSV.")
        for i, rec in enumerate(records, start=1):
            print(f" {i:02d}. Date: {rec['date']} | Gym: {rec['gym']} | Notes: {rec['notes']}")

    # Additional logic could follow here:
    # - Merging or correlating these attendance records with step counts,
    #   weight data, or other daily logs.
    # - Storing or transforming data for further analysis in 'data_analysis.ipynb'.

if __name__ == "__main__":
    main()
