import pytest
from data_adapter import CSVReader, JSONDataProcessor, CSVtoJSONAdapter

@pytest.fixture
def sample_csv_data():
    return [
        {'Name': 'Alice', 'Age': '30'},
        {'Name': 'Bob', 'Age': '25'}
    ]

def test_process_valid_json(sample_csv_data, monkeypatch):
    # Arrange
    class MockCSVReader:
        def read_data(self):
            return sample_csv_data

    monkeypatch.setattr('data_adapter.CSVReader', MockCSVReader)
    adapter = CSVtoJSONAdapter(CSVReader('mock_file.csv'))
    processor = JSONDataProcessor()

    # Act
    processor.process_data(adapter.get_json_data())

    # Assert - Check output (would usually use capsys for this)
    # Output should contain processed data

def test_process_invalid_json():
    # Arrange
    processor = JSONDataProcessor()

    # Act
    processor.process_data("Invalid JSON")

    # Assert - Check output (would usually use capsys for this)
    # Output should indicate invalid JSON data