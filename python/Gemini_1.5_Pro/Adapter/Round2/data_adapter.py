import csv
import json


class CSVReader:
    """Existing class for reading data from CSV files."""

    def __init__(self, filepath):
        self.filepath = filepath

    def read_data(self):
        with open(self.filepath, 'r') as file:
            reader = csv.DictReader(file)
            return list(reader)


class JSONDataProcessor:
    """
    Target interface - expects data in JSON format.
    """

    def process_data(self, json_data):
        if isinstance(json_data, list) and json_data:
            print("Processing JSON data:")
            for item in json_data:
                print(f"- {item}")
        else:
            print("Invalid JSON data format.")


class CSVtoJSONAdapter:
    """
    Adapter: Adapts the CSVReader output to JSON format.
    """

    def __init__(self, csv_reader):
        self.csv_reader = csv_reader

    def get_json_data(self):
        csv_data = self.csv_reader.read_data()
        try:
            json_data = json.dumps(csv_data)
            return json.loads(json_data)  # Return as Python list
        except json.JSONDecodeError:
            print("Error converting CSV to JSON.")
            return None


if __name__ == "__main__":
    csv_file = 'data.csv'  # ชื่อไฟล์ CSV
    csv_reader = CSVReader(csv_file)

    # Using the adapter
    adapter = CSVtoJSONAdapter(csv_reader)
    json_data = adapter.get_json_data()
    processor = JSONDataProcessor()
    processor.process_data(json_data)