import csv
from datetime import datetime

def extract_step_count(health_data_file, output_file):
    """
    Extracts step count and day names from an exported Apple Health CSV file.

    Parameters:
    - health_data_file: Path to the exported CSV file from Apple Health.
    - output_file: Path where the cleaned step_count.csv will be saved.
    """
    try:
        # Open the Apple Health CSV file
        with open(health_data_file, mode='r', encoding='utf-8') as file:
            reader = csv.DictReader(file)
            
            # Prepare the output data
            step_data = []

            # Loop through the health data assuming the format contains 'date' and 'step_count'
            for row in reader:
                # Adjust based on how Apple Health exports data
                date_str = row.get('date', '')
                step_count = row.get('step_count', '')

                # Convert the date to a day of the week
                if date_str and step_count:
                    date_obj = datetime.strptime(date_str, "%Y-%m-%d")  # Adjust the date format if needed
                    day_name = date_obj.strftime('%A')  # Convert date to day name
                    step_data.append([day_name, step_count])

        # Write the processed data to a CSV file
        with open(output_file, mode='w', encoding='utf-8', newline='') as file:
            writer = csv.writer(file)
            writer.writerow(['Days', 'Step_count'])
            writer.writerows(step_data)

        print(f"Step count data successfully saved to {output_file}")

    except FileNotFoundError:
        print("Error: Health data file not found!")
    except Exception as e:
        print(f"An error occurred: {e}")

# Example usage
if __name__ == "__main__":
    health_data_path = "data/health_export.csv"  # Exported file from Apple Health
    output_csv_path = "data/step_count.csv"
    extract_step_count(health_data_path, output_csv_path)
