
"""
extract_macplus_attendance.py

Detailed sample script for a scenario where MAC+ attendance logs are stored
in a local CSV file (gym_attendance.csv) that is updated manually.

Note:
  - This approach preserves privacy: your script logic is public, but my actual
    attendance records and any login credentials remain private and never pushed.

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
    """
    
    load_dotenv()
    user = os.getenv("MACFIT_USER")
    password = os.getenv("MACFIT_PASS")
 

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


if __name__ == "__main__":
    main()
