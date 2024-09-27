import pytest
from data_adapter import CSVReader, JSONDataProcessor, CSVtoJSONAdapter

@pytest.fixture
def sample_csv_data():
    return [
        {'Name': 'Alice', 'Age': '30'},
        {'Name': 'Bob', 'Age': '25'}
    ]

def test_process_valid_json(sample_csv_data, monkeypatch):
    # Arrange: จำลองการทำงานของ read_data() ใน CSVReader
    def mock_read_data(self):
        return sample_csv_data

    # ใช้ monkeypatch จำลองฟังก์ชัน read_data ของ CSVReader
    monkeypatch.setattr(CSVReader, 'read_data', mock_read_data)
    
    adapter = CSVtoJSONAdapter(CSVReader('mock_file.csv'))
    processor = JSONDataProcessor()

    # Act
    processor.process_data(adapter.get_json_data())

def test_process_invalid_json():
    # Arrange
    processor = JSONDataProcessor()

    # Act
    processor.process_data("Invalid JSON")

    # Assert - Check output (would usually use capsys for this)
    # Output should indicate invalid JSON data
